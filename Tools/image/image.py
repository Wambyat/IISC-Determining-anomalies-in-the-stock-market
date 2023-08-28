from PIL import Image
import numpy as np

height = 20
weight = 1000
channel = 3
img_numpy = np.random.randint(0, 256, (height, weight, channel)).astype(np.uint8)
img = Image.fromarray(img_numpy, "RGB")
# make a numpy array of random numbers of shape (20,100,3) and type uint8

# Save the Numpy array as Image
image_filename = "opengenus_image.jpeg"
img.save(image_filename)
