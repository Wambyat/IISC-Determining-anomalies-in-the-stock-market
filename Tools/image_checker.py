import imageio
import pandas as pd
import glob
import os


def merge_text_files(file_list):
    h =[]
    w = []
    i = 0
    for images in file_list:
        i +=1
        print(i)

        img = imageio.imread(images)
        height, width, _ = img.shape
        h.append(height)
        w.append(width)
    
    return h,w


directory = "C:\\Users\\Anirudha\\Downloads\\imgs"

# creating the path string
joined_files = os.path.join(directory, "*.png")

# a list of all csv files in the directory
joined_list = glob.glob(joined_files)
# print(joined_list)
print("Join of dir done.")

h ,w =merge_text_files(joined_list)

print(set(h))
print(set(w))
print("Images unmerged!!!!!!!!!!!!!!!!!!!!!!!!!")
# this is creacking if pandas can handle the file
