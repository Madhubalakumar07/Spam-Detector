# 📩 SMS Spam Detection using Machine Learning

## 📌 Overview

This project is an end-to-end **SMS Spam Detection** application built using **Python**, **Scikit-learn**, and **Streamlit**. It classifies SMS messages as either **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) techniques and machine learning.

The application allows users to enter an SMS message through a simple web interface and instantly predicts whether the message is spam.

---

## 🚀 Features

* Text preprocessing using NLP
* Stopword removal
* Stemming using Porter Stemmer
* TF-IDF Vectorization
* Comparison of multiple machine learning algorithms using GridSearchCV
* Interactive Streamlit web application
* Fast and accurate spam prediction

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* NLTK
* Pandas
* NumPy
* XGBoost
* Pickle

---

## 📂 Project Structure

```text
Spam-Detector/
│
├── app.py                 # Streamlit application
├── requirements.txt       # Project dependencies
├── README.md
│
├── model/
│   ├── model.pkl          # Trained machine learning model
│   └── tfid.pkl           # Trained TF-IDF vectorizer
│
└── notebooks/             # Model training notebooks (optional)
```

---

## ⚙️ Machine Learning Workflow

1. Load the SMS Spam Collection dataset.
2. Clean and preprocess the text.
3. Convert text to lowercase.
4. Tokenize the text.
5. Remove punctuation.
6. Remove English stopwords.
7. Apply Porter Stemming.
8. Convert text into numerical vectors using TF-IDF.
9. Train multiple machine learning models.
10. Perform hyperparameter tuning using GridSearchCV.
11. Save the best-performing model and TF-IDF vectorizer using Pickle.
12. Deploy the trained model with Streamlit.

---

## 🤖 Models Evaluated

* Logistic Regression
* Multinomial Naive Bayes
* Decision Tree Classifier
* Random Forest Classifier
* Extra Trees Classifier
* Gradient Boosting Classifier
* AdaBoost Classifier
* Bagging Classifier
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)
* XGBoost Classifier

---

## 🏆 Best Model

Based on GridSearchCV and test evaluation:

**Multinomial Naive Bayes**

* Cross-validation Accuracy: **98.09%**
* Test Accuracy: **98.07%**
* Precision: **96.83%**

---

## ▶️ Running the Project Locally

### Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📷 Application Preview

You can add screenshots of your application here after deployment.

Example:

```
Home Screen

Prediction Result

Spam Detection Output
```

---

## 📈 Future Improvements

* Deep learning models (LSTM, GRU, Transformers)
* Multilingual spam detection
* Confidence score for predictions
* Message history
* REST API using FastAPI
* Docker deployment
* Real-time spam filtering

---

## 👨‍💻 Author

**Madhubalakumar S**

GitHub: https://github.com/<your-github-username>

LinkedIn: https://linkedin.com/in/<your-linkedin-profile>

---

## 📄 License

This project is licensed under the MIT License.
