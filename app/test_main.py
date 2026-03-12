from fastapi.testclient import TestClient
from app.main import app

# Create a test client using your FastAPI app
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Sentiment Analysis API is running!"}

def test_predict_positive_sentiment():
    response = client.post(
        "/predict",
        json={"text": "I absolutely love this product! It works flawlessly."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "Positive"
    assert "confidence" in data

def test_predict_negative_sentiment():
    response = client.post(
        "/predict",
        json={"text": "This is the worst thing I have ever bought. It broke immediately."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "Negative"
    assert "confidence" in data

def test_predict_empty_text():
    response = client.post(
        "/predict",
        json={"text": "   "}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Review text cannot be empty."