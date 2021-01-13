import pandas as pd
my_obj = pd.Series([4, 7, -5, 3])
print(my_obj.values)
print(my_obj.index)
my_obj2 = pd.Series([8,9,10,11], index=['a','b','c','d']) #setting index

print(my_obj2)

print(my_obj2['a']) #finding value using index

print('a' in my_obj2) #checking some index in series or not

dic_data = {'name':'apple','birthday':'1996-1-1','luckynumber':7 } # setting a dictinary

my_obj3 = pd.Series(dic_data) # turning a dictinary into series

print(my_obj3)