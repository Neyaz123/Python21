def parity(number):
    """Определяет четность введенного числа"""
    if number%2 == 0:
        print('Число четное')
    else:
        print('Число нечетное')
Number = int(input('Введите целое число: '))
parity(Number)
