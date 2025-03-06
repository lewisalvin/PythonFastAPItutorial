from fastapi import FastAPI, Path

#Create instance of fastAPI
app = FastAPI()

patients = {
    1: {
        "name": "braxton",
        "age": 4,
        "trach": "cuffless"
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-patient/{patient_id}")
def get_patient(patient_id: int = Path(description="The ID of the patient you want to view", gt=0, lt=3)):
    return patients[patient_id]