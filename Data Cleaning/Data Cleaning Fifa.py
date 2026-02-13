import os
import pandas as pd

filepath = "fifa21_raw_data.csv"

if os.path.exists(filepath):

    data = pd.read_csv(filepath, encoding="utf-8-sig")
    
    #Proper the longname column
    data["LongName"] = data["LongName"].astype(str).str.strip().str.title()

    data = (
        data.sort_values("LongName").reset_index(drop=True)
        .drop_duplicates(subset=["LongName", "Positions"], keep="first").reset_index(drop=True)
        .dropna(subset=["LongName", "Positions"]).reset_index(drop=True)
    )

    data.to_csv("FifaV1_Sorted.csv", encoding="utf-8-sig", index=False)

    print(data.head(10))

else:
    print(f"File '{filepath}' does not exist.")
