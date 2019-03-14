import pandas as pd
import copy
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
advertising=pd.read_csv('wine.csv')
train,test=train_test_split(advertising,test_size=0.2)#splitting data into training and test data
train_label=train['quality']
test_label=test['quality']
#train_eda=copy.deepcopy(train)
train_eda=train.dropna(how='any',axis=0)
print(train_eda.describe())
print(train_eda.corr())
train_eda_label=train_eda['quality']#removing null data
train=train.drop(columns=['quality'])
train_eda1=train_eda.iloc[:,9:11]
#train_eda=train_eda.drop(columns=['quality'])
test=test.drop(columns=['quality'])
test1=test.dropna(how='any',axis=0)
test1=test1.iloc[:,9:11]
clf1=LinearRegression()
clf1.fit(train,train_label) #fitting Linear regression without EDA
clf2=LinearRegression()
clf2.fit(train_eda1,train_eda_label)

answer=clf1.predict(test)
answer1=clf2.predict(test1)
mean_squared_error_eda=mean_squared_error(test_label,answer1)
r2_score_eda=r2_score(test_label,answer1)
mean_squared_error1 = mean_squared_error(test_label, answer)
r2_score1 = r2_score(test_label,answer)
print("mean squared error before applying EDA is :",mean_squared_error1)
print("R2 score before applying EDA is :",r2_score1)
print("mean Squared error after applying EDA is : ",mean_squared_error_eda)
print("R2 score after applying EDA is : ",r2_score_eda)
