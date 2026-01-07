from fastapi import FastAPI
from pydantic import BaseModel

from sentiment_analysis.models import SentimentAnalysisModel


# Define a simple data structure for inputs
class Query(BaseModel):
    texts: list[str] = []


app = FastAPI(title="Sentiment analysis API")

model = SentimentAnalysisModel()
model.initialize()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment analysis API"}


@app.post("/predict")
def predict(data: Query):
    """Endpoint to make prediction"""
    predictions = model.predict(data.texts)

    return {
        "input_received": data.texts,
        "predictions": predictions,
        "model_version": "1.0.0"
    }
