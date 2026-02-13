import os
import pandas as pd

filepath = "netflix1.csv"

if os.path.exists(filepath):
    
    #Load Data
    data = pd.read_csv(filepath)
    
    #Proper the title column
    data["title"] = data["title"].astype(str).str.strip().str.title()

    data = (
        data.sort_values("title").reset_index(drop=True)
        .drop_duplicates(subset=["title", "release_year"], keep="first").reset_index(drop=True)
        .dropna(subset=["title", "release_year"]).reset_index(drop=True)
    )

    #Save to new CSV
    data.to_csv("NetflixV1_Sorted.csv", index=False)
    print(data.head(10))

else:
    print(f"File '{filepath}' does not exist.")
