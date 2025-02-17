#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Aut@r: Susana Edith Barrientos Galicia
# Introduction Numpy

# import the numpy package as np
import numpy as np

# ccreate 2 new list height and weight

personHeight = [5.2, 5.4, 4.4, 4.5, 5.6, 6]
personWeight = [81, 55, 70, 45, 44]

# create 2 numpy arrays from heigth and weight
personHeight = np.array(personHeight)
personWeight = np.array(personWeight)


# In[2]:


# print 'personHeight' array 

print(personHeight)
print(personWeight)
print(type(personWeight))


# In[3]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Introduction Numpy

import numpy as np
array=np.array([4,9,16,25])
type(array)


# In[4]:


# Aut@r: Susana Edith Barrientos Galicia
# Indexing an Array

# Indexing in 1 dimension

# given array
myArray = np.array([11,22,33,24,57,473])
print(myArray)


# In[5]:


# Aut@r: Susana Edith Barrientos Galicia

# get the 1st element
# indexing starts from '0'
print(myArray[0])
print(myArray[2])


# In[6]:


# Aut@r: Susana Edith Barrientos Galicia
# Indexing an Array

# Indexing in 2 dimension

array = np.array([
                    [101, 231, 321],
                    [412, 512, 622],
                    [712, 821, 912]
                ])
array


# In[7]:


# get the element in 3rd row and 2nd column
print(array[2][1])


# In[16]:


# we can pass ith row and jth column in seeparate brackets ([])
print(array[2][1])


# In[8]:


# pick the second rpw from the array
print(array[2])


# In[9]:


# pick the secon column from the array
print(array[:,2])


# In[10]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Indexing an Array

sample_array = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

sample_array[[0, 4, 7]]


# In[11]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Indexing an Array

a = np.array([[1, 0, 1, 0, 2, 3], [1, 3, 0, 1, 2, 0], [0, 1, 0, 0, 1, 3]])

a[1, 2]
a[2, 1]


# In[12]:


# Aut@r: Susana Edith Barrientos Galicia
# Slicing an Array

myArray = [101, 121, 112, 123, 114]
newArray = myArray[1:4]
newArray


# In[13]:


# first three elements
c= myArray[:3]
c


# In[14]:


# all the elements from 112
d = myArray[2:]
d


# In[15]:


# Aut@r: Susana Edith Barrientos Galicia
# Slicing an Array
# 2D array

array2 = np.array([
                [101, 131, 122, 113, 143],
                [145, 165, 137, 318, 193],
                [240, 241, 252, 253, 324],
                [225, 126, 727, 928, 129]
            ])

print(array2[1:,2:4])


# In[16]:


sample_array = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
sample_array [0:4]


# In[17]:


import numpy as np
a = np.array([[1,0,1,0,2,3], [1,3,0,1,2,0], [0,1,0,0,1,3]])
b = a[:,1:3]
print(b)


# In[18]:


# Aut@r: Susana Edith Barrientos Galicia
# Operation on a Array

arrayOne = np.array([120, 230, 310, 410, 150])
arrayTwo = np.arange(5)


# In[19]:


# add the two arrays
arrayThree = arrayOne + arrayTwo
arrayThree


# In[20]:


# multiply each elements in the array y 4
arrayOne*4


# In[43]:


# get square of each elements
arrayOne**2


# In[21]:


# using numpy with comparison expressions
myArray = np.array([34, 45, 67, 45, 23])

# check with elements aree greeater than or equal to 40
# the comparison condition gives boolean output

newArray = myArray >= 40
newArray


# In[22]:


# elements greater than or equal to 40
myArray[newArray]


# In[23]:


myArray


# In[24]:


myArray[myArray >= 40]


# In[25]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Operation on a Array

import numpy as np
array1 = np.array([[0, 3, 2, 5], [1, 0, 2, -2]])
print(array1 >= 3)


# In[26]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Operation on a Array

import numpy as np
array2 = np.array([[1, 3, 5], [2, 4, 6]])
print((array2*2)**2)


# In[27]:


# Aut@r: Susana Edith Barrientos Galicia
# Arithmetic Functioning in Numpy

# given array
array4 = np.array([5,7,8,2,4])
array4


# In[28]:


# sum
# add all the elements of array
array4.sum()


# In[29]:


# find mininum of array
array4.min()


# In[30]:


# get cue of elemens of array
np.power(array4,3)


# In[31]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Arithmetic Functioning in Numpy

import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
c = a + b
c*5


# In[32]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Arithmetic Functioning in Numpy

import numpy as np
a = np.arange(10)
b = np.power(a,2)
b.min()


# In[33]:


# Aut@r: Susana Edith Barrientos Galicia
# Concatenation of an Array

# conccatenate two 1D array

arrayX = np.array([11, 22, 13])
arrayY = np.array([23, 22, 12])
np.concatenate([arrayX, arrayY])

# You can also concatenate more than two arrays at once.

arrayZ = np.array([23,45])
print(np.concatenate([arrayX, arrayY, arrayZ]))


# In[34]:


# Aut@r: Susana Edith Barrientos Galicia
# Concatenation of an Array

# conccatenate two 2D array

array5 = np.array([
                    [1,2,3], 
                    [4,5,6]
                  ])
array5


# In[35]:


# by default conccateenate() is along 'axis = 0'
np.concatenate([array5, array5])


# In[36]:


# concatenatee along the second axis
np.concatenate([array5, array5], axis=1)


# In[37]:


# Aut@r: Susana Edith Barrientos Galicia
# Test Concatenation of an Array

import numpy as np

x = np.array([[3], [5], [7]])
y = np.array([[5], [7], [9]])

np.concatenate([x, y], axis=1)


# In[39]:


# Aut@r: Susana Edith Barrientos Galicia
# Splitting of an Array

import numpy as np
a = np.arange(24).reshape(4,6)
np.vsplit(a,1)


# In[ ]:




