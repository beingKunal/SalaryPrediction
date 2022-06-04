import numpy as np
import streamlit as st
import pickle

def loadModel():
    with open('savedModel.pkl' , 'rb') as file:
        data = pickle.load(file)
    return data

data = loadModel()
load_regressor = data['regressor']
load_enocoder_con = data['labelEncoderCountry']
load_encoder_edu = data['labelEncoderEducation']

def show_predict_page():
    st.title("Salary Prediction !")
    countries = ("India","Germany","United Kingdom of Great Britain and Northern Ireland","Canada" , "France"                                              
            "Brazil "                                              
            "Poland "                                              
            "Netherlands"                                          
            "Spain",                                           
            "Australia",                                            
            "Italy",                                              
            "Russian Federation",                                   
            "Sweden",                                              
            "Switzerland",                                         
            "Turkey",                                              
            "Israel",                                              
            "Ukraine",                                              
            "Iran, Islamic Republic of...",                       
            "Austria",                                            
            "Mexico",                                              
            "Czech Republic",                                       
            "Norway",                                              
            "Belgium",                                              
            "Argentina"                                            
            "Denmark")

    educationLevel = ("Bachelor's degree" , "Master's degree" , "Less than Bachelor" , "Doctorate degree")
    country = st.selectbox("Select country", countries)
    edLevel = st.selectbox("Education Level" , educationLevel)
    yearOfExperience = st.slider("Year of Experience" , 0 , 50 ,3)    
    test_point = np.array([[country , edLevel ,  yearOfExperience]])
    ok = st.button("Predict Salary")
    if(ok):
        test_point[:,0] = load_enocoder_con.transform(test_point[:,0])
        test_point[:,1] = load_encoder_edu.transform(test_point[:,1])
        test_point = test_point.astype(float)
        predictedSalary = load_regressor.predict(test_point)
        st.subheader(f'Predicted Salary ${predictedSalary[0]:.2f}')
    
    