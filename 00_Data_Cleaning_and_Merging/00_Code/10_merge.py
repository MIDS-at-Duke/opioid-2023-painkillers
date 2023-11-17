import pandas as pd 
import numpy as np

# Read in data
mortality = pd.read_csv('../10_Clean_Data/mortality/mortality.csv')

population = pd.read_csv('../10_Clean_Data/population/final_population_data.csv')

shipments = pd.read_parquet('../01_Source_Data/shipments/shipments_data.gzip')

# First we reshape the population

population_melted = population.melt(id_vars=["GISJOIN", "STATE_CODE", "COUNTY_CODE", "COUNTY", "STATE"],
          var_name="Year",
          value_name="Population")
population_melted.head()
