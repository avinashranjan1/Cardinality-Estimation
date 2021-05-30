import pandas as pd
import os
df = pd.read_csv("/home/hp/Desktop/Thesis/sortedData/aka_title2.csv")

df.sort_values("keyword", inplace = True)
  
# dropping ALL duplicte values
df.drop_duplicates(subset ="keyword",
                     keep = False, inplace = True)      #keyword- Column name
  
print(df.to_string(index=False)) #df.to_string() can be used to print the entire data 
