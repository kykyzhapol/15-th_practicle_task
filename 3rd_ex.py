def progress(a1: float, r: float, n: int) -> float:
    '''
    Recursive function.
    Calculates the n-th term of a progression.
    :return:
    '''
    if n == 1:
        return a1
    return r + progress(a1, r, n - 1)


def main() -> None:
    '''
    Main function. Here user can enter request for function and see the result.
    :return:
    '''
    a1 = float(input('Enter first term (a1) ->'))
    r = float(input('Enter definition (r) ->'))
    n = int(input('Enter n ->'))
    print(progress(a1, r, n))


if __name__ == '__main__':
    main()
