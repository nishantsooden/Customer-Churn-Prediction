# Customer Churn Prediction

This project predicts whether a customer is likely to **churn (leave the service)** using a **Logistic Regression model**.  
It is built as an **end-to-end machine learning project** with proper preprocessing, model pipeline, and deployment using **Streamlit**.

---

##  Problem Statement
Customer churn is a major challenge for subscription-based businesses.  
The goal of this project is to identify customers who are likely to churn based on their usage patterns, services, and support history, so that businesses can take proactive retention actions.

---

##  Dataset Overview
The dataset contains customer-level information including:
- Contract details
- Billing information
- Internet and support services
- Customer tenure and support interactions

**Target Variable**
- `churn` → Yes / No

**Note:**  
Identifier columns such as `customer_id` were removed as they do not contribute to prediction and may cause data leakage.

---

## Features Used
- tenure  
- monthly_charges  
- total_charges  
- contract  
- payment_method  
- internet_service  
- tech_support  
- online_security  
- support_calls  

---

##  Model Used
- **Logistic Regression**
- Implemented using a **complete ML pipeline** including:
  - Data preprocessing
  - Encoding of categorical variables
  - Feature scaling
  - Model training

**Why Logistic Regression?**
- Simple and interpretable baseline model  
- Low risk of overfitting  
- Suitable for binary classification problems like churn  

---

##  Model Performance
- **Training Accuracy:** ~77%
- **Testing Accuracy:** ~77%

The similar train and test accuracy indicates **good generalization** and no overfitting.  
The focus of this project is on building a **stable, explainable, and production-ready model** rather than chasing unrealistically high accuracy.

---

##  Deployment
The trained pipeline is deployed using **Streamlit** to provide real-time churn predictions based on user inputs.

### Run the app locally:
```bash
streamlit run customer_app.py
