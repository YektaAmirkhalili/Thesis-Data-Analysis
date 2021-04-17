import pandas as pd 
import numpy as np 

data = pd.read_csv("new_transactionsDB.csv")

#part 1 - cleaning data - some of the products have " marks 
#delete extra quotation marks 

dataNP = data.values #np_array

for x in np.nditer(dataNP, flags=["refs_ok"], op_flags = ['readwrite']):
  # x[...] = np.where('"' in str(x),'',x)
  x[...] = str.replace(str(x), '"', '')

# print(dataNP[:10]) ok, works fine. 
np.savetxt("noExtra.txt", dataNP, delimiter=' ', fmt='%s')