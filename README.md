# Customer Churn Prediction Using Machine Learning

## Project Overview

Customer churn is a critical business challenge for subscription-based companies, as retaining existing customers is often more cost-effective than acquiring new ones. This project develops a machine learning solution to predict whether a telecom customer is likely to churn based on demographic information, account details, service subscriptions, and billing history.

The objective is to identify customers at risk of leaving the service and provide actionable insights that can support customer retention strategies.

---

## Dataset

**Dataset:** IBM Telco Customer Churn Dataset

The dataset contains information about telecom customers, including:

* Customer demographics
* Account information
* Service subscriptions
* Billing details
* Churn status

**Dataset Size:** 7,043 customer records

**Target Variable:** `Churn`

* Yes = Customer left the company
* No = Customer stayed with the company

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* Streamlit
* Git & GitHub

---

## Project Workflow

### 1. Data Cleaning

* Converted `TotalCharges` from object type to numeric.
* Identified and handled missing values.
* Removed unnecessary columns such as `customerID`.
* Verified data quality and consistency.

### 2. Exploratory Data Analysis (EDA)

Performed exploratory analysis to understand customer behavior and identify factors associated with churn.

Key analyses included:

* Churn distribution
* Contract type vs churn
* Tenure vs churn
* Monthly charges vs churn
* Internet service vs churn
* Feature correlation analysis

### 3. Feature Engineering

* Converted target variable into binary format.
* Applied one-hot encoding to categorical features.
* Prepared data for machine learning algorithms.
* Standardized features where required.

### 4. Model Development

Implemented and evaluated multiple machine learning models:

#### Logistic Regression

Used as a baseline classification model.

**Accuracy:** 80.7%

#### Random Forest Classifier

Used to capture non-linear relationships and evaluate feature importance.

**ROC-AUC Score:** 0.826

---

## Results

| Model               | Performance    |
| ------------------- | -------------- |
| Logistic Regression | 80.7% Accuracy |
| Random Forest       | 79.2% Accuracy |
| Random Forest       | 0.826 ROC-AUC  |

---

## Feature Importance

The most influential factors affecting customer churn were:

1. Total Charges
2. Tenure
3. Monthly Charges
4. Internet Service Type
5. Payment Method
6. Contract Type

These findings indicate that customer retention is strongly influenced by contract duration, service usage, and billing-related factors.

---

## Key Findings

* Customers with lower tenure are more likely to churn.
* Month-to-month contracts exhibit significantly higher churn rates.
* Higher monthly charges are associated with increased churn.
* Fiber optic customers demonstrate relatively higher churn rates.
* Contract type, tenure, and billing features are among the strongest predictors of churn.

---

## Business Recommendations

* Focus retention efforts on customers with low tenure.
* Encourage migration from month-to-month contracts to long-term contracts.
* Review pricing strategies for customers with high monthly charges.
* Investigate churn patterns among fiber optic service users.
* Implement proactive retention campaigns for high-risk customers identified by the model.

---

## Repository Structure

```text
Customer_Churn_Prediction/
│
├── app/
│   └── app.py
│
├── data/
│
├── images/
│
├── models/
│   ├── churn_model.pkl
│   └── scaler.pkl
│
├── customer_churn_prediction.ipynb
├── requirements.txt
└── README.md
```

---

## Future Improvements

* Implement XGBoost and LightGBM models.
* Perform hyperparameter tuning.
* Deploy a production-ready Streamlit application.
* Integrate real-time prediction capabilities.
* Explore advanced customer segmentation techniques.

---

## Conclusion

This project demonstrates an end-to-end machine learning workflow for customer churn prediction, including data cleaning, exploratory data analysis, feature engineering, model development, and business insight generation. The results show that machine learning can effectively identify customers at risk of churn and support data-driven decision-making for customer retention strategies.
