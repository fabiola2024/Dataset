import pandas as pd

df3= pd.read_json(r'C:\Users\NB USER\OneDrive\Desktop\hola\objeto.json')

print(df3.head())

print(df3.index)

print(type(df3))

print(df3.info())

print(df3.tail(5))

print(df3.sample(5))