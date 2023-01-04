## 1. Importing the libraries needed
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# ## 2. Opening and reading the file as an array
file_path = 'C:\\Users\\AU\\Documents\\python\\'      # Edit file path
img_array = mpimg.imread(file_path + "input_img.png") # Edit file name

print ("The M x N x 3 array is as follows:")
print(img_array)

# plt.imshow(img_array, cmap='gray') # Uncomment to verify if it displays correctly
# plt.show()

## 3. Converting the file to grayscale
# Each pixel contains a value each for R, G and B channels
# There are M rows and N columns of pixels
# Hence the array is M x N x 3. To convert it to an M x N matrix we take the average of R, G and B values for each pixel
gray_img = np.mean(img_array, axis=2) # Averaging
print(gray_img)

plt.imshow(gray_img, cmap='gray') # Uncomment to verify if it displays correctly
plt.show()

## 4. Saving the grayscale image as a CSV file
np.savetxt(file_path+"img_matrix.csv", gray_img, delimiter=",")

### *** ~~~ *** ###

# ## 5. Reading the processed (after convolution) CSV file as an array
# UNCOMMENT AS NEEDED

# processed_img = np.genfromtxt(file_path + "processed_img_matrix.csv", delimiter=",")
# print(processed_img)

# ## 6. Displaying processed matrix as an image

# plt.imshow(processed_img, cmap="gray")
# plt.show()

# ## 7. Saving the processed image into a file

# mpimg.imsave(file_path+"processed_img.png", processed_img, cmap="gray")
