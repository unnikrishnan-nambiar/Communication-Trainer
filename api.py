from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import shutil
from training import chat_trainer
from database import progress_db
from llm_wrapper import get_llm  # ✅ Use llm_wrapper (Ollama)

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure upload directory exists

@app.get("/scenario/{category}")
async def get_scenario(category: str):
    """Retrieve a pre-defined scenario from the YAML file."""
    scenario = chat_trainer.get_random_scenario(category)
    return {"scenario": scenario}

@app.post("/chat/{category}")
async def chat_with_ai(
    category: str,
    username: str = Form(...),
    model_name: str = Form("mistral"),  # ✅ Allow user to choose between DeepSeek & Mistral
    user_audio: UploadFile = File(None)
):
    """Process speech input and return AI-generated feedback."""
    if not user_audio:
        raise HTTPException(status_code=400, detail="No audio file provided.")

    file_path = os.path.join(UPLOAD_DIR, user_audio.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(user_audio.file, buffer)

    feedback, score = chat_trainer.evaluate_response(file_path, username, category, model_name)

    return {"feedback": feedback, "score": score}

@app.get("/progress/{username}")
async def get_user_progress(username: str):
    """Retrieve all stored progress for a specific user in a structured format."""
    progress_data = progress_db.get_user_progress(username)

    if not progress_data:
        return {"progress": []}

    # Convert database records into structured data
    structured_progress = []
    for row in progress_data:
        structured_progress.append({
            "Date": row[0],  # ✅ Correctly mapped timestamp
            "Category": row[1],  # ✅ Category column
            "Scenario": row[2],  # ✅ Scenario column
            "Score": row[3]  # ✅ Score column
        })

    return {"progress": structured_progress}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
