# 📘 LLM Tutor

LLM Tutor is a simple AI-powered tutoring system built with [Ollama](https://ollama.ai/) and [Gradio](https://www.gradio.app/).  
It provides an interactive interface for learners to chat with a local LLM.

---

## 🚀 Features
- Clean Gradio web UI
- Chat with Ollama LLM
- Modular code structure for easy extension

---

## 📂 Project Structure
```
llm-tutor/
├─ app.py # Backend
│ ├─ tutor.py # Gradio UI
```

---

## ⚡ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/llm-tutor.git
   cd llm-tutor
   ```
2. Activate the Virtual Environment
   ```
   Create a virtual environment & install dependencies:

   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)

   pip install -r app/requirements.txt
   ```
3. Run the App
   ```
   python tutor.py
   ```
4. Make sure you have Ollama installed and a model pulled (e.g., llama2):
   ```
   ollama run llama2
   ```

---
## 👨‍💻 Author

    Dhanush Moolemane
    💡 Passionate about AI, ML, and building intelligent tutoring systems.
    🔗 GitHub | LinkedIn
---

