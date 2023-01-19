import matplotlib as mp
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import array

# Loads the example seagull image (black and white)
exImg = mpimg.imread('seagull.JPG')

# Loads the example seagull image (color)
exColImg = mpimg.imread('ColorSeagul.JPG')

# Prints out the matrix representation of the picture 
# where every inner list represents a pixel with its RGB code
print(exColImg)
print(exColImg.shape)

# Image is graphed using pyplot
#exPlot = plt.imshow(exImg)
#plt.show()

# Storing the dimensions (m x n) of the image
m = exImg.shape[1]
n = exImg.shape[0]

mColor = exColImg.shape[1]
nColor = exColImg.shape[0]
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
# Note: Traditionally, you can multiply the matrix with a inversed version of the identity matrix
#       However, this will not work in this process as you cannot arithmetically multiply a list (the RGB codes) with numbers

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

# Returns the dimensions of the numpy array
def matrix_dimensions(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    return ((num_rows, num_cols))

# Returns True or False
def can_multiply_matrices(A, B):
  if (len(A[0]) == len(B)):
    return True
  else:
    return False

def matrix_product_entry(A,B,i,j):
  # First check to see if matrices can be mutliplied
  if(not(can_multiply_matrices(A,B))): return False

  entry = 0
  for k in range(matrix_dimensions(A)[1]):
    # Computing dot product of row i from matrix A with row j of matrix B
    # Subtracting 1 from i and j because Python's lists are 0-indexed
    entry += int(A[i-1][k]*B[k][j-1])
  return entry

def matrix_product(A,B):
  # First check to see if matrices can be multiplied
  if(not(can_multiply_matrices(A,B))): return False

  P = []
  for i in range(matrix_dimensions(A)[0]):
    R = []
    #print("i" + str(i))
    for j in range(matrix_dimensions(B)[1]):
      # Adding 1 to i and j because matrix_product_entry expects 1-indexed rows and columns!
      R.append(matrix_product_entry(A,B,i+1,j+1))
    P.append(R)
  return P

# Extract the RGB of each pixel
# Treat it as a matrix and matrix multiply
# Produces a 1x3 matrix 
# Turn that back into RGB code and store it into numpy

def photoEditor(imgMatrix, filterMatrix):
  # Find a way to matrix multiply and convert into numpy.ndarray
  output = []
  for i in range(len(imgMatrix)):
    row = []
    for j in range(len(imgMatrix[0])):

      #Extract original RGB code
      RGBCode = imgMatrix[i][j]

      #Turn into a matrix
      RGBMatrix = []
      for m in RGBCode:
        placeholderMatrix = []
        placeholderMatrix.append(m)
        RGBMatrix.append(placeholderMatrix)

      r = np.array(matrix_product(filterMatrix, RGBMatrix)).flatten()
      row.append(r)
      #print(r)
      #print(array.array('d',RGBCode))
    output.append(row)

  return np.array(output)




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Inputting stuff

input("""
      Seagull PhotoEditor \n
      Choose a photo to edit \n
      1. 
      """)


greyMatrix = [[1/3, 1/3, 1/3], [1/3, 1/3, 1/3], [1/3, 1/3, 1/3]]
redMatrix = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
#plt.imshow([[[255, 255, 255], [0, 0, 0]]])
plt.imshow(photoEditor(exColImg, redMatrix))
plt.show()


#print(transpose([[2,3,4],[5,2,3]]))

#plt.imshow(ImJPG_center)
#plt.show()