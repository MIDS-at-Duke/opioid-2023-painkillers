import pandas as pd
import numpy as np

df = pd.read_csv(
    "arcos_all_washpost.zip", compression="zip", header=0, sep="\t", nrows=10
)

# what columns we want
required_columns = [
    "BUYER_COUNTY",
    "BUYER_STATE",
    "TRANSACTION_DATE",
    "DOSAGE_UNIT",
    "CALC_BASE_WT_IN_GM",
    "MME",
]

chunksize = 10**6
chunks = []

for chunk in pd.read_csv(
    "arcos_all_washpost.zip", compression="zip", sep="\t", chunksize=chunksize
):
    chunk = chunk[required_columns]
    chunk["Year"] = pd.to_datetime(chunk["TRANSACTION_DATE"], format="%Y-%m-%d").dt.year
    chunk_grouped = (
        chunk.groupby(["BUYER_COUNTY", "BUYER_STATE", "Year"])[
            ["MME", "CALC_BASE_WT_IN_GM"]
        ]
        .sum()
        .reset_index()
    )
    chunks.append(chunk_grouped)

df2 = pd.concat(chunks)


# make each buyer county year appear once and sum if appearing multiple times
df2 = (
    df2.groupby(["BUYER_COUNTY", "BUYER_STATE", "Year"])[["MME", "CALC_BASE_WT_IN_GM"]]
    .sum()
    .reset_index()
)


# save this to csv
df2.to_csv("final_shipments.csv", index=False)

# saving to parquet
df2.to_parquet("shipments_data.gzip", compression="gzip")
