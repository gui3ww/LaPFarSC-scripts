import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_theme(style="darkgrid")

summary = pd.read_csv('OUTPUT_id4.txt', sep=';', keep_default_na=True)
summary.info()

sorted_summary = summary.sort_values(by=['SCF steps'], ascending=True)

sns.lineplot(data=sorted_summary,x="SCF steps", y="Enthalpy (Ry)", color='red', linewidth=2.5)
plt.tight_layout()
plt.savefig('OUTPUT_Enthalpy.png',dpi=300)
plt.clf()

sns.lineplot(data=sorted_summary,x="SCF steps", y="Density (g/cm^3)", color='green', linewidth=2.5)
plt.tight_layout()
plt.savefig('OUTPUT_Density.png',dpi=300)
plt.clf()

sns.lineplot(data=sorted_summary,x="SCF steps", y="Volume (Ang^3)", color='blue', linewidth=2.5)
plt.tight_layout()
plt.savefig('OUTPUT_Volume.png',dpi=300)
plt.clf()

sns.lineplot(data=sorted_summary,x="SCF steps", y="SCF Interations", color='gray', linewidth=2.5)
plt.tight_layout()
plt.savefig('OUTPUT_Interations.png',dpi=300)
plt.clf()
