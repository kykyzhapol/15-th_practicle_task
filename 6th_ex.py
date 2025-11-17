def degree5(n):
    import math as m
    '''
    Напишите рекурсивную функцию degree5(n), которая вычисляет,
    какой степенью числа 5 является натуральное число n.
    Если n не степень пяти, функция должна вернуть число -1.
    :return:
    '''
    if n % 5 != 0:
        return -2
    if n == 1:
        return 0
    if n == 5:
        return 1
    return 1 + degree5(n // 5)


print(degree5(125))
