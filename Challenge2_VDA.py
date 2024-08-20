# How are you going to delete indices no 0,1,3 leaving only
# all items in index 2?

import pandas as pd

s1 = pd.Series([0,4,8])
s2 = pd.Series([1,5,9])
s3 = pd.Series([2,6,10])
s4 = pd.Series([5,10,15])

dframe = pd.DataFrame( data = [s1,s2,s3,s4], index = [0,1,2,3], columns = [0,1,2])
print('Original Data Frame\n')
print(dframe)
dframe = dframe.drop([0,1,3])
print('\nData Frame after removing indices 0,1,3\n')
print(dframe)