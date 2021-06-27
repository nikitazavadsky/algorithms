"""It is a recursive implementation of Karatsuba multiplication
algorithm from 'Algorithms Illuminated Part 1 The Basics By Tim Roughgarden'"""


def get_half_power(number: int) -> int:
    """Returns half digit capacity of input number
       Example: 3456 -> 2
                123 -> 1"""
    return len(str(number)) // 2


def split_into_halves(number: int, half_digit_capacity: int) -> tuple:
    """Returns halves of certain number"""
    first_half = str(number)[:-half_digit_capacity]
    second_half = str(number)[-half_digit_capacity:]
    return int(first_half), int(second_half)


def karatsuba_multiplication(number_a, number_b):
    """Calculates result of numbers multiplication
    with optimized Karatsuba algorithm"""
    half_digit_capacity_a = get_half_power(number_a)
    half_digit_capacity_b = get_half_power(number_b)

    if half_digit_capacity_a == 1 or half_digit_capacity_b == 1:
        return number_a*number_b
    else:
        a, b = split_into_halves(number=number_a,
                                 half_digit_capacity=half_digit_capacity_a)
        c, d = split_into_halves(number=number_b,
                                 half_digit_capacity=half_digit_capacity_b)

        ac = karatsuba_multiplication(a, c)
        bd = karatsuba_multiplication(b, d)

        p = a + b
        q = c + d

        pq = karatsuba_multiplication(p, q)

        adbc = pq - ac - bd

        power = len(str(number_a))

        return int((10 ** power * ac) + (10 ** (power/2) * adbc) + bd)


print(karatsuba_multiplication(3456, 3456) == 3456 ** 2)
