import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')

#df.loc[df['BMI Category'] == 'Normal Weight'] = 'Under Weight'
df['BMI Category'].replace('Normal Weight', 'Under Weight', inplace=True)
#exit(df.dtypes)
#print(df.head())
print(df)
#exit()
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
#######summary statistics
print("\nmean calculation :\n ", df.mean(numeric_only=True))
print("\nmedian calculation :\n ", df.median(numeric_only=True))
print("\nmode calculation :\n ", df.mode(numeric_only=True))
print("\nstandard deviation :\n ",df.std(numeric_only=True))
#df1 = df.groupby(['Gender', 'BMI Category','Sleep Disorder']).count()
print(df[['Gender', 'BMI Category','Sleep Disorder']].value_counts()) #frequencies

######data visualization
#df["Age"].plot(kind='hist')
#df.plot(kind='scatter', x='Age', y='Sleep Duration')
#plt.figure(figsize=(8, 6))
'''
plt.hist(df['Age'])
x, y = df['Age'], df['Sleep Duration']
plt.figure(figsize=(8, 6))
plt.scatter(x, y)
x, y = df['BMI Category'], df['Quality of Sleep']
plt.figure(figsize=(8, 6))
plt.bar(x, y)

plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
'''


######correlation analysis
print(df.corr(numeric_only=True))