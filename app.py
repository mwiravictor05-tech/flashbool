import streamlit as st
from analyzer import analyze_feedback
import pandas as pd

st.title("FeedbackLoop AI Dashboard")
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    results = analyze_feedback(df)
    # Display results in Kanban/table format
