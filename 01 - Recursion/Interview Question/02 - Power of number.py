
def power(base, exponent):
    assert exponent >= 0 and int(base) == base, 'Base Must be a positive integer.'
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

print(power(2,4))
