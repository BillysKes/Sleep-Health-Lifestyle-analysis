# Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset Description](#dataset-description)
3. [Summary Statistics](#summary-statistics)
4. [Data preprocessing](#data-preprocessing)
5. [Visualizations](#visualizations)
   1. [Bar-Pie Charts](#Bar-Pie-Charts)
   2. [Scatter Plots](#Scatter-Plots)
   3. [Histograms](#Histograms)
6. [Correlation analysis](#correlation-analysis)
7. [Classification](#classification)
   1. [Support Vector Classifier](#svc)
   2. [Logistic Regression](#llc)




        


# 1. Project overview
The aim of this project is to analyze the Sleep Health and Lifestyle Dataset, which include 400 rows and 13 columns. This dataset provides comprehensive insights into various factors influencing sleep quality and daily habits among individuals. By implementing Exploratory Data Analysis, we intend to uncover patterns, correlations, and significant associations within the data. Finally, we also intend to predict if an individual has a sleep disorder using classification algorithms.


# 2. Dataset Description
The dataset used in this project can be accessed  through Kaggle. You can find more information here : https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset

# 3. Data preprocessing
```
df.loc[df['BMI Category'] == 'Normal Weight', 'BMI Category'] = 'Under Weight'
```
While examining the unique values of BMI Category, we find out a data entry error : ['Overweight' 'Normal' 'Obese' 'Normal Weight']. Under weight category is missing and the normal category is duplicated, so we replace 'Normal Weight' with 'Under Weight'.


```
df.fillna({'Sleep Disorder': 'None'}, inplace=True)
```
Missing values of Sleep disorder are being filled with a string value. 


```
df[['sBP', 'dBP']] = df['Blood Pressure'].str.split('/', expand=True)
df[['sBP', 'dBP']] = df[['sBP', 'dBP']].astype(int)
df.loc[(df['sBP'] < 120) & (df['dBP'] < 80), 'BP category'] = 'normal'
df.loc[(((df['sBP'] < 130) & (df['sBP'] >= 120)) & (df['dBP'] < 80)), 'BP category'] = 'elevated'
df.loc[(((df['sBP']) < 140 & (df['sBP'] >= 130)) | ((df['dBP'] < 90) & (df['dBP'] >= 80))), 'BP category'] = 'hypertension stage 1'
df.loc[(df['sBP'] >= 140) | (df['dBP'] >= 90), 'BP category'] = 'hypertension stage 2'
```
We create two seperate columns for systolic and diastolic Blood pressure. Also, we create another column to label in which BP category the individual belongs to, based on American Heart Association(AHA) guidelines.

# 4. Summary Statistics
```
        Person ID     Age  Sleep Duration  Quality of Sleep  Physical Activity Level  Stress Level  Heart Rate  Daily Steps     sBP     dBP
count     374.00  374.00          374.00            374.00                   374.00        374.00      374.00       374.00  374.00  374.00
mean      187.50   42.18            7.13              7.31                    59.17          5.39       70.17      6816.84  128.55   84.65
std       108.11    8.67            0.80              1.20                    20.83          1.77        4.14      1617.92    7.75    6.16
min         1.00   27.00            5.80              4.00                    30.00          3.00       65.00      3000.00  115.00   75.00
25%        94.25   35.25            6.40              6.00                    45.00          4.00       68.00      5600.00  125.00   80.00
50%       187.50   43.00            7.20              7.00                    60.00          5.00       70.00      7000.00  130.00   85.00
75%       280.75   50.00            7.80              8.00                    75.00          7.00       72.00      8000.00  135.00   90.00
max       374.00   59.00            8.50              9.00                    90.00          8.00       86.00     10000.00  142.00   95.00
```

```
       Gender Occupation BMI Category Blood Pressure Sleep Disorder           BP category
count     374        374          374            374            374                   374
unique      2         11            4             25              3                     4
top      Male      Nurse       Normal         130/85           None  hypertension stage 1
freq      189         73          195             99            219                   232
```


# 5. Visualizations
 

## 5.1 Bar-Pie Charts
<a name="Bar-Pie-Charts"></a>


- Population of males and females are equal
- Most individuals in the dataset have a normal body mass index or they are are in the overweight category
- Almost 60% of the individuals doesn't have any sleep disorder while the rest have insomnia or sleep apnea equally
- Doctors, nurses, engineers and lawyers mainly took part in this research analysis
- Individuals with insomnia have worse quality of sleep and smaller duration of sleep compared to individuals with sleep apnea
- Stress level is slightly higher for individuals who have insomnia compared to those who have sleep apnea. However, individuals who doesnt't any sleep disorder have similar stress levels on average.
- Quality of sleep significantly drops for overweight and obese individuals. 

![barcharts](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/b86258dc-aab8-4e91-9c7d-53c677fb18f9)

![sleep disorders pie](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/c06a376e-5138-4445-9eb2-47cb01ff42f3)

![occupationsDistrib](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/4ccd2666-66fb-4c9f-ad1d-c6cba99323d2)

![occupationsPie](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/4cfdee09-58fc-4695-8e93-5ce80da29e69)


![histogramsNewBetter](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/0d1f6d44-e2d4-49ad-a5b0-de421b5077b6)


![avgBPbySldisorder](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/6772ee33-b1cd-4fdc-bae3-460cd33aa038)

![bmiDistributionperSleepDisorder](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/1c28a43c-538f-433f-804b-684cac6d7422)

![stressLVLbyBMIandSleep](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/ffea0327-3f26-47d2-b5bd-efbc1a1085cd)



## 5.2 Scatter Plots
<a name="Scatter-Plots"></a>
There is a high positive correlation of quality of sleep and sleep duration which means that individuals who sleep longer have higher scores on quality of sleep. Also, there is a negative correlation of heart rate and daily steps which means, individuals who doens't walk a lot tend to have higher heart rate. Also, there is a positive correlation of sbP and dBP which means, individuals with high systolic blood pressure also have high diastolic blood pressure and the reverse. We also notice that high stress levels are associated with low quality of sleep(negative correlation).

- Positive correlation of quality of sleep and sleep duration. As sleep duration increases we notice that individuals report higher ratings on quality of sleep as well whereas the exact opposite happens when sleep duration is shorter.
- Negative correlation of the heart rate(bpm) and the daily steps taken. Individuals who walk more tend to have more normal heart rate due to the benefits of cardiovascular exercise
- Positive correlation of systolic blood pressure(SBP) and diastolic blood pressure(DBP)
- Negative correlation of quality of sleep and stress level. Individuals reporting better quality of sleep tend to report lower stress levels.

![scatterplots](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/987df6e0-d07f-4de2-a94e-69ccee17d74c)


### 5.3 Histograms
<a name="histograms"></a>

- Positive skewness most individuals heart rate is on the range of 65-73 bpm(bits per minute)
- most individual's quality of sleep score is between 6 and 9 
- most individuals are between 45 and 47.5 years old
- Quality of sleep is a bimodal distribution as it has two peaks. Most frequent quality of sleep rating has a bin range 8-8.5 and 6-6.5 

![Figuresubplot](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/cdc2a4af-479f-46f4-aec0-f75c032da4f5)

![systolicAnddiastolicBP_hist](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/5f628f51-1326-42dc-9911-f8aeaeea268f)


# 6. Correlation analysis

```
categories = ['Gender', 'Occupation', 'BMI Category']
temp_df = df.copy()
LE = LabelEncoder()
for label in categories:
    temp_df[label] = LE.fit_transform(temp_df[label])
sb.heatmap(data=temp_df.drop('Person ID', axis=1).corr(numeric_only=True), cmap="YlGnBu", annot=True)
```
Categorical variables such as Gender, Occupation and BMI Category are encoded into numerical labels in order to include them in the correlation analysis.
![betterheatmap](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/56c06e40-2542-47a2-9866-be421a680849)

Generally positive correlations between :
- blood pressure and age
- quality of sleep and sleep duration
- daily steps and physical activity level
- stress level and heart rate

Generaly negative correlations between : 
- stress level an sleep duration
- stress level and quality of sleep
- heart rate and quality of sleep


## Exploring the relationship between variables and the impact of sleep disorder
```
sb.pairplot(data=df.drop('Person ID', axis=1), hue='Sleep Disorder')
```

![pair plot ](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/d8dcb03d-036a-40e2-83d3-2ec837ddbd2f)
![pair plot for SbpDbppng](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/7bc372c8-2fbd-4a4c-9218-9449cb37df7f)


# 7. Classification

```
k_folds = 5
kf = KFold(n_splits=k_folds, shuffle=True, random_state=42)
conf_matrices, scores = [], []
models = {'LR': LogisticRegression(max_iter=100, multi_class='ovr'), 'SVC': SVC(decision_function_shape='ovr')}

for name, model in models.items():
    scores = []
    i = 0
    fig, axes = plt.subplots(1, 5, figsize=(15, 7))

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
                         ax=axes[i - 1])  
        ax.set_aspect('equal')
        ax.set_yticklabels(ax.get_xticklabels(), rotation=0)
        ax.set_title("CM of " + name+" in fold "+str(i))
        ax.set_xlabel('Predicted Label')
        ax.set_ylabel('True Label')
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
    mean_score = np.mean(scores)
    print(name, " Mean Accuracy Score:", mean_score)
plt.tight_layout()
plt.show()
```

We use 5-fold cross-validation to evaluate our models and we also compute a confusion matrix in each fold.

## 7.1 Support Vector Classification 
Mean Accuracy Score for svc model is 71.1%

### Confusion matrix
![svc-5fold-CM](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/63dad22e-3098-476f-867b-85d9d87938be)
```
Overall Classification Report:
               precision    recall  f1-score   support

         0.0       0.70      0.94      0.80       219
         1.0       0.78      0.78      0.78        78
         2.0       0.00      0.00      0.00        77

    accuracy                           0.71       374
   macro avg       0.49      0.57      0.53       374
weighted avg       0.57      0.71      0.63       374
```

## 7.2 Logistic Regression
Mean Accuracy Score for lr model is 87.2% 

### Confusion matrix
![lr-5fold-CM](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/abcb56ee-3815-4b24-91d2-8b16dcb6571a)

```
Overall Classification Report:
               precision    recall  f1-score   support

         0.0       0.93      0.91      0.92       219
         1.0       0.81      0.79      0.80        78
         2.0       0.79      0.83      0.81        77

    accuracy                           0.87       374
   macro avg       0.84      0.85      0.84       374
weighted avg       0.87      0.87      0.87       374
```

