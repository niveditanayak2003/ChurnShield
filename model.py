import joblib
import pandas as pd

# Load trained pipeline
model = joblib.load("model.pkl")

def predict_churn(user_input: dict):
    # Make sure all inputs are strings/numbers — especially for categorical fields
    for k, v in user_input.items():
        # Convert numeric fields to float if possible
        try:
            user_input[k] = float(v)
        except:
            user_input[k] = str(v)
    
    df = pd.DataFrame([user_input])
    prob = model.predict_proba(df)[0][1] * 100
    return prob
