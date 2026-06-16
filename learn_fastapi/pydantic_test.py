from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact: Dict[str,str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated")

patient_info = {'name': 'Nitish', 'age': 21, 'weight' : 71.6, 'married': True, 
                'allergies':['cold', 'fever'], 'contact': {"email": "contact@mail.wow","phone": "12345"}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)
