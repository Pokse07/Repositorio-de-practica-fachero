#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as jl


# In[7]:


Myarray = jl.array([4, 36, 99, 45, 37])


# In[8]:


max = Myarray[0]


# In[10]:


for i in range (0, len(Myarray)):
    if(Myarray[i]>max):
        
        max = Myarray[i]
print(max)


# In[ ]:




