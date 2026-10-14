# 🚀 Deployment Guide: AI Real-Time Fire and Smoke Detection

This handbook provides step-by-step instructions to deploy your **AI-Based Real-Time Fire and Smoke Detection System** for college project reviews, portfolio demonstrations, and production monitoring.

---

## ⚡ Deployment Options Summary

| Method | Cost | Best For | Camera Support | Setup Time |
| :--- | :--- | :--- | :--- | :--- |
| **1. Streamlit Community Cloud** | Free | College Viva, Resume, Online Demo | Browser / Phone Camera + Safe 1-Click Samples | ~3 mins |
| **2. Hugging Face Spaces** | Free | AI/ML Showcase, Portfolio | Browser / Phone Camera + Safe 1-Click Samples | ~4 mins |
| **3. Docker / Render / Railway** | Free / Low | Cloud Servers, Linux VMs, AWS | Browser Camera / RTSP Streams | ~5 mins |
| **4. Cloudflare Tunnel / Ngrok** | Free | Instant Live Public URL from Laptop | Local Webcam + Browser Camera | ~1 min |
| **5. College LAN / Wi-Fi** | Free | Offline Demonstration in College Lab | Direct Local USB Webcam | Instant |

---

## Method 1: Streamlit Community Cloud (Recommended & 100% Free)

Streamlit Community Cloud is the standard, easiest way to deploy Streamlit applications directly from GitHub.

### Step 1: Commit and Push to GitHub
Open PowerShell in your project directory and run:
```powershell
git add .
git commit -m "Prepare deployment configuration: packages.txt, Dockerfile, and dual camera support"
git push origin main
```

### Step 2: Sign In to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Click **Sign in with GitHub** and authorize Streamlit.

### Step 3: Deploy the App
1. Click the **"New app"** button.
2. Select your repository: `BharathiS26/fire-smoke-detector-yolov8`
3. Set **Branch:** `main`
4. Set **Main file path:** `app.py`
5. Click **"Deploy!"**

### Step 4: Your Live URL
Within 2-3 minutes, Streamlit installs dependencies and launches your app with a permanent public link:
`https://<your-custom-name>.streamlit.app`

> **Note on Camera in the Cloud:** Cloud servers have no physical USB webcam attached. Your app has built-in **Browser/Mobile Camera Mode** (`st.camera_input`). When opened on a phone or laptop, visitors click "Capture Live Surveillance Frame" to test detection directly through their device's camera!

---

## Method 2: Hugging Face Spaces (Free AI Cloud Hosting)

Hugging Face Spaces is popular for machine learning projects and provides generous free CPU tiers.

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces) and create a free account.
2. Click **"Create new Space"**.
3. Choose:
   - **Space name:** `fire-smoke-detection-ai`
   - **Space SDK:** `Streamlit`
   - **Hardware:** Free 2 vCPU / 16GB RAM
4. Clone the Hugging Face repository or push your existing files:
```powershell
git remote add hf https://huggingface.co/spaces/<your-hf-username>/fire-smoke-detection-ai
git push hf main
```
5. Hugging Face automatically detects `requirements.txt` and `packages.txt` and builds your live public demo.

---

## Method 3: Docker Container Deployment (Local or Cloud VM)

Use Docker to deploy on any server (Render, Railway, AWS EC2, DigitalOcean, Azure, or locally).

### 1. Build the Docker Image
```bash
docker build -t fire-smoke-ai .
```

### 2. Run the Container
```bash
docker run -d -p 8501:8501 --name fire_smoke_container fire-smoke-ai
```

### 3. Or Run with Docker Compose (With Data Volume Persistence)
```bash
docker compose up -d
```
Access the dashboard at `http://localhost:8501`.

---

## Method 4: Instant Public URL with Cloudflare Tunnel (Zero Setup)

If your app is already running on your laptop and you want an **instant, free, secure HTTPS public URL** to share right now (without pushing to GitHub or signing up for cloud hosting):

1. Download the single-file Cloudflare Tunnel executable:
   [https://github.com/cloudflare/cloudflared/releases/latest](https://github.com/cloudflare/cloudflared/releases/latest) (or run `winget install --id Cloudflare.cloudflared`).
2. Run your app locally:
```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.port 8501
```
3. Open a second PowerShell window and run:
```powershell
cloudflared tunnel --url http://localhost:8501
```
4. Cloudflare outputs a free temporary public URL (e.g. `https://random-words.trycloudflare.com`). Anyone in the world can open that link and test your app live!

---

## Method 5: Share Over College Wi-Fi / LAN (Local Presentation)

To present the project in a college lab or classroom so professors and evaluators can open it on their phones or laptops connected to the same Wi-Fi:

1. Find your laptop's local IP address:
```powershell
ipconfig
# Look for IPv4 Address under Wireless LAN adapter Wi-Fi (e.g., 192.168.1.36)
```
2. Start Streamlit bound to all interfaces (`0.0.0.0`):
```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```
3. Anyone on the same Wi-Fi opens their browser and navigates to:
   `http://192.168.1.36:8501`

---

## 🛡️ Pre-Flight Verification Checklist

Before presenting or submitting your deployed link, verify:

- [x] **YOLOv8 Weights:** `models/fire_smoke_best.pt` is committed in the repository.
- [x] **System Libraries:** `packages.txt` exists (`libgl1`, `libglib2.0-0` for OpenCV).
- [x] **Streamlit Config:** `.streamlit/config.toml` has `headless = true`.
- [x] **False Positive Suppression:** Verified on orange objects/colors.
- [x] **Test Suite:** All 33 unit and integration tests passing (`pytest tests -v`).
- [x] **Dual Camera Support:** Supports both Local USB Webcam and Cloud Browser Camera.
