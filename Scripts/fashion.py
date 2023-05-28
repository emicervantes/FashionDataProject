# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image

# Title and headers
st.title("FITTED AND PREDICTED")
st.write("**Developers:** Emi Cervantes, Christina Orengo, Nathan Samarasena")
image = Image.open('Scripts/spongebob.png')

col1, col2 = st.columns(2)
with col1:
    st.header("spongebob says 'hello!'")
with col2:
    st.image(image)

st.write("Check our Github repo: ")