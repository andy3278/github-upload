import pandas as pd
import numpy as np
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                    'foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three',
                    'two', 'two', 'one', 'three'],
                    'C' : np.random.randn(8),
                    'D' : np.random.randn(8)})
#print(df)
#print(df.groupby(['A','B']).sum())
#%%
candies = [4,2,1,1,2]
extraCandies = 1
new = []
maxcandies = max(candies)
new = []
print(maxcandies)
for i in range(len(candies)):
    if ((candies[i] + extraCandies) >= maxcandies):
        new.append("true")
    else :
        new.append("false")
print(new)
#%%
for i in range(100000,100999):
    if i % 9127 == 0 :
        print(i)
#%%
for i in range(0,999):
    if ((i % 2 ==1 ) and (i % 3 ==1 ) and (i % 4 ==1 )and (i % 5 ==1 )and (i % 6 ==1 )and (i % 7 ==1 )):
        print(i)
#%%
for i in range(0,100):
    if ((i % 3 ==2 ) and (i % 4 ==3 ) and (i % 5 ==4 )):
        print(i)

# %%
def fn (x):
    return x**3+x**-3
x0 = 3.7
fn(x0)
count =0
for i in range(0,1000):

    if fn(x0) >52 :
        fn(x0-0.0001)
        count+=1
        print("l")
    elif fn(x0) == 52 :
        print("correct")
    else :
        fn(x0+0.0001)
        count+=1
        print("s")
print(count)
# %% 
for i in range(0,1000):
    print(i*i+i+41)
    i+=1

# %%
