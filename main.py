import streamlit as st
import pandas as pd
import numpy as np


st.title("Supplier Risk Assessmenent Portal")

st.subheader("Interplex Dashboard")

st.markdown("Key Highlight")
col1, col2, col3, col4 = st.columns(4)

col1.metric(label = "Region 1- China",
            value = 5000.32,
            delta = +6.9)

col2.metric(label = "Region 2 - South East Asia",
            value = 3000.25,
            delta = -4.2)

col3.metric(label = "Region 3 - North America",
            value = 2000,
            delta = -5.2)

col4.metric(label = "Region 4 - Europe",
            value = 500,
            delta = -15.2,
            delta_color = 'inverse')

st.markdown("### Important Graph Charts")

chart1, chart2 = st.columns(2)

chart_data = pd.DataFrame( np.random.randn(50, 4), columns= ['China','SEA','NA','EU'])

chart1.bar_chart(chart_data)

chart2.line_chart(chart_data)

st.dataframe(chart_data)

st.button("Next")