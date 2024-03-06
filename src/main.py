import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from pandas.api.types import CategoricalDtype
from scipy import stats

from modelsML import LE


def graph_plot(type, x, y, xlabel, ylabel, isSubplot, color):
    if (type != 'pie') | (ylabel != 0):
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
    if type == 'hist':
        plt.hist(x)
    elif type == 'scatter':
        plt.scatter(x, y)
    elif type == 'bar':
        if ylabel == 0:  # multibar
            return plt.bar(x, y, 0.4, label=xlabel, color=color)
        plt.bar(x, y, 0.4)
    if type == 'pie':
        plt.pie(x, labels=xlabel, autopct='%1.1f%%')


def my_function(): # gia emfanisi timwn tou graph
    print("Hello from a function")


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

####### data cleaning
print('\ndata types : \n', df.dtypes)  # verifying that data types are all correct
print('\nmissing values : \n', df.isna().sum())  # missing values detection
print('\nduplicates :\n', df[df.duplicated()])  # duplicates detection
print('\n\n', df['BP category'].unique())  # Inconsistencies detection - in one column
'''missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

temp = df
temp['Gender'] = pd.to_numeric(temp['Gender'], errors='coerce')
z_scores = stats.zscore(temp)
abs_z_scores = abs(z_scores)
outlier_rows, outlier_cols = np.where(abs_z_scores > 3)
print("Outlier Rows:", outlier_rows)

# Assuming df is your DataFrame
for column in df.columns:
    print("Column:", column)
    print(df[column].unique())
'''
plt.figure(figsize=(8, 6))
categories=['Gender','Occupation','BMI Category']
for label in categories:
    df[label]=LE.fit_transform(df[label])
sb.heatmap(data=df.drop('Person ID', axis=1).corr(numeric_only=True), cmap="YlGnBu", annot=True)
plt.legend()

####### summary statistics
print("\nmode calculation :\n ", df.mode(numeric_only=True))
#print(df[['Gender', 'BMI Category', 'Sleep Disorder']].value_counts(), "\n")  # frequencies
print("\n\n", round(df.describe(), 2))  # statistics information
print('\n\n', df.describe(include='object'))  # statistics for categorical variables


###### data visualization
'''sb.pairplot(data=df.drop('Person ID', axis=1), hue='Sleep Disorder')
plt.legend()
plt.show()'''
plt.figure(figsize=(8, 6))
graph_plot('hist', df['Sleep Duration'],0,'Sleep Duration','Frequency',True, 'r')
plt.figure(figsize=(8, 6))
plt.subplot(1, 4, 1)
graph_plot('hist', df['Age'],0,'Age','Frequency',True, 'r')
plt.subplot(1, 4, 2)
graph_plot('hist', df['Heart Rate'],0,'Heart rate(bpm)','Frequency',True, 'b')
plt.subplot(1, 4, 3)
graph_plot('hist', df['Daily Steps'],0,'Daily Steps','Frequency',True, 'g')
plt.subplot(1, 4, 4)
graph_plot('hist', df['Quality of Sleep'],0,'Quality of Sleep','Frequency',True, 'y')
plt.figure(figsize=(8, 6))
graph_plot('hist', df['Stress Level'],0,'Stress Level','Frequency',True, 'r')
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
graph_plot('hist', df['dBP'],0,'dBP','Frequency',True, 'r')
plt.subplot(1, 2, 2)
graph_plot('hist', df['sBP'],0,'sBP','Frequency',True, 'r')

plt.figure(figsize=(8, 6))
plt.subplot(1, 4, 1)
graph_plot('scatter', df['Quality of Sleep'], df['Sleep Duration'], 'Quality of Sleep', 'Sleep Duration', True, 'r')
plt.subplot(1, 4, 2)
graph_plot('scatter', df['Heart Rate'], df['Daily Steps'], 'Heart Rate', 'Daily Steps', True, 'r')
plt.subplot(1, 4, 3)
graph_plot('scatter', df['sBP'], df['dBP'], 'sBP', 'dBP', True, 'r')
plt.subplot(1, 4, 4)
graph_plot('scatter', df['Quality of Sleep'], df['Stress Level'], 'Quality of Sleep', 'Stress Level', True, 'r')

plt.figure(figsize=(8, 6))
occupation_count = df['Occupation'].value_counts().reset_index()
graph_plot('bar', occupation_count['Occupation'], occupation_count['count'], 'Occupation', 'Population', True, ['r', 'g', 'b'])

plt.figure(figsize=(8, 6))
gender_population = df['Gender'].value_counts().reset_index()
plt.subplot(2, 2, 1)
graph_plot('bar', gender_population['Gender'], gender_population['count'], 'Gender', 'Population', True, ['r', 'g', 'b'])

desired_order = ['Under Weight', 'Normal', 'Overweight', 'Obese']
df['BMI Category'] = pd.Categorical(df['BMI Category'], categories=desired_order, ordered=True)
plt.subplot(2, 2, 3)
bmiCategory_counts = df['BMI Category'].value_counts().reset_index()
bmiCategory_counts = bmiCategory_counts.sort_values('BMI Category')
plt.title('BMI Category Distribution')
graph_plot('bar', bmiCategory_counts['BMI Category'], bmiCategory_counts['count'], 'BMI Category', 'Count', True, ['r', 'g', 'b'])

plt.subplot(2, 2, 4)
sleep_disorder_counts = df['Sleep Disorder'].value_counts().reset_index()
graph_plot('bar', sleep_disorder_counts['Sleep Disorder'], sleep_disorder_counts['count'], 'Sleep Disorder', 'Count', True, ['r', 'g', 'b'])

plt.figure(figsize=(8, 6))
bpCat_counts = df['BP category'].value_counts().reset_index()
graph_plot('bar', bpCat_counts['BP category'], bpCat_counts['count'], 'blood pressure category', 'Count', True, ['r', 'g', 'b'])

plt.figure(figsize=(8, 6))
genderCounts = df['Occupation'].value_counts().reset_index()
graph_plot('pie', genderCounts['count'], 0,  genderCounts['Occupation'], 0, True, ['r', 'g', 'b'])

plt.figure(figsize=(8, 6))
graph_plot('pie', sleep_disorder_counts['count'], 0,  sleep_disorder_counts['Sleep Disorder'], 0, True, ['r', 'g', 'b'])

plt.figure(figsize=(8, 6))
avgSleepQltBySlDisorder = round(df.groupby('Sleep Disorder')['Quality of Sleep'].mean(), 2)
avgSleepQltBySlDisorder = avgSleepQltBySlDisorder.reset_index()
plt.subplot(1, 4, 1)
graph_plot('bar', avgSleepQltBySlDisorder['Sleep Disorder'], avgSleepQltBySlDisorder['Quality of Sleep'], 'Sleep Disorder', 'Quality of sleep (AVG)', True, ['r', 'g', 'b'])
for i, v in enumerate(avgSleepQltBySlDisorder['Quality of Sleep']):
    plt.text(i, v, str(v), ha='center')

avgSleepDrtBySlDisorder = round(df.groupby('Sleep Disorder')['Sleep Duration'].mean(), 2)
avgSleepDrtBySlDisorder = avgSleepDrtBySlDisorder.reset_index()
plt.subplot(1, 4, 2)
graph_plot('bar', avgSleepDrtBySlDisorder['Sleep Disorder'], avgSleepDrtBySlDisorder['Sleep Duration'], 'Sleep Disorder', 'Sleep Duration (AVG)', True, ['r', 'g', 'b'])
for i, v in enumerate(avgSleepDrtBySlDisorder['Sleep Duration']):
    plt.text(i, v, str(v), ha='center')

avgStressLvlBySlDisorder = round(df.groupby('Sleep Disorder')['Stress Level'].mean(), 2)
avgStressLvlBySlDisorder = avgStressLvlBySlDisorder.reset_index()
plt.subplot(1, 4, 3)
graph_plot('bar', avgStressLvlBySlDisorder['Sleep Disorder'], avgStressLvlBySlDisorder['Stress Level'], 'Sleep Disorder', 'Stress Level (AVG)', True, ['r', 'g', 'b'])
for i, v in enumerate(avgStressLvlBySlDisorder['Stress Level']):
    plt.text(i, v, str(v), ha='center')

avgSleepQltByBmi = round(df.groupby('BMI Category')['Quality of Sleep'].mean(), 2)
avgSleepQltByBmi = avgSleepQltByBmi.reset_index()
plt.subplot(1, 4, 4)
graph_plot('bar', avgSleepQltByBmi['BMI Category'], avgSleepQltByBmi['Quality of Sleep'], 'BMI Category', 'Quality of sleep (AVG)', True, ['r', 'g', 'b'])
for i, v in enumerate(avgSleepQltByBmi['Quality of Sleep']):
    plt.text(i, v, str(v), ha='center')
# plt.title('BMI Category Distribution')
plt.figure(figsize=(8, 6))
avgPhysicalActvLvlBybmi = df.groupby('BMI Category')['Physical Activity Level'].mean()
avgPhysicalActvLvlBybmi = avgPhysicalActvLvlBybmi.reset_index()
graph_plot('bar', avgPhysicalActvLvlBybmi['BMI Category'], avgPhysicalActvLvlBybmi['Physical Activity Level'], 'BMI Category', 'Physical Activity Level (AVG)', True, ['r', 'g', 'b'])

plt.figure(figsize=(8, 6))
avgPhysicalActvLvlBySlDisorders = df.groupby('Sleep Disorder')['Physical Activity Level'].mean()
avgPhysicalActvLvlBySlDisorders = avgPhysicalActvLvlBySlDisorders.reset_index()
graph_plot('bar', avgPhysicalActvLvlBySlDisorders['Sleep Disorder'], avgPhysicalActvLvlBySlDisorders['Physical Activity Level'], 'Sleep Disorder', 'Physical Activity Level (AVG)', True, ['r', 'g', 'b'])

plt.figure(figsize=(8, 6))
avgSBPbySlDisorders = df.groupby('Sleep Disorder')['sBP'].mean()
avgDBPbySlDisorders = df.groupby('Sleep Disorder')['dBP'].mean()
avgSBPbySlDisorders = avgSBPbySlDisorders.reset_index()
avgDBPbySlDisorders = avgDBPbySlDisorders.reset_index()
X_axis = np.arange(len(avgSBPbySlDisorders['Sleep Disorder']))
bar1 = graph_plot('bar', X_axis-0.2, avgSBPbySlDisorders['sBP'], 'Systolic BP', 0 ,True, 'r')
bar2 = graph_plot('bar', X_axis+0.2, avgDBPbySlDisorders['dBP'], 'Diastolic BP', 0, True, 'b')
plt.xticks(X_axis, avgSBPbySlDisorders['Sleep Disorder'])
plt.xlabel("Sleep Disorder")
plt.ylabel("Blood Pressure (AVG)")
plt.title("Average blood pressure per sleep disorder category")
plt.legend((bar1, bar2), ('Systolic BP', 'Diastolic BP'), facecolor='white')


plt.figure(figsize=(8, 6))
N = 3
ind = np.arange(N)
width = 0.2  # Adjust the width as needed
slDisorderPerBMIcat = df.groupby('Sleep Disorder')['BMI Category'].value_counts().reset_index()
#exit(slDisorderPerBMIcat)
xvals = slDisorderPerBMIcat.loc[slDisorderPerBMIcat['BMI Category'] == 'Under Weight', 'count']
bar1 = plt.bar(ind - width, xvals, width, color='r')
yvals = slDisorderPerBMIcat.loc[slDisorderPerBMIcat['BMI Category'] == 'Normal', 'count']
bar2 = plt.bar(ind, yvals, width, color='g')
zvals = slDisorderPerBMIcat.loc[slDisorderPerBMIcat['BMI Category'] == 'Overweight', 'count']
bar3 = plt.bar(ind + width, zvals, width, color='b')
kvals = slDisorderPerBMIcat.loc[slDisorderPerBMIcat['BMI Category'] == 'Obese', 'count']
bar4 = plt.bar(ind + 2*width, kvals, width, color='y')
plt.xlabel("Sleep disorder")
plt.ylabel('Counts')
plt.title("Distribution of BMI categories per sleep disorder")
plt.xticks(ind + width, slDisorderPerBMIcat['Sleep Disorder'].unique())
plt.legend((bar1, bar2, bar3, bar4), ('Underweight ', 'Normal', 'Overweight', 'Obese'))
#exit(slDisorderPerBMIcat['Insomnia'])

plt.figure(figsize=(8, 6))
N = 3
ind = np.arange(N)
width = 0.2  # Adjust the width as needed
slBmiStressLevels = df.groupby(['Sleep Disorder','BMI Category'])['Stress Level'].mean().reset_index()
slBmiStressLevels = slBmiStressLevels[slBmiStressLevels['BMI Category'] != 'Obese']
#exit(slBmiStressLevels)
#exit(slDisorderPerBMIcat)
xvals = slBmiStressLevels.loc[slBmiStressLevels['BMI Category'] == 'Under Weight', 'Stress Level']
bar1 = plt.bar(ind - width, xvals, width, color='r')
yvals = slBmiStressLevels.loc[slBmiStressLevels['BMI Category'] == 'Normal', 'Stress Level']
bar2 = plt.bar(ind, yvals, width, color='g')
zvals = slBmiStressLevels.loc[slBmiStressLevels['BMI Category'] == 'Overweight', 'Stress Level']
bar3 = plt.bar(ind + width, zvals, width, color='b')
plt.xlabel("Sleep disorder")
plt.ylabel('Stress Levels (AVG)')
plt.title("Effects of BMI and sleep  on Stress levels")
plt.xticks(ind + width, slBmiStressLevels['Sleep Disorder'].unique())
plt.legend((bar1, bar2, bar3), ('Underweight ', 'Normal', 'Overweight'))



plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

###### correlation analysis
print("\ncorrelations: ", round(df.corr(numeric_only=True), 3))
