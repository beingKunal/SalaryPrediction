import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

selected = st.sidebar.selectbox("Predict or Explore" , ('Predict' , 'Explore'))
show_predict_page() if(selected == 'Predict') else show_explore_page()
