import pandas as pd
import numpy as np

data = pd.read_csv("https://raw.githubusercontent.com/dangomezm/Special-Project-UN/main/Datos%20Def.csv")

sts_data = np.zeros((3,15))
colnames = np.zeros(15)
sts_data = pd.DataFrame(sts_data)
colnames = pd.DataFrame(colnames)
k = 0
c = 0
for i in range(15):
    colnames.iloc[i] = data.iloc[c, 0]
    c += 3
    for j in range(3):
        sts_data.iloc[j,i] = data.iloc[k,-1]
        k += 1

sts_data.columns = colnames

from T_test import*
T_results = T_test(sts_data, colnames)
T_results.columns = ["DOF", "T value", "T critical", "Comparisson"," Materials"]

T_results.to_excel("T_results.xlsx")