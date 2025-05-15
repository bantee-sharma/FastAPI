from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message":"Patients Management System API"}

@app.get("/predict")
def about():
    return {"message":'A fully functional API to manage your patient records'}