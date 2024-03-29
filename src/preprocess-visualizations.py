import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.preprocessing import LabelEncoder


def graph_plot(type, x, y, xlabel, ylabel, isSubplot, color):
    if isSubplot == 0:
        plt.figure(figsize=(8, 6))
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


pd.set_option('display.max_columns', None)  #
pd.set_option('display.width', None)  # fit more columns

df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')

df.loc[df['BMI Category'] == 'Normal Weight', 'BMI Category'] = 'Under Weight'

df.fillna({'Sleep Disorder': 'None'}, inplace=True)
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
numeric_columns = df.select_dtypes(include=np.number)
z_scores = np.abs((numeric_columns - numeric_columns.mean()) / numeric_columns.std())
outlier_rows = z_scores > 3


categories = ['Gender', 'Occupation', 'BMI Category']
temp_df = df.copy()
LE = LabelEncoder()
for label in categories:
    temp_df[label] = LE.fit_transform(temp_df[label])
sb.heatmap(data=temp_df.drop('Person ID', axis=1).corr(numeric_only=True), cmap="YlGnBu", annot=True)

####### summary statistics
print("\nmode calculation :\n ", df.mode(numeric_only=True))
#print(df[['Gender', 'BMI Category', 'Sleep Disorder']].value_counts(), "\n")  # frequencies
print("\n\n", round(df.describe(), 2))  # statistics information
print('\n\n', df.describe(include='object'))  # statistics for categorical variables

###### data visualization
sb.pairplot(data=df.drop('Person ID', axis=1), hue='Sleep Disorder')
graph_plot('hist', df['Sleep Duration'],0,'Sleep Duration','Frequency',0, 'r')
plt.figure(figsize=(8, 6))
plt.subplot(1, 4, 1)
graph_plot('hist', df['Age'],0,'Age','Frequency',1, 'r')
plt.subplot(1, 4, 2)
graph_plot('hist', df['Heart Rate'],0,'Heart rate(bpm)','Frequency',1, 'b')
plt.subplot(1, 4, 3)
graph_plot('hist', df['Daily Steps'],0,'Daily Steps','Frequency',1, 'g')
plt.subplot(1, 4, 4)
graph_plot('hist', df['Quality of Sleep'],0,'Quality of Sleep','Frequency',1, 'y')
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
graph_plot('hist', df['dBP'],0,'dBP','Frequency',1, 'r')
plt.subplot(1, 2, 2)
graph_plot('hist', df['sBP'],0,'sBP','Frequency',1, 'r')

plt.figure(figsize=(8, 6))
plt.subplot(1, 4, 1)
graph_plot('scatter', df['Quality of Sleep'], df['Sleep Duration'], 'Quality of Sleep', 'Sleep Duration', 1, 'r')
plt.subplot(1, 4, 2)
graph_plot('scatter', df['Heart Rate'], df['Daily Steps'], 'Heart Rate', 'Daily Steps', 1, 'r')
plt.subplot(1, 4, 3)
graph_plot('scatter', df['sBP'], df['dBP'], 'sBP', 'dBP', 1, 'r')
plt.subplot(1, 4, 4)
graph_plot('scatter', df['Quality of Sleep'], df['Stress Level'], 'Quality of Sleep', 'Stress Level', 1, 'r')

occupation_count = df['Occupation'].value_counts().reset_index()
graph_plot('bar', occupation_count['Occupation'], occupation_count['count'], 'Occupation', 'Population', 0, ['r', 'g', 'b'])


gender_population = df['Gender'].value_counts().reset_index()
plt.figure(figsize=(8, 6))
plt.subplot(2, 2, 1)
graph_plot('bar', gender_population['Gender'], gender_population['count'], 'Gender', 'Population', 1, ['r', 'g', 'b'])

desired_order = ['Under Weight', 'Normal', 'Overweight', 'Obese']
df['BMI Category'] = pd.Categorical(df['BMI Category'], categories=desired_order, ordered=True)
plt.subplot(2, 2, 3)
bmiCategory_counts = df['BMI Category'].value_counts().reset_index()
bmiCategory_counts = bmiCategory_counts.sort_values('BMI Category')
plt.title('BMI Category Distribution')
graph_plot('bar', bmiCategory_counts['BMI Category'], bmiCategory_counts['count'], 'BMI Category', 'Count', 1, ['r', 'g', 'b'])

plt.subplot(2, 2, 4)
sleep_disorder_counts = df['Sleep Disorder'].value_counts().reset_index()
graph_plot('bar', sleep_disorder_counts['Sleep Disorder'], sleep_disorder_counts['count'], 'Sleep Disorder', 'Count', 1, ['r', 'g', 'b'])



bpCat_counts = df['BP category'].value_counts().reset_index()
graph_plot('bar', bpCat_counts['BP category'], bpCat_counts['count'], 'blood pressure category', 'Count', 0, ['r', 'g', 'b'])

genderCounts = df['Occupation'].value_counts().reset_index()
graph_plot('pie', genderCounts['count'], 0,  genderCounts['Occupation'], 0, 0, ['r', 'g', 'b'])

graph_plot('pie', sleep_disorder_counts['count'], 0,  sleep_disorder_counts['Sleep Disorder'], 0, 0, ['r', 'g', 'b'])
plt.show()

avgSleepQltBySlDisorder = round(df.groupby('Sleep Disorder')['Quality of Sleep'].mean(), 2)
avgSleepQltBySlDisorder = avgSleepQltBySlDisorder.reset_index()
plt.figure(figsize=(8, 6))
plt.subplot(1, 4, 1)
graph_plot('bar', avgSleepQltBySlDisorder['Sleep Disorder'], avgSleepQltBySlDisorder['Quality of Sleep'], 'Sleep Disorder', 'Quality of sleep (AVG)', 1, ['r', 'g', 'b'])
for i, v in enumerate(avgSleepQltBySlDisorder['Quality of Sleep']):
    plt.text(i, v, str(v), ha='center')

avgSleepDrtBySlDisorder = round(df.groupby('Sleep Disorder')['Sleep Duration'].mean(), 2)
avgSleepDrtBySlDisorder = avgSleepDrtBySlDisorder.reset_index()
plt.subplot(1, 4, 2)
graph_plot('bar', avgSleepDrtBySlDisorder['Sleep Disorder'], avgSleepDrtBySlDisorder['Sleep Duration'], 'Sleep Disorder', 'Sleep Duration (AVG)', 1, ['r', 'g', 'b'])
for i, v in enumerate(avgSleepDrtBySlDisorder['Sleep Duration']):
    plt.text(i, v, str(v), ha='center')

avgStressLvlBySlDisorder = round(df.groupby('Sleep Disorder')['Stress Level'].mean(), 2)
avgStressLvlBySlDisorder = avgStressLvlBySlDisorder.reset_index()
plt.subplot(1, 4, 3)
graph_plot('bar', avgStressLvlBySlDisorder['Sleep Disorder'], avgStressLvlBySlDisorder['Stress Level'], 'Sleep Disorder', 'Stress Level (AVG)', 1, ['r', 'g', 'b'])
for i, v in enumerate(avgStressLvlBySlDisorder['Stress Level']):
    plt.text(i, v, str(v), ha='center')

avgSleepQltByBmi = round(df.groupby('BMI Category')['Quality of Sleep'].mean(), 2)
avgSleepQltByBmi = avgSleepQltByBmi.reset_index()
plt.subplot(1, 4, 4)
graph_plot('bar', avgSleepQltByBmi['BMI Category'], avgSleepQltByBmi['Quality of Sleep'], 'BMI Category', 'Quality of sleep (AVG)', 1, ['r', 'g', 'b'])
for i, v in enumerate(avgSleepQltByBmi['Quality of Sleep']):
    plt.text(i, v, str(v), ha='center')
# plt.title('BMI Category Distribution')
avgPhysicalActvLvlBybmi = df.groupby('BMI Category')['Physical Activity Level'].mean()
avgPhysicalActvLvlBybmi = avgPhysicalActvLvlBybmi.reset_index()
graph_plot('bar', avgPhysicalActvLvlBybmi['BMI Category'], avgPhysicalActvLvlBybmi['Physical Activity Level'], 'BMI Category', 'Physical Activity Level (AVG)', 0, ['r', 'g', 'b'])

avgPhysicalActvLvlBySlDisorders = df.groupby('Sleep Disorder')['Physical Activity Level'].mean()
avgPhysicalActvLvlBySlDisorders = avgPhysicalActvLvlBySlDisorders.reset_index()
graph_plot('bar', avgPhysicalActvLvlBySlDisorders['Sleep Disorder'], avgPhysicalActvLvlBySlDisorders['Physical Activity Level'], 'Sleep Disorder', 'Physical Activity Level (AVG)', 0, ['r', 'g', 'b'])

plt.figure(figsize=(8, 6))
avgSBPbySlDisorders = df.groupby('Sleep Disorder')['sBP'].mean()
avgDBPbySlDisorders = df.groupby('Sleep Disorder')['dBP'].mean()
avgSBPbySlDisorders = avgSBPbySlDisorders.reset_index()
avgDBPbySlDisorders = avgDBPbySlDisorders.reset_index()
X_axis = np.arange(len(avgSBPbySlDisorders['Sleep Disorder']))
bar1 = graph_plot('bar', X_axis-0.2, avgSBPbySlDisorders['sBP'], 'Systolic BP', 0 ,1, 'r')
bar2 = graph_plot('bar', X_axis+0.2, avgDBPbySlDisorders['dBP'], 'Diastolic BP', 0, 1, 'b')
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

plt.figure(figsize=(8, 6))
N = 3
ind = np.arange(N)
width = 0.2  # Adjust the width as needed
slBmiStressLevels = df.groupby(['Sleep Disorder','BMI Category'])['Stress Level'].mean().reset_index()
slBmiStressLevels = slBmiStressLevels[slBmiStressLevels['BMI Category'] != 'Obese']
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


