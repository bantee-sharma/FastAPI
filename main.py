from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message" :"Hello world!"}


@app.get('/predict')
def func():
    return {"message":"CampusX is a education platform where we can learn AI"}