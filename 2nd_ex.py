def count(n):
    '''
    Напишите рекурсивную функцию count(n) для вычисления количества цифр натурального числа.
    :param n:
    :return:
    '''
    n = str(n)
    if len(n) == 1:
        return 1
    return 1 + count(n[:-1])

print(count(999555))