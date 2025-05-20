from fastapi import FastAPI,HTTPException,Path,Query
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
def patient(patient_id:str=Path(...,description="ID of Patient in DB",example="P001")):
    data = data_load()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not foun")

@app.get("/sort")
def sort(sort_by:str = Query(...,description="sort on the basis of height,weight and bmi"), order:str=Query("asc",description="sort in asc and desc order")):

    valid_fields = ["height","weight","bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid Field select from {valid_fields}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail=f"Invalid order select between asc and desc")

