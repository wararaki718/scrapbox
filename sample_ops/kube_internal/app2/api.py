from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def hello():
    return "hello"


@app.get("/hello")
def hello2():
    response = requests.get("http://app:8000/")
    return f'{response.text}, world!'
