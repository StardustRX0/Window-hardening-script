try:
    import yaml
except ImportError:
    yaml = None

import os
import importlib.util
import inspect
import sys
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


def load_module_from_file(filepath: str, config: dict):
    """
    Dynamically loads a Python file given a path (e.g., 'modules/1.1.4.py')
    and instantiates the class inside it that inherits from BaseModule.
    """
    module_name = os.path.basename(filepath).replace(".py", "")

    # 1. Create the spec (how to load the file)
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    if spec is None:
        print(f"[ERROR] Could not create spec for module: {filepath}")
        return None

    # 2. Create the module object
    module = importlib.util.module_from_spec(spec)

    # 3. Execute the module (runs the Python code inside)
    try:
        spec.loader.exec_module(module)  # type: ignore[attr-defined]
    except Exception as e:
        print(f"[ERROR] Could not load {filepath}: {e}")
        return None

    # 4. Find the class in the module that inherits from BaseModule
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, BaseModule) and obj is not BaseModule:
            # Instantiate and return the class
            return obj(config=config)

    # If we reach here, no suitable class was found
    print(f"[WARN] No BaseModule subclass found in {filepath}")
    return None


def main(config_path: str | None = None):
    """
    Main entry point for the hardening framework.

    - Loads and validates configuration.
    - Discovers all module files under 'modules/' recursively.
    - Executes each module's 'apply()' method in sorted order.
    """
    print("--- Python Hardening Framework (CIS Style) ---")

    # 1. Resolve config path
    if config_path:
        cfg_path = Path(config_path).resolve()
    else:
        cfg_path = DEFAULT_CONFIG

    print(f"[INFO] Using config file: {cfg_path}")

    # 2. Load & validate config
    config = load_config(cfg_path)

    validator = ConfigValidator(config)
    if not validator.validate():
        print("CRITICAL: Configuration contains errors. Execution stopped.")
        sys.exit(1)

    # 3. Discover module files recursively
    module_paths: list[str] = []

    # Use the absolute modules directory
    modules_dir_str = str(MODULES_DIR)

    for root, dirs, files in os.walk(modules_dir_str):
        for file in files:
            # Only pick up .py files, ignore __init__.py
            if file.endswith(".py") and file != "__init__.py":
                # Create the full path (e.g. 'modules/Sector 1.1/1.1.1.py')
                full_path = os.path.join(root, file)
                module_paths.append(full_path)

    # Sort paths so they run in a consistent order
    module_paths.sort()

    print(f"[INFO] Modules directory: {MODULES_DIR}")
    print(f"[INFO] Found {len(module_paths)} modules.")

    # 4. Run them
    for full_path in module_paths:
        hardening_task = load_module_from_file(full_path, config)

        if hardening_task:
            try:
                print(f"[INFO] Running module: {full_path}")
                hardening_task.apply()
            except Exception as e:
                print(f"[ERROR] Execution failed for {full_path}: {e}")


if __name__ == "__main__":
    # Permission check for Windows / Linux
    import ctypes

    try:
        # On Unix-like systems
        is_admin = os.getuid() == 0
    except AttributeError:
        # On Windows
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if not is_admin:
        print("CRITICAL: Script must be run as Administrator/Root")
        sys.exit(1)

    # Optional: accept a config path as the first argument
    # This is what the Wazuh Active Response wrapper will use.
    config_arg = sys.argv[1] if len(sys.argv) > 1 else None
    main(config_arg)
