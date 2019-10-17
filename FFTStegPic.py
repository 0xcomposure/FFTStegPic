import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_exists = False
path = ''

# Enter the path of the image and check if it exists
while not img_exists:
    path = input("Enter the path of the image: ")
    if (os.path.exists(path)):
        img_exists = True
    else:
        print("The image \"\033[1m"
              + str(path)
              + "\033[0m\" has not been found.")

# Load the image in grayscale mode
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Compute the two-dimensional FFT.
f = np.fft.fft2(img)
# Swap half-spaces for all axes
fshift = np.fft.fftshift(f)
# Calculate the logarithm
magnitude_spectrum = 20*np.log(np.abs(fshift))

# Display the result with matplotlib
plt.imshow(magnitude_spectrum, cmap='gray')
plt.show()
