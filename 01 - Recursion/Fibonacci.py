
def fibonacci(number):
    assert number >= 0 and int(number) == number, 'The number cannot be negative or non-integer..!'
    if number in [0,1]:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(7))
