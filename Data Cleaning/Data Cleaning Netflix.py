import os
import pandas as pd

filepath = "netflix1.csv"

if os.path.exists(filepath):
    
    #Load Data
    data = pd.read_csv(filepath)
    
    #Proper the title column
    data["title"] = data["title"].astype(str).str.strip().str.title()
    
    #Sort by title
    data = data.sort_values("title").reset_index(drop=True)

    #Remove dupes
    data = data.drop_duplicates(subset=["title", "release_year"], keep="first").reset_index(drop=True)

    #Remove NaN
    data = data.dropna(subset=["title", "release_year"]).reset_index(drop=True)
    #data = data.dropna.reset_index(drop=True)

    #data["director"] = data["director"].fillna("Unknown")
    #data["cast"] = data["cast"].fillna("Unknown")
    #data["rating"] = data["rating"].fillna("Not Rated")

    #Save to new CSV
    data.to_csv("NetflixV1_Sorted.csv", index=False)
    print(data.head(10))

else:
    print(f"File '{filepath}' does not exist.")
