def mod_number(a: int, b: int) -> int:
    '''
    Recursive function.
    Calculates the remainder when dividing a number a by a number b.
    :return:
    '''
    if a - b < b:
        return a - b
    return mod_number(a - b, b)


def main() -> None:
    '''
    Main function. Here user can enter request for function and see the result.
    :return:
    '''
    a = int(input('Enter first number (a) ->'))
    b = int(input('Enter second number (b) ->'))
    print(mod_number(a, b))


if __name__ == '__main__':
    main()
