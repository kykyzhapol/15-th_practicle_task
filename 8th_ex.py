def fib(k: int) -> int:
    '''
    A recursive function that calculates the k-th Fibonacci number.
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    :param k: Position in Fibonacci sequence (non-negative integer)
    :return: k-th Fibonacci number
    '''
    if k <= 0:
        return 0
    if k == 1 or k == 2:
        return 1
    return fib(k - 1) + fib(k - 2)


def main() -> None:
    '''
    Main function. User enters a position and gets the corresponding Fibonacci number.
    :return: None
    '''
    try:
        k = int(input('Enter the position in Fibonacci sequence -> '))

        if k < 0:
            print('Error: Please enter a non-negative integer')
            return

        result = fib(k)
        print(f'The {k}th Fibonacci number is {result}')

    except ValueError:
        print('Error: Please enter a valid integer')


if __name__ == '__main__':
    main()
