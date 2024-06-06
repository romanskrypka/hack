
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost:3001",  # замените на адрес вашего фронтенда
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    text: str

@app.post("/predict_tf")
async def predict(input_data: InputData):
    # Загрузите вашу модель TensorFlow и сделайте предсказание
    result = {"prediction": "dummy_result_tf"}  # Замените это на реальное предсказание
    return result



