# importing libraries
import pandas as pd
import glob
import os
  
# merging the files
joined_files = os.path.join("./data", "*.csv")
print(joined_files)
# A list of all joined files is returned
joined_list = glob.glob(joined_files)

print(joined_list)
  
# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df)