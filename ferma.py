class Critter(object):
    def __init__(self, name, hunger=0, boredom = 0):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger +=1
        self.boredom += 1

    def talk(self):
        print('Привет! Меня зовут ', self.name, " . Сейчас я чувствую себя ", self.mood, "\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("Thanks!")
        self.hunger-=food
        if self.hunger<0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("OMG!")
        self.boredom-=fun
        if self.boredom<0:
            self.boredom = 0
        self.__pass_time()

    @property
    def mood(self):
        unhappiness = self.hunger +self.boredom
        if unhappiness <5:
            m = "прекрасно"
        elif 5<=unhappiness<=10:
            m = "норм"
        elif 10<unhappiness<=15:
            m = "пойдет"
        else:
            m = "ужасно"
        return m

def main():
    crit_name=input("Как назовете свою зверушку?")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print \
            ("""
            Моя зверюшка
            0 - Уйти от первой зверюшки 
            1 - Узнать о самочувствиии зверюшки
            2 - Покормить зверюшку
            3 - Поиграть со зверюшкой
            """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("Вы ушли ко второй зверюшке")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("Такого пункта нет ", choice)
    crit1_name = input("Как назовете свою зверушку?")
    crit1 = Critter(crit1_name)
    choice = None
    while choice != "0":
        print \
            ("""
                Моя зверюшка
                0 - Выйти из фермы 
                1 - Узнать о самочувствиии зверюшки
                2 - Покормить зверюшку
                3 - Поиграть со зверюшкой
                """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            crit1.talk()
        elif choice == "2":
            crit1.eat()
        elif choice == "3":
            crit1.play()
        else:
            print("Такого пункта нет ", choice)



main()

input("\n\nНажмите Enter, чтобы выйти") 
