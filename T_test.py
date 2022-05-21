# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pingouin as pg

# Summation of 15, equal to the total number of comparison made it in this script
s = 0
for i in range (15):
    s = s + i

# T test function, give the parameters and return its comparison 
def T_test(sts_data, colnames):
    mat = sts_data.shape[1]
    T_results = np.zeros((s, 5))
    T_results = pd.DataFrame(T_results)
    k = 0
    c = 0
    for i in range (mat-1):
        k += 1
        for j in range (mat-k):
            set_A = sts_data.iloc[0:3,i]
            set_B = sts_data.iloc[0:3,j+k]
            # Calculate T value
            T_value = pg.ttest(x=set_A, y=set_B, alternative='two-sided', correction=False)

            # Find T critical value
            # q  is the significance level to use
            # df are the degrees of freedom
            
            # Left-tailed test 
            # q = 0.05
            # Right-tailed test
            # q = 1-.05
            # Two-tailed test
            # q = 1-.05/2
        
            T_critical = stats.t.ppf(q = 1-.05/2, df = T_value.iloc[0,1])
            
            T_results.iloc[c,0] = T_value.iloc[0,1]
            T_results.iloc[c,1] = T_value.iloc[0,0]
            T_results.iloc[c,2] = T_critical
        
        
            if abs(T_value.iloc[0,0]) > T_critical:
                T_results.iloc[c,3] = "Statistically Different"
            else: 
                T_results.iloc[c,3] = "NOT Statistically Different"
                
            T_results.iloc[c,4] = colnames.iloc[i,0]+" vs "+colnames.iloc[j+k,0]
            c += 1

    return T_results