def count(a: int, b: int) -> int:
    '''
    A recursive function that calculates how many squares can be cut from a rectangle
    with sides a and b, where each time the largest possible square is cut.

    Base case:
    - If a == b, we can cut one final square

    Recursive cases:
    - If a < b, cut a square of side a from the rectangle
    - If a > b, cut a square of side b from the rectangle

    :param a: Length of the rectangle (natural number)
    :param b: Width of the rectangle (natural number)
    :return: Number of squares that can be cut
    '''
    if a == b:
        return 1
    if a < b:
        return 1 + count(a, b - a)
    return 1 + count(a - b, b)


def main() -> None:
    '''
    Main function. User enters rectangle dimensions and gets the number of squares.
    :return: None
    '''
    try:
        a = int(input('Enter length of rectangle (a) -> '))
        b = int(input('Enter width of rectangle (b) -> '))

        if a <= 0 or b <= 0:
            print('Error: Please enter natural numbers (positive integers)')
            return

        result = count(a, b)
        print(f'From a {a}x{b} rectangle, you can cut {result} squares')

    except ValueError:
        print('Error: Please enter valid integers')


if __name__ == '__main__':
    main()
