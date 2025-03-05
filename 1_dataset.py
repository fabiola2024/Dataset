import pandas as pd

data= pd.read_csv(r'C:\Users\NB USER\OneDrive\Desktop\hola\propiedades\ar_properties.csv.zip', compression='zip')

print(data.head())

print(data.info())

print(data.sample(10))

data.tail(10)


