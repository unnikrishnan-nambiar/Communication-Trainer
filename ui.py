import gradio as gr
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def get_scenario(category):
    """Fetch a scenario based on selected category."""
    response = requests.get(f"{API_URL}/scenario/{category}")
    return response.json().get("scenario", "Error retrieving scenario.")

def chat_with_ai(username, category, model_name, user_audio):
    """Send speech input to the AI and receive feedback."""
    if user_audio is None:
        return "Please record your response before submitting.", None

    files = {'user_audio': open(user_audio, 'rb')}
    data = {"username": username, "category": category, "model_name": model_name}
    
    response = requests.post(f"{API_URL}/chat/{category}", files=files, data=data)
    data = response.json()

    return data.get("feedback", "Error processing response."), f"Score: {data.get('score', 0)}/100"

def get_progress(username):
    """Fetch user progress and format as a DataFrame."""
    response = requests.get(f"{API_URL}/progress/{username}")
    progress_data = response.json().get("progress", [])

    if not progress_data:
        return pd.DataFrame(columns=["Date", "Category", "Scenario", "Score"])

    # Convert progress data to a structured DataFrame
    df = pd.DataFrame(progress_data)
    df.columns = ["Date", "Category", "Scenario", "Score"]  # Ensure correct column mapping
    return df

with gr.Blocks() as demo:
    gr.Markdown("#VERBAL COMMUNICATION TRAINER")

    username_input = gr.Textbox(label="Enter Your Username")
    category_selector = gr.Radio(
        ["impromptu", "storytelling", "conflict"], label="Select Training Category"
    )
    model_selector = gr.Dropdown(["mistral", "llama", "falcon"], label="Select LLM Model", value="mistral")
    
    scenario_text = gr.Textbox(label="Generated Scenario", interactive=False)
    get_scenario_button = gr.Button("Get Scenario")

    audio_input = gr.Audio(type="filepath", label="Record Your Response")

    feedback_text = gr.Textbox(label="AI Feedback", interactive=False)
    score_text = gr.Textbox(label="Score", interactive=False)
    submit_response_button = gr.Button("Submit Response")

    gr.Markdown("## User Progress 📈")
    progress_table = gr.Dataframe(headers=["Date", "Category", "Scenario", "Score"], interactive=False)
    view_progress_button = gr.Button("View Progress")

    # Event Bindings
    get_scenario_button.click(get_scenario, inputs=category_selector, outputs=scenario_text)
    submit_response_button.click(chat_with_ai, inputs=[username_input, category_selector, model_selector, audio_input], outputs=[feedback_text, score_text])
    view_progress_button.click(get_progress, inputs=username_input, outputs=progress_table)

demo.launch()
