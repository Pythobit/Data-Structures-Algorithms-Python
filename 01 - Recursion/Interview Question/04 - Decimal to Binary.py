

def decimalTobinary(number):
    assert int(number) == number, 'The number must be positive integer..!'
    if number == 0:
        return 0
    else:
        return number % 2 + 10 * decimalTobinary(int(number/2))

print(decimalTobinary(10))
