
def factorial(number):
    assert number >= 0 and int(number) == number, 'The number must be positive only..!'
    if number in [0, 1]:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))
