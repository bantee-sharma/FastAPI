from fastapi import FastAPI
import json

app = FastAPI()

def data_load():
    with open("patient.json",'rb') as f:
        data = data_load()
    return data


@app.get('/')
def hello():
    return {"message":"Patients Management System API"}

@app.get('/about')
def about():
    return {"message":'A fully functional API to manage your patient records'}

