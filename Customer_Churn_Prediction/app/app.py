import streamlit as st
import pickle

model = pickle.load(
    open('../models/churn_model.pkl','rb')
)

st.title(
    "Customer Churn Prediction"
)

tenure = st.number_input(
    "Tenure"
)

monthly = st.number_input(
    "Monthly Charges"
)

total = st.number_input(
    "Total Charges"
)

if st.button("Predict"):

    prediction = model.predict(
        [[tenure, monthly, total]]
    )

    if prediction[0] == 1:
        st.error(
            "Customer likely to churn"
        )
    else:
        st.success(
            "Customer likely to stay"
        )