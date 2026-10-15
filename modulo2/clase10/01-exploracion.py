import pandas as pd

dataframe = pd.read_csv("coffe_sales.csv")

print("HEAD")
print(dataframe.head())

""" 
         date                 datetime  ... money    coffee_name
0  2024-03-01  2024-03-01 10:15:50.520  ...  38.7          Latte
1  2024-03-01  2024-03-01 12:19:22.539  ...  38.7  Hot Chocolate
2  2024-03-01  2024-03-01 12:20:18.089  ...  38.7  Hot Chocolate
3  2024-03-01  2024-03-01 13:46:33.006  ...  28.9      Americano
4  2024-03-01  2024-03-01 13:48:14.626  ...  38.7          Latte
"""

print("SHAPE") 

print(dataframe.shape) # (3636, 6) 3636 filas 6 columnas

print("COLUMNAS")
print(dataframe.columns) # Index(['date', 'datetime', 'cash_type', 'card', 'money', 'coffee_name'], dtype='str'

print("INFO")
print(dataframe.info())

""" 
<class 'pandas.DataFrame'>
RangeIndex: 3636 entries, 0 to 3635
Data columns (total 6 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   date         3636 non-null   str    
 1   datetime     3636 non-null   str    
 2   cash_type    3636 non-null   str    
 3   card         3547 non-null   str    
 4   money        3636 non-null   float64
 5   coffee_name  3636 non-null   str  
 """
 

print("DESCRIBE")
print(dataframe.describe())

""" 
             money
count  3636.000000
mean     31.746859
std       4.919926
min      18.120000
25%      27.920000
50%      32.820000
75%      35.760000
max      40.000000
"""