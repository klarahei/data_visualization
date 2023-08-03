import streamlit as st
import pandas as pd
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

selected_files = st.multiselect('select location', file_name_list)

colorlist = ['red', 'green', 'pink', 'yellow', 'blue']
plots = []

for i, selected_file in enumerate(selected_files):
    df1 = pd.read_csv(selected_file)
    p = figure(x_axis_label=x_axis + '(wt.%)', y_axis_label=y_axis + '(wt.%)')
    p.circle(df1[x_axis] / 10000, df1[y_axis] / 10000, color=colorlist[i])
    plots.append(p)

for plot in plots:
    st.bokeh_chart(plot, use_container_width=True)
