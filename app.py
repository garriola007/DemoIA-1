import streamlit as st
import pandas as pd

st.write("Demo IA para Aldo ")

data = pd.read_csv("content/gastronimiaCABA.csv")
data.head()

st.dataframe(data)