# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author


# create header


def createHeader(fullName, gender):
    if gender == "m":
        title = "Mr. "
    elif gender == "f":
        title = "Ms. "
    else:   # not sure, could be male or female
        title = "Mr. or Ms. "
    header = "Dear " + title + "" + fullName + ","  # use concatenation
    return header


print(createHeader("Joe Smith", "m"))
print(createHeader("Susan Jones", "f"))
print(createHeader("Henry Jones", "m"))
print(createHeader("Chris Smith", "?"))
