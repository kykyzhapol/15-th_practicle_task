def ten_to_bin(x: int) -> str:
    '''
    A recursive function that converts a natural number x from decimal
    to binary system. Returns the binary number as a string.

    Base cases:
    - x == 0 returns '0'
    - x == 1 returns '1'

    Recursive case:
    - Convert the quotient (x // 2) and append the remainder (x % 2)
    :param x: Natural number to convert (non-negative integer)
    :return: Binary representation of x as a string
    '''
    if x < 0:
        raise ValueError('Function works only with natural numbers')

    if x == 0:
        return '0'
    if x == 1:
        return '1'

    # Recursively process the quotient and append the remainder
    return ten_to_bin(x // 2) + str(x % 2)


def main() -> None:
    '''
    Main function. User enters a natural number and gets its binary representation.
    :return: None
    '''
    try:
        x = int(input('Enter a natural number -> '))

        if x < 0:
            print('Error: Please enter a natural number (non-negative integer)')
            return

        result = ten_to_bin(x)
        print(f'Binary representation of {x} is: {result}')

        # Verification with built-in function
        print(f'Verification with built-in bin(): {bin(x)[2:]}')

    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
