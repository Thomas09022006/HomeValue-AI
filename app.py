import os
import importlib.util

# Dynamically load pages/1_Home.py as main entrypoint
home_path = os.path.join(os.path.dirname(__file__), "pages", "1_Home.py")
if os.path.exists(home_path):
    spec = importlib.util.spec_from_file_location("home_module", home_path)
    home_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(home_module)

