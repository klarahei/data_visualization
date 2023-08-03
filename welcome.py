import streamlit as st
import pandas as pd
import os
from bokeh.plotting import figure

# List all CSV files in the current directory
file_name_list = [i for i in os.listdir() if i.endswith('csv')]

# Display the list of CSV files
st.write(file_name_list)

# Read the selected CSV file
selected_file = st.selectbox('Select CSV file', file_name_list)
df = pd.read_csv(selected_file)
st.dataframe(df)

# Create a list of elements from the dataframe columns
el_list = df.columns.tolist()[27:80]

# Allow the user to select elements for the x and y axes
x_axis = st.selectbox('Select x-element', el_list)
y_axis = st.selectbox('Select y-element', el_list)

# Allow the user to select locations to display
selected_locations = st.multiselect('Select locations', df['Location'].unique())

# Create a Bokeh figure
p = figure(x_axis_label='x', y_axis_label='y')

# Plot the selected elements for the selected locations
for location in selected_locations:
    location_df = df[df['Location'] == location]
    p.circle(location_df[x_axis] / 10000, location_df[y_axis] / 10000, legend_label=location)

# Display the legend
p.legend.title = "Locations"

# Show the Bokeh plot using Streamlit
st.bokeh_chart(p, use_container_width=True)

