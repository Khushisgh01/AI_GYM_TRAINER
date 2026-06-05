# AI GYM TRAINER — AI Real‑time GYM Coach

A Python + Streamlit project that sets up an **AI-powered real-time Gym Coach**.  
This repository follows a clean, scalable structure (`core/`, `detectors/`, `services/`, `ml_models/`, `static/`) so you can gradually add pose detection (MediaPipe), video processing (OpenCV), AI coaching (Groq), tracking (Pandas), and voice feedback (gTTS).

---

## Contents

- [Demo / First Run](#demo--first-run)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Local Setup (Video1 Steps)](#local-setup-video1-steps)
- [How to Run](#how-to-run)
- [Environment Variables (.env)](#environment-variables-env)
- [Important Note: `__init__.py` (Python Package)](#important-note-initpy-python-package)
- [Common Errors & Fixes](#common-errors--fixes)
- [Best Practices](#best-practices)
- [Roadmap (Suggested)](#roadmap-suggested)
- [License](#license)

---

## Demo / First Run

Once setup is done, running the app shows:

- Page title: **AI GYM Coach**
- Title: **🏋️ AI Real-time GYM Coach**
- Text: **Setup successful!**

---

## Tech Stack

**Core**
- Python

**UI**
- `streamlit==1.54.0`

**Real-time Camera / WebRTC**
- `streamlit-webrtc==0.64.5`

**Computer Vision / Pose**
- `mediapipe==0.10.14`
- `opencv-python-headless==4.10.0.84`

**Data & Tracking**
- `pandas==2.2.3`

**AI Coaching (Optional)**
- `groq>=0.12.0`

**Voice**
- `gtts==2.5.3`

**Environment Config**
- `python-dotenv==1.2.2`

**Tooling**
- `uv` (fast venv + dependency installer)

---

## Project Structure

After completing Video1 steps, your repo will typically look like:

```text
AI_GYM_TRAINER/
├─ main.py
├─ requirements.txt
├─ .env
├─ core/
│  └─ __init__.py
├─ detectors/
│  └─ __init__.py
├─ services/
│  ├─ __init__.py
│  ├─ auth/
│  ├─ coaching/
│  ├─ config/
│  ├─ persistence/
│  ├─ state/
│  ├─ tracking/
│  ├─ ui/
│  └─ vision/
│     └─ __init__.py
├─ static/
└─ ml_models/
   └─ __init__.py
```

**What each folder is for**
- `core/` → shared helpers, constants, types
- `detectors/` → pose detector, rep counter, posture checks
- `services/` → app logic split into modules (vision, coaching, tracking, config, etc.)
- `ml_models/` → any ML models / weights / wrappers
- `static/` → CSS / assets (Streamlit styling, images)

---

## Local Setup (Video1 Steps)

### STEP 1: Create Project Folder

```bash
mkdir folder-name
cd folder-name
```

### STEP 2: Install `uv`

```bash
pip install uv
# OR
pip3 install uv

uv --version
```

### STEP 3: Create Virtual Environment

```bash
uv venv
```

Activate the venv:

**Mac / Linux**
```bash
source .venv/bin/activate
```

**Windows**
```bat
.venv\Scripts\activate
```

### STEP 4: Install Required Packages

Install from `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

Your `requirements.txt` should contain:

```txt
streamlit==1.54.0
streamlit-webrtc==0.64.5
mediapipe==0.10.14
opencv-python-headless==4.10.0.84
pandas==2.2.3
groq>=0.12.0
gtts==2.5.3
python-dotenv==1.2.2
```

### STEP 5: Setup `.env` file

Create a file named `.env` in the root directory.

Example `.env` (safe template):

```env
# App
APP_NAME="AI GYM Coach"

# Groq (only if you use Groq in code)
GROQ_API_KEY=""
GROQ_MODEL="llama-3.1-70b-versatile"

# Optional settings for future use
CAMERA_INDEX=0
```

> Tip: Add `.env` to `.gitignore` so you never push secrets.

### STEP 6: Create Basic Folder Structure

Create directories:

```bash
mkdir core detectors services static ml_models
mkdir services/auth services/coaching services/config services/persistence services/state services/tracking services/ui services/vision
```

Create `__init__.py` files (Windows PowerShell):

```powershell
$null > core\__init__.py
$null > detectors\__init__.py
$null > services\__init__.py
$null > ml_models\__init__.py
$null > services\vision\__init__.py
```

### STEP 7: Add `main.py`

Create `main.py` in project root:

```python
import streamlit as st

st.set_page_config(page_title="AI GYM Coach")

st.title("🏋️ AI Real-time GYM Coach")
st.write("Setup successful!")
```

### STEP 8: First run

Run Streamlit using `uv`:

```bash
uv run streamlit run main.py
```

---

## How to Run

From the project root:

```bash
uv run streamlit run main.py
```

Streamlit will print a local URL (usually `http://localhost:8501`).

---

## Environment Variables (.env)

This project uses a `.env` file for configuration (recommended). Create it in the project root.

### Suggested variables

| Variable | Required | Example | Purpose |
|---|---:|---|---|
| `APP_NAME` | Optional | `"AI GYM Coach"` | App display name / configuration |
| `GROQ_API_KEY` | Optional* | `"gsk_..."` | Groq API key for AI coaching |
| `GROQ_MODEL` | Optional | `"llama-3.1-70b-versatile"` | Groq model selection |
| `CAMERA_INDEX` | Optional | `0` | Default camera device index |

\* Required only if you add Groq-based coaching features.

### Loading `.env` in code (when you add config)

When you start using environment variables in Python, you will typically load them like:

```python
from dotenv import load_dotenv
import os

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY", "")
```

---

## Important Note: `__init__.py` (Python Package)

**Jaise hi aap `__init__.py` file kisi folder me create karte ho, uska matlab hota hai that folder is treated as a Python package.**

### Why it matters
- You can import modules cleanly across folders (recommended for scalable projects).
- It reduces import errors when the project grows into multiple files.

Example imports you’ll use later:

```python
from services.vision.camera import get_camera_stream
from detectors.pose_detector import PoseDetector
```

---

## Common Errors & Fixes

### 1) `ModuleNotFoundError: No module named ...`
**Cause:** Virtual environment not activated OR packages not installed.

**Fix:**
```bash
# activate venv first
# then:
uv pip install -r requirements.txt
```

### 2) Streamlit command works but app doesn’t open
**Fix:**
- Check the terminal logs (Streamlit prints the error).
- Confirm you’re running from the project root (where `main.py` exists).

Run again:
```bash
uv run streamlit run main.py
```

### 3) Port already in use
**Fix:** Run on a different port:
```bash
uv run streamlit run main.py --server.port 8502
```

### 4) Camera not working (when you add webcam)
**Fix checklist:**
- Allow camera permission in browser
- Ensure no other application is using the webcam
- Try different camera index in `.env`:
  ```env
  CAMERA_INDEX=1
  ```

### 5) OpenCV issues
You are using `opencv-python-headless` (good for servers / Docker).  
If you later need full GUI support locally, you may switch to:
- `opencv-python` (instead of headless)

(Only do this if needed, because headless is usually more stable on deployment.)

---

## Best Practices

### 1) Keep code modular
As the project grows:
- Keep Streamlit UI in `main.py`
- Put logic inside:
  - `services/` (app logic)
  - `detectors/` (pose + exercise detection)
  - `core/` (shared utilities/types)

### 2) Do not commit secrets
Add these to `.gitignore`:
```gitignore
.venv/
.env
__pycache__/
*.pyc
.DS_Store
```

### 3) Keep dependencies pinned
Pin versions in `requirements.txt` to avoid “works on my machine” issues.

### 4) Add logging early (recommended)
When you start adding vision + AI features, logs help a lot:
- rep counting debugging
- model outputs
- API responses

---

## Roadmap (Suggested)

You can build the project step-by-step:

### Phase 1 — UI + Webcam
- [ ] Add webcam stream using `streamlit-webrtc`
- [ ] Show live frame preview in the Streamlit UI

### Phase 2 — Pose Detection
- [ ] Use `mediapipe` pose landmarks
- [ ] Draw pose landmarks on frames (OpenCV)

### Phase 3 — Gym Coaching Logic
- [ ] Detect exercise type (squat, push-up, etc.)
- [ ] Count reps based on joint angles
- [ ] Provide posture feedback (e.g., “Back straight”, “Knees aligned”)

### Phase 4 — AI Coach (Groq)
- [ ] Add a “Coach Chat” / feedback panel
- [ ] Generate tips based on detected exercise + form issues

### Phase 5 — Voice Feedback
- [ ] Convert feedback to speech using `gTTS`
- [ ] Play audio in Streamlit

### Phase 6 — Tracking + Persistence
- [ ] Track session stats with `pandas`
- [ ] Save session logs (CSV/SQLite) in `services/persistence`

---

## License
MIT

## Author / Contact

- GitHub: `@Khushisgh01`
