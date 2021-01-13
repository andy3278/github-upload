import pandas as pd

data = {'name': ['Bob', 'Nancy','Amy','Elsa','Jack'],
        'year': [1996, 1997, 1997, 1996, 1997],
        'month': [8, 8, 7, 1, 12],
        'day':[11,23,8,3,11]}
myframe = pd.DataFrame(data)
print(myframe) #name、year、month、day are columns 0-4 are index

myframe3 = pd.DataFrame(data,columns=['name','year', 'month', 'day','luckynumber'])
print(myframe3)

luckynumber = ['3','2','1','7','8'] 
luckynumber = pd.Series(luckynumber) # turn luckynumber into series

myframe3['luckynumber'] = luckynumber # adding new column and fill with values

print(myframe3) 