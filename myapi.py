from fastapi import FastAPI

#Create instance of fastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}