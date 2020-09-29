import math
def func(x):
    """Вычисляет заданное выражение по введённому x"""
    return (math.sqrt(1 - (math.sin(x)**2)))

if __name__ == "__main__":
    number = float(input('Введите число x: '))
    print(math.sqrt(1 - (math.sin(number)**2)))
