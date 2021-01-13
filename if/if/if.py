a=True
b=True
result = 0

def sing(nums:[int]) :
    for num in nums :
        result = num ^ result
    return result
sing([1,1,2,3,3])

if (a^b) == False :
    print("two ele have same bool")
else :
    print("two ele have diff bool")


import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

def answer_one():
    column = df["Gold"]
    max_index = column.idxmax()
    
    
    return max_index
answer_one()

def answer_two():
    col = df["Gold"]
    colw = df["Gold.1"]
    diff_col = df["Gold"] - df["Gold.1"]
    max_index = diff_col.idxmax()
    
    return max_index
answer_two()

def answer_three():
    df[(df['Gold.1'] > 0) & (df['Gold'] > 0)]
    col = df["Gold"]
    colw = df["Gold.1"]
    tot_col = df["Combined total"]
    diff_col = (abs(col-colw))/tot_col
    max_index = diff_col.idxmax()
    
    return max_index
answer_three()

def answer_four():
    df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']
    Points = pd.Series(df['Points'],index=df.index)
    return Points
answer_four()

census_df = pd.read_csv('census.csv')
census_df.head()

def answer_five():
    
    return census_df.groupby('STNAME')['COUNTY'].nunique().idxmax()
answer_five()

def answer_six():
    return census_df[census_df['SUMLEV'] == 50].groupby('STNAME')['CENSUS2010POP'].apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()
answer_six()

def answer_seven():
    temp = census_df[census_df['SUMLEV'] == 50].set_index('CTYNAME')
    yrs = ['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
    res = temp.loc[:,yrs].max(axis=1) - temp.loc[:,yrs].min(axis=1)

    return res.idxmax()
answer_seven()

