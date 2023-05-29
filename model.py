import numpy as np
import streamlit as st
from rg import prdt

def main():
    string="Medical Insurance Cost Prediction"
    st.set_page_config(page_title=string,page_icon="@")

    st.image('health_insurance.jpg',width=300)
    st.title("Medical Insurance Cost Prediction")
    st.markdown("You can predict your health Insurance Cost")
    age=st.number_input('Enter your age')
    gender=st.selectbox("Gender",['--select--','Male','Female'])
    bmi=st.number_input('BMI')
    children=st.number_input('No. of childrens')
    smoker=st.selectbox("Smoker",['--select--','Yes','No'])
    alcoholic=st.selectbox("Alcoholic",['--select--','Yes','No'])
    diabetic=st.selectbox("Diabetic",['--select--','Yes','No'])
    region=st.selectbox("Region",['--select--','SouthEast','SouthWest','NorthEast','NorthWest'])
    a=st.button("Predict")
    if(a):
        ans,ans2,ans3=prdt(age,gender,bmi,children,smoker,alcoholic,diabetic,region)
        st.text("Predicted Value in Euro(€) is: ")
        st.text(ans)
        st.text(ans2)
        st.text(ans3)


if __name__=='__main__':
    main()