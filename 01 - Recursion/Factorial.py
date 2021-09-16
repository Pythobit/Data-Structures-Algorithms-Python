
def factorial(number):
    if number in [0, 1]:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))
