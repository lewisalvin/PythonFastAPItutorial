from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

#Create instance of fastAPI
app = FastAPI()

patients = {
    1: {
        "name": "braxton",
        "age": 4,
        "trach": "cuffless"
    }
}

class Patient(BaseModel):
    name: str
    age: int
    trach: str

class UpdatePatient(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    trach: Optional[str] = None

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-patient/{patient_id}")
def get_patient(patient_id: int = Path(description="The ID of the patient you would like to view", gt=0, lt=3)):
    return patients[patient_id]

@app.get("/patient-by-name/{patient_id}")
def get_patient(*, patient_id: int, name: Optional[str] = None):
    for patient_id in patients:
        if patients[patient_id]["name"] == name:
            return patients[patient_id]
    return {"Data": "No data found."}

@app.post("/create-patient/{patient_id}")
def create_patient(patient_id: int, patient: Patient):
    if patient_id in patients:
        return {"Error": "Student exists."}
    
    patients[patient_id] = patient
    return patients[patient_id]

@app.put("/update-patient/{patient_id}")
def update_patient(patient_id: int, patient: UpdatePatient):
    if patient_id not in patients:
        return {"Error": "Patient does not exist."}
    
    if patient.name != None:
        patients[patient_id].name = patient.name

    if patient.age != None:
        patients[patient_id].age = patient.age

    if patient.trach != None:
        patients[patient_id].trach = patient.trach

    return patients[patient_id]

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: int):
    if patient_id not in patients:
        return {"Error:" "Patient doesn't exists."}
    
    del patients[patient_id]
    return {"Message": " Patient deleted successfully!"}
