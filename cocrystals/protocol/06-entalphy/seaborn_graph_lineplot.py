import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#sns.set_theme(style="ticks")
sns.set_theme(style="darkgrid")
#sns.set_theme(style="white")

summary = pd.read_csv('11OUTPUT_gurthang.txt', sep=';', keep_default_na=True)
summary.info()

sorted_summary = summary.sort_values(by=['SCF steps'], ascending=True)

sns.lineplot(data=sorted_summary,x="SCF steps", y="SCF Interations", color='gray', linewidth=2.5)

plt.tight_layout()
plt.savefig('OUTPUT_11_Interations.png',dpi=300)
