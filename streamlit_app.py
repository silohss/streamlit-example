import pandas as pd
import streamlit as st
sheet_id = "178FW99M2zI-G27OYKkXwquAPmNhc5TQvT6PyV9N41Tk"
sheet_name = "laksa"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
st.dataframe(df)

