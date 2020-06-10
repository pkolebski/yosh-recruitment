'''
Hi!
Our team has prepared several assignments that are similar to our daily tasks as data scientists. Solve the assignments below. Present the results in the form of report. You can prepare the report in a text document, word document, jupyter notebook or in another way which is convenient for you. Send your code and report via e-mail.


Task 1

In dataset.csv file, there exists dataset_category column. Try to match the existing names to the one of: “clothes”, “underwear” or “other”. Once the matching is done, rename the entries accordingly. Also, consider how to make matching the "Niezidentyfikowano" category. Save the results in csv file after changes. Write in the report how many rows exist for each category.


Task 2

In the “types.csv” file there exist pairs of shoe types. Plot confusion/association matrix and interpret the results. Show the matrix and write your description in the short summary.


Task 3

In the folder 'Images' you can find an exemplary dataset with fashion images. All of the images are of the same size. Perform the following actions:
    
    1. Find the image resolution image and count the number of images in the dataset.
    2. Calculate mean and standard deviation of every channel (RGB) of the images in the dataset. Remember to divide pixel values by 255.0
    3. Resize all the images from folder 'images' to the 256x256 size and save them into 'images_256' folder.
    4. Create function to visualize n random images on the single plot and save the plot  into indicated directory.


You can only use imported packages,
Good luck!
'''


import os
import PIL
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def load_data(file_name):
    df = pd.read_csv(file_name)
    return df

df = load_data("dataset.csv")
pass