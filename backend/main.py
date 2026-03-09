import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

from data_engine import load_and_parse_data

app = FastAPI()
app.add_middleware(CORSMiddleware,
                    allow_origins=['*'],
                    allow_credentials=['*'],
                    allow_methods=['*'],
                    allow_headers=['*'],
                    )


# Load data into memory when server starts  
# In a real app, you might use a database, but this is perfect for the hackathon
EMPLOYEE_DB = load_and_parse_data()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API Key not found! Check your .env file.")

groq_client = Groq(api_key=api_key)
class ChatRequest (BaseModel):
   employee_id : str
   message : str

@app.get("/")
def home():
    return {"status" : "Aive",
            "Targets loaded" : f"{len(EMPLOYEE_DB)}"} 


@app.post("/chat")
def chat_with_bot(request : ChatRequest):
        emp_id = request.employee_id
        usr_msg = request.message
        top_issues = EMPLOYEE_DB[request.employee_id]

        prompt = f"""
    You are an empathetic HR Assistant for Deloitte named TIA. 
    You are talking to an employee who might be feeling disengaged.
    According to our internal data, their top areas of concern are: {', '.join(top_issues)}.
    
    Rules:
    1. Be warm, conversational, and supportive. Keep it brief (2-3 sentences max).
    2. Do NOT mention the raw data, "SHAP values", or the specific feature names directly.
    3. Gently steer the conversation to ask how they are feeling about those specific areas of concern.
    
    The employee just said: "{usr_msg}"
    
    Respond directly to the employee:"""
        
    
        try:
            chat_completion=groq_client.chat.completions.create(
                messages = [ {"role" : "system","content" : prompt},
                              {"role" : "user"  , "content" : usr_msg}
                            ],
                model="llama-3.1-8b-instant"
                            )
            response = chat_completion.choices[0].message.content
            
            return {"bot_response": response}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    


# To run: uvicorn main:app --reload