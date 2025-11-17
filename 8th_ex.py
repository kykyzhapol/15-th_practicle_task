def fib(k):
    '''
    Напишите рекурсивную функцию fib(k) для вычисления k-го члена последовательности Фибоначчи
    '''
    if k <= 0:
        return 0
    if k == 1 or k == 2:
        return 1
    return fib(k - 1) + fib(k - 2)


print(fib(15))
