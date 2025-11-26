def degree5(n: int) -> int:
    '''
    A recursive function.
    Calculates whether a function is a power of 5 and by what amount.
    If not, it returns -1.
    :return int:
    '''
    if n % 5 != 0:
        return -2
    if n == 1:
        return 0
    if n == 5:
        return 1
    return 1 + degree5(n // 5)


def main() -> None:
    '''
    Main function. Here user can enter request for function and see the result.
    :return:
    '''
    n = int(input('Enter n number ->'))
    print(degree5(n))


if __name__ == '__main__':
    main()
