#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

pd.set_option("mode.copy_on_write", True)


# In[4]:


merged = pd.read_csv("merged.csv")

merged.head()


# In[9]:


merged.shape


# In[5]:


import pandas as pd

selected_columns = ["COUNTY", "STATE", "Year", "Death Rate", "MME Rate"]
final_dataset = merged[selected_columns]


# In[6]:


final_dataset.head()


# In[10]:


final_dataset.shape


# In[8]:


final_dataset.to_csv("final_dataset.csv", index=False)

