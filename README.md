# 🤖 AI NLP Toolkit with Gemini

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.37+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-4285F4?logo=google&logoColor=white)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A modern, developer-friendly NLP toolkit built on Google Gemini, offering 21+ tasks such as sentiment analysis, translation, summarization, NER, classification, QA, paraphrasing, grammar correction, and more. Comes with a Streamlit UI and a CLI app.

---

## ✨ Features
- 21+ NLP tasks powered by Gemini 2.5 Flash
- Streamlit UI with modern styling and dark theme
- CLI app for quick terminal-driven tasks
- Env-based credential management with `.env`
- Sample inputs reference for faster testing

---

## 🚀 Quick Start

### 1) Clone the repo
```bash
git clone https://github.com/your-org/NLP-Toolkit-with-gen-AI.git
cd NLP-Toolkit-with-gen-AI
```

### 2) Create environment
Using Conda (recommended):
```bash
conda create -n llmapp python=3.11 -y
conda activate llmapp
```

Or with `venv`:
```bash
python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
# Bash
source .venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Configure credentials
Create `.env` in project root:
```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
# Optional for compatibility
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```
Generate key from: https://aistudio.google.com/app/apikey

### 5) Run apps
Streamlit UI:
```bash
streamlit run UI_streamlit.py
```
CLI app:
```bash
python app.py
```

---

## 🧱 Architecture Diagram
```
+------------------------------+
|        Streamlit UI          |
|  (UI_streamlit.py)           |
|   - Auth (Session State)     |
|   - Task Select + Prompts    |
|   - Results Renderer (CSS)   |
+---------------+--------------+
                |
                v
+------------------------------+
|         Gemini Client        |
|  google.generativeai         |
|  - Config from .env          |
|  - Model: gemini-2.5-flash   |
+---------------+--------------+
                |
                v
+------------------------------+
|            Core App          |
|         (app.py CLI)         |
|  - Menus & Task Handlers     |
|  - Calls Gemini via Client   |
+------------------------------+
```

---

## 📁 Folder Structure
```
NLP-Toolkit-with-gen-AI/
├─ LICENSE
├─ README.md
├─ requirements.txt
├─ .env                    # your API keys (not committed)
├─ UI_streamlit.py         # Streamlit UI app
├─ app.py                  # CLI app
├─ reserach/               # notebooks & experiments
│  └─ test.ipynb
├─ SAMPLE_INPUTS.md        # curated sample texts
```

---

## 🧪 Supported NLP Tasks
- Sentiment Analysis
- Language Translation (English → Bangla)
- Language Detection
- Text Summarization
- Keyword Extraction
- Named Entity Recognition (NER)
- Part-of-Speech Tagging
- Topic Modeling
- Text Classification
- Question Answering
- Text Generation
- Emotion Detection
- Intent Detection
- Paraphrase Detection
- Text Paraphrasing
- Grammar Correction
- Hate Speech Detection
- Spam Detection
- Fake News Detection
- Text Simplification
- Opinion Mining

For sample inputs, see: `SAMPLE_INPUTS.md`.

---

## ⚙️ Configuration Notes
- Ensure `.env` has `GOOGLE_API_KEY` without spaces around `=` (e.g., `GOOGLE_API_KEY=...`).
- If using Conda, always `conda activate llmapp` before running.
- The UI renders results in a dark card; adjust CSS under `UI_streamlit.py` if needed.

---

## 🧰 Tech Stack
- Python 3.11
- Streamlit 1.37+
- google-generativeai 0.8+
- python-dotenv

---

## 🔒 Security
- Do not commit `.env` or API keys to source control.
- Rotate keys periodically and follow least-privilege practices.

---

## 📝 License
This project is licensed under the MIT License. See `LICENSE` for details.

## Author
MD UZZAL MIA
