def simmetr(s: str, i: int, j: int) -> bool:
    '''
    A logical function that determines if a substring of s from index i to j is symmetric (palindrome).
    Returns True if the substring is symmetric, False otherwise.

    Base cases:
    - If i > j, substring is empty or fully checked - return True
    - If characters at i and j don't match - return False

    Recursive case:
    - Check if the inner substring (i+1 to j-1) is symmetric
    :param s: String to check
    :param i: Starting index of the substring
    :param j: Ending index of the substring
    :return: True if substring is symmetric, False otherwise
    '''
    if i > j:
        return True
    if s[i] != s[j]:
        return False
    return simmetr(s, i + 1, j - 1)


def main() -> None:
    '''
    Main function. User enters a string and indices to check for symmetry.
    :return: None
    '''
    try:
        s = input('Enter a string -> ')
        i = int(input('Enter starting index -> '))
        j = int(input('Enter ending index -> '))

        if i < 0 or j >= len(s) or i > j:
            print('Error: Invalid indices')
            return

        result = simmetr(s, i, j)
        substring = s[i:j+1]

        if result:
            print(f'The substring "{substring}" is symmetric')
        else:
            print(f'The substring "{substring}" is not symmetric')

    except ValueError:
        print('Error: Please enter valid indices')
    except IndexError:
        print('Error: Indices out of string bounds')


if __name__ == '__main__':
    main()
