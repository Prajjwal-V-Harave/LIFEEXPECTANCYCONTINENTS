#importing required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

#importing dataset

df = pd.read_csv("Life_Exp-EU.csv")

#plotting a scatter plot for the above table

x = df.YEAR
y = df.LIFE_EXP
plt.scatter(x,y)
plt.xlabel("Year",fontsize = 14)
plt.ylabel("Avg life expectancy in EUROPE(in years)", fontsize = 14)

plt.show()

#taking the input year from user

year = int(input("Enter year here: "))

#splitting the data into 2 for training and testing

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# predict values and store

l = []

x = df.YEAR
y = df.LIFE_EXP

mymodel = np.poly1d(np.polyfit(x, y, 2))

x_new = np.arange(year, year + 11)

for i in x_new:
    exp1 = mymodel(year)
    exp = mymodel(i)
    l.append(exp)


#Find mean of values of the decade following input year

def mean(mymodel):
    sumOfNumbers = 0
    for j in mymodel:
        sumOfNumbers = sumOfNumbers + j
    avg = sumOfNumbers / len(mymodel)
    return avg


#Plot and save graph, and print predicted values

print(f"The average life expectancy in EUROPE in the year {year} will be {exp1} years .")
print(f"The mean of the average life expectancies in EUROPE in the decade {year}-{year+10} is {mean(mymodel([year, year+10]))} years .")

x = np.array(x_new)
y = np.array(l)

if mymodel(year+10) <= mymodel(year):
    color = 'red'
else:
    color = 'green'
plt.scatter(x,y)
plt.scatter(x[0],y[0], c = 'g', marker = 's', label = f'Avg life exp in EUROPE in {year}')
plt.scatter(x[1:],y[1:], c =color, marker = 'd', label = f'Avg life exp in EUROPE in {year+10}')

plt.xlabel("Year",fontsize = 14)
plt.ylabel("Avg life expectancy in EUROPE(in years)", fontsize = 14)
plt.title(f"AVERAGE LIFE EXPECTANCIES IN EUROPE in {year}", fontsize = 19, color = 'Blue')
plt.legend()
plt.savefig("AFRICA LIFE EXP.png")
plt.show()

