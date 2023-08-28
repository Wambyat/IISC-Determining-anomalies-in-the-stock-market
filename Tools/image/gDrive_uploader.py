import requests
import json
import os
import glob
headers = {
    "Authorization":"Bearer <<put ya thing here>>"
}

joined_files = os.path.join("", "*.png")
joined_list = glob.glob(joined_files)

for i, filename in enumerate(joined_list):
    if filename.endswith(".png"):
        para = {"name":filename, "parents":["1m3B7PBBojhWNUMhWmCfiu5RCsUeFS6z4"]}
        files = { 'data':('metadata',json.dumps(para),'application/json;charset=UTF-8'), 'file':open(filename,'rb')}
        r = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",headers=headers, files=files)
        print("Uploaded "+filename)