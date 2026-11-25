import pandas as pd

good = pd.read_csv("output/geocoded.csv")
rejected = pd.read_csv("output/rejected.csv")

# TEST 1 (main path): Tariq Road branch ko street-level coordinates milne chahiye
row = good[good["branch_id"] == "MP001"].iloc[0]
assert row["precision"] == "street"
assert 24.7 < row["lat"] < 25.2      # Karachi ke andar

# TEST 2 (failure path): khaali address wali row reject honi chahiye
assert "empty address" in rejected["reasons"].values

# TEST 3: Lahore wali branch ka match nahi hona chahiye
lahore = good[good["branch_id"] == "MP020"].iloc[0]
assert lahore["precision"] == "none"

print("Saare tests pass")