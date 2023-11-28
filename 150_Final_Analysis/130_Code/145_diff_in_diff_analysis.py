#!/usr/bin/env python
# coding: utf-8

# In[774]:


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from plotnine import *


# In[775]:


import pandas as pd
import numpy as np

pd.set_option("mode.copy_on_write", True)


# In[776]:


# import the final dataset for plotting
merged = pd.read_csv("final_dataset.csv")

merged.head()

# ### Diff-in-Diff Analysis (First Version Selected Control)

# > This is the first version of selected control states that have similar GDP, medium income, spending, poverty rates as the treatment state.

# In[797]:


washington_control = ["Massachusetts", "Colorado", "Maryland"]
florida_control = ["Ohio", "Pennsylvania", "Tennessee"]
texas_control = ["Georgia", "Indiana", "Alabama"]


# #### Washington

# In[798]:


# Filter for treatment state (Washington) and control states
treatment_state = merged[merged["STATE"] == "Washington"]
control_states = merged[merged["STATE"].isin(washington_control)]

# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2012]
treatment_post = treatment_state[treatment_state["Year"] >= 2012]
control_pre = control_states[control_states["Year"] < 2012]
control_post = control_states[control_states["Year"] >= 2012]

# Add a new 'Group' column
treatment_pre["Group"] = "Washington"
treatment_post["Group"] = "Washington"
control_pre["Group"] = f"{', '.join(washington_control)}"
control_post["Group"] = f"{', '.join(washington_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[combined_df["Year"] < 2012]  # Adjust based on policy year
combined_df_post = combined_df[
    combined_df["Year"] >= 2012
]  # Adjust based on policy year

# Plot mortality rate
(
    ggplot()
    + geom_smooth(
        combined_df_pre, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_smooth(
        combined_df_post, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_vline(xintercept=2012, linetype="dotted")  # Policy year line
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Washington vs Control States")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# In[799]:


# Add a new 'Group' column
treatment_pre["Group"] = "Washington"
treatment_post["Group"] = "Washington"
control_pre["Group"] = f"{', '.join(washington_control)}"
control_post["Group"] = f"{', '.join(washington_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[combined_df["Year"] < 2012]  # Adjust based on policy year
combined_df_post = combined_df[
    combined_df["Year"] >= 2012
]  # Adjust based on policy year

# Plot MME rate
(
    ggplot()
    + geom_smooth(combined_df_pre, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_smooth(combined_df_post, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_vline(xintercept=2012, linetype="dotted")  # Policy year line
    + xlab("Year")
    + ylab("Opioids Per Capita (MME Rate)")
    + labs(title="Opioids Per Capita (MME Rate) in Washington vs Control States")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# #### Florida

# In[800]:


# Filter for treatment state (Florida) and control states
treatment_state = merged[merged["STATE"] == "Florida"]
control_states = merged[merged["STATE"].isin(florida_control)]

# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2010]
treatment_post = treatment_state[treatment_state["Year"] >= 2010]
control_pre = control_states[control_states["Year"] < 2010]
control_post = control_states[control_states["Year"] >= 2010]

# Add a new 'Group' column
treatment_pre["Group"] = "Florida"
treatment_post["Group"] = "Florida"
control_pre["Group"] = f"{', '.join(florida_control)}"
control_post["Group"] = f"{', '.join(florida_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[
    combined_df["Year"] < 2010
]  # Adjust based on policy year for Florida
combined_df_post = combined_df[
    combined_df["Year"] >= 2010
]  # Adjust based on policy year for Florida

# Plot Death Rate
(
    ggplot()
    + geom_smooth(
        combined_df_pre, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_smooth(
        combined_df_post, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_vline(xintercept=2010, linetype="dotted")  # Policy year line for Florida
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Florida vs Control States")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# In[801]:


# Add a new 'Group' column
treatment_pre["Group"] = "Florida"
treatment_post["Group"] = "Florida"
control_pre["Group"] = f"{', '.join(florida_control)}"
control_post["Group"] = f"{', '.join(florida_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[
    combined_df["Year"] < 2010
]  # Adjust based on policy year for Florida
combined_df_post = combined_df[
    combined_df["Year"] >= 2010
]  # Adjust based on policy year for Florida

# Plot MME rate
(
    ggplot()
    + geom_smooth(combined_df_pre, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_smooth(combined_df_post, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_vline(xintercept=2010, linetype="dotted")  # Policy year line for Florida
    + xlab("Year")
    + ylab("Opioids Per Capita (MME Rate)")
    + labs(title="Opioids Per Capita (MME Rate) in Florida vs Control States")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# #### Texas

# In[802]:


# Filter for treatment state (Texas) and control states
treatment_state = merged[merged["STATE"] == "Texas"]
control_states = merged[merged["STATE"].isin(texas_control)]

# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2007]
treatment_post = treatment_state[treatment_state["Year"] >= 2007]
control_pre = control_states[control_states["Year"] < 2007]
control_post = control_states[control_states["Year"] >= 2007]

# Add a new 'Group' column
treatment_pre["Group"] = "Texas"
treatment_post["Group"] = "Texas"
control_pre["Group"] = f"{', '.join(texas_control)}"
control_post["Group"] = f"{', '.join(texas_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

combined_df_pre = combined_df[combined_df["Year"] <= 2006]
combined_df_post = combined_df[combined_df["Year"] > 2006]

# Plot mortality rate
(
    ggplot()
    + geom_smooth(
        combined_df_pre, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_smooth(
        combined_df_post, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_vline(xintercept=2007, linetype="dotted")
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Texas vs Control States")
    + scale_x_continuous(
        breaks=[2004, 2005, 2006, 2007, 2008, 2009], limits=[2004, 2009]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# ### Diff-in-Diff Analysis (Second Version Selected Controls)

# > This is the second version of the selected control states with similar pre-treatment trends as the treatment state.

# In[803]:


washington_control = ["Utah", "Tennessee", "Maine"]
florida_control = ["Ohio", "Colorado", "Rhode Island", "South Carolina", "Georgia"]
texas_control = ["West Virginia", "New Hampshire", "Kentucky"]


# #### Washington

# In[804]:


# Filter for treatment state (Washington) and control states
treatment_state = merged[merged["STATE"] == "Washington"]
control_states = merged[merged["STATE"].isin(washington_control)]


# In[805]:


# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2012]
treatment_post = treatment_state[treatment_state["Year"] >= 2012]
control_pre = control_states[control_states["Year"] < 2012]
control_post = control_states[control_states["Year"] >= 2012]


# In[806]:


# Add a new 'Group' column
treatment_pre["Group"] = "Washington"
treatment_post["Group"] = "Washington"
control_pre["Group"] = f"{', '.join(washington_control)}"
control_post["Group"] = f"{', '.join(washington_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[combined_df["Year"] < 2012]  # Adjust based on policy year
combined_df_post = combined_df[
    combined_df["Year"] >= 2012
]  # Adjust based on policy year

# Plot mortality rate
(
    ggplot()
    + geom_smooth(
        combined_df_pre, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_smooth(
        combined_df_post, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_vline(xintercept=2012, linetype="dotted")  # Policy year line
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Washington vs Control States")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# In[807]:


# Add a new 'Group' column
treatment_pre["Group"] = "Washington"
treatment_post["Group"] = "Washington"
control_pre["Group"] = f"{', '.join(washington_control)}"
control_post["Group"] = f"{', '.join(washington_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[combined_df["Year"] < 2012]  # Adjust based on policy year
combined_df_post = combined_df[
    combined_df["Year"] >= 2012
]  # Adjust based on policy year

# Plot MME rate
(
    ggplot()
    + geom_smooth(combined_df_pre, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_smooth(combined_df_post, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_vline(xintercept=2012, linetype="dotted")  # Policy year line
    + xlab("Year")
    + ylab("Opioids Per Capita (MME Rate)")
    + labs(title="Opioids Per Capita (MME Rate) in Washington vs Control States")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# ### Florida

# In[808]:


# Filter for treatment state (Florida) and control states
treatment_state = merged[merged["STATE"] == "Florida"]
control_states = merged[merged["STATE"].isin(florida_control)]


# In[809]:


# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2010]
treatment_post = treatment_state[treatment_state["Year"] >= 2010]
control_pre = control_states[control_states["Year"] < 2010]
control_post = control_states[control_states["Year"] >= 2010]


# In[810]:


# Add a new 'Group' column
treatment_pre["Group"] = "Florida"
treatment_post["Group"] = "Florida"
control_pre["Group"] = f"{', '.join(florida_control)}"
control_post["Group"] = f"{', '.join(florida_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[
    combined_df["Year"] < 2010
]  # Adjust based on policy year for Florida
combined_df_post = combined_df[
    combined_df["Year"] >= 2010
]  # Adjust based on policy year for Florida

# Plot Death Rate
(
    ggplot()
    + geom_smooth(
        combined_df_pre, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_smooth(
        combined_df_post, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_vline(xintercept=2010, linetype="dotted")  # Policy year line for Florida
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Florida vs Control States")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# In[811]:


# Add a new 'Group' column
treatment_pre["Group"] = "Florida"
treatment_post["Group"] = "Florida"
control_pre["Group"] = f"{', '.join(florida_control)}"
control_post["Group"] = f"{', '.join(florida_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[
    combined_df["Year"] < 2010
]  # Adjust based on policy year for Florida
combined_df_post = combined_df[
    combined_df["Year"] >= 2010
]  # Adjust based on policy year for Florida

# Plot MME rate
(
    ggplot()
    + geom_smooth(combined_df_pre, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_smooth(combined_df_post, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_vline(xintercept=2010, linetype="dotted")  # Policy year line for Florida
    + xlab("Year")
    + ylab("Opioids Per Capita (MME Rate)")
    + labs(title="Opioids Per Capita (MME Rate) in Florida vs Control States")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# ### Texas

# In[812]:


# Filter for treatment state (Texas) and control states
treatment_state = merged[merged["STATE"] == "Texas"]
control_states = merged[merged["STATE"].isin(texas_control)]


# In[813]:


# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2007]
treatment_post = treatment_state[treatment_state["Year"] >= 2007]
control_pre = control_states[control_states["Year"] < 2007]
control_post = control_states[control_states["Year"] >= 2007]


# In[814]:


# Add a new 'Group' column
treatment_pre["Group"] = "Texas"
treatment_post["Group"] = "Texas"
control_pre["Group"] = f"{', '.join(texas_control)}"
control_post["Group"] = f"{', '.join(texas_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

combined_df_pre = combined_df[combined_df["Year"] <= 2006]
combined_df_post = combined_df[combined_df["Year"] > 2006]

# Plot mortality rate
(
    ggplot()
    + geom_smooth(
        combined_df_pre, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_smooth(
        combined_df_post, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_vline(xintercept=2007, linetype="dotted")
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Texas vs Control States")
    + scale_x_continuous(
        breaks=[2004, 2005, 2006, 2007, 2008, 2009], limits=[2004, 2009]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# ### Diff-in-Diff (Third Version Selected Controls)

# > This is the third version of selected control states that have similar GDP, medium income, spending, poverty rates as the treatment state as well as similar pre-treatment trends as the treatment state.

# In[815]:


# Updated lists of control states for each treatment state
florida_control = ["Ohio", "Oklahoma", "Arkansas"]
washington_control = ["Oregon", "Massachusetts", "Maryland"]
texas_control = ["Alabama", "South Carolina", "Tennessee"]


# #### Washington

# In[816]:


# Filter for treatment state (Washington) and control states
treatment_state = merged[merged["STATE"] == "Washington"]
control_states = merged[merged["STATE"].isin(washington_control)]


# In[817]:


# check
control_states_unique = control_states["STATE"].unique()
print(control_states_unique)


# In[818]:


# check
print(treatment_state["Year"].unique())
print(control_states["Year"].unique())


# In[819]:


# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2012]
treatment_post = treatment_state[treatment_state["Year"] >= 2012]
control_pre = control_states[control_states["Year"] < 2012]
control_post = control_states[control_states["Year"] >= 2012]


# In[820]:


# Add a new 'Group' column
treatment_pre["Group"] = "Washington"
treatment_post["Group"] = "Washington"
control_pre["Group"] = f"{', '.join(washington_control)}"
control_post["Group"] = f"{', '.join(washington_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[combined_df["Year"] < 2012]  # Adjust based on policy year
combined_df_post = combined_df[
    combined_df["Year"] >= 2012
]  # Adjust based on policy year

# Plot mortality rate
(
    ggplot()
    + geom_smooth(
        combined_df_pre, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_smooth(
        combined_df_post, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_vline(xintercept=2012, linetype="dotted")  # Policy year line
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Washington vs Control States")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# In[821]:


# Add a new 'Group' column
treatment_pre["Group"] = "Washington"
treatment_post["Group"] = "Washington"
control_pre["Group"] = f"{', '.join(washington_control)}"
control_post["Group"] = f"{', '.join(washington_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[combined_df["Year"] < 2012]  # Adjust based on policy year
combined_df_post = combined_df[
    combined_df["Year"] >= 2012
]  # Adjust based on policy year

# Plot MME rate
(
    ggplot()
    + geom_smooth(combined_df_pre, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_smooth(combined_df_post, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_vline(xintercept=2012, linetype="dotted")  # Policy year line
    + xlab("Year")
    + ylab("Opioids Per Capita (MME Rate)")
    + labs(title="Opioids Per Capita (MME Rate) in Washington vs Control States")
    + scale_x_continuous(
        breaks=[2009, 2010, 2011, 2012, 2013, 2014], limits=[2009, 2014]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# #### Florida

# In[822]:


# Filter for treatment state (Florida) and control states
treatment_state = merged[merged["STATE"] == "Florida"]
control_states = merged[merged["STATE"].isin(florida_control)]


# In[823]:


# check
control_states_unique = control_states["STATE"].unique()
print(control_states_unique)


# In[824]:


# check
print(treatment_state["Year"].unique())
print(control_states["Year"].unique())


# In[825]:


# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2010]
treatment_post = treatment_state[treatment_state["Year"] >= 2010]
control_pre = control_states[control_states["Year"] < 2010]
control_post = control_states[control_states["Year"] >= 2010]


# In[826]:


# Add a new 'Group' column
treatment_pre["Group"] = "Florida"
treatment_post["Group"] = "Florida"
control_pre["Group"] = f"{', '.join(florida_control)}"
control_post["Group"] = f"{', '.join(florida_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[
    combined_df["Year"] < 2010
]  # Adjust based on policy year for Florida
combined_df_post = combined_df[
    combined_df["Year"] >= 2010
]  # Adjust based on policy year for Florida

# Plot Death Rate
(
    ggplot()
    + geom_smooth(
        combined_df_pre, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_smooth(
        combined_df_post, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_vline(xintercept=2010, linetype="dotted")  # Policy year line for Florida
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Florida vs Control States")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# In[827]:


# Add a new 'Group' column
treatment_pre["Group"] = "Florida"
treatment_post["Group"] = "Florida"
control_pre["Group"] = f"{', '.join(florida_control)}"
control_post["Group"] = f"{', '.join(florida_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

# Filter the combined DataFrame for pre and post policy years
combined_df_pre = combined_df[
    combined_df["Year"] < 2010
]  # Adjust based on policy year for Florida
combined_df_post = combined_df[
    combined_df["Year"] >= 2010
]  # Adjust based on policy year for Florida

# Plot MME rate
(
    ggplot()
    + geom_smooth(combined_df_pre, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_smooth(combined_df_post, aes("Year", "MME Rate", color="Group"), method="lm")
    + geom_vline(xintercept=2010, linetype="dotted")  # Policy year line for Florida
    + xlab("Year")
    + ylab("Opioids Per Capita (MME Rate)")
    + labs(title="Opioids Per Capita (MME Rate) in Florida vs Control States")
    + scale_x_continuous(
        breaks=[2007, 2008, 2009, 2010, 2011, 2012], limits=[2007, 2012]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)


# #### Texas

# In[828]:


# Filter for treatment state (Texas) and control states
treatment_state = merged[merged["STATE"] == "Texas"]
control_states = merged[merged["STATE"].isin(texas_control)]


# In[829]:


# check
control_states_unique = control_states["STATE"].unique()
print(control_states_unique)


# In[830]:


# check
print(treatment_state["Year"].unique())
print(control_states["Year"].unique())


# In[831]:


# Splitting into pre and post policy years for treatment and control groups
treatment_pre = treatment_state[treatment_state["Year"] < 2007]
treatment_post = treatment_state[treatment_state["Year"] >= 2007]
control_pre = control_states[control_states["Year"] < 2007]
control_post = control_states[control_states["Year"] >= 2007]


# In[832]:


# Add a new 'Group' column
treatment_pre["Group"] = "Texas"
treatment_post["Group"] = "Texas"
control_pre["Group"] = f"{', '.join(texas_control)}"
control_post["Group"] = f"{', '.join(texas_control)}"

# Combine all dataframes
combined_df = pd.concat([treatment_pre, treatment_post, control_pre, control_post])

combined_df_pre = combined_df[combined_df["Year"] <= 2006]
combined_df_post = combined_df[combined_df["Year"] > 2006]

# Plot mortality rate
(
    ggplot()
    + geom_smooth(
        combined_df_pre, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_smooth(
        combined_df_post, aes("Year", "Death Rate", color="Group"), method="lm"
    )
    + geom_vline(xintercept=2007, linetype="dotted")
    + xlab("Year")
    + ylab("Overdose Mortality Rate")
    + labs(title="Overdose Mortality Rate in Texas vs Control States")
    + scale_x_continuous(
        breaks=[2004, 2005, 2006, 2007, 2008, 2009], limits=[2004, 2009]
    )
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)
