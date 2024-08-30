import streamlit as st
import pandas as pd

st.write("Demo IA para Aldo ")

data = pd.read_csv("content/gastronimiaCABA.csv")
data.head()

st.dataframe(data)

from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = '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'

from langchain_groq.chat_models import ChatGroq

llm = ChatGroq(
    model_name = "mixtral-8x7b-32768",
    temperature = 0,
    max_tokens = 1000,
    api_key=GROQ_API_KEY
)

from pandasai import SmartDataframe

df = SmartDataframe(data, config={"llm": llm})

st.write(df.chat("cuenta la cantidad de registros"))

consulta = st.text_input('Ingrese consulta')
st.write("Por ejemplo: lista la tabla ordenada alfabeticamente por nombre")
if consulta :
    st.write(df.chat(consulta))