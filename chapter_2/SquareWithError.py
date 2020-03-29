# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author


def square(number):
    answer = number * number
    return  # note: this is an eror, does not return an answer


# main code starts here :
useNumber = input("Enter a number: ")
useNumber = float(useNumber)  # convert to float
numberSquarred = square(useNumber)  # call the function and save the result
print("The sequare of your number is", numberSquarred)  # numberSquarred = None
