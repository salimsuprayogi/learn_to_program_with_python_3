def separateRuns():
    print("******************")
    print(someUndeFinedVariable)  # will cause a run time error
    # nameError
    # someUndeFinedVariable is not defined
    print()  # blank line


def getGroceries():
    print("milk")
    print("flour")
    print("sugar")
    separateRuns()  # call another function


# main code start here:
getGroceries()
