import platform
import pandas as pd
import numpy as np
print('python version:' + platform.python_version())
print('pandas version:' + pd.__version__)
# print(type(np.nan))



l=[69,51,87,97,30,16,51]
p=pd.Series(l)
pds=pd.DataFrame(l)
pdcolumn=pd.DataFrame(l)
# print(pds)
# print(p)

data = [['Robin',26,45.34,'cse'],['Karan',25,78.5,'ece'],['Priya',23,87.67,'cse',],['Varun',22,56,'e'],['Keisha',23,97,'c']]
# print(data)
df=pd.DataFrame(data,columns=['Name','age','marks','branch'])
# print(df)



dataframe= [['Robin',26,45.34,'cse',25],['Karan',25,78.5,'ece',17],['Priya',23,87.67,'ece',17],['Varun',22,56,'c',15],['Keisha',23,'e',97,14]]
# print(data)
dfs=pd.DataFrame(dataframe,columns=['Name','age','marks','branch','salary'])
# print(dfs)
dfs['salary'] = pd.to_numeric(dfs['salary'],)
# unique_salaries = dfs['salary'].sort_values(ascending=False).unique()     # descending order  will be get
unique_salaries = dfs['salary'].sort_values(ascending=False).unique()[2] # if we use [2]  then no if condition
print('Third highest salary',unique_salaries)
# if len(unique_salaries) >= 3:
#     third_highest_salary = unique_salaries[2]
#     print("Third highest salary:", third_highest_salary)



dataframe= [['Robin',26,45.34,'cse',234566],['Karan',25,78.5,'ece',67878],['Priya',23,87.67,'ece',57657],['Varun',22,56,'c',78645],['Keisha',23,'e',97,5664]]
# print(data)
dfs=pd.DataFrame(dataframe,columns=['Name','age','marks','branch','salary'])
# print(dfs)
dfs['salary'] = pd.to_numeric(dfs['salary'], )
third_highest_salary = dfs['salary'].nlargest(3).iloc[-1]
third_highest_salary_index = dfs['salary'].nlargest(3).index[-1]
# print("Third highest salary:", third_highest_salary)








i=pd.Series(l,index=('a','b','c','d','f','f','g'))
datatype=pd.Series(l,index=('a','b','c','d','e','f','g'),dtype=float)
# print(datatype)
# print(p)
# print(i)



le=[1,1,2,3,4,5,5]
li = [num for num in set(le) if le.count(num) > 1]
# print(li)



t=(69,51,87,97,30,16,16)
# print(t)

# indexlist=['1',3,5,6,'7']
# for index,value in enumerate(indexlist):
#     print(index,value)


# indexforvalue=[4,5,6,7,7,8,9]
# valuetofind=int(input("plese enter the value: "))
# findvalue=False
# for index,value in enumerate(indexforvalue):
#     if value == valuetofind:
#         found = True
#         print(f"Index of {valuetofind}: {index}")
#
# if not  findvalue:
#         print(f"The value {valuetofind} not in list" )

# e = [x for x in range(20)]
# spam = (x for x in e if x % 3 == 0)
# # print(e)
# print(next(spam))
# print(next(spam))
# print(next(spam))
# print(next(spam))
# import keyword
# list = keyword.kwlist
# print(list)
# for e in __builtins__.__dict__:
#   print(e)

# def defaultfunction():
#     x=1
#     y=4
#     print( x+y)
# defaultfunction()

# x = memoryview(b"Hello")
# print(x)
# print(x[0])
# print(x[1])
# print(x[2])

import pandas as pd
file_path = 'C:\\Users\\newmek\\Downloads\\business-financial-data-march-2024-csv.csv'
dataframeread = pd.read_csv(file_path)
# dataframeread['Data_value'] = dataframeread['Data_value'].fillna(0)
# filtered_df = dataframeread[dataframeread['Series_title_4'] == 'Trend']
# dataframeread.to_csv(file_path, index=False)

# zero_indices = dataframeread[dataframeread['Data_value'] == 0].index
# zero_indices_list = zero_indices.tolist()
# zero_indices_df = pd.DataFrame(zero_indices_list, columns=['Index'])
array_values = dataframeread.values
indices_with_zeros = [i for i, row in enumerate(array_values) if 0 in row]
print("Indices with 0 values:", indices_with_zeros)
# print(zero_indices)
# print(zero_indices_list)
# print(zero_indices_df)
# print(dataframeread)
# print(filtered_df)
# print(dataframeread.describe())
print(dataframeread.shape)
# print(dataframeread.head(10))




data = [
    ['Robin', 0, 0, 'cse', 25],
    ['Karan', 25, 78.5, 0, 17],
    ['Priya', 23, 67.0, 'ece', 17],
    ['Varun', 22, 0, 'c', 15],
    ['Keisha', 23, 'e', 97, 14]
]

df = pd.DataFrame(data, columns=['Name', 'age', 'marks', 'branch', 'salary'])
print(df)
zero_indices = df.isin([0]).any(axis=1)
indices_with_zeros = df.loc[zero_indices].index.tolist()
# indices_with_zeros = df.index[df.eq(0).any()].tolist()
# indices_with_zeros = df.index[df.eq(0).any(axis=1)].tolist()# array_values = df.values
# print(array_values,'arrayvalues')
# indices_with_zeros = [i for i, row in enumerate(array_values) if 0 in row]
print("Indices with 0 values:", indices_with_zeros)
print("zero_indices with 0 values:", zero_indices)

