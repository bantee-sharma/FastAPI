from fastapi import FastAPI, Path,requests,HTTPException,Query
import json
app = FastAPI()

def load_data():
    with open("patients.json","rb") as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {"message":"Patients Management System API"}

@app.get("/about")
def about():
    return {"message":'A fully functional API to manage your patient records'}

@app.get("/view")
def view():
    data = load_data()
    return data


@app.get('/patient/{patient_id}')
def search(patient_id: str = Path(..., description="ID of the patient in the DB", example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not found")

@app.get('/sort')
def sort_patients(sort_by:str = que)