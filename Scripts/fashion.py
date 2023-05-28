# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image

# Data analysis
df = pd.read_csv("data/fashion3.csv")
col_lst = list(range(2,13))
col_lst.extend([15,17])
df = df.iloc[:,col_lst]
df_clean = df.dropna()
category = ("Dress", "Top", "Bottom", "Outerwear")

# Title and headers
st.title("FITTED AND PREDICTED")
st.write("**Developers:** Emi Cervantes, Christina Orengo, Nathan Samarasena")
st.write("Check our Github repo: [Click here!](https://github.com/emicervantes/FashionDataProject/tree/main)")
image = Image.open('Scripts/spongebob.png')

col1, col2 = st.columns(2)
with col1:
    st.header("spongebob says 'hello!'")
    factor = col1.selectbox("Choose Your Cloth Category:", category)
    waist = st.slider('Your waistt: ' , 20, 50, 0)
    height = st.select_slider(
    'Your height: ',
    options=["4'00ft", "4'01ft", "4'02ft", "4'03ft", "4'04ft", "4'05ft",
    "4'06ft", "4'07ft", "4'08ft", "4'09ft", "4'10ft", "4'11ft", 
    "5'00ft", "5'01ft", "5'01ft", "5'02ft", "5'03ft", "5'04ft", "5'05ft", "4'01ft",
    "5'06ft", "5'07ft", "5'08ft", "5'09ft", "5'10ft", "5'11ft", "6'01ft", "6'02ft",
    "6'03ft", "6'04ft", "6'05ft", "6'06ft", "6'07ft", "6'08ft", "6'09ft", "6'10ft",
    "6'11ft"])
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        cup_size = st.slider('Your cup size: ', 0, 130, 25)
    with sub_col2:
        bra_size = st.slider('Your bra size: ', 0, 130, 25)
with col2:
    st.image(image)