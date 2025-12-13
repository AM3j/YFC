import streamlit as st

# Page configuration
st.set_page_config(
    page_title="TASI Index Analysis",
    page_icon="📊",
)

# Main title and descriptions
st.title("📊 TASI Index Analysis")
st.markdown("""
This page presents comprehensive analysis of the Tadawul All Share Index (TASI) in Saudi Arabia. 
Forecasts will be updated as they become available.
""")

st.divider()

# Seasonality Analysis Section
st.header("Seasonality Analysis")

with st.expander("📋 Methodology", expanded=False):
    st.markdown("""
    **Analysis Approach:**
    - Percentage change calculated based on daily open and close prices
    - Seasonality patterns examined across multiple timeframes: 5, 10, and 15-year averages
    - Historical trends help identify recurring patterns in market behavior
    """)

tab1, tab2, tab3, tab4 = st.tabs(['📅 All Years', '5-Year Average', '10-Year Average', '15-Year Average'])

with tab1:
    st.image("charts/All_Seasonality.png", use_container_width=True)
    
with tab2:
    st.image("charts/5YearAvg.png", use_container_width=True)
    
with tab3:
    st.image("charts/10YearAvg.png", use_container_width=True)
    
with tab4:
    st.image("charts/15YearAvg.png", use_container_width=True)

st.divider()

# Monthly and Weekly Returns Section
st.header("📈 Monthly and Weekly Performance")

with st.expander("📋 Methodology", expanded=False):
    st.markdown("""
    **Analysis Approach:**
    - Average returns calculated from monthly and weekly open-to-close price changes
    - Analysis period: 15 years of historical data
    - Provides insight into temporal patterns and optimal trading periods
    """)

st.subheader("Monthly Returns")
st.image("charts/MonthlyReturn.png", use_container_width=True)


st.subheader("Weekly Returns")
st.image("charts/WeeklyReturn.png", use_container_width=True)

st.divider()

# Trading Days Analysis Section
st.header("📅 Intra-Month Trading Day Analysis")

with st.expander("📋 Methodology", expanded=False):
    st.markdown("""
    **Analysis Approach:**
    - Daily percentage change calculated from open to close for each trading day of the month
    - Averaged over 15 years of historical data
    - **Note:** Analysis based on trading days, not calendar days
    - Helps identify the most favorable days within each month for market participation
    """)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

month = st.selectbox("Choose month", months)
st.image(f"charts/{month}Return.png")

st.divider()

# Footer
st.caption("Data Source: Tadawul All Share Index (TASI) | Analysis Period: Up to 15 years of historical data")
st.caption("⚠️ Disclaimer: Past performance does not guarantee future results. This analysis is for informational purposes only and should not be considered investment advice.")