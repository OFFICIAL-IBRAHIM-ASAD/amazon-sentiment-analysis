# 📦 Amazon Product Sentiment Analysis Pipeline

![CI Pipeline](https://github.com/OFFICIAL-IBRAHIM-ASAD/amazon-sentiment-analysis/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688.svg)

An end-to-end Machine Learning pipeline that classifies Amazon customer reviews into Positive or Negative sentiments. This project demonstrates data engineering, model training, web service deployment, and automated DevOps integration.

## 🚀 Key Features
* **NLP Engine:** Logistic Regression model with TF-IDF vectorization achieving 86% accuracy.
* **REST API:** A high-performance FastAPI microservice for real-time predictions.
* **DevOps/CI-CD:** Automated testing suite via GitHub Actions that validates code on every push.
* **Environment:** Fully containerized logic prepared for cloud deployment.

## 🛠️ Tech Stack
* **Data Science:** Scikit-learn, Pandas, NumPy
* **Web Framework:** FastAPI, Uvicorn
* **Testing/DevOps:** Pytest, GitHub Actions, WSL2 (Ubuntu)
* **Dataset:** Amazon Customer Reviews (Fine Food & Electronics)

## 📁 Project Structure
```text
├── app/
│   ├── main.py          # FastAPI Application
│   ├── test_main.py     # API Integration Tests
│   └── __init__.py
├── models/
│   ├── sentiment_model.pkl    # Trained Classifier
│   └── tfidf_vectorizer.pkl   # Fitted Vectorizer
├── .github/workflows/
│   └── ci.yml           # GitHub Actions Pipeline
└── requirements.txt     # Dependency List

```

## 🚥 Quick Start

1. **Clone the repository:**
```bash
git clone [https://github.com/OFFICIAL-IBRAHIM-ASAD/amazon-sentiment-analysis.git](https://github.com/OFFICIAL-IBRAHIM-ASAD/amazon-sentiment-analysis.git)
cd amazon-sentiment-analysis

```


2. **Run the API:**
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

```


3. **Predict via CLI:**
```bash
curl -X 'POST' '[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)' \
-H 'Content-Type: application/json' \
-d '{"text": "This product is amazing, highly recommended!"}'

```



## 👨‍💻 Author

**Ibrahim Asad**

Student at Beaconhouse National University (BNU)

*Focusing on DevOps, Machine Learning, and Full-Stack Development.*

```

---

### How to apply this:
1. Go to your local WSL terminal.
2. Create/Open the file: `nano README.md`
3. Paste the code above.
4. Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).
5. Push it one last time:
   ```bash
   git add README.md
   git commit -m "docs: add professional project documentation"
   git push origin main
