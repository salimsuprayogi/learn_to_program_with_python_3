# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author

# greeting creator


def greeting_plus():
    firstName = input("Please enter your first name: ")
    lasttName = input("Please enter your last name: ")
    fullName = firstName + " " + lasttName

    print("Hello", fullName, "I hope you are doing well. ")


def greeting_format():
    firstName = input("Please enter your first name: ")
    lasttName = input("Please enter your last name: ")
    fullName = f"{firstName} {lasttName}"

    print(f"Hello {fullName} I hope you are doing well. ")


def greeting_formating():
    firstName = input("Please enter your first name: ")
    lasttName = input("Please enter your last name: ")
    fullName = "{} {}".format(firstName, lasttName)

    print("Hello {} I hope you are doing well. ".format(fullName))


def greeting_format_persen():
    firstName = input("Please enter your first name: ")
    lasttName = input("Please enter your last name: ")
    fullName = "%s %s" % (firstName, lasttName)

    print("Hello %s I hope you are doing well. " % (fullName))


if __name__ == "__main__":
    # greeting_plus()
    # greeting_format()
    # greeting_formating()
    greeting_format_persen()
