# AI Speech Trainer - Verbal Communication Skills Enhancement

This project is an AI-powered verbal communication trainer that helps users improve their speech skills using Mistral-7B and DeepSeek-R1 LLMs.

## Features
- Supports Ollama for local AI model inference (Fast & Free)  
- Provides chat & voice-based training  
- Offers three skill training modules:
  - Impromptu Speaking  
  - Storytelling  
  - Conflict Resolution  
- AI-generated real-time feedback on clarity, engagement, and structure  
- Tracks user progress and scoring using SQLite database  
- Interactive Gradio UI and FastAPI Backend  

## Installation Guide

### 1. Install Python
Python 3.8 or higher is required for this project.

#### Windows Installation
1. Download the latest Python installer from [python.org](https://www.python.org/downloads/)
2. Run the installer and check:
   - "Add Python to PATH"
   - "Install pip"
   - "Install for all users" (recommended)
3. Click "Install Now" and wait for the installation to complete
4. Verify the installation by opening Command Prompt (cmd) and typing:
   ```sh
   python --version
   pip --version
   ```

#### macOS Installation
1. Using Homebrew (recommended):
   ```sh
   brew install python
   ```
   
   Or download from [python.org](https://www.python.org/downloads/macos/)
2. Verify installation:
   ```sh
   python3 --version
   pip3 --version
   ```

#### Linux Installation
For Ubuntu/Debian:
```sh
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

For Fedora/RHEL/CentOS:
```sh
sudo dnf install python3 python3-pip
```

Verify installation:
```sh
python3 --version
pip3 --version
```

### 2. Create a Virtual Environment
Using virtual environments helps isolate project dependencies and prevents conflicts.

#### Windows
```sh
# Navigate to your project directory
cd path\to\AI-Speech-Trainer

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Your command line should now show (venv) at the beginning
```

#### macOS/Linux
```sh
# Navigate to your project directory
cd path/to/AI-Speech-Trainer

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Your command line should now show (venv) at the beginning
```

#### Installing Dependencies
With your virtual environment activated:
```sh
pip install -r requirements.txt
```

### 3. Install Ollama (For Local AI Models)
Ollama is required for running Mistral-7B and DeepSeek-R1 models locally.

#### Windows Installation Steps
1. Download Ollama from the official website: [https://ollama.com](https://ollama.com)  
2. Run the installer (`.exe`) and follow the installation instructions.
3. Verify the installation by opening Command Prompt (`cmd`) and running:
   ```sh
   ollama --version
   ```
   If installed correctly, it will display the Ollama version.

#### macOS/Linux Installation
```sh
curl -fsSL https://ollama.com/install.sh | sh
```

### 4. Download AI Models Locally
Once Ollama is installed, pull the required models:

```sh
ollama pull mistral
ollama pull deepseek-r1
```
This ensures the models run locally without internet dependency.

### 5. Run the Application
#### Start the FastAPI Backend
With your virtual environment activated:
```sh
python api.py
```
The backend will start at http://localhost:8000

#### Start the Gradio UI
In a new terminal, with your virtual environment activated:
```sh
python ui.py
```
The web-based UI will be available at http://localhost:7860

## Features & How It Works

### 1. Skill Training Modules
Users can select from three training categories:

- **Impromptu Speaking**: AI provides a random topic and evaluates response structure.
- **Storytelling**: AI assesses narrative quality and engagement.
- **Conflict Resolution**: AI provides a scenario and evaluates diplomatic response.

### 2. Chat and Voice-Based Interaction
- Users record their speech using the UI.
- AI analyzes the response using DeepSeek-R1 or Mistral.
- Feedback includes clarity, engagement, and structure improvements.

### 3. AI Feedback and Scoring
- AI assigns scores (0-100) based on response quality.
- Feedback includes tips for improvement.
- User progress is tracked and can be viewed in the UI.

## API Endpoints (FastAPI)

### 1. Get a Scenario
Retrieve a speaking scenario based on the selected category.

```sh
GET /scenario/{category}
```
Example:
```sh
curl -X GET "http://localhost:8000/scenario/impromptu"
```

### 2. Submit Speech and Get AI Feedback
Users submit recorded speech, and AI provides feedback and scores.

```sh
POST /chat/{category}
```
Example:
```sh
curl -X POST "http://localhost:8000/chat/storytelling" \
     -F "username=JohnDoe" \
     -F "model_name=mistral" \
     -F "user_audio=@audio.wav"
```

### 3. View User Progress
Get progress history (scores, feedback) for a user.

```sh
GET /progress/{username}
```
Example:
```sh
curl -X GET "http://localhost:8000/progress/JohnDoe"
```

## Folder Structure
```
📂 AI-Speech-Trainer
│── api.py           # FastAPI Backend
│── ui.py            # Gradio UI
│── training.py      # Training Logic (Scenario Selection, AI Feedback)
│── database.py      # SQLite Progress Tracking
│── llm_wrapper.py   # Ollama-Based LLM Handling
│── config.yaml      # Predefined Scenarios
│── uploads/         # Stores User Audio
│── models/          # Local AI Models (Ollama)
│── stt.py           # Speech-to-Text (Whisper)
│── tts.py           # Text-to-Speech (pyttsx3)
│── requirements.txt # Python Dependencies
│── .gitignore       # Files to Ignore in Git
│── README.md        # Project Documentation
```
## Troubleshooting
- **"Python is not recognized as an internal or external command"**: Make sure Python is added to your PATH. You may need to reinstall Python and check the "Add Python to PATH" option.
- **Dependency errors**: Make sure your virtual environment is activated when installing dependencies and running the application.
- **Ollama connection error**: Ensure Ollama is running in the background. You can start it manually if needed.
- **Audio recording issues**: Check your microphone permissions and settings in your operating system.

## Future Improvements
- Support for more LLMs (GPT-4-All, Mixtral)
- Enhanced speech analysis (detect filler words, speech rate)
- More leaderboard features (track improvements over time)

## Credits and Acknowledgments
This project is built using:
- Ollama for LLM-based speech evaluation
- Gradio for an interactive UI
- FastAPI for backend API
- DeepSeek-R1 and Mistral models for AI feedback

Project by: [Unnikrishnan Nambiar  
Contact: [unnikrishnan.b.nambiar@gmail.com]

## License
This project is licensed under the MIT License.
Feel free to modify and use it for non-commercial purposes.
