import streamlit as st
import pandas as pd

st.write('Hello World')

df = pd.read_csv('Galapagos Islands.csv')
st.dataframe(df)
