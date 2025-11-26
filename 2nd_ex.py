def count(n: int) -> int:
    '''
    Recursive function.
    Calculates the number of digits of a natural number n.
    :param n:
    :return:
    '''
    n = str(n)
    if len(n) == 1:
        return 1
    return 1 + count(n[:-1])


def main() -> None:
    '''
    Main function. Here user can enter request for function and see the result.
    :return:
    '''
    n = int(input('Énter number n -->'))
    print(count(n))


if __name__ == '__main__':
    main()
