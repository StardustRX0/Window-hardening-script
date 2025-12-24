try:
    import yaml
except ImportError:
    yaml = None

import os
import importlib.util
import inspect
import sys
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from core.base_module import BaseModule
from core.validator import ConfigValidator

# Base paths, so we don't depend on the current working directory
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR
DEFAULT_CONFIG = REPO_ROOT / "config.yaml"
MODULES_DIR = REPO_ROOT / "modules"


def load_config(path: Path) -> dict:
    """
    Load YAML configuration from the given path.
    """
    if yaml is None:
        print("CRITICAL: PyYAML is not installed. Install it with: pip install pyyaml")
        sys.exit(1)

    try:
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"CRITICAL: Config file not found: {path}")
        sys.exit(1)
    except Exception as e:
        print(f"CRITICAL: Failed to load config from {path}: {e}")
        sys.exit(1)


def _iso_utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _guess_cis_id(hardening_task, module_path: str) -> str:
    """
    Try to infer CIS/control id from common attributes or filename:
    - hardening_task.key / hardening_task.cis_id / hardening_task.id
    - filename "1.1.1" or "1_1_1_1" -> normalize to dots
    """
    for attr in ("key", "cis_id", "id"):
        v = getattr(hardening_task, attr, None)
        if isinstance(v, str) and v.strip():
            return v.strip()

    stem = Path(module_path).stem  # e.g. "1.1.1" or "1_1_1_1"
    # Normalize underscores to dots only if it looks like a numeric control id
    if any(ch.isdigit() for ch in stem):
        return stem.replace("_", ".")
    return stem


def _task_title(hardening_task) -> str:
    for attr in ("title", "name", "description"):
        v = getattr(hardening_task, attr, None)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return hardening_task.__class__.__name__


def emit_json_event(jsonl_path: str, event: dict) -> None:
    """
    Append one JSON object per line (JSONL). Safe: never raises to caller.
    """
    try:
        p = Path(jsonl_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
    except Exception:
        # Never break hardening execution because logging failed
        pass


def load_module_from_file(filepath: str, config: dict):
    """
    Dynamically loads a Python file given a path and instantiates the class
    inside it that inherits from BaseModule.
    """
    module_name = os.path.basename(filepath).replace(".py", "")

    spec = importlib.util.spec_from_file_location(module_name, filepath)
    if spec is None:
        print(f"[ERROR] Could not create spec for module: {filepath}")
        return None

    module = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(module)  # type: ignore[attr-defined]
    except Exception as e:
        print(f"[ERROR] Could not load {filepath}: {e}")
        return None

    for _, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, BaseModule) and obj is not BaseModule:
            return obj(config=config)

    print(f"[WARN] No BaseModule subclass found in {filepath}")
    return None


def main(config_path: str | None = None):
    """
    Main entry point for the hardening framework.
    """
    print("--- Python Hardening Framework (CIS Style) ---")

    # 1) Resolve config path
    cfg_path = Path(config_path).resolve() if config_path else DEFAULT_CONFIG
    print(f"[INFO] Using config file: {cfg_path}")

    # 2) Load & validate config
    config = load_config(cfg_path)

    validator = ConfigValidator(config)
    if not validator.validate():
        print("CRITICAL: Configuration contains errors. Execution stopped.")
        sys.exit(1)

    # 3) JSON changelog settings
    # Prefer env var so your Wazuh wrapper can control where it writes.
    # Examples:
    #  - Windows: C:\ProgramData\Wazuh\logs\hardening\Window-hardening-script.jsonl
    #  - Linux:   /var/ossec/logs/hardening/Ubuntu-hardening-script.jsonl
    if os.name == "nt":
        program_data = os.environ.get("ProgramData", r"C:\ProgramData")
        default_jsonl = Path(program_data) / "Wazuh" / "logs" / "hardening" / "Window-hardening-script.jsonl"
    else:
        default_jsonl = Path("/var/ossec/logs/hardening/Ubuntu-hardening-script.jsonl")
        
    jsonl_path = os.environ.get("HARDENING_JSONL_PATH") or str(default_jsonl)

    repo_name = os.environ.get("HARDENING_REPO_NAME") or str(REPO_ROOT.name)
    os_name = os.environ.get("HARDENING_OS") or ("windows" if os.name == "nt" else "linux")
    dry_run = bool(config.get("general", {}).get("dry_run", False))
    run_id = os.environ.get("HARDENING_RUN_ID") or f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:8]}"

    # 4) Discover module files recursively
    module_paths: list[str] = []
    for root, dirs, files in os.walk(str(MODULES_DIR)):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                module_paths.append(os.path.join(root, file))

    module_paths.sort()

    print(f"[INFO] Modules directory: {MODULES_DIR}")
    print(f"[INFO] Found {len(module_paths)} modules.")

    # 5) Run modules
    for full_path in module_paths:
        hardening_task = load_module_from_file(full_path, config)

        if not hardening_task:
            # Optional: record load failure as JSON
            if jsonl_path:
                emit_json_event(jsonl_path, {
                    "timestamp": _iso_utc_now(),
                    "hardening": {
                        "repo": repo_name,
                        "os": os_name,
                        "run_id": run_id,
                        "module_path": full_path,
                        "result": "ERROR",
                        "message": "Failed to load module (no BaseModule subclass found or import failed).",
                        "dry_run": dry_run,
                    }
                })
            continue

        cis_id = _guess_cis_id(hardening_task, full_path)
        title = _task_title(hardening_task)

        try:
            print(f"[INFO] Running module: {full_path}")
            hardening_task.apply()
            
            events = []
            if hasattr(hardening_task, "get_events"):
                events = hardening_task.get_events()

            if jsonl_path:
                if not events:
                    # No structured events emitted by the module → log generic success
                    emit_json_event(jsonl_path, {
                        "timestamp": _iso_utc_now(),
                        "hardening": {
                            "repo": repo_name,
                            "os": os_name,
                            "run_id": run_id,
                            "cis_id": cis_id,
                            "title": title,
                            "module_path": full_path,
                            "result": "SUCCESS",
                            "message": "Module executed without emitting events.",
                            "dry_run": dry_run,
                        }
                    })
                else:
                    # Export every CHANGED/OK/WARN/ERROR/SKIP line as a JSON event
                    for ev in events:
                        emit_json_event(jsonl_path, {
                            "timestamp": _iso_utc_now(),
                            "hardening": {
                                "repo": repo_name,
                                "os": os_name,
                                "run_id": run_id,
                                "cis_id": cis_id,
                                "title": title,
                                "module_path": full_path,
                                "result": ev.get("result", "SUCCESS"),
                                "message": ev.get("message", ""),
                                "dry_run": dry_run,
                            }
                        })


        except Exception as e:
            print(f"[ERROR] Execution failed for {full_path}: {e}")

            if jsonl_path:
                emit_json_event(jsonl_path, {
                    "timestamp": _iso_utc_now(),
                    "hardening": {
                        "repo": repo_name,
                        "os": os_name,
                        "run_id": run_id,
                        "cis_id": cis_id,
                        "title": title,
                        "module_path": full_path,
                        "result": "ERROR",
                        "message": str(e),
                        "dry_run": dry_run,
                    }
                })


if __name__ == "__main__":
    import ctypes

    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if not is_admin:
        print("CRITICAL: Script must be run as Administrator/Root")
        sys.exit(1)

    config_arg = sys.argv[1] if len(sys.argv) > 1 else None
    main(config_arg)
