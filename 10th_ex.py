from typing import List, Optional


def maxlist(a: List[int]) -> Optional[int]:
    '''
    A recursive function that finds the maximum element in a list of integers.
    Uses divide and conquer approach by comparing the first element
    with the maximum of the rest of the list.

    Base cases:
    - Empty list returns None
    - Single element list returns that element

    Recursive case:
    - Compare first element with maximum of remaining elements
    :param a: List of integers
    :return: Maximum element in the list, or None if list is empty
    '''
    if len(a) == 0:
        return None
    if len(a) == 1:
        return a[0]
    max_rest = maxlist(a[1:])
    return a[0] if a[0] > max_rest else max_rest


def main() -> None:
    '''
    Main function. User enters a list of integers and gets the maximum value.
    :return: None
    '''
    try:
        input_str = input('Enter integers separated by spaces -> ')
        numbers = [int(x) for x in input_str.split()]

        result = maxlist(numbers)

        if result is None:
            print('The list is empty')
        else:
            print(f'The maximum value in the list is: {result}')

    except ValueError:
        print('Error: Please enter valid integers separated by spaces')


if __name__ == '__main__':
    main()


def maxlist(a: List[int]) -> Optional[int]:
    '''
    A recursive function that finds the maximum element in a list of integers.
    Uses divide and conquer approach by comparing the first element
    with the maximum of the rest of the list.

    Base cases:
    - Empty list returns None
    - Single element list returns that element

    Recursive case:
    - Compare first element with maximum of remaining elements
    :param a: List of integers
    :return: Maximum element in the list, or None if list is empty
    '''
    if len(a) == 0:
        return None
    if len(a) == 1:
        return a[0]
    max_rest = maxlist(a[1:])
    return a[0] if a[0] > max_rest else max_rest


def main() -> None:
    '''
    Main function. User enters a list of integers and gets the maximum value.
    :return: None
    '''
    try:
        input_str = input('Enter integers separated by spaces -> ')
        numbers = [int(x) for x in input_str.split()]

        result = maxlist(numbers)

        if result is None:
            print('The list is empty')
        else:
            print(f'The maximum value in the list is: {result}')

    except ValueError:
        print('Error: Please enter valid integers separated by spaces')


if __name__ == '__main__':
    main()