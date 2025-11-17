def mod_number(a, b):
    '''
    Напишите рекурсивную функцию mod_number(a,b)
    для нахождения остатка от деления натурального числа a на натуральное число b.
    :return:
    '''
    if a - b < b:
        return a - b
    return mod_number(a - b, b)


print(mod_number(2, 7))
