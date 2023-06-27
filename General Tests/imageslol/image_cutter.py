import imageio
import pandas as pd
import glob
import os


def merge_text_files(file_list):
    for images in file_list:
        img = imageio.imread(images)
        height, width, _ = img.shape

        # Cut the image in half
        width_cutoff = width // 2
        s1 = img[:, :width_cutoff]
        s2 = img[:, width_cutoff:]

        # Save each half
        imageio.imsave(images.replace(".png","")+"_1.png", s1)
        imageio.imsave(images.replace(".png","")+"_2.png", s2)
        


directory = "C:\\Users\\Anirudha\\Downloads\\images"

# creating the path string
joined_files = os.path.join(directory, "*.png")

# a list of all csv files in the directory
joined_list = glob.glob(joined_files)
# print(joined_list)
print("Join of dir done.")

merge_text_files(joined_list)

print("Images unmerged!!!!!!!!!!!!!!!!!!!!!!!!!")
# this is creacking if pandas can handle the file
