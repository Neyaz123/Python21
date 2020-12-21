import math
def my_exp(x):
    """Вычисляет exp(x) методом разложения в ряд Тейлора"""
    eps = 0.001
    n = 0
    An = x
    expsum = 0
    while math.fabs(An) > eps :
            An = (math.pow(x, n))/(math.factorial(n))
            expsum += An
            n += 1
    return expsum, n

def my_sin(x):
    """Вычисляет sin(x) методом разложения в ряд Тейлора"""
    eps = 0.001
    n = 0
    An = x
    sinsum = 0
    while math.fabs(An) > eps :
        if n == 0:
            An = x/math.factorial(1)
            sinsum
            n += 1
        else:
            An = (math.pow(-1, n+1) * math.pow(x, 2*n-1))/math.factorial(2*n-1)
            sinsum += An
            n += 1
    return sinsum, n

def my_cos(x):
    """Вычисляет cos(x) методом разложения в ряд Тейлора"""
    eps = 0.001
    n = 0
    An = x
    cossum = 0
    while math.fabs(An) > eps :
            An = (math.pow(-1, n)*math.pow(x, 2*n))/math.factorial(2*n)
            cossum += An
            n += 1
    return cossum, n

print('Сумма и кол-во итераций для exp(x) равны соответственно: ', my_exp(int(input('Введите x для exp(x): '))))
print('Сумма и кол-во итераций для sin(x) равны соответственно: ', my_sin(int(input('Введите x для sin(x): '))))
print('Сумма и кол-во итераций для cos(x) равны соответственно: ', my_cos(int(input('Введите x для cos(x): '))))
