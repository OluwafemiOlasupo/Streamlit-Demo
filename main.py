import streamlit as st
import pandas as pd
import numpy as np

st.write("My Cool Chart")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.bar_chart(chart_data)
st.line_chart(chart_data)

# data = pd.read_csv("C:/Users/oluwa/DATA SCIENCE/Data Science & ML/Reinforcing my ML Knowledge/canada_per_capita_income.csv")
# st.write(data) 

# st.write("Hello World")
# x = st.text_input("Favourite movie?")
# st.write(f"Your favourite movie is: {x}")

# is_clicked = st.button("Click Me")
# st.write("## This is a H2 Title!")
