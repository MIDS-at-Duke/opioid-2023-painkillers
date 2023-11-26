import pandas as pd
import numpy as np
import warnings
from plotnine import *

from warnings import filterwarnings

pd.set_option("mode.copy_on_write", True)

df = pd.read_csv(
    "/Users/keonnartey/Desktop/PDS/opioid-2023-painkillers/00_Data_Cleaning_and_Merging/20_Merge_Data/merged.csv"
)

# loading the first few datasets for the dataframe.

df.head()

df.Year.unique()  # unique years in the dataframe for each county and state.

df.STATE.unique()

#### Control states

# Florida = Ohio, Colorado,Rhode Island, South Carolina, Georgia
# Texas  = West Virginia, New Hampshire, Kentucky
# Washington = Utah,Hawaii, Maine

#### Control State 1

# Florida, Effective February, 2010

florida = df[df.STATE == "Florida"]

before_policy_florida = florida[
    florida.Year < 2010
]  # subsetting the data before the the policy
after_policy_florida = florida[
    florida.Year >= 2010
]  # a subset of the data after the policy was passed

# Plotting the Shipments in Florida before the policy was made

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "MME Rate"), method="lm", color="red"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("MME Rate")
    + labs(title="MME Rate in Florida Before the Policy")
    + theme_bw()
)

# Plotting the Deaths in Florida before the policy was made

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "Deaths"), method="lm", color="red"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Florida Before the Policy was made")
    + theme_bw()
)

# Control State for Florida

state_list = [
    "Ohio",
    "Colorado",
    "Rhode Island",
    "South Carolina",
    "Georgia",
]  # using these states as control state for Florida

con_state = df[df.STATE.isin(state_list)]
bf_1 = con_state[con_state.Year < 2010]

# Plotting the Shipments in Florida before the policy was made

(
    ggplot()
    + geom_smooth(bf_1, aes("Year", "MME Rate"), method="lm", color="blue")
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("MME Rate")
    + labs(title="MME Rate of Control States Before the Policy was made")
    + theme_bw()
)

# Plotting the Deaths in Florida before the policy was made

(
    ggplot()
    + geom_smooth(bf_1, aes("Year", "Deaths"), method="lm", color="blue")
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Control States Before the Policy was made")
    + theme_bw()
)

# comparing MME in FLorida vs Control State

(
    ggplot()
    + geom_smooth(bf_1, aes("Year", "MME Rate"), method="lm", color="blue")
    + geom_smooth(
        before_policy_florida, aes("Year", "MME Rate"), method="lm", color="red"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("MME Rate")
    + labs(title="MME Rate in Florida Before the Policy was made")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010],  # , 2011, 2012, 2013, 2014, 2015],
        limits=[2006, 2010],
    )
    + theme_bw()
)


# comparing Deaths in FLorida vs Control State

(
    ggplot()
    + geom_smooth(bf_1, aes("Year", "Deaths"), method="lm", color="blue")
    + geom_smooth(
        before_policy_florida, aes("Year", "Deaths"), method="lm", color="red"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Florida vs Control States before the Policy")
    + scale_x_continuous(
        breaks=[
            2003,
            2004,
            2005,
            2006,
            2007,
            2008,
            2009,
            2010],
        limits=[2003, 2010],
    )
    + theme_bw()
)

#### Control State 2

# Texas: Effective January 4, 2007

texas = df[df.STATE == "Texas"]  # subsetting for Texas

before_policy_texas = texas[
    texas["Year"] < 2007
]  # subsetting the data before the the policy
after_policy_texas = texas[
    texas["Year"] >= 2007
]  # a subset of the data after the policy was passed

## Drug Related Deaths in Texas before Policy passed

(
    ggplot()
    + geom_smooth(before_policy_texas, aes("Year", "Deaths"), method="lm", color="red")
    + geom_vline(xintercept=2007, linetype="dotted")
    + scale_x_continuous(
        breaks=[2004, 2005, 2006, 2007], limits=[2004, 2007]
    )
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Texas Before the Policy was passed")
    + theme_bw()
)

state = [
    "West Virginia",
    "New Hampshire",
    "Kentucky",
]  # using these states as control state for Texas
con_state_1 = df[df.STATE.isin(state)]
bf = con_state_1[con_state_1.Year < 2007]

# Deaths in Control states

(
    ggplot()
    + geom_smooth(bf, aes("Year", "Deaths"), method="lm", color="blue")
    + geom_vline(xintercept=2007, linetype="dotted")
    + scale_x_continuous(
        breaks=[2004, 2005, 2006, 2007], limits=[2004, 2007]
    )
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Control States Before the Policy was passed")
    + theme_bw()
)

# Comparing Deaths in Texas vs Control States

(
    ggplot()
    + geom_smooth(before_policy_texas, aes("Year", "Deaths"), method="lm", color="red")
    + geom_smooth(bf, aes("Year", "Deaths"), method="lm", color="blue")
    + geom_vline(xintercept=2007, linetype="dotted")
    + scale_x_continuous(
        breaks=[2004, 2005, 2006, 2007], limits=[2004, 2007]
    )
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Death Rate in Texas vs Control States")
    + theme_bw()
)

#### Control State 3

# Washington (the State, not Washington, DC), Effective Jan 2, 2012.

washington = df[df.STATE == "Washington"]

before_policy_washington = washington[
    washington.Year < 2012
]  # subsetting the data before the the policy
after_policy_washington = washington[
    washington.Year >= 2012
]  # a subset of the data after the policy was passed

# Shipments in Washington

(
    ggplot()
    + geom_smooth(
        before_policy_washington, aes("Year", "MME Rate"), method="lm", color="red"
    )
    + geom_vline(xintercept=2012, linetype="dotted")
    + xlab("Year")
    + ylab("MME Rate")
    + labs(title="MME Rate in Floria Before the Policy was made")
    + theme_bw()
)

# Deaths in Washington

(
    ggplot()
    + geom_smooth(
        before_policy_washington, aes("Year", "Deaths"), method="lm", color="red"
    )
    + geom_vline(xintercept=2012, linetype="dotted")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010, 2011, 2012],
        limits=[2006, 2012],
    )
    + xlab("Year")
    + ylab("MME Rate")
    + labs(title="MME Rate in Washington Before the Policy was made")
    + theme_bw()
)

state_list_1 = [
    "Utah",
    "Tennessee",
    "Maine",
]  # using these states as control state for Florida
con_state_2 = df[df.STATE.isin(state_list_1)]
bf_2 = con_state_2[con_state_2.Year < 2012]

# shipments in Control States 

(
    ggplot()
    + geom_smooth(bf_2, aes("Year", "MME Rate"), method="lm", color="blue")
    + geom_vline(xintercept=2012, linetype="dotted")
    + xlab("Year")
    + ylab("MME Rate")
    + labs(title="MME Rate in Control States Before the Policy was made")
    + theme_bw()
)

# Shipments in Washington vs Control states

(
    ggplot()
    + geom_smooth(
        before_policy_washington, aes("Year", "MME Rate"), method="lm", color="red"
    )
    + geom_smooth(bf_2, aes("Year", "MME Rate"), method="lm", color="blue")
    + geom_vline(xintercept=2012, linetype="dotted")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010, 2011, 2012],
        limits=[2006, 2012],
    )
    + xlab("Year")
    + ylab("MME Rate")
    + labs(
        title="MME Rate in Washington Vs Control States Before the Policy was made"
    )
    + theme_bw()
)

# Comparing Deaths in Washington vs Control States 

(
    ggplot()
    + geom_smooth(
        before_policy_washington, aes("Year", "Deaths"), method="lm", color="red"
    )
    + geom_smooth(bf_2, aes("Year", "Deaths"), method="lm", color="blue")
    + geom_vline(xintercept=2012, linetype="dotted")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010, 2011, 2012],
        limits=[2006, 2012],
    )
    + xlab("Year")
    + ylab("MME Rate")
    + labs(
        title="Deaths in Washington Vs Control States Before the Policy was made"
    )
    + theme_bw()
)