def progress(a1, r, n):
    '''
    Даны первый член и разность арифметической прогрессии.
    Написать рекурсивную функцию progress(a1,r,n) для нахождения n-го члена прогрессии.
    :return:
    '''
    if n == 1:
        return a1
    return r + progress(a1, r, n-1)

print(progress(1, 10, 3))