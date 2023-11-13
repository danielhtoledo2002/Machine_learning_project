# Manage enviroment  variables
import os
# web framework
import streamlit as st
# OPEN AI
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
# Tool
import pandas as pd
from Models import tsne, logistic_regresion
# st.set_page_config(layout='wide')
# start static  web page


with st.sidebar:
    api_key_file = st.file_uploader("Sube aquí tu Key", st.write("# AMLO CLASIFIER"))
st.write("### TSNE")
# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
with st.spinner("Loading chart"):
    st.plotly_chart(tsne.plot_tsne())

st.write("### Logisic Regresion")
with st.spinner("Loading table"):
    text = st.text_input(
        "", label_visibility="visible", placeholder="Input texto to clasify "
    )
    if st.button("Enviar"):
        if text != "":
            proba = logistic_regresion.predict_text(text)
            st.write(logistic_regresion.predict(proba))




os.environ['OPENAI_API_KEY'] = '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'

llm = ChatOpenAI(model="gpt-3.5-turbo")
query = st.text_input("Enter your input text")
prompt = """ 
You are a virtual assistant that can only classify a text in spanish. The classifications are: security, history, international, support,
    economy and other, but only give me one classification word in spanish 
"""
if st.button("Generate Output"):
    response = llm.invoke(
        [SystemMessage(content=prompt), HumanMessage(content=query)]
    )
    st.write(f"pregunta = {query}")
    st.write(f"## {response.content}")

