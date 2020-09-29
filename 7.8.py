import random
print('Первый игрок бросает кубик')
a = random.randint(1, 6)
print(a)
print('Второй игрок бросает кубик')
b = random.randint(1, 6)
print(b)
if a > b:
    print('Победил первый игрок')
else:
    print('Победил второй игрок')
 
