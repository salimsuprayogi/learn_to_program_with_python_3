# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author


# determine if a number is negative, positive or zero


def negativePositiveZero(value):
    # function to determine negative, positive, or zero
    # return an appropriate string
    if value < 0.0:
        answer = "negative"
    elif value > 0.0:
        answer = "positive"
    else:  # not negative, not positive, must be zero
        answer = "zero"
    return answer


# Test Case
result = negativePositiveZero(-25.7)
print("-25.7 is", result)

result = negativePositiveZero(0.0)
print("0.0 is", result)

result = negativePositiveZero(123.45)
print("123.45 is", result)

# Get user input and call the function
userValue = input("Enter a number: ")
userValue = float(userValue)
userResult = negativePositiveZero(userValue)
print(userValue, "is", userResult)
