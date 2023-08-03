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
colorlist = ['red','green','pink','yellow','blue']
p = figure(x_axis_label = x_axis,y_axis_label = y_axis +'(wt.%))
for i in range(len(file_name_list)):
 df1 = pd.read_csv(file_name_list[i])
 p.circle(df1[x_axis]/10000, df1[y_axis]/10000, color='red')

#show(p)

st.bokeh_chart(p, use_container_width=True)
