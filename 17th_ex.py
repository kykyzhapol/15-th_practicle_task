def simple_num(n: int, d: int = 2) -> int:
    '''
    A recursive helper function that checks if a number is prime.
    Checks divisibility by divisors starting from d up to sqrt(n).
    
    Base cases:
    - If d² > n, no divisors found - number is prime (return 1)
    - If n is divisible by d, number is composite (return 0)
    
    Recursive case:
    - Check divisibility by the next divisor (d + 1)
    :param n: Number to check for primality
    :param d: Current divisor to test
    :return: 1 if prime, 0 if composite
    '''
    if d ** 2 > n:
        return 1
    if n % d == 0:
        return 0
    return simple_num(n, d + 1)


def function1(x: int) -> int:
    '''
    A logical function that determines if a given natural number x is prime.
    Returns 1 if the number is prime, 0 otherwise.
    
    Special cases:
    - Numbers less than 2 are not prime
    - 2 is the only even prime number
    
    :param x: Natural number to check
    :return: 1 if prime, 0 if composite
    '''
    if x < 2:
        return 0
    if x == 2:
        return 1
    if x % 2 == 0:
        return 0
    return simple_num(x)


def main() -> None:
    '''
    Main function. User enters a natural number and checks if it's prime.
    :return: None
    '''
    try:
        x = int(input('Enter a natural number -> '))
        
        if x < 1:
            print('Error: Please enter a natural number (positive integer)')
            return
            
        result = function1(x)
        
        if result == 1:
            print(f'Number {x} is prime')
        else:
            print(f'Number {x} is composite')
            
    except ValueError:
        print('Error: Please enter a valid integer')


if __name__ == '__main__':
    main()
