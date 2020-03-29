# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author

# magic 8 ball
import random


def magic8ball():
    while True:
        print()

        usersQuestion = input(
            "Ask the magic 8 Ball a Question (press enter to quit): ")

        if usersQuestion == "":
            break

        randomAnswer = random.randrange(0, 8)

        if randomAnswer == 0:
            print("It is certain.")

        elif randomAnswer == 1:
            print("Absolutely!.")

        elif randomAnswer == 2:
            print("You may rely on it")

        elif randomAnswer == 3:
            print("Answer is fogy, ask again later.")

        elif randomAnswer == 4:
            print("Concentrate and ask again")

        elif randomAnswer == 5:
            print("Unsure at this point, try again.")

        elif randomAnswer == 6:
            print("No way, due!.")

        elif randomAnswer == 7:
            print("No, no, no, no, no.")


if __name__ == "__main__":
    magic8ball()
