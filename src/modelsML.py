import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder #for converting non-numeric data (String or Boolean) into numbers
from sklearn.metrics import confusion_matrix

pd.set_option('display.max_columns', None)  #
pd.set_option('display.width', None)  # fit more columns

df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
df['BMI Category'] = df['BMI Category'].replace('Normal Weight', 'Under Weight')
df['Sleep Disorder'] = df['Sleep Disorder'].replace(np.nan, 'None')
df[['sBP', 'dBP']] = df['Blood Pressure'].str.split('/', expand=True)
df[['sBP', 'dBP']] = df[['sBP', 'dBP']].astype(int)
df.loc[(df['sBP'] < 120) & (df['dBP'] < 80), 'BP category'] = 'normal'
df.loc[(((df['sBP'] < 130) & (df['sBP'] >= 120)) & (df['dBP'] < 80)), 'BP category'] = 'elevated'
df.loc[(((df['sBP']) < 140 & (df['sBP'] >= 130)) | ((df['dBP'] < 90) & (df['dBP'] >= 80))), 'BP category'] = 'hypertension stage 1'
df.loc[(df['sBP'] >= 140) | (df['dBP'] >= 90), 'BP category'] = 'hypertension stage 2'
df.loc[df['Sleep Disorder'] == 'None', 'slDisorderCat'] = 0
df.loc[df['Sleep Disorder'] == 'Sleep Apnea', 'slDisorderCat'] = 1
df.loc[df['Sleep Disorder'] == 'Insomnia', 'slDisorderCat'] = 2

#print(df['slDisorderCat'].value_counts())  # distribution of class 60-20-20
LE = LabelEncoder()
categories = ['Gender', 'Occupation', 'BMI Category']
for label in categories:
    df[label] = LE.fit_transform(df[label])

df = df.drop(['Person ID', 'sBP', 'dBP', 'Daily Steps'], axis=1)
df = df.select_dtypes(include=np.number)
x = df.iloc[:, :-1]
x = x.to_numpy()
y = df.iloc[:, -1]
y=y.to_numpy()
x_shape = x.shape
y_shape = y.shape

k_folds = 5
kf = KFold(n_splits=k_folds, shuffle=True, random_state=42)
conf_matrices, scores = [], []
models = {'LR': LogisticRegression(max_iter=100), 'SVC': SVC()}

for name, model in models.items():
    scores = []
    i = 0
    fig, axes = plt.subplots(1, 5, figsize=(15, 7))  # Adjust figure size as needed

    for train_index, test_index in kf.split(x):
        X_train, X_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]
        model.fit(X_train, y_train)
        i = i + 1
        y_pred = model.predict(X_test)
        conf_matrix = confusion_matrix(y_test, y_pred)
        conf_matrices.append(conf_matrix)
        # Calculate accuracy score
        score = model.score(X_test, y_test)
        scores.append(score)
        cm = confusion_matrix(y_pred, y_test)
        ax = sns.heatmap(cm, cmap='BuPu', fmt='',linewidth=3, annot=True,
                         xticklabels=(['(None)', '(Sleep_Apnea)', '(Insomnia)']),
                         yticklabels=(['(None)', '(Sleep_Apnea)', '(Insomnia)']),
                         ax=axes[i - 1])  # Assign the axis object here
        ax.set_aspect('equal')  # Adjust aspect ratio here
        ax.set_yticklabels(ax.get_xticklabels(), rotation=0)
        ax.set_title("CM of " + name+" in fold "+str(i))
        ax.set_xlabel('Predicted Label')
        ax.set_ylabel('True Label')
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
    mean_score = round(np.mean(scores),3)
    print(name, " Mean Accuracy Score:", mean_score)
plt.tight_layout()
plt.show()

# Calculate mean accuracy score

