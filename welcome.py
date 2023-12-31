import streamlit as st
import pandas as pd

#import matplotlib.pyplot as plt
#import numpy as np
import os
from bokeh.plotting import figure
from bokeh.models import Rect

file_name_list = []
for i in os.listdir():
 if i.endswith('csv'):
    file_name_list.append(i)
  
st.write(file_name_list)

df = pd.read_csv('CC1-raw.csv', sep=r';')
#st.dataframe(df)

el_list = df.columns.tolist()
x_axis = st.selectbox('select x-element', el_list)
y_axis = st.selectbox('select y-element', el_list)

select_data = st.multiselect('select data', file_name_list)
#color definition

labellist = select_data
colorlist = ['green', 'red','pink','yellow','blue','purple','orange']
p = figure(x_axis_label = x_axis + '(wt.%)',y_axis_label = y_axis + '(wt.%)')
for i in range(len(select_data)):
 df1 = pd.read_csv(select_data[i], sep=r';')
 p.circle(df1[x_axis], df1[y_axis], color=colorlist[i],legend_label = labellist[i])


p.xgrid.visible = False
p.ygrid.visible = False

# Adding outlining lines on all sides using Rect glyphs
#p.add_glyph(Rect(x='x', y='y', width='width', height='height', line_color="black", line_width=2, fill_alpha=0))

#show(p)
st.bokeh_chart(p, use_container_width=True)
