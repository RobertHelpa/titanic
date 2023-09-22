import pandas as pd

df = pd.read_csv('titanic.csv')

df.info()
print(df.head(10))