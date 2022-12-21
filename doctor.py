import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
df=pd.read_excel('data.xlsx')

temperature=df['temperature'].unique().tolist()
age=df['age'].unique().tolist()

temperature_selection=st.slider('Temperature:',min(temperature),max(temperature),(min(temperature),max(temperature)))
time_selection=st.multiselect('Age :',age,default=age)


# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['temperature'].between(*temperature_selection)) & (df['age'].isin(time_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

df=df[mask]

st.title("Excel check")
st.table(df)

df=df.set_index("age")
st.experimental_rerun()
