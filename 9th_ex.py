def combin(n: int, k: int) -> int:
    '''
    A recursive function that calculates C(n, k) - combinatorial combination
    (binomial coefficient) using the recurrence relation:
    C(n, k) = C(n-1, k-1) + C(n-1, k)

    Base cases:
    - C(n, 0) = C(n, n) = 1
    - C(n, k) = 0 if k > n or k < 0

    Example: C(5, 2) = C(4, 1) + C(4, 2)
    :param n: Total number of elements
    :param k: Number of elements to choose
    :return: Number of ways to choose k elements from n elements
    '''
    if k == 0 or k == n:
        return 1
    if k > n or k < 0:
        return 0
    return combin(n - 1, k - 1) + combin(n - 1, k)


def main() -> None:
    '''
    Main function. User enters n and k values to calculate binomial coefficient.
    :return: None
    '''
    try:
        n = int(input('Enter total number of elements (n) -> '))
        k = int(input('Enter number of elements to choose (k) -> '))

        if n < 0:
            print('Error: n must be non-negative')
            return

        result = combin(n, k)
        print(f'C({n}, {k}) = {result}')

    except ValueError:
        print('Error: Please enter valid integers')


if __name__ == '__main__':
    main()
