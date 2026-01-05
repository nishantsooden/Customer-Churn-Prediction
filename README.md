# 🔄 Customer Churn Prediction

## 📌 Project Overview
Customer Churn Prediction is an **end-to-end Machine Learning project** that predicts whether a customer is likely to **churn (leave the service)**.  
The project uses a **Logistic Regression model** with a complete preprocessing and modeling pipeline and is deployed using **Streamlit** for real-time predictions.

---

## 🎯 Problem Statement
Customer churn is a major challenge for **subscription-based businesses**.  
The objective of this project is to identify customers who are likely to churn based on their usage patterns, service subscriptions, and support history, enabling businesses to take **proactive retention actions**.

---

## 📊 Dataset Overview
The dataset contains customer-level information such as:
- Contract details
- Billing and payment information
- Internet and support services
- Customer tenure and support interactions

### 🎯 Target Variable
- **`churn`** → Yes / No

### ⚠️ Note
Identifier columns such as **`customer_id`** were removed as they do not contribute to prediction and may lead to **data leakage**.

---

## 🧾 Features Used
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

## 🧠 Model Used
- **Logistic Regression**

### 🔧 ML Pipeline Includes:
- Data preprocessing
- Encoding categorical variables
- Feature scaling
- Model training and evaluation

### ❓ Why Logistic Regression?
- Simple and highly interpretable  
- Low risk of overfitting  
- Well-suited for **binary classification** problems like customer churn  

---

## 📈 Model Performance
- **Training Accuracy:** ~77%  
- **Testing Accuracy:** ~77%  

The similar training and testing accuracy indicates **good generalization** and no overfitting.  
The focus of this project is on building a **stable, explainable, and production-ready model**, rather than chasing unrealistically high accuracy.

---

## 🚀 Deployment
The trained machine learning pipeline is deployed using **Streamlit**, allowing users to input customer details and receive **real-time churn predictions**.

---



## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone < https://github.com/nishantsooden/Customer-Churn-Prediction.git >
cd Customer_Churn_Prediction

Customer-Churn-Prediction/
│
├── data/
│   └── customer_churn_dataset.csv
│
├── Model/
│   └── customer.pkl
│
├── Notebooks/
│   └── customer.ipynb
│
├── Src/
│   └── customer_app.py
│
├── requirements.txt
├── README.md
└── .gitignore

2️⃣ Create and activate virtual environment

python -m venv myenv
myenv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run Streamlit app
streamlit run Src/app.py



