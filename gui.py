"""Launcher for Desktop GUI application."""
import sys
import importlib.util
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent / "fire-smoke-detector-yolov8"
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

target_gui = PROJECT_DIR / "gui.py"
spec = importlib.util.spec_from_file_location("desktop_gui", target_gui)
mod = importlib.util.module_from_spec(spec)
sys.modules["desktop_gui"] = mod
spec.loader.exec_module(mod)

launch_gui = mod.launch_gui

if __name__ == "__main__":
    launch_gui()
