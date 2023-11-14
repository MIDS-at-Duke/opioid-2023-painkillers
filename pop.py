#!/usr/bin/env python
# coding: utf-8

# ## Using the nhgis platform to get census data for the years 2006-2015

# For 2006 and 2007, we extracted the population for all counties from the 1970-2007 data hosted on the nhgis website.

import pandas as pd
import numpy as np

# Read in the data
pop2006 = pd.read_csv("nhgis0001_ds231_2006_county.csv")
pop2007 = pd.read_csv("nhgis0001_ds231_2007_county.csv")


# merge both pop2006 and pop2007 on STATEFP and COUNTYFP
pop = pd.merge(pop2006, pop2007, on=["STATEFP", "COUNTYFP"])

# only keep the columns we need
pop = pop[
    [
        "GISJOIN_x",
        "STATEFP",
        "COUNTYFP",
        "COUNTY_x",
        "STATE_x",
        "AGWD001_x",
        "AGWD001_y",
    ]
]

# rename columns
pop.columns = ["GISJOIN", "STATEFP", "COUNTYFP", "COUNTY", "STATE", "2006", "2007"]
pop


# On the nhgis data, we couldn't find the population for 2008 as a single year, but found a dataset for 2008-2012 population, which we are using as a proxy for 2008 only.

df2008 = pd.read_csv("data2008.csv", engine="python")
df2008

# join with pop dataframe sith statea, countya in df2008 and  statefp, countyfp in pop
df2008 = pd.merge(
    df2008, pop, left_on=["STATEA", "COUNTYA"], right_on=["STATEFP", "COUNTYFP"]
)

# drop columns we don't need
df2008 = df2008[
    [
        "GISJOIN_x",
        "STATEFP",
        "COUNTYFP",
        "COUNTY_x",
        "STATE_x",
        "2006",
        "2007",
        "QSPE001",
    ]
]

# rename columns
df2008.columns = [
    "GISJOIN",
    "STATE_CODE",
    "COUNTY_CODE",
    "COUNTY",
    "STATE",
    "2006",
    "2007",
    "2008",
]

df2008


# Next: Merging with 2010 data, we couldn't find 2009 data on the website, so merging with 2010 first, then will try to extrapolate for 2009.

data2010 = pd.read_csv("2010pop.csv", engine="python")
data2010

data2010 = pd.merge(
    data2010,
    df2008,
    right_on=["STATE_CODE", "COUNTY_CODE"],
    left_on=["STATEA", "COUNTYA"],
)
data2010

# drop columns we don't need
data2010 = data2010[
    [
        "GISJOIN_x",
        "STATE_CODE",
        "COUNTY_CODE",
        "COUNTY_x",
        "STATE_x",
        "2006",
        "2007",
        "2008",
        "H7V001",
    ]
]

# rename columns
data2010.columns = [
    "GISJOIN",
    "STATE_CODE",
    "COUNTY_CODE",
    "COUNTY",
    "STATE",
    "2006",
    "2007",
    "2008",
    "2010",
]


# drop rows with missing values

data2010 = data2010.dropna()

data2010


# add 3 new columns for 2009, 2011 and 2012 and fill them with the data from 2008

data2010["2009"] = data2010["2008"]
data2010["2011"] = data2010["2008"]
data2010["2012"] = data2010["2008"]

data2010


# ADDING 2013 data, it has population data on certain states, so we adding it for those and filling rest as NAN for now

# load 2013 data from csv
data2013 = pd.read_csv("data2013.csv", engine="python")
data2013 = data2013[["GISJOIN", "STATEA", "COUNTYA", "COUNTY", "STATE", "SBLE001"]]


# join the data2010 with data2013 but keep all rows in 2010, if that row not in 2013, then add NaN (do right on left on)
data2010 = pd.merge(
    data2010, data2013, how="left", left_on=["GISJOIN"], right_on=["GISJOIN"]
)


# change state_x and county_x to state and county
data2010 = data2010[
    [
        "GISJOIN",
        "STATE_CODE",
        "COUNTY_CODE",
        "COUNTY_x",
        "STATE_x",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "SBLE001",
    ]
]

# change SBLE001 to 2013 - just come column cleaning
data2010.columns = [
    "GISJOIN",
    "STATE_CODE",
    "COUNTY_CODE",
    "COUNTY",
    "STATE",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
]


# 2014
#

# add 2014 and 2015 data now and merge just like we did for 2013

data2014 = pd.read_csv("data2014.csv", engine="python")
data2014 = data2014[["GISJOIN", "STATEA", "COUNTYA", "COUNTY", "STATE", "AAA5E001"]]
data2014


data2010 = data2010[
    [
        "GISJOIN",
        "STATE_CODE",
        "COUNTY_CODE",
        "COUNTY_x",
        "STATE_x",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "AAA5E001_x",
    ]
]


# change AAA5E001_x to 2014 - just come column cleaning
data2010.columns = [
    "GISJOIN",
    "STATE_CODE",
    "COUNTY_CODE",
    "COUNTY",
    "STATE",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
]

# change 2013 and 2014 to integer (exclude nan PLS)

data2010["2013"] = (
    pd.to_numeric(data2010["2013"], errors="coerce").fillna(0).astype(int)
)
data2010["2014"] = (
    pd.to_numeric(data2010["2014"], errors="coerce").fillna(0).astype(int)
)


# now add 2015 data
data2015 = pd.read_csv("data2015.csv", engine="python")
data2015 = data2015[["GISJOIN", "STATEA", "COUNTYA", "COUNTY", "STATE", "ACK2E001"]]


data2010 = pd.merge(
    data2010, data2015, how="left", left_on=["GISJOIN"], right_on=["GISJOIN"]
)


data2010 = data2010[
    [
        "GISJOIN",
        "STATE_CODE",
        "COUNTY_CODE",
        "COUNTY_x",
        "STATE_x",
        "2006",
        "2007",
        "2008",
        "2009",
        "2010",
        "2011",
        "2012",
        "2013",
        "2014",
        "ACK2E001",
    ]
]

# change ACK2E001 to 2015 - just come column cleaning

data2010.columns = [
    "GISJOIN",
    "STATE_CODE",
    "COUNTY_CODE",
    "COUNTY",
    "STATE",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
    "2015",
]

data2010
data2010["2015"] = (
    pd.to_numeric(data2010["2015"], errors="coerce").fillna(0).astype(int)
)


final = data2010


# # FINAL DATASET


final.head()


# But there are a few problems with this. The `nhgis` data source does not have complete population data for some years. In some years there is no proper data available, whereas for some years there is data for some years.
#
# Here is the summary:
# 1. Complete data for `2006`, `2007`, `2010`
# 2. There is data for 2008-2012 - single population
# 3. Data for 2013,2014,2015 is incomplete (only for some states)
#
# Since we have complete data for 2007 and 2010, we can just extrapolate and assume that the change in 2008 and 2009 will be uniform. For example, if population for Durham County was 100000 in 2007 and 130000 in 2010, we can assume uniform change and have 110000 in 2008 and 120000 in 2009, which will be suffecient for our analysis.

# check data for 2007 and 2010 and extrapolate for 2008 and 2009
# Calculate the yearly change from 2007 to 2010
# Calculate the yearly change from 2007 to 2010
yearly_change = (final["2010"] - final["2007"]) / 3

# Calculate the population data for 2008 and 2009
final.loc[:, "2008"] = (final["2007"] + yearly_change).astype(int)
final.loc[:, "2009"] = (final["2007"] + 2 * yearly_change).astype(int)


#


# We had obtained data for `2008-2012` and filled in for all those years, but as we already filled above for 2008 and 2009, we are using those values for 2012, since they were higher than 2010 census data, and population generally increases.
#
# Now we will do the same for 2011, use `2010` and `2012` to see the change and assume it was uniform for 2011 also hence just use the midpoint

# Calculate the yearly change from 2010 to 2012
yearly_change = (final["2012"] - final["2010"]) / 2

# Calculate the population data for 2011
final.loc[:, "2011"] = (data2010["2010"] + yearly_change).astype(int)


# # Filling in missing values for 2013, 2014, 2015 using moving avg of last 5 years
#
# For `2013`, `2014` and `2015`, we obtained the data from `nhgis` but the problem is that data was for limited number of counties and not for all. For the rest of the counties, we are using the 5 year moving average to fill in

######### 2013 #########
# find avg growth rate in from 2008 to 2012 and extrapolate for 2013, 2014 and 2015

# Calculate the yearly change from 2008 to 2012
yearly_change = (final["2012"] - final["2008"]) / 4

# multiply with 2012 to get 2013, 2014 and 2015

final.loc[:, "2013"] = (final["2012"] + yearly_change).astype(int)

######### 2014 #########

yearly_change = (final["2013"] - final["2009"]) / 4

final.loc[:, "2014"] = (final["2013"] + yearly_change).astype(int)

######### 2015 #########

yearly_change = (final["2014"] - final["2010"]) / 4

final.loc[:, "2015"] = (final["2014"] + yearly_change).astype(int)

final.drop("Avg_Growth_Rate_2013", axis=1, inplace=True)


#### OUR FINAL DATA ####
# save it to a csv
final.to_csv("final_population_data.csv", index=False)


###JUST CHECKING
# remove where state is Alaska
# final = final[final["STATE"] != "Alaska"]


# # which county has the county code 91
# final[(final["COUNTY_CODE"] == 91) & (final["STATE_CODE"] == 12)]
# # which state is 12

# final.columns
