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
bra_lst = df['bra size'].unique()
cup_lst = df['cup size'].unique()

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
    'Your height (ft): ',
    options=["4'00", "4'01", "4'02", "4'03", "4'04", "4'05",
    "4'06", "4'07", "4'08", "4'09", "4'10", "4'11", 
    "5'00", "5'01", "5'01", "5'02", "5'03", "5'04", "5'05", "4'01",
    "5'06", "5'07", "5'08", "5'09", "5'10", "5'11", "6'01", "6'02",
    "6'03", "6'04", "6'05", "6'06", "6'07", "6'08", "6'09", "6'10",
    "6'11"])
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        cup_size = sub_col1.selectbox("Choose Your Cloth Category:", 
        bra_lst)
    with sub_col2:
        bra_size = sub_col2.selectbox("Choose Your Cloth Category:", 
        cup_lst)
with col2:
    st.image(image)