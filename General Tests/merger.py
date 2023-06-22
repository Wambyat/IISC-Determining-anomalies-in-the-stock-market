# importing libraries
import pandas as pd
import glob
import os
  
# merging the files
joined_files = os.path.join("./data", "*.csv")
print(joined_files)
# A list of all joined files is returned
joined_list = glob.glob(joined_files)

# print(joined_list)
print("Join of dir done.")

def merge_text_files(file_list, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in file_list:
            with open(file_name, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')  # Add a new line after each file's content

# Example usage
file_list = joined_list
output_file = 'merged.csv'
merge_text_files(file_list, output_file)
print("Files merged!!!!!!!!!!!!!!!!!!!!!!!!!")