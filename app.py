from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message":"hello world"}

@app.get("/predict")
def hii():
    return "Predict the value"