# In[403]:


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from plotnine import *


# In[404]:


import pandas as pd
import numpy as np

pd.set_option("mode.copy_on_write", True)


# In[405]:


# import the final dataset for plotting
merged = pd.read_csv("final_dataset.csv")

merged.head()

# ### Pre-Post Analysis

# #### Washington

# In[406]:


# Filter for Washington state
df_washington = merged[merged["STATE"] == "Washington"]


# In[407]:


# check
unique_states_washington = df_washington["STATE"].unique()
print(unique_states_washington)


# In[408]:


# Splitting into pre and post policy years
df_washington_pre = df_washington[df_washington["Year"] < 2012]
df_washington_post = df_washington[df_washington["Year"] >= 2012]


# In[409]:


# Check
unique_years_pre_washington = df_washington_pre["Year"].unique()
print(unique_years_pre_washington)


# In[410]:


# Check
unique_years_post_washington = df_washington_post["Year"].unique()
print(unique_years_post_washington)


# In[411]:


# Creating the Mortality rate plot
(
    ggplot()
    # Plot treatment, pre-policy year
    + geom_smooth(
        df_washington_pre,
        aes(x="Year", y="Death Rate", color="'Pre-policy'"),
        method="lm",
    )
    # Plot treatment, post-policy year
    + geom_smooth(
        df_washington_post,
        aes(x="Year", y="Death Rate", color="'Post-policy'"),
        method="lm",
    )
    # Policy treatment line
    + geom_vline(xintercept=2012, linetype="dotted")
    # Labels
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(
        title="Pre-post Analysis: Overdose Mortality Rate for Washington",
        color="Policy Period",
    )
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
)


# In[412]:


# Creating the MME Rate plot
(
    ggplot()
    # Plot pre-policy year (Washington) for MME Rate
    + geom_smooth(
        df_washington_pre,
        aes(x="Year", y="MME Rate", color="'Pre-policy'"),
        method="lm",
    )
    # Plot post-policy year (Washington) for MME Rate
    + geom_smooth(
        df_washington_post,
        aes(x="Year", y="MME Rate", color="'Post-policy'"),
        method="lm",
    )
    # Policy treatment line
    + geom_vline(xintercept=2012, linetype="dotted")
    # Labels and Title
    + xlab("Year")
    + ylab("Opiods Per Capita (MME Rate)")
    + labs(
        title="Pre-post Analysis: Opiods Per Capita (MME Rate) for Washington",
        color="Policy Period",
    )
    # X-axis scale
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
)


# #### Florida

# In[413]:


# Filter for Florida state
df_florida = merged[merged["STATE"] == "Florida"]


# In[414]:


# check
unique_states = df_florida["STATE"].unique()
print(unique_states)


# In[415]:


# Splitting into pre and post policy years
df_florida_pre = df_florida[df_florida["Year"] < 2010]
df_florida_post = df_florida[df_florida["Year"] >= 2010]


# In[416]:


# Check
unique_years_pre_florida = df_florida_pre["Year"].unique()
print(unique_years_pre_florida)


# In[417]:


# check
unique_years_post_florida = df_florida_post["Year"].unique()
print(unique_years_post_florida)


# In[418]:


# Creating the Mortality Rate plot
(
    ggplot()
    # Plot pre-policy year (Florida) for Death Rate
    + geom_smooth(
        df_florida_pre, aes(x="Year", y="Death Rate", color="'Pre-policy'"), method="lm"
    )
    # Plot post-policy year (Florida) for Death Rate
    + geom_smooth(
        df_florida_post,
        aes(x="Year", y="Death Rate", color="'Post-policy'"),
        method="lm",
    )
    # Policy treatment line
    + geom_vline(xintercept=2010, linetype="dotted")
    # Labels and Title
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(
        title="Pre-post Analysis: Overdose Mortality Rate for Florida",
        color="Policy Period",
    )
    # X-axis scale
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
)


# In[419]:


# Creating the MME rate plot
(
    ggplot()
    # Plot pre-policy year (Florida) for MME Rate
    + geom_smooth(
        df_florida_pre, aes(x="Year", y="MME Rate", color="'Pre-policy'"), method="lm"
    )
    # Plot post-policy year (Florida) for MME Rate
    + geom_smooth(
        df_florida_post, aes(x="Year", y="MME Rate", color="'Post-policy'"), method="lm"
    )
    # Policy treatment line
    + geom_vline(xintercept=2010, linetype="dotted")
    # Labels and Title
    + xlab("Year")
    + ylab("Opioids Per Capita (MME Rate)")
    + labs(
        title="Pre-post Analysis: Opioids Per Capita (MME Rate) for Florida",
        color="Policy Period",
    )
    # X-axis scale
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
)


# #### Texas

# In[420]:


# Filter for Texas state
df_texas = merged[merged["STATE"] == "Texas"]


# In[421]:


# check
unique_states_texas = df_texas["STATE"].unique()
print(unique_states_texas)


# In[422]:


# Splitting into pre and post policy years
df_texas_pre = df_texas[df_texas["Year"] < 2007]
df_texas_post = df_texas[df_texas["Year"] >= 2007]


# In[423]:


# Check
unique_years_pre_texas = df_texas_pre["Year"].unique()
print(unique_years_pre_texas)


# In[424]:


# Check
unique_years_post_texas = df_texas_post["Year"].unique()
print(unique_years_post_texas)


# In[425]:


# Creating the Mortality rate plot
(
    ggplot()
    # Plot pre-policy year (Texas) for Death Rate
    + geom_smooth(
        df_texas_pre, aes(x="Year", y="Death Rate", color="'Pre-policy'"), method="lm"
    )
    # Plot post-policy year (Texas) for Death Rate
    + geom_smooth(
        df_texas_post, aes(x="Year", y="Death Rate", color="'Post-policy'"), method="lm"
    )
    # Policy treatment line
    + geom_vline(xintercept=2007, linetype="dotted")
    # Labels and Title
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(
        title="Pre-post Analysis: Overdose Mortality Rate for Texas",
        color="Policy Period",
    )
    # X-axis scale
    + scale_x_continuous(
        breaks=[2004, 2005, 2006, 2007, 2008, 2009], limits=[2004, 2009]
    )
    + theme_bw()
)
