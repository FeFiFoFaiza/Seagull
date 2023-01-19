import matplotlib as mp
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Loads the example seagull image (black and white)
exImg = mpimg.imread('seagull.JPG')

# Loads the example seagull image (color)
exColImg = mpimg.imread('ColorSeagul.JPG')

# Used for userInput and as a placeholder
# By default it is the colored version of the image
matrixChoice = exColImg
m = 0
n = 0
globalCustomRow = []

# Prints out the matrix representation of the picture
# where every inner list represents a pixel with its RGB code
#print(exColImg)
#print(exColImg.shape)

# Image is graphed using pyplot
#exPlot = plt.imshow(exImg)
#plt.show()

# Storing the dimensions (m x n) of the image

def dimensions():
  m = matrixChoice.shape[1]
  n = matrixChoice.shape[0]
  print("""
      The dimensions of this image is: """ + str(m) + """ by """ + str(n))

# You cannot return anything as it will break the while 
# loop that controls the main interaction
# Hence the employment of a global customrow variable
def createCustomMatrixRow(row):
  customRowList = row.split(',')
  for i in range(len(3)):
    try:
      globalCustomRow[i] = int(customRowList[i])
    except IndexError:
      globalCustomRow[i] = 0


# Cropping the image
def crop(x1, x2, y1, y2):
  croppedImg = matrixChoice[x1:x2, y1:y2]
  return croppedImg

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

def inverse(matrix):
    return (255 - matrix)

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


greyMatrix = [[1/3, 1/3, 1/3], [1/3, 1/3, 1/3], [1/3, 1/3, 1/3]]
redMatrix = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
blueMatrix = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]
greenMatrix = [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
saturateMatrix = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
permutedMatrix = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
userMatrix = [[0.7, 0.15, 0.15], [0.15, 0.7, 0.15], [0.15, 0.15, 0.7]]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Inputting stuff

# Choosing which image
imageChoice = input("""
      Seagull PhotoEditor \n
      Choose a photo to edit \n
      1. Seagull Image (Colored)
      2. Seagull Image (Black and White) \n
      Your Choice: """)

try:
    if int(imageChoice) == 1:
      matrixChoice = exColImg
      dimensions()
    elif int(imageChoice) == 2:
      matrixChoice = exImg
      dimensions()
    else:
      print("You make me sad :(")

except ValueError:
    print('\nUse numbers you illiterate peasant. \nDefaulting to default.')

# Choosing how to edit the image
while (True): 
  editChoice = input("""\n
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      Please input what function you want to do: \n
      Your Answer: """)

  try: 
    if editChoice == "help":

      print ("""
      Make sure to keep everything lowercase\n
      about   --    Describes model and mission
      crop    --    Crops the image
      exit    --    Exits the program
      filter  --    Applies a filter onto the image
      flip    --    Reverses the image across its vertical or horizontal axis
      info    --    Provides the dimensions of the image
      rotate  --    Rotates the image 90 degrees clockwise or counterclockwise
      """)

    elif editChoice == "about":

      print("""
      This is a very basic and rudimentary photo editor that uses matplotlib and numpy arrays
      to manipulate and generate images. 
      Created by Aaron and Faiza for Semester 1 Linear Algebra Final Project
      """)

    elif editChoice == "crop":

      xrange = input("""
      Insert the range of included x-values
      ex.   10 250
            The cropped image will include pixels that have an x-coordinate between 10 and 250 inclusively
      x range: """)

      yrange = input("""
      Insert the range of included y-values
      y range: """)

      try:
        xrange = xrange.split(' ')
        yrange = yrange.split(' ')

        matrixChoice = crop(int(xrange[0]), int(xrange[1]), int(yrange[0]), int(yrange[1]))

      except:
        print('''\n
        Perhaps you made an error. READ and try again next time.''')

    elif editChoice == "exit":
      break
    elif editChoice == "filter":
      filterChoice = input("""
      You can choose to use one of the preset filters or make your own.
      1. Saturate
      2. Invert
      3. Greyscale
      4. Red-scale
      5. Blue-scale
      6. Green-scale
      7. User
      8. Permute
      9. Custom
      Your choice: """)

      try:
        if int(filterChoice) == 1:
          matrixChoice = photoEditor(matrixChoice, saturateMatrix)
        elif int(filterChoice) == 2:
          matrixChoice = inverse(matrixChoice)
        elif int(filterChoice) == 3:
          matrixChoice = photoEditor(matrixChoice, greyMatrix)
        elif int(filterChoice) == 4:
          matrixChoice = photoEditor(matrixChoice, redMatrix)
        elif int(filterChoice) == 5:
          matrixChoice = photoEditor(matrixChoice, blueMatrix)
        elif int(filterChoice) == 6:
          matrixChoice = photoEditor(matrixChoice, greenMatrix)
        elif int(filterChoice) == 7:
          matrixChoice = photoEditor(matrixChoice, userMatrix)
        elif int(filterChoice) == 8:
          matrixChoice = photoEditor(matrixChoice, permutedMatrix)
        elif int(filterChoice) == 9:
          
          customMatrix = []

          customRow = input("""
          Please enter the first row [separated by space]: 
          ex.   [1, 2, 3] -> 1,2,3\n        """)
          createCustomMatrixRow(customRow)
          customMatrix.append(globalCustomRow)
          customRow = input("And now the second: \n        ")
          createCustomMatrixRow(customRow)
          customMatrix.append(globalCustomRow)
          customRow = input("The third? \n        ")
          createCustomMatrixRow(customRow)
          customMatrix.append(globalCustomRow)

          matrixChoice = photoEditor(matrixChoice, customMatrix)
        else:
          print("""
          There were nine options....How do you mess that up?
          """)
      except:
        print('''\n
        Perhaps you made an error. READ and try again next time.''')

    elif editChoice == "flip":
      reflectAxis = input("""
      Do you want to flip horizontally or vertically?
      1. horizontally
      2. vertically
      Your choice: """)

      try:
        if int(reflectAxis) == 1:
          matrixChoice = horFlip(matrixChoice)
        elif int(reflectAxis) == 2:
          matrixChoice = vertFlip(matrixChoice)
      except:
        print('''\n
        Perhaps you made an error. READ and try again next time.''')

    elif editChoice == "info":
      dimensions()
    elif editChoice == "rotate":
      direction = input("""
      Which direction shall it rotate?
      1. clockwise
      2. counterclockwise
      """)

      try:
        if int(direction) == 1:
          matrixChoice = rotate90CW(matrixChoice)
        elif int(direction) == 2:
          matrixChoice = rotate90CCW(matrixChoice)
        else:
          print("""
          There's literally only two options. TWO.
          """)
      except:
        print('''\n
        Perhaps you made an error. READ and try again next time.''')

    
    plt.imshow(matrixChoice)
    plt.show()

  except:
    print('''
    \nMy guy, how can you mess this up???''')


#plt.imshow([[[255, 255, 255], [0, 0, 0]]])
#plt.imshow(photoEditor(exColImg, redMatrix))
#plt.show()


#print(transpose([[2,3,4],[5,2,3]]))

#plt.imshow(ImJPG_center)
#plt.show()
