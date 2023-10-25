#
# LaPFarSC/UFRJ
# @author https://github.com/gui3ww (GEMMendes)
# @date   25/out/2023
#
# Input file: mdpout_descriptors.txt
# Origin command: mdpocket --trajectory_file ../trajectory_superimposed.dcd --trajectory_format dcd -f ../step3_input.pdb --selected_pocket mdpout_all_atom_pdensities_CAVIDADE_5.pdb 
#
# *BEFORE RUN, CHANGE OUTPUT FILE*
# 1. Replace all "  " to " "
# 2. Replace " " to ";" 
#
#
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import re

sns.set_theme(style="darkgrid")
summary = pd.read_csv('mdpout_descriptors.txt', sep=';', keep_default_na=True)
summary.info()

pattern = re.compile("^([A-Z]{3})$")
list_cols = list(summary)
i = 1
for col in list_cols:
   if not col=='snapshot' and not pattern.match(col):
     sns.lineplot(data=summary,x="snapshot", y=col,  linewidth=0.6)
     plt.tight_layout()
     plt.savefig('GRAPH'+str(i)+'_mdpout_descriptors_'+col+'.png',dpi=300)
     plt.clf()
     i +=1
     
print("END.")
