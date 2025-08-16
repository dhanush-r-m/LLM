import gradio as gr
import requests
import json

def query_ollama(prompt, model="llama3.1:8b"):
    """Query Ollama API with the given prompt"""
    try:
        url = "http://localhost:11434/api/generate"
        data = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        
        response = requests.post(url, json=data)
        response.raise_for_status()
        
        result = response.json()
        return result.get("response", "Sorry, I couldn't generate a response.")
        
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure Ollama is running on localhost:11434"
    except Exception as e:
        return f"Error: {str(e)}"

def tutor_response(user_input, history, subject, level):
    """Generate tutor response based on user input and context"""
    if not user_input.strip():
        return history, history, ""
    
    # Customize prompt based on subject & level
    system_prompt = f"You are a helpful tutor for {subject} at {level} level. Explain concepts step by step in a clear and engaging way. Use examples when helpful."
    full_prompt = system_prompt + "\n\nStudent: " + user_input
    
    # Query the LLM
    reply = query_ollama(full_prompt)
    
    # Add to history
    history.append(("👨‍🎓 " + user_input, "👩‍🏫 " + reply))
    
    return history, history, ""  # Return empty string to clear input

def clear_chat():
    """Clear the chat history"""
    return [], []

# Create Gradio interface
with gr.Blocks(title="LLM Tutor", theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🎓 LLM Tutor with Ollama + Gradio")
    gr.Markdown("Ask questions and get personalized tutoring in your chosen subject!")
    
    with gr.Row():
        subject = gr.Dropdown(
            ["Math", "Physics", "History", "Programming", "Chemistry", "Biology"], 
            label="Choose Subject",
            value="Math"
        )
        level = gr.Dropdown(
            ["Beginner", "Intermediate", "Advanced"], 
            label="Level",
            value="Beginner"
        )
    
    chatbot = gr.Chatbot(height=400, label="Tutor Chat")
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="Ask me a question...", 
            label="Your Question",
            scale=4
        )
        submit_btn = gr.Button("Submit", scale=1, variant="primary")
    
    clear = gr.Button("Clear Chat", variant="secondary")
    
    # State to store chat history
    state = gr.State([])
    
    # Event handlers
    def handle_submit(user_input, history, subject, level):
        return tutor_response(user_input, history, subject, level)
    
    # Submit on button click or Enter key
    submit_btn.click(
        handle_submit, 
        inputs=[msg, state, subject, level], 
        outputs=[chatbot, state, msg]
    )
    
    msg.submit(
        handle_submit, 
        inputs=[msg, state, subject, level], 
        outputs=[chatbot, state, msg]
    )
    
    # Clear chat
    clear.click(
        clear_chat, 
        inputs=None, 
        outputs=[chatbot, state]
    )

if __name__ == "__main__":
    demo.launch()