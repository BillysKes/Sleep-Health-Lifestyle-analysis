import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn import svm



df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
df['BMI Category'].replace('Normal Weight', 'Under Weight', inplace=True)
df['Sleep Disorder'].replace(np.nan, 'None', inplace=True)
pd.set_option('display.max_columns', None)  #
pd.set_option('display.width', None)  # fit more columns
df[['sBP', 'dBP']] = df['Blood Pressure'].str.split('/', expand=True)
df[['sBP', 'dBP']] = df[['sBP', 'dBP']].astype(int)
df.loc[(df['sBP'] < 120) & (df['dBP'] < 80), 'BP category'] = 'normal'
df.loc[(((df['sBP'] < 130) & (df['sBP'] >= 120)) & (df['dBP'] < 80)), 'BP category'] = 'elevated'
df.loc[(((df['sBP']) < 140 & (df['sBP'] >= 130)) | ((df['dBP'] < 90) & (df['dBP'] >= 80))), 'BP category'] = 'hypertension stage 1'
df.loc[(df['sBP'] >= 140) | (df['dBP'] >= 90), 'BP category'] = 'hypertension stage 2'

df.loc[df['Sleep Disorder'] == 'None', 'slDisorderCat'] = 0
df.loc[df['Sleep Disorder'] == 'Sleep Apnea', 'slDisorderCat'] = 1
df.loc[df['Sleep Disorder'] == 'Insomnia', 'slDisorderCat'] = 2

X = df[df.columns[:-1]]
y = df.iloc[:, -1:]
X = X._get_numeric_data().to_numpy()
X_train, X_test, y_train, y_test = train_test_split( X, y, train_size=0.80, test_size=0.20, random_state=101)

print(y_train)
print(y_test)
#clf = svm.SVC(decision_function_shape='ovo')
#clf.fit(X, y)
#print(train_test_split(y, shuffle=False))
'''poly = svm.SVC(kernel='poly', degree=3, C=1).fit(X_train, y_train)
rbf = svm.SVC(kernel='rbf', gamma=0.5, C=0.1).fit(X_train, np.ravel(y_train))
rbf_pred = rbf.predict(X_test)
poly_pred = poly.predict(X_test)

poly_accuracy = accuracy_score(y_test, poly_pred)
poly_f1 = f1_score(y_test, poly_pred, average='weighted')
print('Accuracy (Polynomial Kernel): ', "%.2f" % (poly_accuracy*100))
print('F1 (Polynomial Kernel): ', "%.2f" % (poly_f1*100))
rbf_accuracy = accuracy_score(y_test, rbf_pred)
rbf_f1 = f1_score(y_test, rbf_pred, average='weighted')
print('Accuracy (RBF Kernel): ', "%.2f" % (rbf_accuracy*100))
print('F1 (RBF Kernel): ', "%.2f" % (rbf_f1*100))
#print(rbf_pred)
#print(poly_pred)'''
