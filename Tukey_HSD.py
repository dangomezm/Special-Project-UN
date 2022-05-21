# Import packages
import pandas as pd
import numpy as np
from scipy.stats import tukey_hsd

# Tukey's HSD function, the main goal of this script is return the statistic value
# Tukey criterion was determined in Excel and it will be compare with this value.
def Tukey_HSD(sts_data):
    data = sts_data
    Tukey_result = tukey_hsd(data.iloc[:,0],
                             data.iloc[:,1],
                             data.iloc[:,2],
                             data.iloc[:,3],
                             data.iloc[:,4],
                             data.iloc[:,5],
                             data.iloc[:,6],
                             data.iloc[:,7],
                             data.iloc[:,8],
                             data.iloc[:,9],
                             data.iloc[:,10],
                             data.iloc[:,11],
                             data.iloc[:,12],
                             data.iloc[:,13],
                             data.iloc[:,14])
    return Tukey_result


