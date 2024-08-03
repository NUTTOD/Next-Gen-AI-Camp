import os
from glob import glob
from PIL import Image

directory = "curriculum/Dataset/"
path = os.path.join(directory, "thai-handwritten-dataset", "*", "*")
all_file = glob(path)

idx = 100
image = Image.open(all_file[idx])
print(image.size)
image