# Open all pngs in this folder and save them as 1.png,2.png ...
import os
import glob

joined_files = os.path.join("./", "*.png")
joined_list = glob.glob(joined_files)

for i, filename in enumerate(joined_list):
    if filename.endswith(".png"):
        os.rename(filename,str(i+1)+".png")
        print("Renamed "+filename+" to "+str(i+1)+".png")