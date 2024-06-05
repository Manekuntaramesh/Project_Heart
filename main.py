#main
import streamlit as st
import pickle
import os
import sklearn
import pandas as pd
from streamlit_option_menu import option_menu



# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Heart care Analysis',

                           ['Heart Disease Prediction','Details'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart'],
                           default_index=0)

st.image("https://static8.depositphotos.com/1020482/913/i/600/depositphotos_9134432-stock-photo-doctor-with-big-red-heart.jpg")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
  st.title('Heart Disease Prediction using ML')

st.subheader("Please Enter your Age ")

age = st.number_input('Age')

st.subheader("Please Enter your Gender")
st.text("male = 0 , female = 1") 
sex = st.selectbox(
       "Selecte you Gender",("0","1"))


st.subheader("Selecte you chest pain types")
st.text("0: Typical angina , 1: Atypical angina,2: Non-anginal pain,3: Asymptomatic")
cp = st.selectbox(
      "chest pain types",("0","1","2","3"))

st.subheader("Please Enter you Resting Blood Pressure")
trestbps = st.number_input("Enter Your Blood Pressure Rate (95-200)",min_value=95,max_value=200,step=1)

st.subheader("Serum Cholestoral in mg/dl")
chol = st.number_input("Enter Your Cholestrol Level Value (125-565)",min_value=125,max_value=565,step=1)

st.subheader("Fasting blood sugar")
st.text("fbs>120 mg/dl (0 = false; 1 = true)")
fbs = st.selectbox('fbs',("0","1"))

st.subheader("Resting Electrocardiographic results")
st.text("0:Nothing, 1:non-normal, 2:Possible")
restecg = st.selectbox('restecg',("0","1","2"))

st.subheader("Maximum Heart Rate achieved")
thalach = st.number_input("Enter You Maximum Heart Rate (70-200)",min_value=70,max_value=200,step=1)

st.subheader("Exercise induced angina")
st.text("1 = yes; 0 = no")
exang = st.selectbox('exang',("1","0"))

st.subheader("Oldpeak")
st.text(" ST depression induced by exercise relative to rest")
oldpeak = st.number_input('Enter the oldpeak(0.0-4.0)')

st.subheader("slope")
st.text("0: Upsloping, 1: Flatsloping, 2: Downslopins ")
slope = st.selectbox('Slope of the peak exercise ST segment',("0","1","2"))

st.subheader("CA") 
st.text(" Number of major vessels (0-3) colored by flourosopy")
ca = st.selectbox('Major vessels colored by flourosopy',("0","1","2","3"))

st.subheader("Thalium stress result") 
st.text("0 = normal;1 = fixed defect; 2 = reversable defect")
thal = st.selectbox("thal",("0","1","2"))

    # code for Prediction
heart_diagnosis=''

heart_disease_model=pickle.load(open(r"C:\Users\manne\Heart.pkl","rb"))

       

    # creating a button for Prediction

if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            st.image(r"C:\Users\manne\OneDrive\Screenshots\Conformed (1).png")
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            st.image(r"C:\Users\manne\OneDrive\Screenshots\Healthy.png")
st.success(heart_diagnosis)


## Details of the heart Disease
if selected == "Details":

## header 
 st.header("Heart Disease Explanation")

 st.subheader("Means")

 st.text("Heart disease is a general term that means that the heart is not working normally. Babies can be born with heart disease. This is called congenital heart disease. If people get heart disease later, it is called acquired heart disease. Most heart disease is acquired.")
 st.subheader("Unserstanding heart Disease")
 st.image("https://m.media-amazon.com/images/I/71v0kFtsC7L._AC_UF1000,1000_QL80_.jpg")

 st.subheader("Symptoms")
 st.text("A person can have heart disease and not feel sick. Some people with heart disease have symptoms. This is when there are changes or pain in the body to show a disease is there. Some symptoms of heart disease are:")
 st.text("Pain in the chest — the heart muscle is not getting enough flow to keep it going.")
 st.text("Trouble breathing—blood may back up into the lungs.")
 st.text("Palpitations (a feeling that the heart is beating too fast, too hard, or not regularly).")
 st.text("Swelling of feet or legs—blood is backing up from the heart into the lower body.")
 st.text("Feeling weak because the body and brain are not getting enough blood to supply them with oxygen.")
 st.text("Cyanosis (skin turning a blue colour) means that too little oxygen is in the bloodstream to supply the cells in the body.")

 st.subheader("Heart Disease Causes")
 st.image("https://previews.123rf.com/images/designua/designua1511/designua151100015/48191743-heart-attack-infographics-in-low-color-style-isolated-icon-and-object-heart-disease-factors.jpg")

 st.subheader("Fllow this")
 st.image("https://www.heart.org/-/media/Images/Health-Topics/Heart-Attack/5-ways-to-lower-heart-attack.jpg")


 st.subheader("THANK YOU ")