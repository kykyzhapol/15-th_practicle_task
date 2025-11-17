def maxlist(a):
    '''
    Рекурсивная функция для вычисления максимального элемента списка целочисленных элементов
    '''
    if len(a) == 0:
        return None
    if len(a) == 1:
        return a[0]
    max_rest = maxlist(a[1:])
    return a[0] if a[0] > max_rest else max_rest


print(maxlist([10, 1, 3, 500]))
