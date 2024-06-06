
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch

app = FastAPI()

origins = [
    "http://localhost:3001",  # Замените на адрес вашего фронтенда
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

@app.post("/predict_pt")
async def predict(input_data: InputData):
    # Загрузите вашу модель PyTorch и сделайте предсказание
    result = {"prediction": "dummy_result_pt"}  # Замените это на реальное предсказание
    return result



