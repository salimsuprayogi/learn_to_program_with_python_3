# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author


# Absolute Value Program


def absoluteValue(valueIn):
    # Function to detemine generate the absolute value
    if valueIn >= 0:
        valueOut = valueIn
    else:
        valueOut = -1 * valueIn
    return valueOut


# Test Case
result = absoluteValue(10.5)
print("The absolute value of 10.5 is", result)

print()

result = absoluteValue(-8)
print("The absolute value of -8 is", result)

print()

# Get user input and convert to a floating point number
userNumber = input("Enter a number: ")
userNumber = float(userNumber)

# Call the function with the user's number and print the answer
result = absoluteValue(userNumber)
print("The ansolute value of", userNumber, "is", result)
