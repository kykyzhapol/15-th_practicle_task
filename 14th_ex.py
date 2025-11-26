def numbers(x: int) -> None:
    '''
    A recursive function that prints the digits of a natural number x in reverse order.
    Each digit is printed on a separate line.

    Base case:
    - Empty string (when all digits have been processed) returns None

    Recursive case:
    - Print the last digit and call function with remaining digits
    :param x: Natural number to process
    :return: None
    '''
    x = str(x)
    if x == '':
        return None
    print(x[-1])
    return numbers(x[:-1])


def main() -> None:
    '''
    Main function. User enters a natural number and sees its digits in reverse order.
    :return: None
    '''
    try:
        x = int(input('Enter a natural number -> '))

        if x <= 0:
            print('Error: Please enter a natural number (positive integer)')
            return

        print(f'Digits of {x} in reverse order:')
        numbers(x)

    except ValueError:
        print('Error: Please enter a valid integer')


if __name__ == '__main__':
    main()