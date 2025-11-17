def pownum(a, n):
    '''
    для расчета степени n вещественного числа a (n — натуральное число)
    :param a:
    :param n:
    :return:
    '''
    if n == 1:
        return a
    return a * pownum(a, n-1)

print(pownum(2.5, 10))