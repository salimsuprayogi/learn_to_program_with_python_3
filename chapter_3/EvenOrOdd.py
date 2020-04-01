# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author


# Determine is a given integer is even or odd
# even = genap, odd = ganjil *author


def isEven(valueIn):
    # Function to determine if a number is even or odd
    reminder = valueIn % 2  # modulus / sisa bagi *author
    if reminder == 0:
        return True  # kembali menggunakan bolean benar *author
    else:
        return False  # kembali menggunakan bolean salah *author


def printEvenOrOdd(someValue):
    if isEven(someValue):  # call function *author
        print(someValue, "is even")
    else:
        print(someValue, "is odd")


# Test Case
printEvenOrOdd(10)
printEvenOrOdd(11)

# Get user input and convert to an integer
userNumber = input("Enter an integer: ")
userNumber = int(userNumber)

# Pass in the user's number
printEvenOrOdd(userNumber)
