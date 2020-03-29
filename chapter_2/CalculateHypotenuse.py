# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author

# mencari panjang hypotenuse


def calculate_hypotenus(side1, side2):
    side1 = float(side1)
    side2 = float(side2)
    hypot = ((side1 * 2) + (side2 ** 2)) ** 0.5
    return hypot


firstTriangelSide1 = input("Enter side 1: ")
firstTriangelSide2 = input("Enter side 2: ")
hypot1 = calculate_hypotenus(firstTriangelSide1, firstTriangelSide2)

print()

firstTriangelSide1 = input("Enter side 1: ")
firstTriangelSide2 = input("Enter side 2: ")
hypot2 = calculate_hypotenus(firstTriangelSide1, firstTriangelSide2)

print()

print("The hypotenus of the first trangle is: ", hypot1)
print("The hypotenus of the first trangle is: ", hypot2)
