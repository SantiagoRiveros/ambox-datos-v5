import pandas as pd

dataframe = pd.read_csv("titanic.csv")

# Cuantos pasajeros hay por genero?:

print(dataframe["Sex"].value_counts())

""" 
Sex
male      577
female    314
 """

# Pasajeros por clase:

print(dataframe["Pclass"].value_counts())

""" 
Pclass
3    491
1    216
2    184
 """

# Pasajeros que sobrevivieron:
print(dataframe["Survived"].value_counts())
""" 
Survived
0    549
1    342
"""

# Pasajeros por puerto de embarque:
print(dataframe["Embarked"].value_counts())

""" 
Embarked
S          644
C          168
Q           77
Unknown      2
"""

