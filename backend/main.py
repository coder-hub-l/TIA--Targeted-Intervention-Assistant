from fastapi import FastAPI, HTTPException
from data_engine import load_and_parse_data

app = FastAPI()

# Load data into memory when server starts
# In a real app, you might use a database, but this is perfect for the hackathon
EMPLOYEE_DB = load_and_parse_data()

@app.get("/")
def read_root():
    return {"status": "Server is running", "target_employees": len(EMPLOYEE_DB)}

@app.get("/employee/{emp_id}")
def get_employee_context(emp_id: str):
    """
    Frontend calls this to know what to talk about.
    """
    if emp_id not in EMPLOYEE_DB:
        raise HTTPException(status_code=404, detail="Employee not found or not selected for contact")
    
    return {
        "employee_id": emp_id,
        "top_issues": EMPLOYEE_DB[emp_id],
        "suggested_opener": f"I noticed some trends regarding {EMPLOYEE_DB[emp_id][0].replace('_', ' ')}. How are you feeling about that?"
    }

# To run: uvicorn main:app --reload