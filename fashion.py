# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
from sklearn.decomposition import TruncatedSVD
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Data analysis
df = pd.read_csv("../data/fashion3.csv")
col_lst = list(range(2,13))
col_lst.extend([15,17])
df = df.iloc[:,col_lst]
df_clean = df.dropna()
category = ("Dress", "Top", "Bottom", "Outerwear")
bra_lst = sorted(df_clean['bra size'].unique())
cup_lst = ["AA", "A", "B", "C", "D", "DD", "DDD", "DDDD", "H",
            "I", "J", "K"]
fitting = ["Small", "Fit", "Large"]

# modeling
col_lst = [4,11]
score = df_clean.iloc[:,col_lst].apply(lambda iterator: ((iterator - iterator.min())/(iterator.max() - iterator.min())).round(2))
score["avg"] = score.mean(axis=1)
 # Add user id and category
score.insert(0, "user_id", score.index + 1)
score.insert(1, "item_id", df_clean["category"])
y1 = score.loc[score["item_id"] == 1]
y2 = score.loc[score["item_id"] == 2]
y3 = score.loc[score["item_id"] == 3]
y4 = score.loc[score["item_id"] == 4]
y1 = y1["avg"]
y2 = y2["avg"]
y3 = y3["avg"]
y4 = y4["avg"]

df_d = df_clean[df_clean['category'] == 1]
df_d = df_d[['waist','height_inches','cup size', 'bra size','fit']].copy()
df_top = df_clean[df_clean['category'] == 2]
df_top = df_top[['waist','height_inches','cup size', 'bra size','fit']].copy()
df_bottoms = df_clean[df_clean['category'] == 3]
df_bottoms = df_bottoms[['waist','height_inches','fit']].copy()
df_ow = df_clean[df_clean['category'] == 4]
df_ow = df_ow[['waist','height_inches','cup size', 'bra size','fit']].copy()

scaler = StandardScaler()
#dress
reg1 = KNeighborsRegressor(n_neighbors=15)
U = df_d
scaler.fit(U)
U_scaled = scaler.transform(U)
reg1.fit(U_scaled,y1)
# tops
reg2 = KNeighborsRegressor(n_neighbors=15)
X = df_top
scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
reg2.fit(X_scaled,y2)
# bottoms
reg3 = KNeighborsRegressor(n_neighbors=15)
Z = df_bottoms
scaler.fit(Z)
Z_scaled = scaler.transform(Z)
reg3.fit(Z_scaled,y3)
# outwear
reg4 = KNeighborsRegressor(n_neighbors=15)
W = df_ow
scaler.fit(W)
W_scaled = scaler.transform(W)
reg4.fit(W_scaled,y4)


# Title and headers
st.title("FITTED AND PREDICTED")
st.write("**Developers:** Emi Cervantes, Christina Orengo, Nathan Samarasena")
st.write("Check our Github repo: [Click here!](https://github.com/emicervantes/FashionDataProject/tree/main)")
image = Image.open('../Scripts/spongebob.png')

col1, col2 = st.columns(2)
with col1:
    fit = col1.selectbox("Fitting: ", fitting)
    waist = st.slider('Your waistt: ' , 20, 50, 0)
    height = st.select_slider(
    'Your height (ft): ',
    options=[4.00, 4.01, 4.02, 4.03, 4.04, 4.05,
    4.06, 4.07, 4.08, 4.09, 4.10, 4.11, 
    5.00, 5.01, 5.02, 5.03, 5.04, 5.05, 
    5.06, 5.07, 5.08, 5.09, 5.10, 5.11, 6.01, 6.02,
    6.03, 6.04, 6.05, 6.06, 6.07, 6.08, 6.09, 6.10,
    6.11])
    cup_size = st.selectbox("Your Cup Size:", bra_lst)
    bra_size = st.selectbox("Your Bra Size:", cup_lst)
    factor = col1.selectbox("Choose Your Cloth Category:", category)
with col2:
    st.image(image)

if(fit == "Small"):
    fit = 2
elif(fit == "Big"):
    fit = 1
else:
    fit = 3

if(bra_size == "AA"):
    bra_size = 1
elif(bra_size == "A"):
    bra_size = 2
elif(bra_size == "B"):
    bra_size = 3
elif(bra_size == "C"):
    bra_size = 4
elif(bra_size == "D"):
    bra_size = 5
elif(bra_size == "DD"):
    bra_size = 6
elif(bra_size == "DDD"):
    bra_size = 7
elif(bra_size == "DDDD"):
    bra_size = 8
elif(bra_size == "H"):
    bra_size = 9
elif(bra_size == "I"):
    bra_size = 10
elif(bra_size == "J"):
    bra_size = 11
else:
    bra_size = 12

st.header("Your Size Recommendations:")
if (factor == "Dress"):
    x = np.array([waist, height,cup_size,bra_size,fit]).reshape(1,-1)
    scaler.fit(x)
    x_scaled = scaler.transform(x)
    pred = reg1.predict(x_scaled)
elif (factor == "Top"):
    x = np.array([waist, height,cup_size,bra_size,fit]).reshape(1,-1)
    scaler.fit(x)
    x_scaled = scaler.transform(x)
    pred = reg2.predict(x_scaled)
elif (factor == "Bottom"):
    x = np.array([waist, height, fit]).reshape(1,-1)
    scaler.fit(x)
    x_scaled = scaler.transform(x)
    pred = reg3.predict(x_scaled)
else:
    x = np.array([waist, height,cup_size,bra_size,fit]).reshape(1,-1)
    scaler.fit(x)
    x_scaled = scaler.transform(x)
    pred = reg4.predict(x_scaled)

st.write(pred)
