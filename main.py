import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from scipy import stats


def graph_plot(type, x, y, xlabel, ylabel, isSubplot):
    if type == 'hist':
        if y == 0:
            plt.hist(x)  # create proportion percentage plots also
        else:
            plt.hist(x,y)  # create proportion percentage plots also
    elif type == 'scatter':
        plt.scatter(x, y)
    elif type == 'bar':
        plt.bar(x, y)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)


def my_function(): # gia emfanisi timwn tou graph
    print("Hello from a function")

df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
# df.loc[df['BMI Category'] == 'Normal Weight'] = 'Under Weight'
df['BMI Category'].replace('Normal Weight', 'Under Weight', inplace=True)
df['Sleep Disorder'].replace(np.nan, 'None', inplace=True)
# print(df['Sleep Disorder'].describe())
# exit(df.loc[df['Sleep Disorder'] == 'None'])
pd.set_option('display.max_columns', None)  #
pd.set_option('display.width', None)  # fit more columns
df[['sBP', 'dBP']] = df['Blood Pressure'].str.split('/', expand=True)
df[['sBP', 'dBP']] = df[['sBP', 'dBP']].astype(int)
# print(df)

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
####### summary statistics
print("\nmean calculation :\n ", df.mean(numeric_only=True))
print("\nmedian calculation :\n ", df.median(numeric_only=True))
print("\nmode calculation :\n ", df.mode(numeric_only=True))
print("\nstandard deviation :\n ", df.std(numeric_only=True))
print(df[['Gender', 'BMI Category', 'Sleep Disorder']].value_counts(), "\n")  # frequencies
# exit()
###### data visualization

plt.subplot(1, 4, 1)
graph_plot('hist', df['Age'],0,'Age','Frequency',True)
plt.subplot(1, 4, 2)
graph_plot('hist', df['Heart Rate'],0,'Heart rate(bpm)','Frequency',True)
plt.subplot(1, 4, 3)
graph_plot('hist', df['Daily Steps'],0,'Daily Steps','Frequency',True)
plt.subplot(1, 4, 4)
graph_plot('hist', df['Quality of Sleep'],0,'Quality of Sleep','Frequency',True)

plt.figure(figsize=(8, 6))
plt.subplot(1, 4, 1)
graph_plot('scatter', df['Quality of Sleep'], df['Sleep Duration'], 'Quality of Sleep', 'Sleep Duration', True)
plt.subplot(1, 4, 2)
graph_plot('scatter', df['Heart Rate'], df['Daily Steps'], 'Heart Rate', 'Daily Steps', True)
plt.subplot(1, 4, 3)
graph_plot('scatter', df['sBP'], df['dBP'], 'sBP', 'dBP', True)
plt.subplot(1, 4, 4)
graph_plot('scatter', df['Quality of Sleep'], df['Stress Level'], 'Quality of Sleep', 'Stress Level', True)

plt.figure(figsize=(8, 6))
occupation_count = df['Occupation'].value_counts().reset_index()
graph_plot('bar', occupation_count['Occupation'], occupation_count['count'], 'Occupation', 'Population', True)

plt.figure(figsize=(8, 6))
gender_population = df['Gender'].value_counts().reset_index()
plt.subplot(2, 2, 1)
graph_plot('bar', gender_population['Gender'], gender_population['count'], 'Gender', 'Population', True)

desired_order = ['Under Weight', 'Normal', 'Overweight', 'Obese']
df['BMI Category'] = pd.Categorical(df['BMI Category'], categories=desired_order, ordered=True)
plt.subplot(2, 2, 3)
bmiCategory_counts = df['BMI Category'].value_counts().reset_index()
bmiCategory_counts = bmiCategory_counts.sort_values('BMI Category')
plt.title('BMI Category Distribution')
graph_plot('bar', bmiCategory_counts['BMI Category'], bmiCategory_counts['count'], 'BMI Category', 'Count', True)

plt.subplot(2, 2, 4)
sleep_disorder_counts = df['Sleep Disorder'].value_counts().reset_index()
graph_plot('bar', sleep_disorder_counts['Sleep Disorder'], sleep_disorder_counts['count'], 'Sleep Disorder', 'Count', True)

plt.figure(figsize=(8, 6))
avgSleepQltBySlDisorder = round(df.groupby('Sleep Disorder')['Quality of Sleep'].mean(), 2)
avgSleepQltBySlDisorder = avgSleepQltBySlDisorder.reset_index()
plt.subplot(1, 4, 1)
graph_plot('bar', avgSleepQltBySlDisorder['Sleep Disorder'], avgSleepQltBySlDisorder['Quality of Sleep'], 'Sleep Disorder', 'Quality of sleep (AVG)', True)
for i, v in enumerate(avgSleepQltBySlDisorder['Quality of Sleep']):
    plt.text(i, v, str(v), ha='center')

avgSleepDrtBySlDisorder = round(df.groupby('Sleep Disorder')['Sleep Duration'].mean(), 2)
avgSleepDrtBySlDisorder = avgSleepDrtBySlDisorder.reset_index()
plt.subplot(1, 4, 2)
graph_plot('bar', avgSleepDrtBySlDisorder['Sleep Disorder'], avgSleepDrtBySlDisorder['Sleep Duration'], 'Sleep Disorder', 'Sleep Duration (AVG)', True)
for i, v in enumerate(avgSleepDrtBySlDisorder['Sleep Duration']):
    plt.text(i, v, str(v), ha='center')

avgStressLvlBySlDisorder = round(df.groupby('Sleep Disorder')['Stress Level'].mean(), 2)
avgStressLvlBySlDisorder = avgStressLvlBySlDisorder.reset_index()
plt.subplot(1, 4, 3)
graph_plot('bar', avgStressLvlBySlDisorder['Sleep Disorder'], avgStressLvlBySlDisorder['Stress Level'], 'Sleep Disorder', 'Stress Level (AVG)', True)
for i, v in enumerate(avgStressLvlBySlDisorder['Stress Level']):
    plt.text(i, v, str(v), ha='center')

avgSleepQltByBmi = round(df.groupby('BMI Category')['Quality of Sleep'].mean(), 2)
avgSleepQltByBmi = avgSleepQltByBmi.reset_index()
plt.subplot(1, 4, 4)
graph_plot('bar', avgSleepQltByBmi['BMI Category'], avgSleepQltByBmi['Quality of Sleep'], 'BMI Category', 'Quality of sleep (AVG)', True)
for i, v in enumerate(avgSleepQltByBmi['Quality of Sleep']):
    plt.text(i, v, str(v), ha='center')
# plt.title('BMI Category Distribution')
plt.figure(figsize=(8, 6))
avgPhysicalActvLvlBybmi = df.groupby('BMI Category')['Physical Activity Level'].mean()
avgPhysicalActvLvlBybmi = avgPhysicalActvLvlBybmi.reset_index()
graph_plot('bar', avgPhysicalActvLvlBybmi['BMI Category'], avgPhysicalActvLvlBybmi['Physical Activity Level'], 'BMI Category', 'Physical Activity Level (AVG)', True)

plt.figure(figsize=(8, 6))
avgPhysicalActvLvlBySlDisorders = df.groupby('Sleep Disorder')['Physical Activity Level'].mean()
avgPhysicalActvLvlBySlDisorders = avgPhysicalActvLvlBySlDisorders.reset_index()
graph_plot('bar', avgPhysicalActvLvlBySlDisorders['Sleep Disorder'], avgPhysicalActvLvlBySlDisorders['Physical Activity Level'], 'Sleep Disorder', 'Physical Activity Level (AVG)', True)
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
###### correlation analysis
print("\ncorrelations: ", df.corr(numeric_only=True))
