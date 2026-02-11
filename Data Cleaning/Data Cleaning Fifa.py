import os
import pandas as pd

filepath = "fifa21_raw_data.csv"

if os.path.exists(filepath):

    data = pd.read_csv(filepath, encoding="utf-8-sig")
    
    #Proper the longname column
    data["LongName"] = data["LongName"].astype(str).str.strip().str.title()

    #data["LongName"] = data["LongName"].apply(lambda x: x.encode("latin-1").decode("utf-8-sig") if isinstance(x, str) else x)
    #for col in data.select_dtypes(include=["object"]).columns:
        #data[col] = data[col].apply(
            #lambda x: x.encode("latin-1").decode("utf-8-sig") if isinstance(x, str) else x)
    
    #Sort, remove duplicates, and handle missing values
    data = data.sort_values("LongName").reset_index(drop=True)
    data = data.drop_duplicates(subset=["LongName", "Positions"], keep="first").reset_index(drop=True)
    data = data.dropna(subset=["LongName", "Positions"]).reset_index(drop=True)
    #data = data.dropna.reset_index(drop=True)

    data.to_csv("FifaV1_Sorted.csv", encoding="utf-8-sig", index=False)

    print(data.head(10))

else:
    print(f"File '{filepath}' does not exist.")
