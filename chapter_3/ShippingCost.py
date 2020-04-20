# I say thank you Irv Kalb
# Allow me to learn to use your source code

# Source Code   : https://github.com/Apress/learn-to-prog-w-python-3
# By            : Source code for 'Learn to Program with Python 3' by Irv Kalb

# Author        : Salim Suprayogi
# Rewrite the code to learn and understand the code
# Menulis ulang kode untuk belajar, memahami dan membiasakan diri dengan bahasa pemrograman
# Sebagian comment di buat oleh Author

NOT_YET = "We don't ship there yet"


def calculateShipping(country, nWidgets):
    # Function to determine shipping cost, based on country and quantity

    if (country == "USA") or (country == "US") or (country == "United States"):
        if nWidgets < 50:
            shippingCost = 6.25
        elif nWidgets < 100:
            shippingCost = 9.50
        elif nWidgets < 150:
            shippingCost = 12.75
        else:
            shippingCost = 15.00

    elif country == "canada":
        if nWidgets < 50:
            shippingCost = 8.25
        elif nWidgets < 100:
            shippingCost = 12.50
        elif nWidgets < 150:
            shippingCost = 18.75
        else:
            shippingCost = 25.00

    else:
        shippingCost = NOT_YET  # special value to say that we don't ship to this country

    return shippingCost


# get user input then call the above function
userWidget = input("How many widgets are you buying ? ")
userWidget = int(userWidget)  # convert to integer

userCountry = input("What country are you shipping to ? ")

# call the function to see much it will cost to ship
amountForShipping = calculateShipping(userCountry, userWidget)
if amountForShipping == NOT_YET:
    print("Sorry, we don't ship to", userCountry)
else:
    print("It will cost $", amountForShipping, "to ship your package")
