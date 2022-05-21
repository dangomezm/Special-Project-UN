# Import packages
import pandas as pd
import numpy as np

# Import database from GitHub
data = pd.read_csv("https://raw.githubusercontent.com/dangomezm/Special-Project-UN/main/Datos%20Def.csv")

sts_data = np.zeros((3,15))   # Chosen materials
colnames = np.zeros(15)       # ID materials
sts_data = pd.DataFrame(sts_data)
colnames = pd.DataFrame(colnames)
k = 0
c = 0

# Loop that assign the value of each materials to its corresponding column
for i in range(len(colnames)):
    colnames.iloc[i] = data.iloc[c, 0]
    c += 3
    for j in range(sts_data.shape[0]):
        sts_data.iloc[j,i] = data.iloc[k,-1]
        k += 1

# Assign ID material
sts_data.columns = colnames

# Import T_test function, to know about what is done in this function
# go the the script T_test.py
from T_test import*
T_results = T_test(sts_data, colnames)
T_results.columns = ["DOF", "T value", "T critical", "Comparison"," Materials"]

T_results.to_excel("T_results.xlsx") # Import the T result to an excel file

# Import Tukey's HSD function, to know about what is done in this function
# go the the script Tukey_HSD.py
from Tukey_HSD import*
Tukey_results = Tukey_HSD(sts_data)
print(Tukey_results )
