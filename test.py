from fastapi import FastAPI,HTTPException,Path
import json

app = FastAPI()

def data_load():
    with open("patients.json",'rb') as f:
        data = json.load(f)
    return data


@app.get('/')
def hello():
    return {"message":"Patients Management System API"}

@app.get('/about')
def about():
    return {"message":'A fully functional API to manage your patient records'}

@app.get("/view")
def view():
    data = data_load()
    return data

@app.get("/patient/{patient_id}")
def patients(patient_id:str=Path(...,description="ID of patient in DB",example='P001')):
    data = data_load()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

