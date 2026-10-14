# 🔥 AI-Based Real-Time Fire and Smoke Detection System

An enterprise-grade, modular computer vision system for real-time fire and flame hazard monitoring leveraging fine-tuned **YOLOv8** deep learning, **robust Windows camera hardware backend negotiation (DirectShow / MSMF)**, **hybrid flame chrominance fusion (RGB + HSV)**, **multi-frame temporal confirmation**, **3x3 spatial zone mapping**, **asynchronous SMTP email notifications**, and **persistent SQLite incident auditing**.

[![Tests](https://img.shields.io/badge/Tests-32%20Passed-brightgreen.svg)](fire-smoke-detector-yolov8/tests/)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/YOLOv8-Ultralytics-orange.svg)](https://github.com/ultralytics/ultralytics)
[![UI](https://img.shields.io/badge/Streamlit-1.65.0-red.svg)](https://streamlit.io/)
[![Database](https://img.shields.io/badge/Database-SQLite3-lightgrey.svg)](https://sqlite.org/)

---

## 🚀 How to Run the Frontend (2 Easy Ways)

You can view and interact with the fire detection frontend using **either the Web Dashboard or the Desktop GUI**:

### Option A: Web Dashboard (Streamlit) — Recommended
You can launch the web frontend directly with:
```powershell
.\.venv\Scripts\activate
streamlit run app.py
```
*(Or simply run `python app.py` — it will automatically launch the Streamlit dashboard in your web browser!)*

Features on the **"🔥 Real-Time Fire Display & Monitor"** primary tab:
- **Instant 1-Click Fire Test Station:** Test 4 real fire samples (**Candle Flame**, **Campfire**, **Fireplace**, **Lighter**) with one click and see glowing red bounding boxes, confidence, and alert telemetry immediately!
- **Live Webcam Fire Display:** Stream your local webcam using the robust `CameraSource` manager (DirectShow/MSMF) with real-time fire bounding boxes and instant flashing hazard alert banners.
- **Single Image & Video Inspector:** Upload custom media or select demo video clips (`sample_fire_demo.mp4`).
- **Operator Action Center:** Review active alarms, assign operator notes, **Acknowledge** hazards, and mark incidents **Resolved**.
- **Incident Audit Log:** Persistent SQLite history, UUIDs, multi-criteria filtering (Class, Severity, Status, Camera), and snapshot gallery.

---

### Option B: Standalone Desktop GUI (Native Window)
If you prefer a native desktop window without a browser:
```powershell
.\.venv\Scripts\activate
python gui.py
# or: python app.py --gui
```
Features:
- Native GUI window with live viewport, real-time fire detection, and flashing red hazard badge.
- Instant 1-click fire test buttons for Candle, Campfire, Fireplace, and Lighter flame.
- Start/Stop Webcam button, sensitivity slider, and audio alarm toggle.
- Real-time hazard activity log.

---

## 📧 Automated Email Alerts (.env)

Real-time email alerting for confirmed hazard incidents is optional:
1. Copy `.env.example` to `.env`:
   ```powershell
   copy .env.example .env
   ```
2. Configure your SMTP settings in `.env` (e.g., Gmail, Outlook, or institutional SMTP).
3. If unconfigured, the system runs normally with email alerts safely disabled.

---

## 🛠️ Command-Line Detection (OpenCV Window)

Run live detection on your webcam:
```powershell
python main.py --source 0
```

Run detection with a specific camera identifier:
```powershell
python main.py --source 0 --camera-id cam_warehouse_east
```

Run detection on the preloaded fire demonstration video:
```powershell
python main.py --source fire-smoke-detector-yolov8/data/sample_videos/sample_fire_demo.mp4
```

---

## 🧪 Run Automated Test Suite

Verify all **32 automated unit and integration tests (100% passing)**:
```powershell
.\.venv\Scripts\activate
pytest fire-smoke-detector-yolov8/tests -v
```

---

## 📁 Preloaded Fire Test Samples
The project includes genuine, high-resolution fire test samples located in `fire-smoke-detector-yolov8/data/sample_images/`:
- `candle_fire.jpg`: Sharp candle flame in dark room (YOLO Conf: **82.0%**)
- `lighter_fire.jpg`: Hand holding a lit lighter (YOLO Conf: **81.6%**)
- `fireplace_fire.jpg`: Roaring stone fireplace (YOLO Conf: **50.4%**)
- `campfire_fire.jpg`: Outdoor night campfire with smoke (YOLO Conf: **35.5%**)
- `sample_fire_demo.mp4`: 120-frame video clip of roaring flames for video testing.

---

## ⚠️ Safety & Compliance Disclaimer

> [!CAUTION]
> **RESEARCH AND EARLY-WARNING MONITORING AID ONLY**
> 1. This software application is developed as an academic engineering project for educational and research demonstrations.
> 2. It is **NOT certified** under industrial fire safety standards (e.g., **NFPA 72**, **EN 54**, or **UL 268**) and must never be deployed as the sole or primary life-safety alarm system.
> 3. **NEVER ignite real fires or hazardous materials** to test this software. Always test using computer monitor playback, the provided high-resolution fire image samples (`data/sample_images/`), or pre-recorded video clips.

---

## 📚 College Viva & Technical Documentation
All 12 architecture diagrams, methodology breakdowns, and viva questions are located in:
`fire-smoke-detector-yolov8/docs/`
