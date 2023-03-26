import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import pickle
st.set_page_config(page_title='Soil Moisture Prediction')

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1557234195-bd9f290f0e4d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80");
background-size: cover;
}
</style>

'''


st.markdown(page_bg_img,unsafe_allow_html=True)
st.title("Soil Moisture predictor:chart:")
Month = st.text_input("Enter Month")
Day = st.number_input("Enter Day")
pm1 = st.number_input("Enter pm1")
pm2 = st.number_input("Enter pm2")
pm3 = st.number_input("Enter pm3")
am = st.number_input("Enter am")
lum = st.number_input("Enter lum")
temp = st.number_input("Enter temp")
humd = st.number_input("Enter humd")
pres = st.number_input("Enter pres")
list = [Month, Day, pm1,pm2, pm3, am,lum,
       temp, humd,pres]
input = pd.DataFrame([list],columns=['Month', 'Day', 'avg_pm1', 'avg_pm2', 'avg_pm3', 'avg_am', 'avg_lum','avg_temp', 'avg_humd', 'avg_pres'])
if st.button("Predict Moisture"):
    model = pickle.load(open('soil moisture prediction.pkl','rb'))
    result = model.predict(input)
    st.header("Soil Moisture : "+str(result[0]))