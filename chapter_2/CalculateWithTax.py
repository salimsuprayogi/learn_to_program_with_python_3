# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author

TAX_RATE = .09  # 9 percent tax
COST_PER_SMALL_WIDGET = 5.00
COST_PER_LARGE_WIDGET = 8.00


def calculateCost(nSmallWidgets, nLargeWidgets):
    subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET) + \
        (nLargeWidgets * COST_PER_LARGE_WIDGET)
    taxAmount = subTotal * TAX_RATE
    totalCost = subTotal + taxAmount
    return totalCost


total1 = calculateCost(4, 3)
print("Total for first order is", total1)

total2 = calculateCost(12, 15)
print("Total for first order is", total2)
