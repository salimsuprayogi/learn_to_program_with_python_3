# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author


def myFunction(aVariable):  # use one parameter
    # aVariable = 20
    aVariable = aVariable + 1  # change a local (parameter) variable, 20 + 1
    return aVariable  # and return it (aVariable) , aVariable = 21


# main code starts here :
someVariable = 20  # param1
someVariable = myFunction(someVariable)  # myFunction(20)
print(someVariable)  # someVariable = 21
