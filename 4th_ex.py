def sum_progress(a1, r, n):
    '''
    Даны первый член и разность арифметической прогрессии.
    Написать рекурсивную функцию sum_progress(a1,r,n) для нахождения суммы n членов прогрессии.
    :return:
    '''
    if n == 1:
        return a1
    return (a1 + (n - 1) * r) + sum_progress(a1, r, n-1)


print(sum_progress(1, 2, 3))