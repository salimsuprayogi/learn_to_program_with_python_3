# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author


def calculateAverage(param1, param2, param3, param4):
    # Jumlahkan angka, bagi dengan jumlah angka
    total = param1 + param2 + param3 + param4
    average = total / 4.0
    return average


yardsOnRun1 = 4
yardsOnRun2 = 6.5
yardsOnRun3 = 2.5
yardsOnRun4 = -2

averageYardsPerRun = calculateAverage(
    yardsOnRun1, yardsOnRun2, yardsOnRun3, yardsOnRun4)
print("Average yards per run is: ", averageYardsPerRun)


yardsOnRun1 = 0
yardsOnRun2 = 25.5
yardsOnRun3 = 0
yardsOnRun4 = 12

averageYardsPerRun = calculateAverage(
    yardsOnRun1, yardsOnRun2, yardsOnRun3, yardsOnRun4)
print("Average yards per run is: ", averageYardsPerRun)
