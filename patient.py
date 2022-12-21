import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
df=pd.read_excel('data.xlsx')
st.title("Patients Details ")
st.table(df)

st.sidebar.header("options")
option_form=st.sidebar.form("option_form",True)
user_name=option_form.text_input("Name")
user_age=option_form.text_input("Age")
user_pulse=option_form.text_input("Pulse")
user_temperature=option_form.text_input("Temperature")
add_data=option_form.form_submit_button()
if st.button('pop'):
    df.drop(index=df.index[-1],axis=0,inplace=True)
    df.to_excel('data.xlsx',index=False)
    st.warning("Details in the last row has been deleted")
    st.write(df)

if add_data:
    if([len(user_name)!=0] and [user_age>str(0)] and [user_pulse>str(0)] and [user_temperature>str(0)]):
        new_data={"name":user_name,"age":int(user_age),"pulse":int(user_pulse),"temperature":int(user_temperature)}
        df=df.append(new_data,ignore_index=True)
        st.write(user_name.upper()+ ' ,  your details have been added ')
        st.table(df)
        df.to_excel('data.xlsx',index=False)
    else:
        st.warning('Caution wrong details entered ,Please enter correct details ! .')


