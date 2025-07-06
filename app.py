import streamlit as st
from model import predict_churn 

st.set_page_config(page_title="ChurnShield",layout="centered")

st.title("ChurnShield - Customer Churn Predictor")
st.subheader("Predict if a customer will churn based on their profile")

# Collect customer ID
customer_id = st.text_input("🆔 Customer ID (optional)")

# DO NOT include this in the `inputs` dictionary
# Leave the rest of inputs the same

#Provide the input fields
inputs={
    "tenure": st.slider("Tenure (months)", 0, 72, 12),
    "MonthlyCharges": st.number_input("Monthly Charges", 0.0, 200.0, 70.0),
    "TotalCharges": st.number_input("Total Charges", 0.0, 10000.0, 1000.0),
    "gender": st.selectbox("Gender", ["Male", "Female"]),
    "SeniorCitizen": st.selectbox("Senior Citizen", [0, 1]),
    "Partner": st.selectbox("Partner", ["Yes", "No"]),
    "Dependents": st.selectbox("Dependents", ["Yes", "No"]),
    "PhoneService": st.selectbox("Phone Service", ["Yes", "No"]),
    "MultipleLines": st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"]),
    "InternetService": st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"]),
    "OnlineSecurity": st.selectbox("Online Security", ["Yes", "No", "No internet service"]),
    "OnlineBackup": st.selectbox("Online Backup", ["Yes", "No", "No internet service"]),
    "DeviceProtection": st.selectbox("Device Protection", ["Yes", "No", "No internet service"]),
    "TechSupport": st.selectbox("Tech Support", ["Yes", "No", "No internet service"]),
    "StreamingTV": st.selectbox("Streaming TV", ["Yes", "No", "No internet service"]),
    "StreamingMovies": st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"]),
    "Contract": st.selectbox("Contract", ["Month-to-month", "One year", "Two year"]),
    "PaperlessBilling": st.selectbox("Paperless Billing", ["Yes", "No"]),
    "PaymentMethod": st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]),
}


if st.button("Predict Churn Risk"):
    result = predict_churn(inputs)
    st.success(f"📉 Predicted Churn Risk for {customer_id if customer_id else 'Customer'}: {round(result, 2)}%")
    
    if result > 60:
        st.error("⚠️ High churn risk! Consider retention strategies.")
    elif result > 30:
        st.warning("⚠️ Moderate risk. Monitor this customer.")
    else:
        st.info("✅ Low churn risk. Customer likely to stay.")

print("Done")