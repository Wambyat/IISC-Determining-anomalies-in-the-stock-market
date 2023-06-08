import pandas as pd
import numpy as np
from PIL import Image

#This convert a single value into 3 rgb values. We will normalise the value to be between 0 and 255.
# @params: value: the value to convert
#          m: the max value of the range
#          n: the min value of the range
# @return: a tuple of 3 values (r,g,b)

def convert_value_to_rgb(value,m,n):

    min_value = n
    max_value = m

    normalized_value = (value - min_value) / (max_value - min_value)
    rgb_value = int(normalized_value * 255)

    rgb = (rgb_value,rgb_value/2,rgb_value/3)

    return rgb

#convert a 1d dataframe to a array of int
df = np.random.exponential(2.5, 100)
n = min(df)
m = max(df)
# Convert each value to RGB
rgb_array = np.array([convert_value_to_rgb(value,m,n) for value in df])

#sort this np array in ascending order basing on first value
rgb_array = rgb_array[rgb_array[:,0].argsort()]

#reshaping so we can see a gradient.
rgb_array=rgb_array.reshape(50,2,3).astype(np.uint8)
print(rgb_array)

img = Image.fromarray(rgb_array,mode= "RGB")
image_filename = "new.jpeg"
img.save(image_filename)
