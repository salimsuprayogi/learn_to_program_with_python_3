# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author

# What to wear


def whatToWear(temperature):
    if temperature > 90:
        clothes = "swim suit"
    elif temperature > 70:
        clothes = "short"
    elif temperature > 50:
        clothes = "long pants"
    else:
        clothes = "thermal underwear and long pants"
    return "Put on " + clothes


print(whatToWear(100))
print(whatToWear(40))
print(whatToWear(71))
