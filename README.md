# TIA - Targeted Intervention Assistant

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

TIA is an AI-driven, context-aware retention assistant. It utilizes a custom data pipeline to inject predictive machine learning metrics (SHAP values) directly into a Llama-3 prompt, translating cold HR data into empathetic conversations designed to prevent employee attrition.

## ⚙️ Core Features
1. **Dynamic Context Injection (RAG-lite):** Intercepts user queries and injects employee-specific predictive HR data (SHAP values) directly into the Llama-3 system prompt before generation.
2. **Decoupled Client-Server Architecture:** A lightweight vanilla JavaScript/CSS frontend communicates asynchronously with a scalable Python FastAPI backend via REST endpoints.
3. **Lightning-Fast Inference:** Utilizes the Groq API to run the Llama-3-8b foundation model at near-instant speeds for real-time conversational flow.
4. **Secure Data Handling:** Employs strict CORS middleware and environment variables (`.env`) to ensure API keys and backend logic remain completely hidden from the client side.
5. **Automated Data Parsing:** A custom Python data engine uses Pandas to parse complex, tabular machine learning output into human-readable narrative context on server startup.

## 🏗️ Architecture Stack
* **The Brain (Backend):** Python, FastAPI, Pandas, Groq API (Llama-3-8b). Hosted dynamically on Render.
* **The Face (Frontend):** Vanilla JavaScript, HTML5, CSS3 (Flexbox). Hosted statically on GitHub Pages.
* **The Data:** Pre-computed Machine Learning SHAP values stored securely on the server to guide the LLM's behavioral logic without exposing raw data to the end user.

---

## 🚀 Local Installation & Setup

Want to run TIA on your own machine? Follow these exact steps to get the frontend and backend talking locally.

### Prerequisites
* Python 3.9+
* A free API key from [Groq](https://console.groq.com/)

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/opensoft-bot.git](https://github.com/YOUR_GITHUB_USERNAME/opensoft-bot.git)
cd opensoft-bot
```

### 2. Set Up the Python Backend
Open a terminal inside the project folder and create a virtual environment to install the dependencies safely.

**Windows:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Your Environment Variables
You must securely provide your Groq API key for the LLM to function.
1. Inside the `backend` folder, create a new file named exactly `.env`.
2. Add your Groq API key to the file like this:
```text
GROQ_API_KEY=gsk_your_api_key_here
```

### 4. Start the FastAPI Server
With your virtual environment still active, boot up the local server:
```bash
uvicorn main:app --reload
```
*The backend is now running at`http://127.0.0.1:8000`*

### 5. Launch the Frontend
Because the frontend is pure HTML/CSS/JS, you don't need a complex Node.js server. 
1. Open the `frontend` folder.
2. If you are using VS Code, right-click `index.html` and select **"Open with Live Server"**.
3. Alternatively, simply double-click `index.html` to open it directly in your web browser. 

*(Note: If you are running this locally, ensure the `fetch` URL in `script.js` is pointed to `http://127.0.0.1:8000/chat` instead of the live Render production URL).*

---

## 🏆 Hackathon Context
This project was engineered as a competitive submission for the Preparation of Open Soft GC at IIT Kharagpur organised by the Pt. Madan Mohan Malaviya Hall of Residence and Deloitte. It was designed to showcase the integration of predictive analytics with generative AI to solve real-world corporate retention challenges .
