import shutil
import os
import glob

source_dir = '/path/to/source_folder'
target_dir = '/path/to/dest_folder'

joined_files = os.path.join("./", "*.png")
joined_list = glob.glob(joined_files)
target_dir = os.path.join("./", "img10k/")
i = 0
for i, filename in enumerate(joined_list):
    if i>10000 and i<20000:
        target_dir = os.path.join("./", "img20k/")
    elif i>20000 and i<30000:
        target_dir = os.path.join("./", "img30k/")
    elif i>30000 and i<40000:
        target_dir = os.path.join("./", "img40k/")
    elif i>40000 and i<50000:
        target_dir = os.path.join("./", "img50k/")
    elif i>50000 and i<60000:
        target_dir = os.path.join("./", "img60k/")
    elif i>60000 and i<70000:
        target_dir = os.path.join("./", "img70k/")
    elif i>70000 and i<80000:
        target_dir = os.path.join("./", "img80k/")
    elif i>80000:
        target_dir = os.path.join("./", "img90k/")
    print("Moving "+filename+" to "+target_dir)
    shutil.move(filename, target_dir)
