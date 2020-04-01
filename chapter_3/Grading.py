# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author


# Convert a number score to a letter grade
# menentukan kelas berdasarkan nilai siswa *author


def letterGrade(score):
    if score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"  # fall through or default case
    return letter


grade1 = letterGrade(75)
print(grade1)
grade2 = letterGrade(82)
print(grade2)
print(letterGrade(95))  # call and print in one statement
