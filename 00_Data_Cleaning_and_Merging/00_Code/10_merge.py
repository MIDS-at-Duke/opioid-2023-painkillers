
# # Loading the data sets
# 
# Initially we load all our three base files:
# 
# 1. Mortality
# 2. Population
# 3. Shipment

import pandas as pd 
import numpy as np

# Read in data
mortality = pd.read_csv('../10_Clean_Data/mortality/mortality.csv')

population = pd.read_csv('../10_Clean_Data/population/final_population_data.csv')

shipments = pd.read_parquet('../01_Source_Data/shipments/shipments_data.gzip')

# First we reshape the population because population had a column for each year
population_melted = population.melt(id_vars=["GISJOIN", "STATE_CODE", "COUNTY_CODE", "COUNTY", "STATE"],
          var_name="Year",
          value_name="Population")
population_melted.head()


# # Some Data Cleaning



#in population, change District Of Columbia to District of Columbia for STATE (capital O to lowercase o) -> spent hours trying to figure out why it wasn't merging
population_melted['STATE'] = population_melted['STATE'].replace('District Of Columbia', 'District of Columbia')


#remove Alaska from mortality,shipment and population data
mortality['State'] = mortality['State'].str.strip()
mortality = mortality[mortality['State'] != 'AK']
shipments['BUYER_STATE'] = shipments['BUYER_STATE'].str.strip()
shipments = shipments[shipments['BUYER_STATE'] != 'AK']
population_melted['STATE'] = population_melted['STATE'].str.strip()
population_melted = population_melted[population_melted['STATE'] != 'Alaska']


#also remove PR (Puerto Rico) from shipment data
shipments = shipments[shipments['BUYER_STATE'] != 'PR']


#value counts for county and state pair for mortality - just to see if there are any repitions. 13 count means there are 13 years of data for that county. Some counties dont have data in all years
(mortality.groupby(['County', 'State']).size()).sort_values(ascending=False)



mortality.head()
shipments.head()


#check for nas 
population_melted.isna().sum()
shipments.isna().sum()
mortality.isna().sum()


# remove the second word from COUNTY variable and make it lowercase (some counties also have the word Parish - in Louisiana)
#population_melted['COUNTY'] = population_melted['COUNTY'].str.replace(' county', '', case=False).str.lower()
population_melted['COUNTY'] = population_melted['COUNTY'].str.replace(' county', '', case=False).str.replace(' parish', '', case=False).str.lower()
population_melted.head()


# remove the second word from BUYER_COUNTY variable in shipments and make it lowercase
shipments['BUYER_COUNTY'] = shipments['BUYER_COUNTY'].str.replace(' county', '', case=False).str.replace(' parish', '', case=False).str.lower()
shipments.head()


#remove words like county and parish from mortality county variable and make it lowercase because its not in other datasets
mortality['County'] = mortality['County'].str.replace(' county', '', case=False).str.replace(' parish', '', case=False).str.lower()
mortality.head()


#Since we are merging on county and state, we need to make sure that the county and state names are the same across all datasets.
#Mapping state names to abbreviations

state_dict = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}
state_dict = dict(map(reversed, state_dict.items()))


#add a column to mortality to match the state abbreviations
#remove whitespace from state column before the state name
mortality['State Name'] = mortality['State'].map(state_dict)


mortality.head()


#do the same for shipments
shipments['State Name'] = shipments['BUYER_STATE'].map(state_dict)


shipments.head()


# ## NOW WE HAVE ALL 3 DATASETS AND NECESSARY DATA CLEANING AND ADDITIONS ARE DONE. LETS CHECK ALL 3 now

#shape of all three
print(mortality.shape)
print(shipments.shape)
print(population_melted.shape)


#number of states in each
print(len(mortality['State Name'].unique()))
print(len(shipments['State Name'].unique()))
print(len(population_melted['STATE'].unique()))

#find the difference in states between mortality and shipments
set(shipments['State Name'].unique()) - set(mortality['State Name'].unique())
#find the difference in states between mortality and population
#set(population_melted['STATE'].unique()) - set(mortality['State Name'].unique())


#remove Guam, Northern Mariana Islands, U.S. Virgin Islands from shipments
shipments = shipments[shipments['State Name'] != 'Guam']
shipments = shipments[shipments['State Name'] != 'Northern Mariana Islands']
shipments = shipments[shipments['State Name'] != 'U.S. Virgin Islands']




#checking all three after cleaning
shipments.head()


mortality.head(5)

population_melted.head()


#checking number of unique counties state pairs in each
print(len(mortality.groupby(['County', 'State Name'])))
print(len(shipments.groupby(['BUYER_COUNTY', 'State Name'])))
print(len(population_melted.groupby(['COUNTY', 'STATE'])))



#years in each, make year in shipments int
mortality['Year'] = mortality['Year'].astype(int)
shipments['Year'] = shipments['Year'].astype(int)
population_melted['Year'] = population_melted['Year'].astype(int)


print("mortality:",  mortality['Year'].unique())
print("shipments:", shipments['Year'].unique())
print("population:", population_melted['Year'].unique())




# # Merging Process # #


#in mortality, the county in Indiana called 'laporte' is named as 'la porte', se we need to change that
mortality['County'] = mortality['County'].replace('la porte', 'laporte')

#also in mortality, the county in Pennslyvania called 'mckean' is named as 'mc kean', se we need to change that
mortality['County'] = mortality['County'].replace('mc kean', 'mckean')



#now merge the three datasets
#first merge mortality and population outer
mortality_population = pd.merge(mortality,population_melted, how='outer', left_on=['County', 'State Name', 'Year'], right_on=['COUNTY', 'STATE', 'Year'],validate="1:1",
indicator=True)

mortality_population._merge.value_counts()


#total unique counties in florida
len(mortality_population[mortality_population['STATE'] == 'Florida']['COUNTY'].unique())


#check the left only
mortality_population[mortality_population['_merge'] == 'left_only'] #none will be returned for this
#There is no left_only merge, which means that the only missing data we have now is in the mortality dataset because of the missing counties in the mortality dataset (less than 10). We will impute them later on.



mortality_population


#mortality_population[mortality_population['County'] == 'district of columbia']



#check counties in alabama in mortality_population
mortality_population[mortality_population['State Name'] == 'Alabama']['County'].unique()


#change st and st. to saint in mortality_population
mortality_population['COUNTY'] = mortality_population['COUNTY'].str.replace('st ', 'saint ', case=False)
mortality_population['COUNTY'] = mortality_population['COUNTY'].str.replace('st. ', 'saint ', case=False)

#change desoto to de soto in mortality_population
mortality_population['COUNTY'] = mortality_population['COUNTY'].str.replace('desoto', 'de soto', case=False)
mortality_population['COUNTY'] = mortality_population['COUNTY'].str.replace('dewitt', 'de witt', case=False)



#check counties in florida in mortality_population
mortality_population[mortality_population['STATE'] == 'Florida']['COUNTY'].unique()



#find all counties in Louisiana in mortality_population
len(mortality_population[mortality_population['State Name'] == 'Florida']['COUNTY'].unique())


#total unique county-state in mortality_population
len(mortality_population.groupby(['COUNTY', 'STATE']))



#change de kalb dekalb in shipments
shipments['BUYER_COUNTY'] = shipments['BUYER_COUNTY'].replace('de kalb', 'dekalb')

#change st and st. to saint in shipments
shipments['BUYER_COUNTY'] = shipments['BUYER_COUNTY'].replace('st. ', 'saint ')
shipments['BUYER_COUNTY'] = shipments['BUYER_COUNTY'].replace('st ', 'saint ')

#a few other county name mismatches which were found which prevented merging properly
shipments['BUYER_COUNTY'] = shipments['BUYER_COUNTY'].str.replace('desoto', 'de soto', case=False)
shipments['BUYER_COUNTY'] = shipments['BUYER_COUNTY'].str.replace('dewitt', 'de witt', case=False)
shipments['BUYER_COUNTY'] = shipments['BUYER_COUNTY'].str.replace('la porte', 'laporte', case=False)




###just some checking
#show where shipments is null for State Name
shipments[shipments['State Name'].isnull()]

#remove this state (PW) from shipments
shipments = shipments[shipments['State Name'].notna()]

shipments.isna().sum()


shipments.groupby(['BUYER_COUNTY', 'State Name', 'Year']).size().reset_index(name='count').sort_values(by='count', ascending=False)



#merge shipments and mortality_population
mortality_population_shipments = pd.merge(mortality_population,shipments, how='outer', left_on=['COUNTY', 'STATE', 'Year'], right_on=['BUYER_COUNTY', 'State Name', 'Year'], indicator = 'merge_indicator')

mortality_population_shipments['merge_indicator'].value_counts()



mortality_population_shipments[mortality_population_shipments.merge_indicator == "left_only"]['Year'].value_counts()


#give me all counties in Indiana in shipments (checking)
shipments[shipments['State Name'] == 'Indiana']['BUYER_COUNTY'].unique()



#check the right onlys before 2015
mortality_population_shipments[(mortality_population_shipments.merge_indicator == "right_only") & (mortality_population_shipments['Year'] < 2015)]

#get the unique county names from above
mortality_population_shipments[(mortality_population_shipments.merge_indicator == "right_only") & (mortality_population_shipments['Year'] < 2015)]['BUYER_COUNTY'].unique()




#we can just remove the above and also remove data after 2015
mortality_population_shipments = mortality_population_shipments[(mortality_population_shipments['Year'] <= 2015) & (mortality_population_shipments.merge_indicator != "right_only")]



mortality_population_shipments




#clean up and only keep relevant columns
mortality_population_shipments = mortality_population_shipments[['COUNTY', "STATE", 'State Name_x', 'Year', 'Deaths', 'Population', 'BUYER_COUNTY', 'BUYER_STATE', 'MME', 'CALC_BASE_WT_IN_GM', 'merge_indicator']]



mortality_population_shipments




#remove la prte and mc kean county since we dont have population data for them so better to clean
mortality_population_shipments = mortality_population_shipments[mortality_population_shipments['COUNTY'] != 'la porte']
mortality_population_shipments = mortality_population_shipments[mortality_population_shipments['COUNTY'] != 'mc kean']

mortality_population_shipments




merged = mortality_population_shipments




merged
#we still havent removed 2003,2004,2005 data (as that data is not in shipments) but we might need it later


# # Imputation for death rate (normalized)


#calculate death rate

merged['Death Rate'] = merged['Deaths']/merged['Population']



merged



#impute the missing values for death rate based on the avg of that county
#merged['Death Rate'] = merged.groupby(['COUNTY', 'Year'])['Death Rate'].transform(lambda x: x.fillna(x.mean()))


# In[929]:


#find alabama in 2003 and sort by death rate
#merged[(merged['STATE'] == 'Alabama') & (merged['Year'] == 2003)].sort_values(by='Death Rate', ascending=False)


####### IMPUTATION FOR DEATH RATE ########
#find the avg death rate for states in a particular year and assign that to the missing values
merged['Death Rate'] = merged.groupby(['STATE', 'Year'])['Death Rate'].transform(lambda x: x.fillna(x.mean()))



#count unique buyer-county-year rows in shipments
##shipments.groupby(['BUYER_COUNTY', 'BUYER_STATE', 'Year']).size().reset_index(name='count').sort_values(by='count', ascending=False)



#check how many MME columns are null and after 2006 and count unique buyer-county-year rows in shipments
merged


####### TINA CAN U CHECK BEFORE I CREATE THE DATASET FOR THIS ########




#which counties have null MME

#shipments
#shipments.isna().sum()



merged['MME Rate'] = merged['MME']/merged['Population']

merged['MME Rate'] = merged.groupby(['STATE', 'Year'])['MME Rate'].transform(lambda x: x.fillna(x.mean()))

merged.to_csv('../20_Merge_Data/merged.csv', index=False)