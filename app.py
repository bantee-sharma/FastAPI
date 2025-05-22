from fastapi import FastAPI, Path,requests,HTTPException,Query
import json
from pydantic import BaseModel,Field
from typing import Annotated

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[int, Field(...,description="ID of the Patient",examples=["P001"])]
    name: Annotated[str, Field(...,description="Name of patient")]
    city:str = Field(description="City name of patient")
    age:int = Annotated
    gender:str
    height:float
    weight:float

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

def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_fields}')
    
    if order not in ["acs",'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data


