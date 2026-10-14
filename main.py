"""Root launcher for main.py delegating into fire-smoke-detector-yolov8."""
import sys
from pathlib import Path

# Add project package root to sys.path
PROJECT_DIR = Path(__file__).resolve().parent / "fire-smoke-detector-yolov8"
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from main import run_pipeline

if __name__ == "__main__":
    run_pipeline()
