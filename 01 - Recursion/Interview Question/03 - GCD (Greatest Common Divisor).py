"""
GCD (Greatest common divisor) - is the largest positive integer that divides the numbers without a remainder.
"""


def gcd(num_1, num_2):
    assert int(num_1) == num_1 and int(num_2) == num_2, 'The numbers must be integers only.'
    if num_1 < 0:
        num_1 = -1 * num_1
    if num_2 < 0:
        num_2 = -1 * num_2
    if num_2 == 0:
        return num_1
    else:
        return gcd(num_2, num_1 % num_2)


print(gcd(48, -18))
