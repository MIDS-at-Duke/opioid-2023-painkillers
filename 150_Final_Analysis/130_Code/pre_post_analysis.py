#!/usr/bin/env python
# coding: utf-8

# In[243]:


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from plotnine import *


# In[244]:


import pandas as pd
import numpy as np

pd.set_option("mode.copy_on_write", True)


# In[245]:


# import the final dataset for plotting
merged = pd.read_csv("final_dataset.csv")

merged.head()


# ### Pre-Post Analysis

# #### Washington

# In[246]:


# Filter for Washington state
df_washington = merged[merged["STATE"] == "Washington"]


# In[247]:


# check
unique_states_washington = df_washington["STATE"].unique()
print(unique_states_washington)


# In[248]:


# Splitting into pre and post policy years
df_washington_pre = df_washington[df_washington["Year"] < 2012]
df_washington_post = df_washington[df_washington["Year"] >= 2012]


# In[249]:


# Check
unique_years_pre_washington = df_washington_pre["Year"].unique()
print(unique_years_pre_washington)


# In[250]:


# Check
unique_years_post_washington = df_washington_post["Year"].unique()
print(unique_years_post_washington)


# In[251]:


# Creating the Mortality rate plot
(
    ggplot()
    # Plot treatment, pre-policy year
    + geom_smooth(
        df_washington_pre, aes("Year", "Death Rate"), method="lm", color="blue"
    )
    # Plot treatment, post-policy year
    + geom_smooth(
        df_washington_post, aes("Year", "Death Rate"), method="lm", color="red"
    )
    # Policy treatment line
    + geom_vline(xintercept=2012, linetype="dotted")
    # labels
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Pre-post Analysis: Overdose Mortality Rate for Washington")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
)


# In[252]:


# Creating the MME Rate plot
(
    ggplot()
    # Plot pre-policy year (Washington) for MME Rate
    + geom_smooth(df_washington_pre, aes("Year", "MME Rate"), method="lm", color="blue")
    # Plot post-policy year (Washington) for MME Rate
    + geom_smooth(df_washington_post, aes("Year", "MME Rate"), method="lm", color="red")
    # Policy treatment line
    + geom_vline(xintercept=2012, linetype="dotted")
    # Labels
    + xlab("Year")
    + ylab("Opiods Per Capita (MME Rate)")
    + labs(title="Pre-post Analysis: Opiods Per Capita (MME Rate) for Washington")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
)


# #### Florida

# In[253]:


# Filter for Florida state
df_florida = merged[merged["STATE"] == "Florida"]


# In[254]:


# check
unique_states = df_florida["STATE"].unique()
print(unique_states)


# In[255]:


# Splitting into pre and post policy years
df_florida_pre = df_florida[df_florida["Year"] < 2010]
df_florida_post = df_florida[df_florida["Year"] >= 2010]


# In[256]:


# Check
unique_years_pre_florida = df_florida_pre["Year"].unique()
print(unique_years_pre_florida)


# In[257]:


unique_years_post_florida = df_florida_post["Year"].unique()
print(unique_years_post_florida)


# In[258]:


# Creating the Mortality Rate plot
(
    ggplot()
    # Plot pre-policy year (Florida)
    + geom_smooth(df_florida_pre, aes("Year", "Death Rate"), method="lm", color="blue")
    # Plot post-policy year (Florida)
    + geom_smooth(df_florida_post, aes("Year", "Death Rate"), method="lm", color="red")
    # Policy treatment line
    + geom_vline(xintercept=2010, linetype="dotted")
    # Labels
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Pre-post Analysis: Overdose Mortality Rate for Florida")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
)


# In[259]:


# Creating the MME rate plot
(
    ggplot()
    # Plot pre-policy year (Florida) for MME Rate
    + geom_smooth(df_florida_pre, aes("Year", "MME Rate"), method="lm", color="blue")
    # Plot post-policy year (Florida) for MME Rate
    + geom_smooth(df_florida_post, aes("Year", "MME Rate"), method="lm", color="red")
    # Policy treatment line
    + geom_vline(xintercept=2010, linetype="dotted")
    # Labels
    + xlab("Year")
    + ylab("Opiods Per Capita (MME Rate)")
    + labs(title="Pre-post Analysis: Opiods Per Capita (MME Rate) for Florida")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
)


# #### Texas

# In[260]:


# Filter for Texas state
df_texas = merged[merged["STATE"] == "Texas"]


# In[261]:


# check
unique_states_texas = df_texas["STATE"].unique()
print(unique_states_texas)


# In[262]:


# Splitting into pre and post policy years
df_texas_pre = df_texas[df_texas["Year"] < 2007]
df_texas_post = df_texas[df_texas["Year"] >= 2007]


# In[263]:


# Check
unique_years_pre_texas = df_texas_pre["Year"].unique()
print(unique_years_pre_texas)


# In[264]:


# Check
unique_years_post_texas = df_texas_post["Year"].unique()
print(unique_years_post_texas)


# In[265]:


# Creating the Mortality rate plot
(
    ggplot()
    # Plot pre-policy year (Texas)
    + geom_smooth(df_texas_pre, aes("Year", "Death Rate"), method="lm", color="blue")
    # Plot post-policy year (Texas)
    + geom_smooth(df_texas_post, aes("Year", "Death Rate"), method="lm", color="red")
    # Policy treatment line
    + geom_vline(xintercept=2007, linetype="dotted")
    # Labels
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Pre-post Analysis: Overdose Mortality Rate for Texas")
    + scale_x_continuous(
        breaks=[2004, 2005, 2006, 2007, 2008, 2009], limits=[2004, 2009]
    )
    + theme_bw()
)
