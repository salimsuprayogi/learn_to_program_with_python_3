# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author

# determine if two numbers represent a square

# Function to determine if length and widht represent a aquare


def isSquare(length, widht):
    if length == widht:
        itsASquare = True
    else:
        itsASquare = False
    return itsASquare


# Test Cases
result = isSquare(5, 5)
if result:
    # true
    print("5 and 5 represent a aquare")
else:
    # false
    print("5 and 5 do not represent a square")

if isSquare(7.5, 8.5):
    print("7.5 and 8.5 represent a square")
else:
    print("7.5 and 8.5 do not represent a square")

# Get user input convert to float and call the function.
userLenght = input("Enter a lenght: ")
userLenght = float(userLenght)

userWidth = input("Enter a width: ")
userWidth = float(userWidth)

if isSquare(userLenght, userWidth):
    print(userLenght, "and", userWidth, "represent a square")
else:
    print(userLenght, "and", userWidth, "do not represent a square")
