# MediPlus Pharmacy - Task 1: Geocode Addresses

Branch addresses (Karachi) ko latitude/longitude mein badalta hai, aur har result ke saath precision likhta hai.

## How to run

    pip install -r requirements.txt
    python src/geocode.py
    python test/test_geocode.py

Input files: data/branches_sample.csv and data/gazetteer_karachi.csv
Output files: output/geocoded.csv and output/rejected.csv

## Result (sample data)

- 23 rows in file: 4 rejected (empty id, empty address, duplicate id, too short address)
- 19 valid rows: street-level 10, area-level 7, no match 2

## Decision and trade-off

Decision: every result gets a precision tag (street, area or none).

Why: pharmacy catchments are small (about 500-800 m), and an area centre can be several km away from the real branch.

Trade-off: area-level branches cannot be used for precise analysis until a GPS pin is added.

## Tests

- Main path: Tariq Road branch gets street-level coordinates inside Karachi.
- Failure path: empty address row is rejected, and the Lahore branch gets no match.
- Missing input file gives a clear error message instead of a crash.

## Limitations

Coordinates are approximate, and misspelled addresses will not match.