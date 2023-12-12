import pandas as pd
import numpy as np
from dask.distributed import Client

client = Client()
client

# Load Dask
import dask.dataframe as dd

# select certain columns to keep
selected_columns = [
    "BUYER_STATE",
    "BUYER_COUNTY",
    "TRANSACTION_DATE",
    "DOSAGE_UNIT",
    "CALC_BASE_WT_IN_GM",
    "MME",
]

opiod_df = dd.read_csv(
    "arcos_all_washpost.tsv",
    sep="\t",
    usecols=selected_columns,
)

opiod_df["Year"] = dd.to_datetime(
    opiod_df["TRANSACTION_DATE"], format="%Y-%m-%d"
).dt.year

opiod_df = (
    opiod_df.groupby(["BUYER_COUNTY", "BUYER_STATE", "Year"])["MME"].sum().reset_index()
)

result_df = opiod_df.compute()

print("The head of the opioids shipment dataset is: ")
result_df.head()
