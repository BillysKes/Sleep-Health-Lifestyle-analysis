# Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset Description](#dataset-description)
3. [Statistical Information](#statistical-information)
4. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
   1. [Bar-Pie Charts](#Bar-Pie-Charts)
   2. [Scatter Plots](#Scatter-Plots)
   3. [Histograms](#Histograms)
5. [Predictive modelling](predictive-modelling)
6. [Model evaluation](model-evaluation)
   




        


# 1. Project overview
The aim of this project is to analyze the Sleep Health and Lifestyle Dataset, which include 400 rows and 13 columns. This dataset provides comprehensive insights into various factors influencing sleep quality and daily habits among individuals. By implementing Exploratory Data Analysis, we intend to uncover patterns, correlations, and significant associations within the data.


# 2. Dataset Description
The dataset used in this project can be accessed  through Kaggle. You can find more information here : https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset

# 3. Statistical information


# 4. Exploratory Data Analysis (EDA)
## 4.1 Bar-Pie Charts
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



## 4.2 Scatter Plots
<a name="Scatter-Plots"></a>
There is a high positive correlation of quality of sleep and sleep duration which means that individuals who sleep longer have higher scores on quality of sleep. Also, there is a negative correlation of heart rate and daily steps which means, individuals who doens't walk a lot tend to have higher heart rate. Also, there is a positive correlation of sbP and dBP which means, individuals with high systolic blood pressure also have high diastolic blood pressure and the reverse. We also notice that high stress levels are associated with low quality of sleep(negative correlation).

- Positive correlation of quality of sleep and sleep duration. As sleep duration increases we notice that individuals report higher ratings on quality of sleep as well whereas the exact opposite happens when sleep duration is shorter.
- Negative correlation of the heart rate(bpm) and the daily steps taken. Individuals who walk more tend to have more normal heart rate due to the benefits of cardiovascular exercise
- Positive correlation of systolic blood pressure(SBP) and diastolic blood pressure(DBP)
- Negative correlation of quality of sleep and stress level. Individuals reporting better quality of sleep tend to report lower stress levels.

![scatterplots](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/987df6e0-d07f-4de2-a94e-69ccee17d74c)


## 4.3 Histograms
<a name="histograms"></a>

- Positive skewness most individuals heart rate is on the range of 65-73 bpm(bits per minute)
- most individual's quality of sleep score is between 6 and 9 
- most individuals are between 45 and 47.5 years old
- Quality of sleep is a bimodal distribution as it has two peaks. Most frequent quality of sleep rating has a bin range 8-8.5 and 6-6.5 

![Figuresubplot](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/cdc2a4af-479f-46f4-aec0-f75c032da4f5)

![systolicAnddiastolicBP_hist](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/5f628f51-1326-42dc-9911-f8aeaeea268f)


## Correlation analysis

![betterheatmap](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/56c06e40-2542-47a2-9866-be421a680849)

![pair plot ](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/d8dcb03d-036a-40e2-83d3-2ec837ddbd2f)
![pair plot for SbpDbppng](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/7bc372c8-2fbd-4a4c-9218-9449cb37df7f)


# 5. Predictive modelling


# 6. Model evaluation



