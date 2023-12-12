# %%
import pandas as pd
import numpy as np
import warnings
from plotnine import *

from warnings import filterwarnings

pd.set_option("mode.copy_on_write", True)

df = pd.read_csv(
    "/Users/shailaguereca/Documents/Practical_Data_Science/Opiods Team Project/merged.csv"
)

# %%
# Plotting each of the control states vs Florida
df_Florida = df[
    (
        df["STATE"].isin(
            [
                "Florida",
                "Ohio",
                "Arkansas",
                "Oklahoma",
            ]
        )
    )
    & (df["Year"] < 2010)
]

# Plotting using ggplot
plot_mme_rate = (
    ggplot(df_Florida, aes(x="Year", y="Death Rate", color="STATE"))
    + geom_point()
    + geom_smooth(method="lm")
    + facet_wrap("~ STATE", scales="free_y")
)
print(plot_mme_rate)

# %%
# Florida vs several options for control states
df_Florida = df[
    (
        df["STATE"].isin(
            [
                "Florida",
                "Ohio",
                "Arkansas",
                "Oklahoma",
            ]
        )
    )
    & (df["Year"].between(2007, 2010))
]

# Plotting using ggplot with all states in one plot
Florida_Control_States_DeathRate = (
    ggplot(df_Florida, aes(x="Year", y="Death Rate", color="STATE", group="STATE"))
    + geom_point()
    + geom_smooth(method="lm", se=False)
    + scale_y_continuous(limits=(0, 0.0002))
    + labs(
        title="Death Rate Trends Before 2010 for Selected States and Florida",
        x="Year",
        y="Death Rate",
    )
)
print(Florida_Control_States_DeathRate)

# %%
# Filter data for the specified states and years before 2010
df_Florida = df[
    (
        df["STATE"].isin(
            [
                "Florida",
                "Ohio",
                "Arkansas",
                "Oklahoma",
            ]
        )
    )
    & (df["Year"].between(2007, 2010))
]

# Plotting using ggplot with all states in one plot
Florida_Control_States_MMERate = (
    ggplot(df_Florida, aes(x="Year", y="MME Rate", color="STATE", group="STATE"))
    + geom_point()
    + geom_smooth(method="lm", se=False)
    + scale_y_continuous(limits=(0, 500))
    + labs(
        title="MME Rate Trends Before 2010 for Selected States and Florida",
        x="Year",
        y="MME Rate",
    )
)
print(Florida_Control_States_MMERate)

# %%
# Filter data for the specified states and years 2007 to 2009 for Death Rate
df_death_rate = df[
    (
        df["STATE"].isin(
            [
                "Washington",
                "Massachusetts",
                "Maryland",
                "Oregon",
            ]
        )
    )
    & (df["Year"].between(2009, 2012))
]

# Plotting Death Rate using ggplot for the specified states
plot_death_rate = (
    ggplot(df_death_rate, aes(x="Year", y="Death Rate", color="STATE", group="STATE"))
    + geom_point()
    + geom_smooth(method="lm", se=False)
    + scale_y_continuous(limits=(0, 0.0002))
    + labs(
        title="Death Rate Trends (2009, 2012) for Selected States and Washington",
        x="Year",
        y="Death Rate",
    )
)

# Filter data for the specified states and years 2007 to 2009 for MME Rate
df_mme_rate = df[
    (
        df["STATE"].isin(
            [
                "Washington",
                "Massachusetts",
                "Maryland",
                "Oregon",
            ]
        )
    )
    & (df["Year"].between(2009, 2012))
]

# Plotting MME Rate using ggplot for the specified states
plot_mme_rate = (
    ggplot(df_mme_rate, aes(x="Year", y="MME Rate", color="STATE", group="STATE"))
    + geom_point()
    + geom_smooth(method="lm", se=False)
    + scale_y_continuous(limits=(0, 500))
    + labs(
        title="MME Rate Trends for Selected States and Washington",
        x="Year",
        y="MME Rate",
    )
)

# Displaying the plots
print(plot_death_rate)
print(plot_mme_rate)

# %%
# Filter data for the specified states and years 2007 to 2009 for Death Rate
df_death_rate = df[
    (
        df["STATE"].isin(
            [
                "Texas",
                "Alabama",
                "Tennessee",
                "North Carolina",
            ]
        )
    )
    & (df["Year"].between(2004, 2007))
]

# Plotting Death Rate using ggplot for the specified states
plot_death_rate = (
    ggplot(df_death_rate, aes(x="Year", y="Death Rate", color="STATE", group="STATE"))
    + geom_point()
    + geom_smooth(method="lm", se=False)
    + scale_y_continuous(limits=(0, 0.0002))
    + labs(
        title="Death Rate Trends (2007-2009) for Selected States and Texas",
        x="Year",
        y="Death Rate",
    )
)

# Filter data for the specified states and years 2007 to 2009 for MME Rate
df_mme_rate = df[
    (
        df["STATE"].isin(
            [
                "Texas",
                "Alabama",
                "Tennessee",
                "North Carolina",
            ]
        )
    )
    & (df["Year"].between(2004, 2007))
]

# Plotting MME Rate using ggplot for the specified states
plot_mme_rate = (
    ggplot(df_mme_rate, aes(x="Year", y="MME Rate", color="STATE", group="STATE"))
    + geom_point()
    + geom_smooth(method="lm", se=False)
    + scale_y_continuous(limits=(0, 500))
    + labs(
        title="MME Rate Trends (2007-2009) for Selected States and Texas",
        x="Year",
        y="MME Rate",
    )
)

# Displaying the plots
print(plot_death_rate)
print(plot_mme_rate)
