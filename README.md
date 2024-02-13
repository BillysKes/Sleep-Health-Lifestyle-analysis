## Project overview
The aim of this data science project is to analyze the Sleep Health and Lifestyle Dataset, which encompasses 400 rows and 13 columns. This dataset provides comprehensive insights into various factors influencing sleep quality and daily habits among individuals. By implementing Exploratory Data Analysis, we intend to uncover patterns, correlations, and significant associations within the data.


## Dataset
The dataset used in this project can be accessed  through Kaggle. You can find more information here : https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset

## Statistical information


## Bar-Pie Charts

Among the four BMI categories, Majority of individuals have normal body mass index or they are overweight while individuals with normal BMI are slightly more numbered compared to overweight. Also, most individuals don't have any sleep disorder but those who have ie.sleep apnea, insomnia, if combined, they are almost as equal in number compared to those who don't have any sleep problems. Observing the distribution of individuals divided among different occupations we understands that nurse, doctors and engineers are the majority. Also, individuals with insomnia have the worst score on quality of sleep, with a score of 6.5 while individuals who don't have any sleep disorder score at 7.5, so it is noticable that sleep disorders affects sleep quality. We end up on the same conclusion when we examine the relation of sleep disorders and the amount of sleep individuals have on average. Stress levels are also higher for people having insomnia or sleep apnea. Also, examining the average quality of sleep of individuals with different body mass index, we obverve worse score for due to sleep apnea and insomnia compared to normal BMI.

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



## Scatter Plots
There is a high positive correlation of quality of sleep and sleep duration which means that individuals who sleep longer have higher scores on quality of sleep. Also, there is a negative correlation of heart rate and daily steps which means, individuals who doens't walk a lot tend to have higher heart rate. Also, there is a positive correlation of sbP and dBP which means, individuals with high systolic blood pressure also have high diastolic blood pressure and the reverse. We also notice that high stress levels are associated with low quality of sleep(negative correlation).

- Positive correlation of quality of sleep and sleep duration. As sleep duration increases we notice that individuals report higher ratings on quality of sleep as well whereas the exact opposite happens when sleep duration is shorter.
- Negative correlation of the heart rate(bpm) and the daily steps taken. Individuals who walk more tend to have more normal heart rate due to the benefits of cardiovascular exercise
- Positive correlation of systolic blood pressure(SBP) and diastolic blood pressure(DBP)
- Negative correlation of quality of sleep and stress level. Individuals reporting better quality of sleep tend to report lower stress levels.

![scatterplots](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/987df6e0-d07f-4de2-a94e-69ccee17d74c)


## Histograms

- Positive skewness most individuals heart rate is on the range of 65-73 bpm(bits per minute)
- most individual's quality of sleep score is between 6 and 9 
- most individuals are between 45 and 47.5 years old
- Quality of sleep is a bimodal distribution as it has two peaks. Most frequent quality of sleep rating has a bin range 8-8.5 and 6-6.5 

![Figuresubplot](https://github.com/BillysKes/Sleep-Health-Lifestyle-analysis/assets/73298709/cdc2a4af-479f-46f4-aec0-f75c032da4f5)



