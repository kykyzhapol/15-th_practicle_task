def nod(a: int, b: int) -> int:
    '''
    A recursive function that calculates the greatest common divisor (GCD)
    of two natural numbers using the Euclidean algorithm.
    :param a: First natural number
    :param b: Second natural number
    :return: Greatest common divisor of a and b
    '''
    if a > b:
        return nod(a - b, b)
    if b > a:
        return nod(a, b - a)
    return a


def main() -> None:
    '''
    Main function. User enters two numbers and gets their GCD.
    :return: None
    '''
    try:
        a = int(input('Enter first number -> '))
        b = int(input('Enter second number -> '))

        if a <= 0 or b <= 0:
            print('Error: Please enter natural numbers (positive integers)')
            return

        result = nod(a, b)
        print(f'The greatest common divisor of {a} and {b} is {result}')

    except ValueError:
        print('Error: Please enter valid integers')


if __name__ == '__main__':
    main()