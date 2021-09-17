
def SumofDigits(number):
    assert number >= 0 and int(number) == number, 'The number must be positive...!'
    if number == 0:
        return number
    else:
        return int(number % 10) + SumofDigits(int(number//10))

print(SumofDigits(1234))
