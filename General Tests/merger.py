# importing libraries
import pandas as pd
import glob
import os

#This function takes a list of file names and merges them into one output file.
# @param file_list: A list of file names to be merged
# @param output_file: The output file name
# @return: None
def merge_text_files(file_list, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in file_list:
            with open(file_name, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')  # Add a new line after each file's content


# creating the path string
joined_files = os.path.join("./data", "*.csv")

# a list of all csv files in the directory
joined_list = glob.glob(joined_files)
# print(joined_list)
print("Join of dir done.")

output_file = 'merged.csv'
merge_text_files(joined_list, output_file)

# print("Files merged!!!!!!!!!!!!!!!!!!!!!!!!!")
# this is creacking if pandas can handle the file
df = pd.read_csv(output_file)
print(df.head())
print(df.shape)