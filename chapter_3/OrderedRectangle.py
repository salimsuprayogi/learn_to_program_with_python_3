# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author

# Determine if the four side lengths represent a Rectangle or not:


def isRectangle(left, top, right, bottom):
    # Function is to determine if four side represent a Rectanglr
    # Is a rectangle if left is the sam as the right
    # and top is the sam as the buttom
    if left == right:
        if top == bottom:
            return True
    return False


def printRectangle(someLeft, someTop, someRight, someBottom):
    if isRectangle(someLeft, someTop, someRight, someBottom):
        print(someLeft, someTop, someRight,
              someBottom, "represent a rectangle")
    else:
        print(someLeft, someTop, someLeft, someBottom, "does not a rectangle")


# test case
printRectangle(5, 6, 5, 6)
printRectangle(5, 6, 5, 8)


# get user input and call the function
userLeft = input("Enter the left: ")
userLeft = int(userLeft)
userTop = input("Enter the top: ")
userTop = int(userTop)
userRight = input("Enter the right: ")
userRight = int(userRight)
userBottom = input("Enter the bottom: ")
userBottom = int(userBottom)

printRectangle(userLeft, userTop, userRight, userBottom)
