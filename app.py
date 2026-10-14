"""
Root launcher for AI Fire & Smoke Detection System.

Supports:
  1. Streamlit Web Dashboard:
     streamlit run app.py
     python app.py --web
     python app.py (default opens browser automatically)

  2. Standalone Desktop GUI:
     python app.py --gui
     python gui.py
"""
import sys
import subprocess
from pathlib import Path

# Add project package root to sys.path
PROJECT_DIR = Path(__file__).resolve().parent / "fire-smoke-detector-yolov8"
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))


def is_running_under_streamlit() -> bool:
    """Check if script is being executed by the Streamlit runner."""
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        return get_script_run_ctx() is not None
    except Exception:
        return False


if is_running_under_streamlit():
    # Executed via 'streamlit run app.py'
    app_path = PROJECT_DIR / "app.py"
    with open(app_path, "r", encoding="utf-8") as f:
        code = compile(f.read(), str(app_path), "exec")
        exec(code, globals())
else:
    # Executed via 'python app.py' directly
    args = sys.argv[1:]
    if "--gui" in args or "--desktop" in args:
        print("[*] Launching Standalone Desktop GUI...")
        from gui import launch_gui
        launch_gui()
    else:
        print("=" * 65)
        print(" 🔥 AI REAL-TIME FIRE & SMOKE DETECTION DASHBOARD ")
        print("=" * 65)
        print("[*] Launching Streamlit Web Dashboard in your browser...")
        print("[*] (Tip: To open Desktop GUI instead, run: python app.py --gui)")
        app_target = str(PROJECT_DIR / "app.py")
        cmd = [sys.executable, "-m", "streamlit", "run", app_target, "--server.headless=false"]
        subprocess.run(cmd)
