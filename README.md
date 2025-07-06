
# 🔮 ChurnShield – Customer Churn Predictor

ChurnShield is a real-time machine learning web app that predicts the probability of a customer leaving a service based on their profile. Built using Python, Scikit-learn, and Streamlit, this project helps businesses identify customers at risk of churn and take proactive measures to retain them.

---

## 📊 Features

- 🔍 Predicts customer churn based on 20+ profile inputs
- 💡 Uses a trained Random Forest classifier wrapped in a full preprocessing pipeline
- 🎛️ Clean Streamlit UI for interactive input
- 📁 Real-world dataset from the telecom industry

---

## 🚀 Quick Start

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/niveditanayak2003/ChurnShield
cd ChurnShield
```

### 📥 2. Download Dataset

Download the dataset from Kaggle:  
[Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

Place the CSV file in the `data/` folder as:

```
ChurnShield/data/telco_churn.csv
```

### 📦 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 🧠 4. Train the Model

```bash
python train_model.py
```

This will train the model and create a `model.pkl` file.

### 🌐 5. Launch the Web App

```bash
streamlit run app.py
```

Your app will open at `http://localhost:8501`

---

## 🗂️ Project Structure

```
ChurnShield/
├── data/
│   └── telco_churn.csv
├── app.py                # Streamlit UI
├── model.py              # Model loading & prediction logic
├── train_model.py        # Data cleaning, training pipeline
├── model.pkl             # Trained model
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project overview (this file)
```

---

## ⚙️ Requirements

```
streamlit
pandas
scikit-learn
joblib
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 👩‍💻 Author

**Nivedita**   
📫 [LinkedIn](https://www.linkedin.com/in/nivedita33) | [GitHub](https://github.com/niveditanayak2003)

---

## 📃 License

This project is open-source and available under the MIT License.
