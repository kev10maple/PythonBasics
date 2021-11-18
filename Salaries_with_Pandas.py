import numpy as np
import pandas as pd

sal = pd.read_csv('Salaries.csv')

#Question 1
print(sal.head())

#Question 2
print(sal.info())

#Question 3
def average(toavg):
    return sum(toavg) / len(toavg)

print(f"Average of first 10000 items: {average(sal['BasePay'][0:10000])}")

#Question 4
print(f"Highest amount of TotalPayBenefits: {max(sal['TotalPayBenefits'])}")

#Question 5
data_joseph = sal.loc[sal['EmployeeName'] == 'JOSEPH DRISCOLL']
print(f"Job Title of Joseph: {data_joseph['JobTitle']}")

#Question 6
print(f"How much Joseph makes: {data_joseph['TotalPayBenefits']}")

#Question 7
highest_pay = sal.loc[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]
print(f"Highest paid person: {highest_pay['EmployeeName']}")

#Question 8
lowest_pay = sal.loc[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]
print(f"Lowest paid person: {lowest_pay['EmployeeName']}")
#print(f"Lowest paid amount: {lowest_pay['TotalPayBenefits']}")
#The lowest paid person is getting paid a negative amount

#Question 9
print(sal.groupby('Year').mean())

#Question 10
print(f"Unique Job Titles: {len(sal['JobTitle'].value_counts())}")

#Question 11
print(sal['JobTitle'].value_counts()[0:7])

#Question 12
jobs_2013 = sal.loc[sal['Year'] == 2013]['JobTitle'].value_counts()
print(f"Number of Job Titles represented by 1 person in 2013: {jobs_2013.value_counts()[1]}")

#Question 13
print(f"Number of job titles with 'Chief': {len(sal.loc[sal['JobTitle'].str.contains('CHIEF')])}")

#Question 14
print(sal['JobTitle'].apply(lambda x : len(x)).corr(sal['TotalPay']))
#The correlation is very small so no

