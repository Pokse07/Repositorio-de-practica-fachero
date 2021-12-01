#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = {'id': [1, 2, 3, 4, 5, 6, 7, 7],
        'first_name': ['Sigrid', 'Kennedy', 'Theodoric', 'Sigrid', 'Kennedy', 'Beatrix', 'Olimpia', 'Olimpia'],
        'last_name': ['Mannock', 'Donnell', 'Rivers', 'Mannock', 'Donnell', 'Parlett', 'Guenther', 'Guenther'],
        'age': [27, 31, 36, 27, 53, 48, 36, 36],
        'amount': [7.17, 1.90, 1.11, 7.17, 1.41, 6.69, 4.62, 4.62]}


# In[3]:


df = pd.DataFrame(data, columns = ['id', 'first_name', 'last_name', 'age', 'amount'])
df


# In[8]:


df = df.drop_duplicates(df.columns[~df.columns.isin(['id'])],
                        keep='first')
df


# In[ ]:




