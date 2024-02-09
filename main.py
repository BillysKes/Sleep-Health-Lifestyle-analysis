import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from scipy import stats

df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
#df.loc[df['BMI Category'] == 'Normal Weight'] = 'Under Weight'
df['BMI Category'].replace('Normal Weight', 'Under Weight', inplace=True)
df['Sleep Disorder'].replace(np.nan, 'None', inplace=True)

#print(df['Sleep Disorder'].describe())
#exit(df.loc[df['Sleep Disorder'] == 'None'])
pd.set_option('display.max_columns', None) #
pd.set_option('display.width', None)         # fit more columns
df[['sBP', 'dBP']] = df['Blood Pressure'].str.split('/', expand=True)
df[['sBP', 'dBP']] = df[['sBP', 'dBP']].astype(int)
#print(df)

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
print("\nstandard deviation :\n ",df.std(numeric_only=True))
print(df[['Gender', 'BMI Category','Sleep Disorder']].value_counts(),"\n") #frequencies
#exit()
###### data visualization

plt.subplot(1, 4, 1)
plt.hist(df['Age']) # create proportion percentage plots also
plt.ylabel('Frequency')
plt.xlabel('Age')
plt.subplot(1, 4, 2)
plt.hist(df['Heart Rate'])
plt.ylabel('Frequency')
plt.xlabel('Heart rate(bpm)')
plt.subplot(1,4,3)
plt.hist(df['Daily Steps'])
plt.ylabel('Frequency')
plt.xlabel('Daily Steps')
plt.subplot(1,4,4)
plt.hist(df['Quality of Sleep'])
plt.ylabel('Frequency')
plt.xlabel('Quality of Sleep')

plt.figure(figsize=(8, 6))
x, y = df['Quality of Sleep'], df['Sleep Duration']
plt.subplot(1, 4, 1)
plt.scatter(x, y)
plt.ylabel('Sleep Duration')
plt.xlabel('Quality of Sleep')
x, y = df['Heart Rate'], df['Daily Steps']
plt.subplot(1, 4, 2)
plt.scatter(x, y)
plt.ylabel('Daily Steps')
plt.xlabel('Heart Rate')
x, y = df['sBP'], df['dBP']
plt.subplot(1, 4, 3)
plt.scatter(x, y)
plt.ylabel('dBP')
plt.xlabel('sBP')
x, y = df['Quality of Sleep'], df['Stress Level']
plt.subplot(1, 4, 4)
plt.scatter(x, y)
plt.ylabel('Stress Level')
plt.xlabel('Quality of Sleep')

plt.figure(figsize=(8, 6))
occupation_count = df['Occupation'].value_counts().reset_index()
plt.bar(occupation_count['Occupation'], occupation_count['count'])
plt.ylabel('Population')
plt.xlabel('Occupation')
plt.figure(figsize=(8, 6))
gender_population = df['Gender'].value_counts().reset_index()
plt.subplot(2, 2, 1)
plt.bar(gender_population['Gender'], gender_population['count'])
plt.ylabel('Population')
plt.xlabel('Gender')
desired_order = ['Under Weight', 'Normal', 'Overweight', 'Obese']
df['BMI Category'] = pd.Categorical(df['BMI Category'], categories=desired_order, ordered=True)
#exit(df['BMI Category'].unique())

plt.subplot(2, 2, 3)
bmiCategory_counts = df['BMI Category'].value_counts().reset_index()
bmiCategory_counts = bmiCategory_counts.sort_values('BMI Category')
plt.bar(bmiCategory_counts['BMI Category'], bmiCategory_counts['count'])
plt.xlabel('BMI Category')
plt.ylabel('Count')
plt.title('BMI Category Distribution')
plt.subplot(2, 2, 4)
sleep_disorder_counts = df['Sleep Disorder'].value_counts().reset_index()
plt.bar(sleep_disorder_counts['Sleep Disorder'], sleep_disorder_counts['count'])
plt.xlabel('Sleep Disorder')
plt.ylabel('Count')

plt.figure(figsize=(8, 6))
mean_sleep_quality_by_slDisorder = df.groupby('Sleep Disorder')['Quality of Sleep'].mean()
mean_sleep_quality_by_slDisorder=mean_sleep_quality_by_slDisorder.reset_index()
plt.subplot(1, 4, 1)
plt.bar(mean_sleep_quality_by_slDisorder['Sleep Disorder'], mean_sleep_quality_by_slDisorder['Quality of Sleep'])
plt.xlabel('Sleep Disorder')
plt.ylabel('Quality of sleep (AVG)')
mean_sleep_duration_by_slDisorder = df.groupby('Sleep Disorder')['Sleep Duration'].mean()
mean_sleep_duration_by_slDisorder = mean_sleep_duration_by_slDisorder.reset_index()
plt.subplot(1, 4, 2)
plt.bar(mean_sleep_quality_by_slDisorder['Sleep Disorder'], mean_sleep_duration_by_slDisorder['Sleep Duration'])
plt.xlabel('Sleep Disorder')
plt.ylabel('Sleep Duration (AVG)')
mean_stressLvl_by_sleepDisorder = df.groupby('Sleep Disorder')['Stress Level'].mean()
mean_stressLvl_by_sleepDisorder = mean_stressLvl_by_sleepDisorder.reset_index()
plt.subplot(1, 4, 3)
plt.bar(mean_stressLvl_by_sleepDisorder['Sleep Disorder'], mean_stressLvl_by_sleepDisorder['Stress Level'])
plt.xlabel('Sleep Disorder')
plt.ylabel('Stress Level (AVG)')
mean_sleep_quality_by_bmi = df.groupby('BMI Category')['Quality of Sleep'].mean()
mean_sleep_quality_by_bmi = mean_sleep_quality_by_bmi.reset_index()
plt.subplot(1, 4, 4)
plt.bar(mean_sleep_quality_by_bmi['BMI Category'], mean_sleep_quality_by_bmi['Quality of Sleep'])
plt.xlabel('BMI Category')
plt.ylabel('Quality of sleep (AVG)')
#plt.title('BMI Category Distribution')
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

###### correlation analysis
print("\ncorrelations: ", df.corr(numeric_only=True))
