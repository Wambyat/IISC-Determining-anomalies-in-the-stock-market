import pandas as pd
import numpy as np
from PIL import Image

def convert_value_to_rgb(value,m,n):
    min_value = n
    max_value = m

    normalized_value = (value - min_value) / (max_value - min_value)
    rgb_value = int(normalized_value * 255)

    rgb = (rgb_value, rgb_value, rgb_value)

    return rgb

#convert a 1d dataframe to a array of int
df = np.random.exponential(3.45, 10000)
n = min(df)
m = max(df)
# Convert each value to RGB
rgb_array = np.array([convert_value_to_rgb(value,m,n) for value in df])

#sort this np array in ascending order basing on first value
rgb_array = rgb_array[rgb_array[:,0].argsort()]

#drop the last 6 values
rgb_array=rgb_array.reshape(4,250,3).astype(np.uint8)
print(rgb_array)

img = Image.fromarray(rgb_array, "RGB")
image_filename = "new.jpeg"
img.save(image_filename)
