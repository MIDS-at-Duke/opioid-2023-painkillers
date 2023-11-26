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


# ### Diff-in-Diff Analysis (First Version Selected Control)

# In[266]:


washington_control = ["Massachusetts", "Colorado", "Maryland"]
florida_control = ["Ohio", "Pennsylvania", "Tennessee"]
texas_control = ["Georgia", "Indiana", "Alabama"]


# #### Washington

# In[267]:


# Filter for treatment state (Washington) and control states
treatment_state_washington = merged[merged["STATE"] == "Washington"]
control_states_washington = merged[merged["STATE"].isin(washington_control)]

# Filter for treatment state (Washington) and control states
treatment_state = merged[merged["STATE"] == "Washington"]
control_states = merged[merged["STATE"].isin(washington_control)]


# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2012]
treatment_post = treatment_state[treatment_state["Year"] >= 2012]
control_pre = control_states[control_states["Year"] < 2012]
control_post = control_states[control_states["Year"] >= 2012]


# In[268]:


# Creating the plot
(
    ggplot()
    # Plot treatment group pre-policy
    + geom_smooth(treatment_pre, aes("Year", "Death Rate"), method="lm", color="blue")
    # Plot treatment group post-policy
    + geom_smooth(treatment_post, aes("Year", "Death Rate"), method="lm", color="blue")
    # Plot control group pre-policy
    + geom_smooth(control_pre, aes("Year", "Death Rate"), method="lm", color="red")
    # Plot control group post-policy
    + geom_smooth(control_post, aes("Year", "Death Rate"), method="lm", color="red")
    # Policy treatment line
    + geom_vline(xintercept=2012, linetype="dotted")
    # Labels
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Washington vs Control States")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
)


# In[269]:


# Filter for treatment state (Washington) and control states
treatment_state = merged[merged["STATE"] == "Washington"]
control_states = merged[merged["STATE"].isin(washington_control)]

# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2012]
treatment_post = treatment_state[treatment_state["Year"] >= 2012]
control_pre = control_states[control_states["Year"] < 2012]
control_post = control_states[control_states["Year"] >= 2012]

# Creating the plot
(
    ggplot()
    # Plot treatment group pre-policy for MME Rate
    + geom_smooth(treatment_pre, aes("Year", "MME Rate"), method="lm", color="blue")
    # Plot treatment group post-policy for MME Rate
    + geom_smooth(treatment_post, aes("Year", "MME Rate"), method="lm", color="blue")
    # Plot control group pre-policy for MME Rate
    + geom_smooth(control_pre, aes("Year", "MME Rate"), method="lm", color="red")
    # Plot control group post-policy for MME Rate
    + geom_smooth(control_post, aes("Year", "MME Rate"), method="lm", color="red")
    # Policy treatment line
    + geom_vline(xintercept=2012, linetype="dotted")
    # Labels
    + xlab("Year")
    + ylab("Opiods Per Capita (MME Rate)")
    + labs(title="Opiods Per Capita (MME Rate) in Washington vs Control States")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
)


# #### Florida

# In[270]:


# Filter for treatment state (Florida) and control states
treatment_state = merged[merged["STATE"] == "Florida"]
control_states = merged[merged["STATE"].isin(florida_control)]

# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2010]
treatment_post = treatment_state[treatment_state["Year"] >= 2010]
control_pre = control_states[control_states["Year"] < 2010]
control_post = control_states[control_states["Year"] >= 2010]

# Creating the plot for Death Rate
(
    ggplot()
    + geom_smooth(treatment_pre, aes("Year", "Death Rate"), method="lm", color="blue")
    + geom_smooth(treatment_post, aes("Year", "Death Rate"), method="lm", color="blue")
    + geom_smooth(control_pre, aes("Year", "Death Rate"), method="lm", color="red")
    + geom_smooth(control_post, aes("Year", "Death Rate"), method="lm", color="red")
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Florida vs Control States")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
)


# In[271]:


# Filter for treatment state (Florida) and control states
treatment_state = merged[merged["STATE"] == "Florida"]
control_states = merged[merged["STATE"].isin(florida_control)]

# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2010]
treatment_post = treatment_state[treatment_state["Year"] >= 2010]
control_pre = control_states[control_states["Year"] < 2010]
control_post = control_states[control_states["Year"] >= 2010]

# Creating the plot for MME Rate
(
    ggplot()
    + geom_smooth(treatment_pre, aes("Year", "MME Rate"), method="lm", color="blue")
    + geom_smooth(treatment_post, aes("Year", "MME Rate"), method="lm", color="blue")
    + geom_smooth(control_pre, aes("Year", "MME Rate"), method="lm", color="red")
    + geom_smooth(control_post, aes("Year", "MME Rate"), method="lm", color="red")
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Opiods Per Capita (MME Rate)")
    + labs(title="Opiods Per Capita (MME Rate) in Florida vs Control States")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
)


# #### Texas

# In[272]:


# Filter for treatment state (Texas) and control states
treatment_state = merged[merged["STATE"] == "Texas"]
control_states = merged[merged["STATE"].isin(texas_control)]

# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2007]
treatment_post = treatment_state[treatment_state["Year"] >= 2007]
control_pre = control_states[control_states["Year"] < 2007]
control_post = control_states[control_states["Year"] >= 2007]

# Creating the plot for Death Rate
(
    ggplot()
    + geom_smooth(treatment_pre, aes("Year", "Death Rate"), method="lm", color="blue")
    + geom_smooth(treatment_post, aes("Year", "Death Rate"), method="lm", color="blue")
    + geom_smooth(control_pre, aes("Year", "Death Rate"), method="lm", color="red")
    + geom_smooth(control_post, aes("Year", "Death Rate"), method="lm", color="red")
    + geom_vline(xintercept=2007, linetype="dotted")
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Texas vs Control States")
    + scale_x_continuous(
        breaks=[2004, 2005, 2006, 2007, 2008, 2009], limits=[2004, 2009]
    )
    + theme_bw()
)


# ### Diff-in-Diff Analysis (Second Version Selected Controls)

# In[273]:


washington_control = ["Utah", "Tennessee", "Maine"]
florida_control = ["Ohio", "Colorado", "Rhode Island", "South Carolina", "Georgia"]
texas_control = ["West Virginia", "New Hampshire", "Kentucky"]


# #### Washington

# In[274]:


# Filter for treatment state (Washington) and control states
treatment_state = merged[merged["STATE"] == "Washington"]
control_states = merged[merged["STATE"].isin(washington_control)]


# In[275]:


# check
control_states_unique = control_states["STATE"].unique()
print(control_states_unique)


# In[276]:


# check
print("Unique years in treatment_state:", treatment_state["Year"].unique())
print("Unique years in control_states:", control_states["Year"].unique())


# In[277]:


# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2012]
treatment_post = treatment_state[treatment_state["Year"] >= 2012]
control_pre = control_states[control_states["Year"] < 2012]
control_post = control_states[control_states["Year"] >= 2012]


# In[278]:


# Creating the Mortality Rate plot
(
    ggplot()
    # Plot treatment group pre-policy
    + geom_smooth(treatment_pre, aes("Year", "Death Rate"), method="lm", color="blue")
    # Plot treatment group post-policy
    + geom_smooth(treatment_post, aes("Year", "Death Rate"), method="lm", color="blue")
    # Plot control group pre-policy
    + geom_smooth(control_pre, aes("Year", "Death Rate"), method="lm", color="red")
    # Plot control group post-policy
    + geom_smooth(control_post, aes("Year", "Death Rate"), method="lm", color="red")
    # Policy treatment line
    + geom_vline(xintercept=2012, linetype="dotted")
    # Labels
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Washington vs Control States")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
)


# In[279]:


# Creating the MME rate plot
(
    ggplot()
    # Plot treatment group pre-policy for MME Rate
    + geom_smooth(treatment_pre, aes("Year", "MME Rate"), method="lm", color="blue")
    # Plot treatment group post-policy for MME Rate
    + geom_smooth(treatment_post, aes("Year", "MME Rate"), method="lm", color="blue")
    # Plot control group pre-policy for MME Rate
    + geom_smooth(control_pre, aes("Year", "MME Rate"), method="lm", color="red")
    # Plot control group post-policy for MME Rate
    + geom_smooth(control_post, aes("Year", "MME Rate"), method="lm", color="red")
    # Policy treatment line
    + geom_vline(xintercept=2012, linetype="dotted")
    # Labels
    + xlab("Year")
    + ylab("Opiods Per Capita (MME Rate)")
    + labs(title="Opiods Per Capita (MME Rate) in Washington vs Control States")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
)


# #### Florida

# In[280]:


# Filter for treatment state (Florida) and control states
treatment_state = merged[merged["STATE"] == "Florida"]
control_states = merged[merged["STATE"].isin(florida_control)]


# In[281]:


# check
control_states_unique = control_states["STATE"].unique()
print(control_states_unique)


# In[282]:


# check
print(treatment_state["Year"].unique())
print(control_states["Year"].unique())


# In[283]:


# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2010]
treatment_post = treatment_state[treatment_state["Year"] >= 2010]
control_pre = control_states[control_states["Year"] < 2010]
control_post = control_states[control_states["Year"] >= 2010]


# In[284]:


# Creating the plot for Death Rate
(
    ggplot()
    + geom_smooth(treatment_pre, aes("Year", "Death Rate"), method="lm", color="blue")
    + geom_smooth(treatment_post, aes("Year", "Death Rate"), method="lm", color="blue")
    + geom_smooth(control_pre, aes("Year", "Death Rate"), method="lm", color="red")
    + geom_smooth(control_post, aes("Year", "Death Rate"), method="lm", color="red")
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Florida vs Control States")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
)


# In[285]:


# Filter for treatment state (Florida) and control states
treatment_state = merged[merged["STATE"] == "Florida"]
control_states = merged[merged["STATE"].isin(florida_control)]

# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2010]
treatment_post = treatment_state[treatment_state["Year"] >= 2010]
control_pre = control_states[control_states["Year"] < 2010]
control_post = control_states[control_states["Year"] >= 2010]

# Creating the plot for MME Rate
(
    ggplot()
    + geom_smooth(treatment_pre, aes("Year", "MME Rate"), method="lm", color="blue")
    + geom_smooth(treatment_post, aes("Year", "MME Rate"), method="lm", color="blue")
    + geom_smooth(control_pre, aes("Year", "MME Rate"), method="lm", color="red")
    + geom_smooth(control_post, aes("Year", "MME Rate"), method="lm", color="red")
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Opiods Per Capita (MME Rate)")
    + labs(title="Opiods Per Capita (MME Rate) in Florida vs Control States")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
)


# #### Texas

# In[286]:


# Filter for treatment state (Texas) and control states
treatment_state = merged[merged["STATE"] == "Texas"]
control_states = merged[merged["STATE"].isin(texas_control)]


# In[287]:


# check
control_states_unique = control_states["STATE"].unique()
print(control_states_unique)


# In[288]:


# check
print(treatment_state["Year"].unique())
print(control_states["Year"].unique())


# In[289]:


# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2007]
treatment_post = treatment_state[treatment_state["Year"] >= 2007]
control_pre = control_states[control_states["Year"] < 2007]
control_post = control_states[control_states["Year"] >= 2007]


# In[290]:


# Creating the plot for Death Rate
(
    ggplot()
    + geom_smooth(treatment_pre, aes("Year", "Death Rate"), method="lm", color="blue")
    + geom_smooth(treatment_post, aes("Year", "Death Rate"), method="lm", color="blue")
    + geom_smooth(control_pre, aes("Year", "Death Rate"), method="lm", color="red")
    + geom_smooth(control_post, aes("Year", "Death Rate"), method="lm", color="red")
    + geom_vline(xintercept=2007, linetype="dotted")
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Texas vs Control States")
    + scale_x_continuous(
        breaks=[2004, 2005, 2006, 2007, 2008, 2009], limits=[2004, 2009]
    )
    + theme_bw()
)

