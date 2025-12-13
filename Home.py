import streamlit as st

st.title("Yaqeen Forecasting Center")
st.markdown("For Time Series Analysis. *Where data meets time*")


# When clicked the user will send to desired page
st.page_link("pages/Indicators_of_KSA.py", label="Indicators of the Kingdom of Saudi Arabia (KSA)", icon="📊",
            width='content', help="In progress")
# When clicked the user will send to desired page
st.page_link("pages/TASI.py", label="TASI Index", icon="📊",
            width='content', help="In progress")

st.subheader("Upcoming Analysis:")
st.markdown("- NQ100 Index")
st.markdown("- S&P 500 Index")
st.markdown("- Gold Index")





