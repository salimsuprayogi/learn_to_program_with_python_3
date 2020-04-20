# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author

# determine if two numbers represent a square


def isSquare(lenght, width):
    # function to determine if lenght and width represent a square
    if lenght == width:
        itsASquare = True
    else:
        itsASquare = False
    return itsASquare


def printSquare(aLenght, aWidht):
    # Intermidiate function to determine that checks for a square and prints the result
    theResult = isSquare(aLenght, aWidht)
    if theResult:
        print(aLenght, "and", aWidht, "represent a square")
    else:
        print(aLenght, "and", aWidht, "do not represent a square")


# Test Case
printSquare(5, 5)

printSquare(7.5, 8.5)

# Get a user input convert to floats and call the function
userLength = input("Enter a lenght: ")
userLength = float(userLength)

userWidth = input("Enter a widht: ")
userWidth = float(userWidth)

# call function
printSquare(userLength, userWidth)
