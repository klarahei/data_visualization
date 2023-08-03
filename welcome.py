import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
import os
from bokeh.plotting import figure

file_name_list = []
for i in os.listdir():
 if i.endswith('csv'):
    file_name_list.append(i)
  
st.write(file_name_list)

df = pd.read_csv('Galapagos Islands.csv')
st.dataframe(df)


el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select x-element', el_list)
y_axis = st.selectbox('select y-element', el_list)

st.multiselect('select location', file_name_list)
#
p = figure(x_axis_label = 'x',y_axis_label ='y')
p.circle(file_name_list['Mg']/10000, df['Si']/10000)

#show(p)

st.bokeh_chart(p, use_container_width=True)
