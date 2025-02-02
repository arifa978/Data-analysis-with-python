import pandas as pd
data = pd.read_csv ("tourist_record.csv")
pd.set_option('display.max_column',None)
print(data)
updated_data=data.dropna()
print(updated_data)
updated_data2=data['Main_Purpose'].fillna(1000,inplace=False)
pd.set_option('display.max_column',None)
print(updated_data2)
