import math
def square(a, b, c):
    """Вычисляет площадь треугольника по формуле Герона"""
    p = ((a+b+c)/2)
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S

if __name__ == "__main__":
    a1, b1, c1 = map(float, input().split( ))
    square(a1, b1, c1)
