import gradio as gr
from translator import CodeTranslator
import subprocess
import tempfile
import os

translator = CodeTranslator()

def translate_and_run(python_code):
    cpp_code = translator.translate(python_code)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".cpp") as tmp_cpp:
        tmp_cpp.write(cpp_code.encode("utf-8"))
        cpp_path = tmp_cpp.name

    exe_path = cpp_path.replace(".cpp", ".out")

    try:
        compile_result = subprocess.run(
            ["g++", cpp_path, "-o", exe_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        if compile_result.returncode != 0:
            return cpp_code, f"❌ Compilation Error:\n{compile_result.stderr}"

        run_result = subprocess.run(
            [exe_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        return cpp_code, run_result.stdout if run_result.stdout else "✅ Compiled successfully, but no output."
    except Exception as e:
        return cpp_code, f"⚠️ Error during execution: {str(e)}"
    finally:
        if os.path.exists(cpp_path):
            os.remove(cpp_path)
        if os.path.exists(exe_path):
            os.remove(exe_path)

with gr.Blocks() as demo:
    gr.Markdown("## 🐍➡️💨 Python to C++ Translator (StarCoder)")
    with gr.Row():
        python_input = gr.Code(label="Python Code", language="python")
        cpp_output = gr.Code(label="Generated C++", language="cpp")
    run_output = gr.Textbox(label="Execution Result", lines=5)

    translate_btn = gr.Button("Translate & Run")

    translate_btn.click(
        fn=translate_and_run,
        inputs=python_input,
        outputs=[cpp_output, run_output]
    )

if __name__ == "__main__":
    demo.launch()
