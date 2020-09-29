def bmi(mass, height):
    """Вычисляет ИМТ"""
    return (mass/((height/100)**2))

Mass, Height = map(float, input('Введите вес(в кг) и рост(в см) через пробел: ').split( ))
BMI = bmi(Mass, Height)

if BMI < 18.5:
    print('Ниже нормального веса')
elif 18.5 <= BMI <25:
    print('Нормальный вес')
elif 25 <= BMI < 30:
    print('Избыточный вес')
elif 30 <= BMI < 35:
    print('Ожирение 1 степени')
elif 35 <= BMI < 40:
    print('Ожирение 2 степени')
elif BMI >= 40:
    print('Ожирение 3 степени')
