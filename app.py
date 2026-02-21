import streamlit as st
import pandas as pd
import pickle


model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Loan Approval Prediction", layout="centered")
st.title("Loan Approval Prediction App")
st.write("Enter applicant details to predict loan approval status.")


loan_id = st.number_input("Loan ID", min_value=1)
no_of_dependents = st.number_input("No. of Dependents", min_value=0)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
income_annum = st.number_input("Annual Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (months)", min_value=1)
cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900)
residential_assets_value = st.number_input("Residential Assets Value", min_value=0)
commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0)
luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0)
bank_asset_value = st.number_input("Bank Asset Value", min_value=0)


input_df = pd.DataFrame({
    "loan_id": [loan_id],
    " no_of_dependents": [no_of_dependents],
    " education": [education],
    " self_employed": [self_employed],
    " income_annum": [income_annum],
    " loan_amount": [loan_amount],
    " loan_term": [loan_term],
    " cibil_score": [cibil_score],
    " residential_assets_value": [residential_assets_value],
    " commercial_assets_value": [commercial_assets_value],
    " luxury_assets_value": [luxury_assets_value],
    " bank_asset_value": [bank_asset_value],
})


if st.button("Predict Loan Status"):
    prediction = model.predict(input_df)[0]

    if prediction == "Approved":
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")