import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#sns.set_theme(style="ticks")
#sns.set_theme(style="darkgrid")
sns.set_theme(style="white")

summary = pd.read_csv('sacubitril-coformers-OK.txt', sep='	', keep_default_na=True)

summary.info()

# Plot 
sns.relplot(data=summary, x="atoms (unit cell)", y="enthalpy (eV)/ atoms", hue="co-former", style="spg n°", 
	size="volume (Ang^3)", sizes=(50, 200),
	 alpha=0.8, height=6, aspect=.8, palette="muted")            
            
plt.savefig('sacubitril-enthalpy-OK.png',dpi=300)
