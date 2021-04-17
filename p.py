import pandas as pd
import numpy as np 

data = pd.read_csv('data.csv')
# print(data.head()) 

newD = data.values
# print(newD)

for x in np.nditer(newD, flags=["refs_ok"], op_flags = ['readwrite']):
  # x[...] = np.where('"' in str(x),'',x)
  x[...] = str.replace(str(x), '"', '')

print(newD)

# for colName, insideSeries in data.iteritems():
#   if '"' in colName:
#     colName2 = colName.replace('"','')
#   for index, value in insideSeries.iteritems():
#     if '"' in value:
#       value2 = value.replace('"', '')

# dataNew = pd.DataFrame(value2, colName2)

# print(dataNew.head())



















# for colName, colData in data.iteritems():
#   if '"' in colName:
#     colName = colName.replace('"', '')
#     continue
#   if '"' in colData.values:
#     colData.values = colData.values.replace('"','')

# print(data.head())


# for key, value in data.iteritems():
  # counter = 0
  # if '"' in value:
  #   counter += 1
  # print(key)
  
# # print(counter)    
# import re 

# someSTR = 'hello"'

# if ('"' in someSTR):
# someSTR.apply(lambda x: re.findall('"', str(x)))

# if ('"' in someSTR):
#   newSTR = someSTR.replace('"','')

# print(someSTR)  
# print(newSTR)

