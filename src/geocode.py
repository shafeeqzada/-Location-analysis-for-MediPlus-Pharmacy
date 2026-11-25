import pandas as pd

import os, sys

# agar input file na mile to saaf message do, crash nahi
for path in ["data/branches_sample.csv", "data/gazetteer_karachi.csv"]:
    if not os.path.exists(path):
        print("ERROR: file nahi mili ->", path)
        sys.exit(1)

branches = pd.read_csv("data/branches_sample.csv")
places = pd.read_csv("data/gazetteer_karachi.csv")

places["name"] = places["name"].str.lower().str.replace("-", " ")
places = places.sort_values("precision", ascending = False)

branches["reasons"] = ""
branches.loc[branches["branch_id"].isna(), "reasons"] = "missing branch_id"
branches.loc[branches["address"].isna(), "reasons"] = "empty address"
branches.loc[branches["address"].str.len() < 8, "reasons"] = "address too short"
branches.loc[branches["branch_id"].duplicated() &( branches["reasons"] == ""), "reasons"] = "duplicate branch_id"

rejected = branches[branches["reasons"] != ""]
good = branches[branches["reasons"] == ""].copy()

lats , lons , precisions = [] , [], []
for address in good["address"]:
    text = address.lower().replace("-", " ").replace(",", " ")
    lat = None
    lon = None
    precision = "none"

    for _, place in places.iterrows():
        if place["name"] in text:
            lat, lon , precision = place["lat"] , place["lon"], place["precision"]
            break
    lats.append(lat)
    lons.append(lon)
    precisions.append(precision)

good["lat"] = lats
good["lon"] = lons
good["precision"] = precisions

good.to_csv("output/geocoded.csv", index = False)
rejected.to_csv("output/rejected.csv", index = False)


print(good["precision"].value_counts())
print("rejected:", len(rejected))

 