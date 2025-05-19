from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import logging
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


model_path = "model.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
    logger.info("Model loaded successfully from %s", model_path)
else:
    logger.error("Model file not found!")
    model = None


app = FastAPI()


class InputData(BaseModel):
    feature1: float
    feature2: float


@app.get("/")
def home():
    logger.info("Home endpoint hit")
    return {"message": "Welcome to the ML prediction API"}

@app.get("/health")
def health_check():
    status = model is not None
    logger.info("Health check: %s", status)
    return {"status": "ok" if status else "model not loaded"}

@app.post("/predict")
def predict(data: InputData):
    if model is None:
        logger.error("Prediction attempted but model not loaded")
        raise HTTPException(status_code=500, detail="Model not loaded")

    features = [[data.feature1, data.feature2]]
    logger.info("Received prediction request with data: %s", features)
    prediction = model.predict(features)
    logger.info("Prediction result: %s", prediction)
    return {"prediction": prediction.tolist()}

