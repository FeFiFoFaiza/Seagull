import matplotlib as mp
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Loads the example seagull image
exImg = mpimg.imread('seagull.JPG')

exColImg = mpimg.imread('ColorSeagul.JPG')

# Prints out the matrix representation of the picture 
# where every inner list represents a pixel with its RGB code
#print(exImg)

# Image is graphed using pyplot
#exPlot = plt.imshow(exImg)
#plt.show()

# Storing the dimensions (m x n) of the image
m = exImg.shape[1]
n = exImg.shape[0]
print("The dimensions of this image is: " + str(m) + " by " + str(n))

# Cropping the image 
ImJPG_center = exImg[100:m-100, 100:n-100]
    
# Rotates and flips
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    newMatrix = []
    for i in range(cols):
        newRow = []
        for j in range(rows):
            newRow.append(matrix[j][i])
        newMatrix.append(newRow)
    return newMatrix

# Reflects over the y-axis
# By reversing the order of elements in each row
def vertFlip(matrix):
    return [ row[::-1] for row in matrix ]

# Rotates it 90 deg clockwise
def rotate90CW(matrix):
    return vertFlip(transpose(matrix))

# Rotates it 90 deg counter clockwise
def rotate90CCW(matrix):
    return transpose(vertFlip(matrix))

# Reflects over the x-axis
# By rotating after transposing
def horFlip(matrix):
    return rotate90CCW(transpose(matrix))

def darken(matrix):
    return (matrix - 50)

def contrast(matrix):
    return (50 - matrix)


plt.imshow(contrast(exImg))
plt.show()

#print(transpose([[2,3,4],[5,2,3]]))

#plt.imshow(ImJPG_center)
#plt.show()