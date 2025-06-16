from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Caricamento modello all'avvio
model = joblib.load("model.joblib")

# Definizione struttura dati input
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.get("/")
def root():
    return {"message": "API pronta per le predizioni!"}

@app.post("/predict")
def predict(data: InputData):
    # Prepara i dati per la predizione
    X = np.array([[data.feature1, data.feature2, data.feature3]])
    prediction = model.predict(X)
    return {"prediction": int(prediction[0])}
