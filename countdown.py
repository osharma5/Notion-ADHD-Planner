import streamlit as st
from datetime import datetime

deadline = "01-15-2026"
deadline_date = datetime.strptime(deadline, "%m-%d-%Y")

# Calculate days left
today = datetime.today()
days_left = (deadline_date - today).days

st.title(f"{days_left} Days left!")

