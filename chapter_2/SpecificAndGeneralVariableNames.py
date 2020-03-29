# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author


def calculateAverage(param1, param2, param3, param4):  # use 4 parameter
    # add up the nimbers and dide by the number of numbers
    total = param1 + param2 + param3 + param4  # ex = 4 + 6.5 + 2.5 + -2
    average = total / 4.0  # 11 / 4.0 = 2.75
    return average  # hand back the answer to the caller, average = 2,75


# main code starts here :
# first
yardsOnRun1 = 4  # param1
yardsOnRun2 = 6.5  # param2
yardsOnRun3 = 2.5  # param3
yardsOnRun4 = -2  # param4

# calculateAverage(param1, param2, param3, param4)
averageYardsPerRun = calculateAverage(
    yardsOnRun1, yardsOnRun2, yardsOnRun3, yardsOnRun4)
# averageYarsPerRuns = average
print("Average yards per run is:", averageYardsPerRun)

# second
yardsOnRun1 = 0
yardsOnRun2 = 25.5
yardsOnRun3 = 0
yardsOnRun4 = 12

# calculateAverage(param1, param2, param3, param4)
averageYardsPerRun = calculateAverage(
    yardsOnRun1, yardsOnRun2, yardsOnRun3, yardsOnRun4)
print("Average yards per run is:", averageYardsPerRun)
