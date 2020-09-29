def func(s, n):
    """Возвращает строку в верхнем регистре если длина строки s больше n"""
    if len(s) > n:
        return s.upper()
    else:
        return s

if __name__ == "__main__":
    Str = str(input('Введите строку: '))
    n = int(input('Введите число n: '))
    print(func(Str, n))
