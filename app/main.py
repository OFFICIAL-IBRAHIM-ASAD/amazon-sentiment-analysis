import os
import joblib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# 1. Initialize the FastAPI application
app = FastAPI(
    title="Amazon Sentiment Analysis API", 
    description="An NLP microservice for predicting customer sentiment.",
    version="1.0"
)

# 2. Configure CORS to allow requests from local frontends (e.g., a Next.js app on port 3000 or Spring Boot on 8080)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Define the path to the saved models
# This ensures it finds the models directory regardless of where you run the script from
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'sentiment_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'models', 'tfidf_vectorizer.pkl')

# 4. Load the trained models on startup
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
except FileNotFoundError:
    raise RuntimeError("Model files not found. Ensure you have run the training notebook.")

# 5. Define the expected data format from the user
class ReviewRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float

# 6. Create the prediction endpoint
@app.post("/predict", response_model=SentimentResponse)
async def predict_sentiment(request: ReviewRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Review text cannot be empty.")
    
    # Vectorize the incoming text
    text_vectorized = vectorizer.transform([request.text])
    
    # Make the prediction
    prediction = model.predict(text_vectorized)[0]
    
    # Get the confidence score (probability of the predicted class)
    probabilities = model.predict_proba(text_vectorized)[0]
    confidence = max(probabilities) * 100
    
    return SentimentResponse(
        sentiment=prediction,
        confidence=round(confidence, 2)
    )

# 7. Add a simple health check endpoint
@app.get("/")
async def root():
    return {"message": "Sentiment Analysis API is running!"}