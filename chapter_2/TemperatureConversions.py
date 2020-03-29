def F2C(nDegreesF):
    # rumus
    nDegreesF = (nDegreesF - 32) * (5.0 / 9.0)
    return nDegreesF


def C2F(nDegreesC):
    # rumus
    nDegreesC = (1.8 * nDegreesC) + 32
    return nDegreesC


# main code stars here:
# code ask the user to input values for conversasion:
# first
usersTempF = input("Enter a value of degrees Fahrenheit: ")  # input users
usersTempF = float(usersTempF)  # convert input usert to be float

# convert Fahrenheit to Celsius // call function F2C()
convertTempC = F2C(usersTempF)

print(usersTempF, "degrees Fahrenheit is:",
      convertTempC, "degrees Centigrade.")

# second
usersTempC = input("Enter a value of degrees Celcius: ")  # input users
usersTempC = float(usersTempC)  # convert input usert to be float

# convert Celsius to Fahrenheit // call function C2F()
convertTempF = C2F(usersTempC)

print(usersTempC, "degrees Centigrade is:",
      convertTempF, "degrees Fahrenheit.")
