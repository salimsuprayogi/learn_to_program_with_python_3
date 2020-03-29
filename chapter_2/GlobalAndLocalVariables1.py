# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author

someVariable = 20


def myFunction():
    global someVariable  # tell python that you are using a global variable
    someVariable = someVariable + 1  # someVariable = 20


# main code starts here :
myFunction()  # call function
print(someVariable)  # 21 + 1
