import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

data = pd.read_csv('tips.csv')
print("_______DATA FROM CSV_________")
print(data)
data['paid'] = data.tip + data.total_bill
paid = data.paid
print("_______ADD CALCULATED PAID COLUMN_________")
print(data)
male = data[data.sex == 'Male']
female = data[data.sex == 'Female']
print("_______DISPLAY DATA SUBSET MALES_________")
print(male)
print("_______DISPLAY DATA SUBSET FEMALES_________")
print(female)

cor = data["total_bill"].corr(data["tip"])
print("_______DISPLAY CORRELATION BETWEEN BILL AMOUNT AND TIP AMOUNT_________")
print(cor)

mpl.bar("Male", np.mean(male.tip))
mpl.bar("Female", np.mean(female.tip))
mpl.ylabel("Tips")
mpl.xlabel("Sex")
mpl.title("Male vs Female Tippers")
mpl.show()