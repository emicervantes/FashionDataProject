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
    waist = st.slider('Your waist: ', 0, 130, 25)
    height = st.slider('Your height: ', 0, 130, 25)
    cup_size = st.slider('Your cup size: ', 0, 130, 25)
    bra_size = st.slider('Your bra size: ', 0, 130, 25)
with col2:
    st.image(image)