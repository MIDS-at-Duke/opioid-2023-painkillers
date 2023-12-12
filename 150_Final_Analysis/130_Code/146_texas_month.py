# %%
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from plotnine import *

# %%
import pandas as pd
import numpy as np

pd.set_option("mode.copy_on_write", True)

# %%
# import the month dataset
month = pd.read_csv("monthly.csv")

# %%
month.head()

# %%
# sum MME and population for all states in each month for each year
result = (
    month.groupby(["BUYER_STATE", "Month", "Year"])[["MME", "Population"]]
    .sum()
    .reset_index()
)

# %%
# calculate MME per capita
result["MME_per_capita"] = result["MME"] / result["Population"]

# %%
result

# %%
# plot for texas monthwise in 2006 and 2007

texas = result[result["BUYER_STATE"] == "TX"]

texas_2006 = texas[texas["Year"] == 2006]

texas_2007 = texas[texas["Year"] == 2007]

texas_2006 = texas_2006.sort_values(by="Month")

texas_2007 = texas_2007.sort_values(by="Month")

plt.plot(texas_2006["Month"], texas_2006["MME_per_capita"], label="2006")

plt.plot(texas_2007["Month"], texas_2007["MME_per_capita"], label="2007")

plt.legend()

plt.xlabel("Month")

plt.ylabel("MME per capita")

plt.title("MME per capita in Texas in 2006 and 2007")

plt.show()

# %%
# create the final dataset for plotting
selected_columns = ["BUYER_STATE", "Month", "Year", "MME_per_capita"]
month_final = result[selected_columns]

month_final.head()  # Displaying the first few rows of the new dataset

# %% [markdown]
# ### Texas Pre-Post MME rate

# %%
month_final_texas = month_final[month_final["BUYER_STATE"] == "TX"]

month_final_texas["Relative_Month"] = (
    (month_final_texas["Year"] - 2007) * 12 + month_final_texas["Month"] - 12
)

# %%
# Filtering data for Texas
month_final_texas = month_final[month_final["BUYER_STATE"] == "TX"]

# Creating new column for x-axis (time relative to policy change)
month_final_texas["Relative_Month"] = (
    month_final_texas["Year"] - 2007
) * 12 + month_final_texas["Month"]

# Splitting into pre and post policy periods
month_final_texas_pre = month_final_texas[month_final_texas["Relative_Month"] < 0]
month_final_texas_post = month_final_texas[month_final_texas["Relative_Month"] >= 0]

# Creating the MME rate plot
pre_post_plot = (
    ggplot()
    # Plot pre-policy period (Texas) for MME Rate
    + geom_smooth(
        month_final_texas_pre,
        aes(x="Relative_Month", y="MME_per_capita", color="'Pre-policy'"),
        method="lm",
    )
    # Plot post-policy period (Texas) for MME Rate
    + geom_smooth(
        month_final_texas_post,
        aes(x="Relative_Month", y="MME_per_capita", color="'Post-policy'"),
        method="lm",
    )
    # Policy treatment line (x-intercept at 0)
    + geom_vline(xintercept=0, linetype="dotted")
    # Labels and Title
    + xlab("Months Relative to Policy Change")
    + ylab("Opioids Per Capita (MME Rate)")
    + labs(
        title="Pre-post Analysis: Opioids Per Capita (MME Rate) for Texas",
        color="Policy Period",
    )
    # X-axis scale
    + scale_x_continuous(breaks=range(-12, 13, 1), limits=[-12, 12])
    + theme_bw()
)

pre_post_plot

# %% [markdown]
# ### Texas diff-in-diff MME rate

# %%
month_final_texas

# %%
texas_control = ["AL", "SC", "TN"]

# %%
# Filtering data for Texas and control states
month_final_texas = month_final[month_final["BUYER_STATE"] == "TX"]
month_final_control = month_final[month_final["BUYER_STATE"].isin(texas_control)]

# Creating new column for x-axis (time relative to policy change)
month_final_texas["Relative_Month"] = (
    month_final_texas["Year"] - 2007
) * 12 + month_final_texas["Month"]
month_final_control["Relative_Month"] = (
    month_final_control["Year"] - 2007
) * 12 + month_final_control["Month"]

# Splitting into pre and post policy periods for treatment and control
treatment_pre = month_final_texas[month_final_texas["Relative_Month"] < 0]
treatment_post = month_final_texas[month_final_texas["Relative_Month"] >= 0]
control_pre = month_final_control[month_final_control["Relative_Month"] < 0]
control_post = month_final_control[month_final_control["Relative_Month"] >= 0]

# Add 'Group' column
treatment_pre["Group"] = "Texas"
treatment_post["Group"] = "Texas"
control_pre["Group"] = "Alabama, South Carolina, Tennessee"
control_post["Group"] = "Alabama, South Carolina, Tennessee"

# Combine all dataframes
combined_df_pre = pd.concat([treatment_pre, control_pre])
combined_df_post = pd.concat([treatment_post, control_post])

# Creating the ggplot for Difference-in-Differences analysis
diff_in_diff_plot = (
    ggplot()
    # Plot pre-policy period for both groups
    + geom_smooth(
        combined_df_pre,
        aes(x="Relative_Month", y="MME_per_capita", color="Group"),
        method="lm",
    )
    # Plot post-policy period for both groups
    + geom_smooth(
        combined_df_post,
        aes(x="Relative_Month", y="MME_per_capita", color="Group"),
        method="lm",
    )
    # Policy treatment line (x-intercept at 0)
    + geom_vline(xintercept=0, linetype="dotted")
    # Labels and Title
    + xlab("Months Relative to Policy Change")
    + ylab("Opioids Per Capita (MME Rate)")
    + labs(
        title="Opioids Per Capita (MME Rate) in Texas vs Control States",
        color="Group",
    )
    # X-axis scale
    + scale_x_continuous(breaks=range(-12, 13, 1), limits=[-12, 12])
    + theme_bw()
    + theme(
        legend_position="top", legend_box="horizontal", legend_title=element_blank()
    )
)

diff_in_diff_plot
