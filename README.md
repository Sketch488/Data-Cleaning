This repository contains a Python script to clean and preprocess raw FIFA 21 player data.
The script reads a CSV file containing player information, processes the data, and outputs a cleaned, sorted CSV file.

Features:
1. Reads a raw CSV file (fifa21_raw_data.csv) containing FIFA 21 player data.
2. Standardizes the LongName column by stripping whitespace and capitalizing names.
3. Sorts players alphabetically by name.
4. Removes duplicate player entries based on LongName and Positions.
5. Drops rows with missing LongName or Positions.
6. Outputs a cleaned CSV file FifaV1_Sorted.csv.

Libraries:
1. Pandas

