from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

app = FastAPI()

# Load the SVM model
svm_model_filename = os.environ.get('SVM_MODEL_FILENAME', 'svm_model.pkl')
try:
    with open(svm_model_filename, 'rb') as svm_model_file:
        svm_classifier = joblib.load(svm_model_file)
except FileNotFoundError:
    raise HTTPException(status_code=500, detail="Model file not found")

class Passenger(BaseModel):
    Age: float
    Fare: float
    Pclass: int
    Sex: str

@app.post("/predict/")
def predict_survival(passenger: Passenger):
    data = passenger.dict()
    sex = data['Sex']
    age = data['Age']
    
    if (sex == 'female') or (sex == 'Female'):
        # If passenger is female, predict "survived"
        prediction = True
    elif (sex == 'male') or (sex == 'Male'):
        if age < 18:
            # If passenger is male and less than 18 years old, predict "survived"
            prediction = True
        else:
            prediction = False
    else:
        # If sex is not specified correctly, return an error response
        raise HTTPException(status_code=400, detail="Invalid input")

    return {"survived": prediction}
