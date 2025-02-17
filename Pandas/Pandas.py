#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Aut@r: Susana Edith Barrientos Galicia
# Introduction Pandas

import pandas as pd


# In[18]:


# creating pandas Series

numbers = range(1,100,5)
pd.Series(numbers)


# In[19]:


# create a oject series
string = "Hi", "How", "are", "you", "?"
pd.Series(string)


# In[20]:


# creat a Series with an arbitrary list

s = pd.Series([345, 'London', 34.5, -34.45, 'Happy Birthay'])
s


# In[21]:


# to set index values for a series

marks = [60, 89, 74, 86]

subject = ["Maths", "Science", "English", "Social Science"]
pd.Series(marks, index = subject)


# In[22]:


# To create a series from a dictionary

data = {'Maths': 60, 'Science': 80, 'English': 76, 'Social Science': 86}
pd.Series(data)


# In[23]:


# A series with missing values

subject = ["Maths", "Science", "Art and Craft", "Social Science"]
marksSeries = pd.Series(data, index = subject)
(print(marksSeries))


# In[25]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Introduction Pandas

import pandas as pd
index = ['Apple', 'Banana', 'Orange']
quantity = [34, 20, 30, 40]
pd.Series(data=quantity, index=subject)


# In[14]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Series

import pandas as pd
dict = {'A':30, 'B':40, 'C':50}
index = ['A', 'B', 'D']
pd.Series(data=dict, index=index)


# In[26]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Series

import pandas as pd
s1 = pd.Series([1, 2, 5, 6.5])
s2 = pd.Series(['first', 35, 'college', 62.5])
s1


# In[27]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Series 
s2


# In[28]:


# Aut@r: Susana Edith Barrientos Galicia
# Manipulating Series

# to check for null values using isnull
marksSeries.isnull()


# In[29]:


# Aut@r: Susana Edith Barrientos Galicia
# Manipulating Series

# to check for null values using notnull
marksSeries.notnull()


# In[30]:


# Aut@r: Susana Edith Barrientos Galicia
# Manipulating Series

# to know the subjeccts in which sccore is more than 75
marksSeries[marksSeries >75]


# In[31]:


# Aut@r: Susana Edith Barrientos Galicia
# Manipulating Series

# to assign 68 marks to 'Art and Craft'

marksSeries["Art and Craft"] = 68
marksSeries


# In[32]:


# Aut@r: Susana Edith Barrientos Galicia
# Manipulating Series

# to check whether Maths marks are 73
marksSeries.Maths ==73


# In[22]:


# or you may use
marksSeries["Maths"]== 73


# In[33]:


# Aut@r: Susana Edith Barrientos Galicia
# Manipulating Series - Sorting a numeric series

# create a padas series
values = pd.Series([23, 45, 41, 23, 34, 55, 34, 20])
values


# In[34]:


# ascending order
values.sort_values(ascending = True)


# In[35]:


# descending order
values.sort_values(ascending = False)


# In[36]:


# Aut@r: Susana Edith Barrientos Galicia
# Manipulating Series - Sorting a categories series

# create a padas series
stringValues = pd.Series(["a", "j", "d", "f", "t", "a"])
stringValues


# In[37]:


# ascending order
stringValues.sort_values(ascending = True)


# In[38]:


# descending order
stringValues.sort_values(ascending = False)


# In[39]:


# Aut@r: Susana Edith Barrientos Galicia
# Manipulating Series - Rank Series

marksSeries.rank(ascending = True, pct=False)


# In[45]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Manipulating Series

import pandas as pd
data = [0.85, 0.8, 0.98, 0.74, 0.4, 0.55, 0.94, 0.42, 0.43, 0.92]
ser = pd.Series(data=data)


# In[46]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Manipulating Series

ser.sort_values(ascending=False)


# In[49]:


data = range(10)
new_ser = pd.Series(data=data)
new_ser[new_ser==5]


# In[50]:


# Aut@r: Susana Edith Barrientos Galicia
# Introduction to Dataframes and Creating DataFrame

import pandas as pd
a1 = ['Hogwarts', 'Durmstrang', 'Beauxbatons']
a2 = ['Hogwarts', 'Durmstrang', 'Beauxbatons']
a3 = ['Hogwarts', 'Durmstrang', 'Beauxbatons']
school = [a1, a2, a3]
inst = ['School_1', 'School_2', 'School_3']
Muggle_data = pd.DataFrame(data=school, columns=inst)
Muggle_data


# In[51]:


# Aut@r: Susana Edith Barrientos Galicia
# Introduction to Dataframes and Creating DataFrame

import pandas as pd

data = {'A':[1,2,3,4,5], 'B':[1,0,1,1,0]}
df = pd.DataFrame(data=data)
#df.C = df.A + df.B


# In[46]:


# Aut@r: Susana Edith Barrientos Galicia
# concatenate Pandas Series

import pandas as pd

seriesA = pd.Series([101, 102, 103, 104, 105, 106])
seriesB= pd.Series([107, 108, 109, 110, 111, 112])

# concatenate the pandas series
pd.concat([seriesA, seriesB])


# In[48]:


# Aut@r: Susana Edith Barrientos Galicia
# Add a Hierarchical Index on Pandas Series

pd.concat([seriesA, seriesB], keys = ['a', 'b'])


# In[53]:


# Aut@r: Susana Edith Barrientos Galicia
# Label the Index

pd.concat([seriesA, seriesB], keys = ['a', 'b'], names=['Series', 'Row ID'])


# In[86]:


# Aut@r: Susana Edith Barrientos Galicia
# Label the Index

df1 = pd.DataFrame({
    'Name': ['ebay', 'edwin', 'suba', 'praha', 'jon'],
    'Compony': ['Apple', 'Walmart', 'Intel', 'cummins', 'Ford'],
    'Salary' : [67000, 90000, 87000, 69000, 78000]},
    index=[101, 102, 103, 104, 105])

print("The first dataframe is : \n",df1, "\n\n")

df2 = pd.DataFrame({
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'Compony': ['Apple', 'Walmart', 'Intel', 'cummins', 'Ford'],
    'Salary' : [89000, 80000, 79000, 97000, 88000]},
    index=[101, 102, 103, 104, 105])

print("The second dataframe is: \n", df2)


# In[87]:


# Aut@r: Susana Edith Barrientos Galicia
# Concatenating Pandas Dataframes using .concat()

print(pd.concat([df1,df2]))


# In[64]:


# Aut@r: Susana Edith Barrientos Galicia
# Concatenating Pandas Dataframes Horizontally

pd.concat([df1, df2], axis=1)


# In[88]:


# Aut@r: Susana Edith Barrientos Galicia
# Concatenating data frames ignoring index values

pd.concat([df1, df2], ignore_index=True)


# In[69]:


# Aut@r: Susana Edith Barrientos Galicia
# Concatenating data frames ignoring index values

import numpy as np
import pandas as pd
ser1 = pd.Series(list('abcd'))
ser2 = pd.Series(np.arange(4))


# In[70]:


df = pd.concat([ser1, ser2], axis=1)


# In[71]:


df


# In[71]:


df = pd.concat([ser1, ser2], axis=0)
df


# In[72]:


# Aut@r: Susana Edith Barrientos Galicia
# Concatenating data frames ignoring index values

import pandas as pd
data1={'Physics': [77, 75, 100, 10, 59], 'Chemistry': [85, 70, 99, 30, 80]}
df1=pd.DataFrame(data=data1)
data2={'Student_ID': [0, 1, 2, 3, 4], 'Maths': [80, 90, 88, 25, 90]}
df2=pd.DataFrame(data=data2)
df3=pd.concat([df1, df2], join='inner', axis=0, ignore_index=True)


# In[75]:


df3


# In[73]:


# Aut@r: Susana Edith Barrientos Galicia
# data frames ignoring index values

import pandas as pd
data1={'Student_ID': [3, 4, 6, 8, 10], 'CGPA': [4.5, 3, 4.37, 3.5, 4]}
df1=pd.DataFrame(data=data1)
data2={'Student_ID': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
'Maths': [4,52, 5, 2.5, 3, 3.9, 2.8, 4.75, 3.68, 5, 4.8]}
df2=pd.DataFrame(data=data2)
df3=pd.merge(df2, df1, on='Student_ID', how='left')


# In[77]:


df3


# In[94]:


# Aut@r: Susana Edith Barrientos Galicia
# data frames index values

import pandas as pd
header = pd.MultiIndex.from_product([['Before Course','After Course'],['Marks']])
d=([[82,95],[78,89]])
 
my_df = pd.DataFrame(d,
 index=['Alisa','Bobby'],
 columns=header)

print(my_df.stack(level=0).unstack(level=0))


# In[93]:


# Aut@r: Susana Edith Barrientos Galicia
# data frames index values

import pandas as pd
df = pd.DataFrame({"Gender": ["Male", "Male", "Female", "Female", "Female", "Female", "Male", "Male", "Female"],
 "Movie_Genre": ["Action", "Comedy", "Drama", "Action", "Comedy", "Drama", "Action", "Drama", "Action"],
 "Rating": [1, 5, 3, 2, 3, 4, 4, 5, 4]})


# In[78]:


pd.pivot_table(data=df, index='Gender', values='Rating')


# In[92]:


pd.pivot_table(data=df, index='Gender', values='Rating', aggfunc='mean')


# In[83]:


pd.pivot_table(data=df, index='Gender', values='Rating')


# In[84]:


pd.pivot_table(data=df, index='Gender' , values='Rating', aggfunc='sum')


# In[ ]:


pd.pivot_table(data=df, index='Gender', 'Movie_Genre' , values='Rating', aggfunc='sum')


# In[86]:


pd.pivot_table(data=df, index=['Gender', 'Movie_Genre'] , values='Rating', aggfunc='sum')


# In[87]:


pd.pivot_table(data=df, index=['Gender', 'Movie_Genre'] , values='Rating')


# In[88]:


pd.pivot_table(data=df, index='Gender' , values='Rating', aggfunc='sum')


# In[89]:


# correcto

pd.pivot_table(data=df, index=['Gender', 'Movie_Genre'] , values='Rating', aggfunc='sum')


# In[90]:


# Aut@r: Susana Edith Barrientos Galicia
# data frames index values

import pandas as pd

df_employee = [('John', 3400, 'Sydeny'),
 ('Robert', 3000, 'Chicago'),
 ('Aadi', 1600, 'New York'),
 ('Robert', 3000, 'Chicago'),
 ('Robert', 3000, 'Chicago'),
 ('Robert', 3000, 'Texas'),
 ('Aadi', 4000, 'London'),
 ('Sachin', 3000, 'Chicago')]

df_employee = pd.DataFrame(df_employee, columns=['Name', 'Salary', 'City'])

df_employee[df_employee.duplicated('Name')].shape


# In[101]:


# Aut@r: Susana Edith Barrientos Galicia
# Map and Replace

dfOne = pd.DataFrame({
    'Country':['China', 'India', 'Usa', 'Indonesia', 'Brazil'],
    'Population' : [1403500365, 1324171354,322179605,261115456,2076652865]
})


# In[103]:


dfOne


# In[106]:


# create a directory
capital = {
    'Germany':'Berlin',
    'Brazil':'Brasilia',
    'Hungary':'Budapest',
    'China':'Beijing',
    'India':'New Delhi',
    'Norway': 'Oslo',
    'Francia':'Paris',
    'Indonesia':'Jakarta',
    'USA':'Washington',
}

dfOne['Capital']=dfOne['Country'].map(capital)
dfOne


# In[109]:


# Aut@r: Susana Edith Barrientos Galicia
# Map and Replace

df7 = pd.DataFrame({
    'col1':[23,10,20],
    'col2':[67,30,56]},
    index=[1,2,3])

print(df7)


# In[112]:


dict1 = {10:"A", 20:"B"}

df7['col1'].replace(dict1, inplace=True)
print(df7)


# In[130]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Map and Replace

import pandas as pd
data = {'Student1': {'name': 'Emma', 'age': '27', 'sex': 'Female'},
 'Student2': {'name': 'Mike', 'age': '22', 'sex': 'Male'}}
df_students = pd.DataFrame(data=data)
df_students


# In[131]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Map and Replace

df_students['Student2'].replace('Mike', 'John', inplace=True)
df_students


# In[132]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Map and Replace

df_students.replace(['Mike', 'John'], inplace=True)
df_students


# In[134]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Map and Replace

df_students.replace(['Mike', 'John'], inplace=True)
df_students


# In[137]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Map and Replace

df_students['Student2']=df_students['Student2'].map({'Mike':'John'})
df_students


# In[148]:


# Aut@r: Susana Edith Barrientos Galicia
# Groupoy in Pandas


#create d data frame
import pandas as pd
dataFrame=pd.DataFrame({
    'Product_ID':[101,102,103,104,105,106],
    'Food_Product':['Cakes','Biscuis','Fruit','Beverages','Cakes','Beverages'],
    'Brand':['Baskin Robins','Blue Riband','Peach','Horlicks','Mars Muffin','Miranda'],
    'Sales':[5000, 8000, 7600, 5500, 6500, 9000],
    'Profit':[55000, 67000, 89000, 78000, 55000,90000]})
print(dataFrame)


# In[149]:


dataFrame


# In[153]:


# Number of Unique Column Values Per Group
dataFrame.groupby("Food_Product")["Sales"].nunique().to_frame()


# In[154]:


# Sort Groupby Results
dataFrame.groupby("Food_Product")["Sales"].sum().to_frame().reset_index()


# In[155]:


# Sort Groupby Results
dataFrame.groupby("Food_Product")["Sales"].sum().to_frame().reset_index().sort_values(by='Sales')


# In[156]:


# Sort Groupby Results
dataFrame.groupby("Food_Product").agg({'Sales':['min', 'max', 'mean']})


# In[ ]:




