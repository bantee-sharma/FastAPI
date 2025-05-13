from flask import Flask,request

app = Flask(__name__)


@app.route("/")
def hello():
    return {"messege":"welcome to flask"}


@app.route("/pred",methods = ["GET","POST"])
def hiii():
    if request.method == "GET":
        return {"messege":"CampusX is a Education platform where we can learn AI"}
    else:
        return "We are going to predict future values"