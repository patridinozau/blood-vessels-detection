# Project title: Blood Vessels Detection in Retinal Fundus Images
# Team name: 3 stripes
# First stage of implementation: 10-15%

import skimage
import matplotlib.pyplot as plt
import sys
import tkinter as tk
from tkinter import filedialog
import numpy as np
import cv2
import os

# upload the retinal fundus image
root = tk.Tk()
root.withdraw()  # hide the main Tkinter window

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.tif *.tiff")],
)

# Exit if no file was selected
if not file_path:
    print("No file selected.")
    sys.exit()

# turn the original image into a grayscale image
ImgIn = skimage.io.imread(file_path)
if len(ImgIn.shape) == 3:
  ImgGray = np.uint8(skimage.color.rgb2gray(ImgIn)*255)
else:
  ImgGray = ImgIn









