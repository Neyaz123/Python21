import random
def game():
    """Запускает игру"""
    rand = random.randint(1, 5)
    x = int(input('Введите целое число от 1 до 5: '))
    if x != rand:
        print('Повторите еще раз')
    else:
        print('Победа')

if __name__ == "__main__":
    game()
