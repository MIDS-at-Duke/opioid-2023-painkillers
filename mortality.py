# To aggregate the deaths dataset
import pandas as pd


########## JUST CHECKING ON ONE FILE ##########
# dataf = pd.read_csv("Underlying Cause of Death, 2003.txt", sep="\t", header=None)

# dataf = dataf[dataf[2].notnull()]
# dataf[5].value_counts()


required = (
    "Drug poisonings (overdose) Unintentional (X40-X44)",
    "Drug poisonings (overdose) Suicide (X60-X64)",
    "Drug poisonings (overdose) Undetermined (Y10-Y14)",
    "All other drug-induced causes",
    "Drug/Alcohol Induced Cause",
)


# dataf = dataf[dataf[5].isin(required)]
# dataf.columns = dataf.iloc[0]
# dataf = dataf[1:]
# df_grouped = dataf.groupby(["County", "Year"])["Deaths"].sum().reset_index()
# df_grouped
# # change year and deaths column to int
# dataf["Deaths"] = pd.to_numeric(dataf["Deaths"], errors="coerce")
# dataf = dataf.dropna(subset=["Deaths"])
# dataf["Deaths"] = dataf["Deaths"].astype(int)


# for all files from 2003 to 2015
def process_file(file_name):
    # read the file into a DataFrame
    df = pd.read_csv(file_name, sep="\t", header=None)

    # perform the necessary transformations

    df = df[df[5].isin(required)]
    df.columns = df.iloc[0]
    df = df[1:]
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df = df.dropna(subset=["Year"])
    df["Year"] = df["Year"].astype(float).astype(int)
    df["Deaths"] = pd.to_numeric(df["Deaths"], errors="coerce")
    df = df.dropna(subset=["Deaths"])
    df["Deaths"] = df["Deaths"].astype(int)
    df_grouped = df.groupby(["County", "Year"])["Deaths"].sum().reset_index()

    return df_grouped


# list of file names
file_names = [
    "Underlying Cause of Death, 2003.txt",
    "Underlying Cause of Death, 2004.txt",
    "Underlying Cause of Death, 2005.txt",
    "Underlying Cause of Death, 2006.txt",
    "Underlying Cause of Death, 2007.txt",
    "Underlying Cause of Death, 2008.txt",
    "Underlying Cause of Death, 2009.txt",
    "Underlying Cause of Death, 2010.txt",
    "Underlying Cause of Death, 2011.txt",
    "Underlying Cause of Death, 2012.txt",
    "Underlying Cause of Death, 2013.txt",
    "Underlying Cause of Death, 2014.txt",
    "Underlying Cause of Death, 2015.txt",
]

# apply the function to each file name
dfs = [process_file(file_name) for file_name in file_names]

# concatenate all the DataFrames into a single DataFrame
df_all = pd.concat(dfs)

# save df_all to csv
df_all.to_csv("mortality.csv", index=False)
