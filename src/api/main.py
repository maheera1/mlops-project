from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
import numpy as np
from models.predictor import Predictor
from data.data_processor import DataProcessor

app = FastAPI(
    title="Innovate Analytics ML API",
    description="API for machine learning predictions",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
predictor = None
data_processor = DataProcessor()

class PredictionRequest(BaseModel):
    features: list[float]

@app.on_event("startup")
async def startup_event():
    global predictor
    # Load the model on startup
    model_path = "models/saved/model"
    predictor = Predictor(model_path)

@app.post("/predict")
async def predict(request: PredictionRequest):
    try:
        # Convert input to numpy array
        features = np.array(request.features).reshape(1, -1)
        
        # Make prediction
        prediction = predictor.predict(features)
        
        return {"prediction": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.get("/ready")
async def readiness_check():
    """Readiness check endpoint"""
    return {"status": "ready"}

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Innovate Analytics ML API",
        "version": "1.0.0",
        "status": "operational"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 