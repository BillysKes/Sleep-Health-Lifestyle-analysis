import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder #for converting non-numeric data (String or Boolean) into numbers
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix

df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
df['BMI Category'] = df['BMI Category'].replace('Normal Weight', 'Under Weight')
df['Sleep Disorder'] = df['Sleep Disorder'].replace(np.nan, 'None')
#exit(df['Sleep Disorder'].value_counts())
pd.set_option('display.max_columns', None)  #
pd.set_option('display.width', None)  # fit more columns
'''sns.pairplot(data=df.drop('Person ID', axis=1), hue='Sleep Disorder')
plt.legend()
plt.show()'''
df[['sBP', 'dBP']] = df['Blood Pressure'].str.split('/', expand=True)
df[['sBP', 'dBP']] = df[['sBP', 'dBP']].astype(int)
df.loc[(df['sBP'] < 120) & (df['dBP'] < 80), 'BP category'] = 'normal'
df.loc[(((df['sBP'] < 130) & (df['sBP'] >= 120)) & (df['dBP'] < 80)), 'BP category'] = 'elevated'
df.loc[(((df['sBP']) < 140 & (df['sBP'] >= 130)) | ((df['dBP'] < 90) & (df['dBP'] >= 80))), 'BP category'] = 'hypertension stage 1'
df.loc[(df['sBP'] >= 140) | (df['dBP'] >= 90), 'BP category'] = 'hypertension stage 2'
df.loc[df['Sleep Disorder'] == 'None', 'slDisorderCat'] = 0
df.loc[df['Sleep Disorder'] == 'Sleep Apnea', 'slDisorderCat'] = 1
df.loc[df['Sleep Disorder'] == 'Insomnia', 'slDisorderCat'] = 2
#sns.pairplot(data=df, vars(['sBP','dBP']), hue='Sleep Disorder')
#plt.legend()
#sns.pairplot(data=df.drop('Person ID', axis=1), y_vars=['sBP', 'dBP'], hue='Sleep Disorder')
#plt.legend()
#plt.show()
#print(df['slDisorderCat'].value_counts())  # distribution of class 60-20-20
LE = LabelEncoder()
categories = ['Gender','Occupation','BMI Category']
for label in categories:
    df[label] = LE.fit_transform(df[label])

'''sns.heatmap(data=df.drop('Person ID', axis=1).corr(numeric_only=True), cmap="YlGnBu", annot=True)
plt.legend()
plt.show()'''
df = df.drop(['Person ID', 'sBP','dBP','Daily Steps'], axis=1)
df = df.select_dtypes(include=np.number)
x = df.iloc[:, :-1]
y = df.iloc[:, -1]
x_shape=x.shape
y_shape=y.shape
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.33,random_state=32, shuffle=True)
LR = LogisticRegression().fit(x_train, y_train)
LR_training_score=round(LR.score(x_train,y_train)*100,2)
LR_testing_score=round(LR.score(x_test,y_test)*100,2)
print(f"LR training score :",LR_training_score)
print("LR testing score :",LR_testing_score)

LR_y_pred=LR.predict(x_test)
models_predictions = [LR_y_pred]
model = {1: 'LR_y_pred', 2: 'xgb_y_pred', 3: 'CBC_y_pred', 4: 'GBC_y_pred', 5: 'svc_y_pred'}

plt.figure(figsize=(15, 7))
for i, y_pred in enumerate(models_predictions, 1):
    cm = confusion_matrix(y_pred, y_test)
    plt.subplot(2, 3, i)
    sns.heatmap(cm, cmap='BuPu', linewidth=3, fmt='', annot=True,
                xticklabels=['(None)', '(Sleep_Apnea)', '(Insomnia)'],
                yticklabels=['(None)', '(Sleep_Apnea)', '(Insomnia)'])
    plt.title(' CM of  ' + model[i])
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    plt.show()

print(f1_score(y_test, y_pred, average="macro"))
print(precision_score(y_test, y_pred, average="macro"))
print(recall_score(y_test, y_pred, average="macro"))