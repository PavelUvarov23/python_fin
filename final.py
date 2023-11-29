# import libs

import numpy as np
import pandas as pd
import random

#init list
columnName = 'whoAmI'
lst = ['robot']*10
lst +=['human']*10
random.shuffle(lst)
# create dataframe
data = pd.DataFrame({columnName:lst})
print(data.head())

"""**Задача: перевести dataFrame в one hot**

"""

# with dummies:

 df_dummies = pd.get_dummies(data, columns=[columnName, ])
 data = data.join(df_dummies)
 print(data)

# without dummies
# Вариант 1

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)

# without dummies
# Вариант 2

for uniq in data.whoAmI.unique():
  data[uniq] = (data.whoAmI == uniq).astype(int)
print(data)



