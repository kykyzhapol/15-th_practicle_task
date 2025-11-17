def combin(n, k):
    '''
    Рекурсивная функция для вычисления C(n, k) - комбинаторного сочетания
    как работает:
    C(5, 2) = C(4, 1) + C(4, 2)
    '''
    if k == 0 or k == n:
        return 1
    if k > n or k < 0:
        return 0
    return combin(n - 1, k - 1) + combin(n - 1, k)

print(combin(4, 3))
