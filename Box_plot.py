# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a folder called "outputs", which contains the boxplots created in this function
folder = "Outputs"
if not os.path.exists(folder):
    os.makedirs(folder)
if not os.path.exists(folder):
    os.makedirs(folder)

plt.close("all") # Close old plots

# Import the database
data = pd.read_csv("G:/My Drive/UNIVERSIDAD DEL NORTE/10mo/Special project/PF/Datos Def.csv")
col_names = data.columns 

# Create the bloxplots
fig, axs = plt.subplots(1,1, figsize=(12,8),sharey= True,)
sns.boxplot(data = data, x= col_names[0], y= col_names[4], ax=axs)
axs.set_title('Boxplot IDT Failure Strain', size=20)
# fig.suptitle("IDT Failure Strain", size=22)
sns.set_style("darkgrid")
plt.xlabel("HMA Mixes ID", size=16)
plt.xticks(fontsize=12, rotation=90)
plt.yticks(fontsize=14)
plt.ylabel("IDT Failure Strain [Inch/Inch]", size=16)
axs.spines['bottom'].set_color('k')
axs.spines['left'].set_color('k')
axs.spines['top'].set_color('k')
axs.spines['right'].set_color('k')
plt.savefig(os.path.join(folder, 'Boxplot.png'), dpi=500, bbox_inches='tight')

# Mix type 
Type_B = data.loc[data['HMA_MixType'] == "Type B"]
Type_C = data.loc[data['HMA_MixType'] == "Type C"]
Type_D = data.loc[data['HMA_MixType'] == "Type D"]

# Mix type B
plt.close("all")
type_b = sns.boxplot(data = Type_B, x= col_names[0], y= col_names[4])
type_b.set_title('Boxplot IDT Failure Strain - Mix Type B')
type_b.set_xlabel("HMA Mixes ID")
type_b.set_ylabel("IDT Failure Strain [Inch/Inch]")
plt.savefig(os.path.join(folder, 'Boxplot Mix Type B.png'), dpi=500, bbox_inches='tight')

# Mix type C
plt.close("all")
type_c = sns.boxplot(data = Type_C, x= col_names[0], y= col_names[4])
type_c.set_title('Boxplot IDT Failure Strain - Mix Type C')
type_c.set_xlabel("HMA Mixes ID")
type_c.set_ylabel("IDT Failure Strain [Inch/Inch]")
plt.savefig(os.path.join(folder, 'Boxplot Mix Type C.png'), dpi=500, bbox_inches='tight')

# Mix type D
plt.close("all")
type_d = sns.boxplot(data = Type_D, x= col_names[0], y= col_names[4])
type_d.set_title('Boxplot IDT Failure Strain - Mix Type D')
type_d.set_xlabel("HMA Mixes ID")
type_d.set_ylabel("IDT Failure Strain [Inch/Inch]")
plt.savefig(os.path.join(folder, 'Boxplot Mix Type D.png'), dpi=500, bbox_inches='tight')

# General similar
plt.close("all")
mat = ["HMA TTI 00008b","HMA TTI 00005", "HMA TTI 00015","HMA TTI 00032", "HMA TTI 00024",
       "HMA TTI 00016", "HMA TTI 00040", "HMA TTI 00017"]
similar = data.loc[data['HMAMixes_ID'].isin(mat)]
data_s = sns.boxplot(data = similar, x= col_names[0], y= col_names[4])
data_s.set_title('Boxplot IDT Failure Strain - Data similar')
data_s.set_xlabel("HMA Mixes ID")
data_s.set_ylabel("IDT Failure Strain [Inch/Inch]")
data_s.set_xticklabels(data_s.get_xticklabels(),rotation = 90)
plt.savefig(os.path.join(folder, 'Boxplot Mix Data similar.png'), dpi=500, bbox_inches='tight')

# Normal datasets
plt.close("all")
# normal = ["HMA TTI 00001", "HMA TTI 00007", "HMA TTI 00005", "HMA TTI 00009", "HMA TTI 00032"]
normal = ["HMA TTI 00024","HMA TTI 00017"]
data_normal = data.loc[data['HMAMixes_ID'].isin(normal)]
data_n = sns.boxplot(data = data_normal, x= col_names[0], y= col_names[4])
data_n.set_title('Boxplot IDT Failure Strain - Abnormal data ')
data_n.set_xlabel("HMA Mixes ID")
data_n.set_ylabel("IDT Failure Strain [Inch/Inch]")
# data_n.set_xticklabels(data_n.get_xticklabels(),rotation = 90)
plt.savefig(os.path.join(folder, 'Boxplot Mix Normal data F.png'), dpi=500, bbox_inches='tight')