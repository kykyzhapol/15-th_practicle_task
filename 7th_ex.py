def nod(a, b):
    '''
    Напишите рекурсивную функцию nod(a,b),
    которая вычисляет наибольший общий делитель двух натуральных чисел a и b.
    :return:
    '''
    if a > b:
        return nod(a - b, b)
    if b > a:
        return nod(a, b - a)
    return a


print(nod(18, 12))
