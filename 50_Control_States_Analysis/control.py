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


# States =  "Ohio","Colorado","Rhode Island","South Carolina","Georgia"

Ohio = df[df.STATE == "Ohio"]
Ohio_before_policy = Ohio[Ohio.Year < 2010]

Colorado = df[df.STATE == "Colorado"]
Colorado_before_policy = Colorado[Colorado.Year < 2010]


Rhode_island = df[df.STATE == "Rhode Island"]
Rhode_island_before_policy = Rhode_island[Rhode_island.Year < 2010]

South_carolina = df[df.STATE == "South Carolina"]
South_carolina_before_policy = South_carolina[South_carolina.Year < 2010]

Georgia = df[df.STATE == "Georgia"]
Georgia_before_policy = Georgia[Georgia.Year < 2010]

# comparing MME in Florida vs Ohio

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "MME Rate"), method="lm", color="red"
    )
    + geom_smooth(
        Ohio_before_policy, aes("Year", "MME Rate"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("MME Rate")
    + labs(title="MME Rate in Florida vs Ohio Before the Policy was made")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010],  # , 2011, 2012, 2013, 2014, 2015],
        limits=[2006, 2010],
    )
    + theme_bw()
)

# comparing Deaths in Florida vs Ohio

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "Deaths"), method="lm", color="red"
    )
    + geom_smooth(Ohio_before_policy, aes("Year", "Deaths"), method="lm", color="blue")
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Florida vs Ohio Before the Policy was made")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010],  # , 2011, 2012, 2013, 2014, 2015],
        limits=[2006, 2010],
    )
    + theme_bw()
)

# comparing MME in FLorida vs Colorado

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "MME Rate"), method="lm", color="red"
    )
    + geom_smooth(
        Colorado_before_policy, aes("Year", "MME Rate"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("MME Rate")
    + labs(title="MME Rate in Florida vs Colorado Before the Policy was made")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010],  # , 2011, 2012, 2013, 2014, 2015],
        limits=[2006, 2010],
    )
    + theme_bw()
)

# comparing Deaths in FLorida vs Colorado

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "Deaths"), method="lm", color="red"
    )
    + geom_smooth(
        Colorado_before_policy, aes("Year", "Deaths"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Florida vs Colorado Before the Policy was made")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010],  # , 2011, 2012, 2013, 2014, 2015],
        limits=[2006, 2010],
    )
    + theme_bw()
)

# comparing MME in Florida vs Rhode Island

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "MME Rate"), method="lm", color="red"
    )
    + geom_smooth(
        Rhode_island_before_policy, aes("Year", "MME Rate"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("MME Rate")
    + labs(title="MME Rate in Florida vs Rhode Island Before the Policy was made")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010],  # , 2011, 2012, 2013, 2014, 2015],
        limits=[2006, 2010],
    )
    + theme_bw()
)

# comparing Deaths in Florida vs Rhode Island

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "Deaths"), method="lm", color="red"
    )
    + geom_smooth(
        Rhode_island_before_policy, aes("Year", "Deaths"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Florida vs Rhode Island Before the Policy was made")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010],  # , 2011, 2012, 2013, 2014, 2015],
        limits=[2006, 2010],
    )
    + theme_bw()
)

# comparing MME in Florida vs South Carolina

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "MME Rate"), method="lm", color="red"
    )
    + geom_smooth(
        South_carolina_before_policy, aes("Year", "MME Rate"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("MME Rate")
    + labs(title="MME Rate in Florida vs South Carolina Before the Policy was made")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010],  # , 2011, 2012, 2013, 2014, 2015],
        limits=[2006, 2010],
    )
    + theme_bw()
)

# comparing Deaths in Florida vs South Carolina

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "Deaths"), method="lm", color="red"
    )
    + geom_smooth(
        South_carolina_before_policy, aes("Year", "Deaths"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Florida vs South Carolina Before the Policy was made")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010],  # , 2011, 2012, 2013, 2014, 2015],
        limits=[2006, 2010],
    )
    + theme_bw()
)

# comparing MME in Florida vs Georgia

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "MME Rate"), method="lm", color="red"
    )
    + geom_smooth(
        Georgia_before_policy, aes("Year", "MME Rate"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("MME Rate")
    + labs(title="MME Rate in Florida vs Georgia Before the Policy was made")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010],  # , 2011, 2012, 2013, 2014, 2015],
        limits=[2006, 2010],
    )
    + theme_bw()
)

# comparing Deaths in Florida vs Georgia

(
    ggplot()
    + geom_smooth(
        before_policy_florida, aes("Year", "Deaths"), method="lm", color="red"
    )
    + geom_smooth(
        Georgia_before_policy, aes("Year", "Deaths"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2010, linetype="dotted")
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Florida vs Georgia Before the Policy was made")
    + scale_x_continuous(
        breaks=[2006, 2007, 2008, 2009, 2010],  # , 2011, 2012, 2013, 2014, 2015],
        limits=[2006, 2010],
    )
    + theme_bw()
)

#### Control State 2

#Texas: Effective January 4, 2007

texas = df[df.STATE == "Texas"]  # subsetting for Texas

before_policy_texas = texas[
    texas["Year"] < 2007
]  # subsetting the data before the the policy

## Drug Related Deaths in Texas before Policy passed


West_virginia = df[df.STATE == "West Virginia"]
West_virginia_before_policy = West_virginia[West_virginia.Year < 2007]


New_Hampshire = df[df.STATE == "New Hampshire"]
New_Hampshire_before_policy = New_Hampshire[New_Hampshire.Year < 2007]

Kentucky = df[df.STATE == "Kentucky"]
Kentucky_before_policy = Kentucky[Kentucky.Year < 2007]

# Comparing Deaths in Texas vs West Virginia

(
    ggplot()
    + geom_smooth(before_policy_texas, aes("Year", "Deaths"), method="lm", color="red")
    + geom_smooth(
        West_virginia_before_policy, aes("Year", "Deaths"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2007, linetype="dotted")
    + scale_x_continuous(breaks=[2004, 2005, 2006, 2007], limits=[2004, 2007])
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Texas vs West Virginia Before the Policy was passed")
    + theme_bw()
)

# Comparing Deaths in Texas vs New Hampshire

(
    ggplot()
    + geom_smooth(before_policy_texas, aes("Year", "Deaths"), method="lm", color="red")
    + geom_smooth(
        New_Hampshire_before_policy, aes("Year", "Deaths"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2007, linetype="dotted")
    + scale_x_continuous(breaks=[2004, 2005, 2006, 2007], limits=[2004, 2007])
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Texas vs New Hampshire Before the Policy was passed")
    + theme_bw()
)

# Comparing Deaths in Texas vs Kentucky

(
    ggplot()
    + geom_smooth(before_policy_texas, aes("Year", "Deaths"), method="lm", color="red")
    + geom_smooth(
        Kentucky_before_policy, aes("Year", "Deaths"), method="lm", color="blue"
    )
    + geom_vline(xintercept=2007, linetype="dotted")
    + scale_x_continuous(breaks=[2004, 2005, 2006, 2007], limits=[2004, 2007])
    + xlab("Year")
    + ylab("Deaths")
    + labs(title="Deaths in Texas vs Kentucky Before the Policy was passed")
    + theme_bw()
)

washington = df[df.STATE == "Washington"]

before_policy_washington = washington[
    washington.Year < 2012
]  # subsetting the data before the the policy

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

#### Control State 3

# Washington (the State, not Washington, DC), Effective Jan 2, 2012.

