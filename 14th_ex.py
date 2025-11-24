def numbers(x: int):
    '''
    Напишите рекурсивную функцию numbers(x), которая выводит
    на экран цифры натурального числа x в обратном порядке.
    Функция должна выводить по одной цифре в строке.
    :return:
    '''
    x = str(x)
    if x == '':
        return None
    print(x[-1])
    return numbers(x[:-1])


numbers(100)