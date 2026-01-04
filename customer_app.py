import streamlit as st
import pandas as pd
import joblib


model = joblib.load("customer.pkl")   

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="centered"
)

st.title("📉 Customer Churn Prediction App")
st.write(
    """
    This application predicts whether a customer is likely to **churn**  
    using a **Logistic Regression model with a full ML pipeline**.
    """
)

st.divider()

st.subheader("🔢 Enter Customer Details")

tenure = st.number_input("Tenure (months)", min_value=0, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)
support_calls = st.number_input("Number of Support Calls", min_value=0, value=1)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

payment_method = st.selectbox(
    "Payment Method",
    ["Credit", "Debit", "UPI", "Cash"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No"]
)


input_data = pd.DataFrame({
    "tenure": [tenure],
    "monthly_charges": [monthly_charges],
    "total_charges": [total_charges],
    "contract": [contract],
    "payment_method": [payment_method],
    "internet_service": [internet_service],
    "tech_support": [tech_support],
    "online_security": [online_security],
    "support_calls": [support_calls]
})


if st.button("🔮 Predict Churn"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.divider()

    if prediction == "Yes" or prediction == 1:
        st.error(f"❌ Customer is likely to churn")
    else:
        st.success(f"✅ Customer is likely to stay")

    st.info(f"📊 Churn Probability: {probability:.2f}")

st.divider()
st.caption("Built with ❤️ using Streamlit | Logistic Regression ML Pipeline")
