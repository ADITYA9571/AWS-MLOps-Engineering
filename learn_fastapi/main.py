"Building the FastApi- sample codes"

import json
from fastapi import FastAPI, Path, HTTPException, Query # importing the required library
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal, Optional

# Default api version
app = FastAPI() # creating the instance of the app

class Patient(BaseModel):
    #  fields required to create a patient
    name:Annotated[str,Field(...,description="Name of the patient")]
    city:Annotated[str,Field(...,description="City of the patient")]
    age:Annotated[int,Field(...,description="Age of the patient")]
    gender:Annotated[Literal['male','female','others'],
                    Field(...,description="Gender of the patient")]
    height:Annotated[float, Field(...,gt=0,description="Enter the height of the patient")]
    weight:Annotated[float, Field(...,gt=0,description="Enter the height of the patient")]
    id:Annotated[str,Field(...,description="Name of the patient",examples=['P001'])]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round((self.weight/self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "underweight"
        elif self.bmi>25.5:
            return "overweight"
        else:
            return "normal"


class Patient_update(BaseModel): 
    #  fields required to create a patient
    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None)]
    gender:Annotated[Optional[Literal['male','female','others']],
                    Field(default=None)]
    height:Annotated[Optional[float], Field(default=None)]
    weight:Annotated[Optional[float], Field(default=None)]



def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
        return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)


# First Endpoint- GET hello
@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message':'A fully functional API to manage patients'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(...,
                    description = 'Id of the patiet in the database',
                    examples= 'P001')):

    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail = 'Patient id doesnt exists')

@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description= "Sort by Height and Weight"),
                    order: str = Query('asc', description='Sort in asc or desc order')):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid field. select again")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. select again")

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse = sort_order)

    return sorted_data

@app.post('/create')
def create_patient(patient:Patient):
    data = load_data() #load the data
    if patient.id in data:
        raise HTTPException(status_code=400,detail="patient already exists")
    data[patient.id] = patient.model_dump(exclude=['id'])

    save_data(data)
    return JSONResponse(status_code=201, content={"message": "patient created successfully"})


@app.put('/edit/{patient_id}')
def update_patient(patient_id : str, patient_update:Patient_update):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient id not found')
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value
    
    # existing patient info -> pydantic object -> updated bmi -> verdict updated
    existing_patient_info['id'] = patient_id
    patient_pydantic_object = Patient(**existing_patient_info)

    # -> pydantic object -> dict -> add dict to data -> save
    existing_patient_info = patient_pydantic_object.model_dump(exclude='id')
    data[patient_id] = existing_patient_info
    save_data(data)

    return JSONResponse(status_code=200, content = {'message':'Data updated successfully'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient doesnt exists')
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200, content={'message':'Patient Deleted'})

