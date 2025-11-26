from typing import List


def search(a: List[int], x: int) -> int:
    '''
    A recursive function that determines if integer x is present in list a.
    Returns 1 if x is found in the list, 0 otherwise.

    Base cases:
    - Empty list returns 0 (element not found)
    - First element matches x returns 1 (element found)

    Recursive case:
    - Search for x in the remaining elements of the list
    :param a: List of integers to search through
    :param x: Integer value to search for
    :return: 1 if x is found in a, 0 otherwise
    '''
    try:
        if a[0] == x:
            return 1
        return search(a[1:], x)
    except IndexError:
        return 0


def main() -> None:
    '''
    Main function. User enters a list of integers and a number to search for.
    :return: None
    '''
    try:
        input_str = input('Enter integers separated by spaces -> ')
        numbers = [int(x) for x in input_str.split()]

        x = int(input('Enter number to search for -> '))

        result = search(numbers, x)

        if result == 1:
            print(f'Number {x} was found in the list')
        else:
            print(f'Number {x} was not found in the list')

    except ValueError:
        print('Error: Please enter valid integers')


if __name__ == '__main__':
    main()
