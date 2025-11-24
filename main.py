try:
    import yaml
except ImportError:
    yaml = None

import os
import importlib.util
import inspect
import sys
from core.base_module import BaseModule
from core.validator import ConfigValidator

def load_config(path="config.yaml"):
    if yaml is None:
        print("CRITICAL: PyYAML is not installed. Install it with: pip install pyyaml")
        sys.exit(1)
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def load_config(path="config.yaml"):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def load_module_from_file(filepath, config):
    """
    Dynamically loads a python file given a path (e.g., "modules/1.1.4.py")
    and instantiates the class inside it.
    """
    module_name = os.path.basename(filepath).replace(".py", "")
    
    # 1. Create the spec (How to load the file)
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    if spec is None:
        return None
    
    # 2. Create the module
    module = importlib.util.module_from_spec(spec)
    
    # 3. Execute the module (runs the python code inside)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"[ERROR] Could not load {filepath}: {e}")
        return None

    # 4. Find the class in the module that inherits from BaseModule
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, BaseModule) and obj is not BaseModule:
            # Instantiate and return the class
            return obj(config=config)
    
    return None

def main():
    print("--- Python Hardening Framework (CIS Style) ---")
    
    # 1. Load & Validate Config
    try:
        config = load_config()
        validator = ConfigValidator(config)
        if not validator.validate():
            print("CRITICAL: Configuration contains errors. Execution stopped.")
            sys.exit(1)
    except Exception as e:
        print(f"CRITICAL: Config error: {e}")
        sys.exit(1)

    modules_dir = "modules"
    
    # --- NEW: Recursive File Search ---
    module_paths = []
    
    # os.walk goes through every subfolder automatically
    for root, dirs, files in os.walk(modules_dir):
        for file in files:
            # Only pick up .py files, ignore __init__.py
            if file.endswith(".py") and file != "__init__.py":
                # Create the full path (e.g. "modules/Sector 1.1/1.1.1.py")
                full_path = os.path.join(root, file)
                module_paths.append(full_path)

    # Sort paths so they run in order (1.1.1 before 1.1.4)
    # Python sorts strings smartly, so "modules/1.1/..." comes before "modules/1.2/..."
    module_paths.sort()

    print(f"Found {len(module_paths)} modules.")

    # --- Run Them ---
    for full_path in module_paths:
        hardening_task = load_module_from_file(full_path, config)
        
        if hardening_task:
            try:
                hardening_task.apply()
            except Exception as e:
                print(f"[ERROR] Execution failed for {full_path}: {e}")

if __name__ == "__main__":
    # Permission Check for Windows
    import ctypes
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if not is_admin:
        print("CRITICAL: Script must be run as Administrator/Root")
        sys.exit(1)

    main()