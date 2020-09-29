def maxnumber(number1, number2):
    """Определяет какое из двух введенных чисел больше"""
    if number1 > number2:
        return number1
    else:
        return number2

Number1, Number2 = map(int, input('Введите два целых числа через пробел: ').split( ))
print('Большее из введеных чисел: ', maxnumber(Number1, Number2))
