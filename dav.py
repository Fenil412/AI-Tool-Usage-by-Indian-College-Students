import pandas as pd
import numpy as np
df = pd.read_csv('Students.csv')
columns_to_null = ['Daily_Usage_Hours', 'Trust_in_AI_Tools', 'Preferred_AI_Tool']
for col in columns_to_null:
    null_indices = np.random.choice(df.index, size=int(0.1 * len(df)), replace=False)
    df.loc[null_indices, col] = np.nan
df.to_csv('Updated_Students.csv', index=False)