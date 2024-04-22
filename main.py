
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">The Flat-Price-Predictor in Gurgaon is a tool or system designed to forecast and estimate the prices of flats or apartments in the Indian state of Haryana. It utilizes various data and factors, including market trends, location, property features, and economic indicators, to provide potential buyers or investors with insights into expected flat prices in the region.</p>', unsafe_allow_html=True)

st.sidebar.success("Select a demo above.")