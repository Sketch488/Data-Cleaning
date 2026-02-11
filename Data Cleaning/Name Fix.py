import pandas as pd
import os

filepath = "fifa21_raw_data.csv"

if os.path.exists(filepath):

    try:
        data = pd.read_csv(filepath, encoding="utf-8-sig")

    except UnicodeDecodeError:
        try:
            print("utf-8-sig encoding failed, trying utf-8 encoding...")
            data = pd.read_csv(filepath, encoding="utf-8")

        except UnicodeDecodeError:
            print("utf-8 encoding failed, trying latin1 encoding...")
            data = pd.read_csv(filepath, encoding="latin1")

    print("File loaded successfully.")

else:
    print("File not found.")
