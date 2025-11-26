def pownum(a: float, n: int) -> float:
    '''
    Recursive function to calculate the power of a number n
    :param a:
    :param n:
    :return:
    '''
    if n == 1:
        return a
    return a * pownum(a, n-1)


def main() -> None:
    '''
    Main function. Here user can enter request for function and see the result.
    :return:
    '''
    a = int(input('Enter power of number -->'))
    n = int(input('Enter number -->'))
    print(pownum(a, n))


if __name__ == '__main__':
    main()