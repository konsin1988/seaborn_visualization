import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1, 2, 3, 4, 5],
    'shape': ['o', 's', 'D', '^', 'v']})

sns.scatterplot(data=data, x='x', y='y', marker=list(data['shape']))

plt.show()