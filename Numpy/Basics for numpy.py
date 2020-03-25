#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python - basic numpy

# In[1]:


import numpy as np


# ## Calculation

# In[2]:


#np array, unlike list, can caculate every element in the array for two arrays
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_height = np.array(height)
np_weight = np.array(weight)


# In[4]:


print(np_height)
print(np_weight)


# In[10]:


np_weight/np_height**2


# In[11]:


weight/height**2 #this is one disadvantage for list


# In[12]:


weight+height #extend list


# In[13]:


np_weight+np_height #perform calculation


# In[14]:


#np array only contain one type
np.array([1,"type",True])


# ## Subsetting

# In[15]:


bmi = np_weight/np_height**2
bmi[0]


# In[18]:


bmi>23


# In[22]:


height < 1 # one of the difference of list and array


# In[24]:


bmi[bmi>23]


# ## 2D numpy arrays

# ### Types

# In[25]:


type(np_height)


# In[27]:


np_2d = np.array([height,weight])
print(np_2d)


# In[28]:


type(np_2d)


# In[29]:


np_2d.shape #no brackets


# ### subsetting

# In[30]:


np_2d[0]


# In[31]:


np_2d[0,1]


# In[32]:


np_2d[0][1]


# In[34]:


np_2d[:,3:4]


# In[35]:


np_2d[:,3:]


# ## Basic statistics

# In[36]:


np.mean(np_2d[0])


# In[37]:


np.median(np_2d[0,:])


# In[38]:


np.corrcoef(np_2d[0],np_2d[1])


# In[39]:


np.std(np_2d[1])


# In[40]:


np.sum(np_2d[1])


# In[41]:


np.sort(np_2d[1])


# In[43]:


np.random.normal(0,4,50) #argument: mean, std, number


# In[45]:


height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height,weight))
print(np_city)

