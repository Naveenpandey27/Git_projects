import pandas as pd
import numpy as np

# Reading csv file
df = pd.read_csv("file.csv")
# printing top 5 rows
df.head()
print(df)


# 2nd way 

df = df.isnull().sum()
df = df.value_counts()