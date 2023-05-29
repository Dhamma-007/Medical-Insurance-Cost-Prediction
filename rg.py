import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

insurance_dataset=pd.read_csv("insurance.csv")
insurance_dataset.replace({'sex':{'male':0,'female':1}},inplace=True)
insurance_dataset.replace({'smoker':{'yes':0,'no':1}},inplace=True)
insurance_dataset.replace({'alcoholic':{'yes':0,'no':1}},inplace=True)
insurance_dataset.replace({'diabetic':{'yes':0,'no':1}},inplace=True)
insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}},inplace=True)
X=insurance_dataset.drop(columns='charges',axis=1)
Y=insurance_dataset['charges']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)
regressor=LinearRegression()
regressor.fit(X_train,Y_train)
model2=DecisionTreeRegressor()
model2.fit(X_train,Y_train)
model3 = GradientBoostingRegressor()
model3.fit(X_train,Y_train)
def prdt(age,sex,bmi,children,smoker,alcoholic,diabetic,region):
    age=int(age)
    if(sex=='Male'):
        sex=int(0)
    else:
        sex=int(1)
    if(smoker=='Yes'):
        smoker=int(0)
    else:
        smoker=int(1)
    if(region=='SouthEast'):
        region=int(0)
    elif(region=='SouthWest'):
        region=int(1)
    elif(region=='NorthEast'):
        region=int(2)
    else:
        region=int(3)
    if (alcoholic == 'Yes'):
        alcoholic = int(0)
    else:
        alcoholic = int(1)
    if (diabetic == 'Yes'):
        diabetic = int(0)
    else:
        diabetic = int(1)

    input_data=(age,sex,bmi,children,smoker,alcoholic,diabetic,region)
    input_data_np_array=np.asarray(input_data)
    input_data_rehsaped=input_data_np_array.reshape(1,-1)
    result=regressor.predict(input_data_rehsaped)
    result2=model2.predict(input_data_rehsaped)
    result3=model3.predict(input_data_rehsaped)
    return result,result2,result3

