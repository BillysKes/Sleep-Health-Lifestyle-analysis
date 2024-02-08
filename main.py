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
#df1 = df.groupby(['Gender', 'BMI Category','Sleep Disorder']).count()
print(df[['Gender', 'BMI Category','Sleep Disorder']].value_counts(),"\n") #frequencies

###### data visualization
#df["Age"].plot(kind='hist')
#df.plot(kind='scatter', x='Age', y='Sleep Duration')
#plt.figure(figsize=(8, 6))



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
x, y = df['Quality of Sleep'], df['Sleep Duration']
plt.figure(figsize=(8, 6))
plt.scatter(x, y)
plt.ylabel('Sleep Duration')
plt.xlabel('Quality of Sleep')
x, y = df['Heart Rate'], df['Daily Steps']
plt.figure(figsize=(8, 6))
plt.scatter(x, y)
plt.ylabel('Daily Steps')
plt.xlabel('Heart Rate')
x, y = df['sBP'], df['dBP']
plt.figure(figsize=(8, 6))
plt.scatter(x, y)
plt.ylabel('dBP')
plt.xlabel('sBP')
x, y = df['Quality of Sleep'], df['Stress Level']
plt.figure(figsize=(8, 6))
plt.scatter(x, y)
plt.ylabel('Stress Level')
plt.xlabel('Quality of Sleep')

x, y = df['BMI Category'], df['Quality of Sleep']
plt.figure(figsize=(8, 6))
plt.bar(x, y)
plt.ylabel('Quality of Sleep')
plt.xlabel('BMI Category')
x, y = df['Gender'], df['Person ID']
plt.figure(figsize=(8, 6))
plt.bar(x, y)
plt.ylabel('Population')
plt.xlabel('Gender')
x, y = df['Occupation'], df['Person ID']
plt.figure(figsize=(8, 6))
plt.bar(x, y)
plt.ylabel('Population')
plt.xlabel('Occupation')
# Define the desired order of categories
desired_order = ['Under Weight', 'Normal', 'Overweight', 'Obese']
# Convert 'BMI Category' column to categorical with desired order
df['BMI Category'] = pd.Categorical(df['BMI Category'], categories=desired_order, ordered=True)
#exit(df['BMI Category'].unique())

# Sort DataFrame by 'BMI Category' column
df = df.sort_values('BMI Category')
# Plotting
plt.figure(figsize=(8, 6))
plt.bar(df['BMI Category'], df['Person ID'])
plt.xlabel('BMI Category')
plt.ylabel('Count')
plt.title('BMI Category Distribution')
#exit(df['Sleep Disorder'].unique())
plt.figure(figsize=(8, 6))
plt.bar(df['Sleep Disorder'], df['Person ID'])
plt.xlabel('Sleep Disorder')
plt.ylabel('Count')
mean_sleep_quality_by_slDisorder = df.groupby('Sleep Disorder')['Quality of Sleep'].mean()
mean_sleep_quality_by_slDisorder=mean_sleep_quality_by_slDisorder.reset_index()
plt.figure(figsize=(8, 6))
plt.bar(mean_sleep_quality_by_slDisorder['Sleep Disorder'], mean_sleep_quality_by_slDisorder['Quality of Sleep'])
plt.xlabel('Sleep Disorder')
plt.ylabel('Quality of sleep (AVG)')


#plt.title('BMI Category Distribution')
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

###### correlation analysis
print("\ncorrelations: ", df.corr(numeric_only=True))
