def square(number):
    answer = number * number
    return answer  # note: this is not an eror, return an answer


# main code starts here :
useNumber = input("Enter a number: ")
useNumber = float(useNumber)  # convert to float
numberSquarred = square(useNumber)  # call the function and save the result
print("The sequare of your number is", numberSquarred)  # numberSquarred = None
