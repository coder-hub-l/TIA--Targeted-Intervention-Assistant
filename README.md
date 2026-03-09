# TIA - Targeted Intervention Assistant
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
<p>TIA is a context-aware HR chatbot designed to understand employee sentiment using the data a company already collects. By injecting predictive machine learning data (SHAP values) into a dynamic Llama-3 pipeline, TIA drives personalized conversations to uncover why employees want to leave and helps retain top talent.</p>
**## Features**
  
1.Dynamic Context Injection (RAG-lite): Intercepts user queries and injects employee-specific predictive HR data (SHAP values) directly into the Llama-3 system prompt before generation.
2.Decoupled Client-Server Architecture: A lightweight vanilla JavaScript/CSS frontend communicates asynchronously with a scalable Python FastAPI backend via REST endpoints.
3.Lightning-Fast Inference: Utilizes the Groq API to run the Llama-3-8b foundation model at near-instant speeds for real-time conversational flow.
4.Secure Data Handling: Employs strict CORS middleware and environment variables (.env) to ensure API keys and backend logic remain completely hidden from the client side.
5.Automated Data Parsing: A custom Python data engine uses Pandas to parse complex, tabular machine learning output into human-readable narrative context on server startup.
