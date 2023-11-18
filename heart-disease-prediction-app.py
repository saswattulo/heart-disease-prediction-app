import pickle
import pandas as pd
import warnings
import streamlit as st
import random
import streamlit.web.cli as stcli
from tips_file import *

warnings.filterwarnings('ignore')

st.title('Heart Disease Predictor :anatomical_heart: ')
pca_model = pickle.load(open('pca_model.pkl', 'rb'))
main_model = pickle.load(open('main_model.pkl', 'rb'))
scaler_model = pickle.load(open('scaler.pkl', 'rb'))
co = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh',
      'exng', 'oldpeak', 'slp', 'caa', 'thall']
cols = ['age', 'trtbps', 'chol', 'thalachh', 'oldpeak']  # continuous data
cols2 = ['sex', 'cp', 'fbs', 'restecg', 'exng', 'slp', 'caa', 'thall']  # descrete datas
def main():
    age = st.number_input('Enter your age', min_value=1., max_value=120.,step=1.,format="%.2f")
    sex = st.selectbox('Select your sex', ['Male ♂️', 'Female ♀️'])
    if(sex=='Male'):
        sex=float(1.0)
    else:
        sex=float(0.0)
    cp = st.selectbox('Select your chest pain type',['typical angina','atypical angina','non anginal pain','asymptomatic'] )
    if(cp=='typical angina'):
        cp=float(0.0)
    elif(cp=='atypical angina'):
        cp=float(1.0)
    elif(cp=='non anginal pain'):
        cp=float(2.0)
    else:
        cp=float(3.0)
    trtbps = st.number_input('Enter your resting blood pressure (in mm Hg)', min_value=0)
    chol = st.number_input('Enter your cholestoral in mg/dl fetched via BMI sensor', min_value=0)
    fbs = st.selectbox('Is yours fasting blood sugar > 120 mg/dl',['Yes','No'])
    if(fbs=='Yes'):
        fbs=float(1.0)
    else:
        fbs=float(0.0)
    restecg = st.selectbox('Enter your resting electrocardiographic results',['Normal','Having ST T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)','Showing probable or definite left ventricular hypertrophy by Estes criteria'])
    if(restecg=='Normal'):
        restecg=float(0.0)
    elif(restecg=='Having ST T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)'):
        restecg=float(1.0)
    else:
        restecg=float(2.0)
    thalachh = st.number_input('Enter your maximum heart rate achieved value', min_value=0)
    exng = st.selectbox('Do you have exercise induced angina',['Yes','No'])
    if(exng=='Yes'):
        exng=float(1.0)
    else:
        exng=float(0.0)
    oldpeak = st.number_input('Enter your oldpeak value', min_value=0)
    slp = st.selectbox('Select the slope of the peak exercise ST segment', ['Unsloping','Flat','Downsloping'])
    if(slp=='unsloping'):
        slp=float(0.0)
    elif(slp=='flat'):
        slp=float(1.0)
    else:
        slp=float(2.0)
    caa = st.selectbox('Select the number of major vessels',[1,2,3])
    thall = st.selectbox('Select your thalassemia value', ['Null','fixed defect','normal','reversable defect'])
    if(thall=='Null'):
        thall=float(0.0)
    elif(thall=='fixed defect'):
        thall=float(1.0)
    elif(thall=='normal'):
        thall=float(2.0)
    else:
        thall=float(3.0)

    data={
        'age':age,'sex':sex,'cp':cp,'trtbps':trtbps,'chol':chol,'fbs':fbs,'restecg':restecg,'thalachh':thalachh,'exng':exng,'oldpeak':oldpeak,'slp':slp,'caa':caa,'thall':thall
    }
    user_input=pd.DataFrame(data,index=[0])

    co = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh','exng', 'oldpeak', 'slp', 'caa', 'thall']

    user_input[cols] = scaler_model.transform(user_input[cols])
    user_input = pca_model.transform(user_input)
    pred = main_model.predict(user_input)
    pred = int(pred)
    if st.button('Submit'):
        if(pred==1):
            st.write("You have more chance of heart disease")
            st.write('Tips for you 😊')
            st.write(random_tips())
        else:
            st.write("You have less chance of heart disease")
            st.write('Tips for you 😊')
            st.write(random_tips())


if __name__ == "__main__":
    main()

