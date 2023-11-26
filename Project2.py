#Analyze demographic data using Pandas from a dataset of demographic data that was extracted from the 1994 Census database. Round all decimals to the nearest tenth.
#1 How many women and men are represented in this dataset? This should be a Pandas series with gender names as the index labels. (sex column)
#2 What is the average age of women?
#3What is the percentage of people who have a Bachelor's degree?
#4What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
#5What percentage of people without advanced education make more than 50K?
#6What is the minimum number of hours a person works per week?
#7What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
#8What country has the highest percentage of people that earn >50K and what is that percentage?
#9Identify the most popular occupation for those who earn >50K in India.

import pandas as pd 

df=pd.read_csv('project2_data.csv')

#1
gender_count=(df['sex'].value_counts())
print(gender_count)

#2 
print('mean women age')
women_age_mean =round(df[df['sex'] =='Female']['age'].mean(),1)
print(women_age_mean)

#3
print('Bachelors count %')
bachelor_count=(df['education'].value_counts())
print(round(bachelor_count.loc['Bachelors']/len(df['education'])*100,1))

#4
print('higher education >50K')
filtered=df[['education','income']]
higher_edu=filtered[filtered['education'].isin(['Bachelors','Masters','Doctorate'])]
income=higher_edu[higher_edu['income']=='>50K']
percentage=round(len(income)/len(higher_edu)*100,1)
print(percentage)

#5 
print('no higher education>50K')
no_higher_edu=filtered[~filtered['education'].isin(['Bachelors','Masters','Doctorate'])]
income_noedu=no_higher_edu[no_higher_edu['income']=='>50K']
percentage=round((len(income_noedu))/len(no_higher_edu)*100,1)
print(percentage)	

#6
print('min_hours')
min_hours=df['hours.per.week'].min()
print(min_hours)

#7
print('min hours >50K')
min_count=df['hours.per.week'].value_counts().get(1)
print(min_count) 

#8
country_income=df[['income','native.country']]
#creating a new column as binary mask 
country_income['income_binary']=df['income']=='>50K'
country_percentage = country_income.groupby('native.country')['income_binary'].mean() * 100
highest_percentage_country = country_percentage.idxmax()
print('Country with the highest percentage of people that earn >50K and what is that percentage')
print(highest_percentage_country, round(country_percentage.loc[highest_percentage_country],1),'%')

#9
print('Most popular occupation for those who earn >50K in India')
filtered=df[['occupation','income','native.country']]
india=filtered[filtered['native.country']=='India']
india_50=india.drop(columns=['native.country'])
india_50=india_50[india_50['income']=='>50K']
india_occupation=india_50.groupby('occupation')['income'].count()
print(india_occupation.idxmax())