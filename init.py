import matplotlib as mp
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Loads the example seagull image
exImg = mpimg.imread('seagull.JPG')

# Prints out the matrix representation of the picture 
# where every inner list represents a pixel with its RGB code
print(exImg)

# Image is graphed using pyplot
exPlot = plt.imshow(exImg)
plt.show()

# Storing the dimensions (m x n) of the image
m = exImg.shape[1]
n = exImg.shape[0]
print("The dimensions of this image is: " + str(m) + " by " + str(n))

# Cropping the image 
ImJPG_center = exImg[100:m-100, 100:n-100]

# Creating a function that will transpose matrices
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
transpose(exImg)

plt.imshow(ImJPG_center)
plt.show()