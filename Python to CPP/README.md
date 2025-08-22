# 🐍➡️💨 Python to C++ Translator (StarCoder + Gradio)

This project uses the open-source **[StarCoder](https://huggingface.co/bigcode/starcoder)** model to automatically translate Python code into **C++**, with an interactive **Gradio UI**.  
It can also compile & run the generated C++ safely inside a **Docker sandbox**.  

---

## 🚀 Features
- Translate **Python → C++** using StarCoder
- Interactive **Gradio UI** (code editor + output panel)
- **Compile & execute** generated C++ automatically
- Runs safely inside **Docker** (sandbox execution)

---

## 📂 Project Structure
```
python-to-cpp/
│── app.py # Main Gradio app
│── translator.py # Model inference + translation
│── requirements.txt # Python dependencies
│── Dockerfile # Container setup
│── docker-compose.yml # Optional orchestration
│── README.md # Project documentation

```


---

## 🛠️ Installation

### 1. Clone the repo
```bash
cd python-to-cpp
```

### 2. Install dependencies (local run)
```
pip install -r requirements.txt
```

### 3. Run the app
```
python app.py
```

Open 👉 http://localhost:7860

---

## 🐳 Docker Setup (Recommended for Safety)
```
Build image
docker build -t python-to-cpp .

Run container
docker run -p 7860:7860 python-to-cpp


Or using docker-compose:

docker-compose up --build
```

## 🖼️ Demo UI

Left panel → Write Python code

Right panel → Translated C++ code

Output box → Compilation or execution result\

## 👨‍💻 Author

Built by Dhanush Moolemane