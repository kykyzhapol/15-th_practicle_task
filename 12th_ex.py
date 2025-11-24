def search(a: list, x: int):
    '''
    Написать рекурсивную функцию search(a,x), определяющую, имеется ли среди
    целочисленных значений списка a, число x.
    Если число x содержится в списке функция должна возвращать 1, иначе - 0.
    :return:
    '''
    try:
        if a[0] == x:
            return 1
        return search(a[1:], x)
    except IndexError:
        return 0

print(search([1,2,3,4,5], 5))