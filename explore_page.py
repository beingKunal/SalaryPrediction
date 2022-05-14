import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def shorten_categories(categories , cutOff):
    country_map = {}
    for country in categories.keys():
        if(categories[country] >= cutOff):
            country_map[country] = country
        else:
            country_map[country] = 'Others' 
    return country_map

def refactorEdLevel(edLevel):
    if("Master’s degree" in edLevel):
        return "Master's degree"
    if("Bachelor’s degree" in edLevel):
        return "Bachelor's degree"
    if("Other doctoral" in edLevel or "Professional degree" in edLevel):
        return "Doctorate degree"
    return "Less than Bachelor"

def refactorYearofPro(yearsOfPro):
    if(yearsOfPro == 'More than 50 years'):
        return 50
    if(yearsOfPro == 'Less than 1 year'):
        return 0.5
    return float(yearsOfPro)

@st.cache
def loadData():
    # data cleaning
    df = pd.read_csv('survey_results_public.csv')
    df  = df.loc[: , ['Country' , 'EdLevel','YearsCodePro','ConvertedCompYearly']]
    df.rename(columns={'ConvertedCompYearly' : 'Salary'} , inplace = True)
    salaryNaIndex = df.loc[df.Salary.isnull(),:].index
    df.drop(labels = salaryNaIndex , axis = 0 , inplace=True)
    countries_count = df.Country.value_counts()
    df =  df.dropna()
    countries_count_res = shorten_categories(countries_count , 400)
    df['Country'] = df['Country'].map(countries_count_res)
    df = df.loc[(df.Salary <= 250000) & (df.Salary>10000) , :]
    df = df.loc[~(df.Country == 'Others'),:]
    df.YearsCodePro = df.YearsCodePro.apply(refactorYearofPro)    
    df.EdLevel = df.EdLevel.apply(refactorEdLevel)
    return df
    
df = loadData()

def show_explore_page():
    st.title("Explore developer Salaries survey")
    st.write("""
    ### Stack overflow developer survey 2021
    """)
    data = df["Country"].value_counts()

    fig1 , ax1 = plt.subplots(figsize=(12,14))
    ax1.pie(data , labels=data.index , autopct="%1.1f%%" ,shadow=True , startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)