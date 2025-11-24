try:
    import yaml
except ImportError:
    yaml = None

import os
import importlib.util
import inspect
import sys
from core.base_module import BaseModule

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
    config = load_config()
    modules_dir = "modules"
    
    # Get all .py files in modules directory
    module_files = [f for f in os.listdir(modules_dir) if f.endswith(".py") and f != "__init__.py"]
    
    # Sort them naturally so 1.1.1 runs before 1.1.4
    module_files.sort()

    for file in module_files:
        full_path = os.path.join(modules_dir, file)
        
        # Load and Run
        hardening_task = load_module_from_file(full_path, config)
        
        if hardening_task:
            try:
                hardening_task.apply()
            except Exception as e:
                print(f"[ERROR] Execution failed for {file}: {e}")

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