class Board:
    def __init__(self):
        self.a1 = ' '
        self.a2 = ' '
        self.a3 = ' '
        self.b1 = ' '
        self.b2 = ' '
        self.b3 = ' '
        self.c1 = ' '
        self.c2 = ' '
        self.c3 = ' '

    def __str__(self):
            return ('    1   2   3\n'
                '  _____________\n'+
               'A | '+ str(self.a1) +' |'+ ' '+ str(self.a2) +' |'+ ' '+ str(self.a3) +' |\n'+
                '  -------------\n'+
               'B | '+ str(self.b1) +' |'+ ' '+ str(self.b2) +' |'+ ' '+ str(self.b3) +' |\n'+
                '  -------------\n'+
               'C | '+ str(self.c1) +' |'+ ' '+ str(self.c2) +' |'+ ' '+ str(self.c3) +' |\n'+
               '  -------------\n')

    def add_c(self,pos):
        if pos == 'A1':
            self.a1 = Cross()
        elif pos == 'A2':
            self.a2 = Cross()
        elif pos == 'A3':
            self.a3 = Cross()
        elif pos == 'B1':
            self.b1 = Cross()
        elif pos == 'B2':
            self.b2 = Cross()
        elif pos == 'B3':
            self.b3 = Cross()
        elif pos == 'C1':
            self.c1 = Cross()
        elif pos == 'C2':
            self.c2 = Cross()
        elif pos == 'C3':
            self.c3 = Cross()

    def add_z(self, pos):
        if pos == 'A1':
            self.a1 = Zero()
        elif pos == 'A2':
            self.a2 = Zero()
        elif pos == 'A3':
            self.a3 = Zero()
        elif pos == 'B1':
            self.b1 = Zero()
        elif pos == 'B2':
            self.b2 = Zero()
        elif pos == 'B3':
            self.b3 = Zero()
        elif pos == 'C1':
            self.c1 = Zero()
        elif pos == 'C2':
            self.c2 = Zero()
        elif pos == 'C3':
            self.c3 = Zero()

    def nec(self):
        if self.a1 != ' ' and self.a2 != ' ' and self.a3 != ' ' and self.b1 != ' ' and self.b2 != ' ' and self.b3 != ' ' and self.c1 != ' ' and self.c2 != ' ' and self.c3 != ' ':
            return True
        else:
            return False

class Cross:
    def __str__(self):
        return ("\033[31m{}".format("X")+"\033[30m")

class Zero:
    def __str__(self):
        return ("\033[34m{}".format('O')+"\033[30m")

class Player:
    def __init__(self,name,sign):
        self.name = name
        self.a1 = ' '
        self.a2 = ' '
        self.a3 = ' '
        self.b1 = ' '
        self.b2 = ' '
        self.b3 = ' '
        self.c1 = ' '
        self.c2 = ' '
        self.c3 = ' '
        self.sign = sign

    def move(self,pos,board):
        if pos == 'A1':
            self.a1 = 1
            if self.sign == 'X':
                board.add_c(pos)
            else:
                board.add_z(pos)
        elif pos == 'A2':
            self.a2 = 1
            if self.sign == 'X':
                board.add_c(pos)
            else:
                board.add_z(pos)
        elif pos == 'A3':
            self.a3 = 1
            if self.sign == 'X':
                board.add_c(pos)
            else:
                board.add_z(pos)
        elif pos == 'B1':
            self.b1 = 1
            if self.sign == 'X':
                board.add_c(pos)
            else:
                board.add_z(pos)
        elif pos == 'B2':
            self.b2 = 1
            if self.sign == 'X':
                board.add_c(pos)
            else:
                board.add_z(pos)
        elif pos == 'B3':
            self.b3 = 1
            if self.sign == 'X':
                board.add_c(pos)
            else:
                board.add_z(pos)
        elif pos == 'C1':
            self.c1 = 1
            if self.sign == 'X':
                board.add_c(pos)
            else:
                board.add_z(pos)
        elif pos == 'C2':
            self.c2 = 1
            if self.sign == 'X':
                board.add_c(pos)
            else:
                board.add_z(pos)
        elif pos == 'C3':
            self.c3 = 1
            if self.sign == 'X':
                board.add_c(pos)
            else:
                board.add_z(pos)

    def check(self):
        if (self.a1 == 1 and self.a2 == 1 and self.a3 == 1 ):
            return True
        elif (self.b1 == 1 and self.b2 == 1 and self.b3 == 1 ):
            return True
        elif (self.c1 == 1 and self.c2 == 1 and self.c3 == 1 ):
            return True
        elif (self.a1 == 1 and self.b1 == 1 and self.c1 == 1 ):
            return True
        elif (self.a2 == 1 and self.b2 == 1 and self.c2 == 1 ):
            return True
        elif (self.a3 == 1 and self.b3 == 1 and self.c3 == 1 ):
            return True
        elif (self.a1 == 1 and self.b2 == 1 and self.c3 == 1 ):
            return True
        elif (self.a3 == 1 and self.b2 == 1 and self.c1 == 1 ):
            return True
        else:
            return False


def help():
    print("Игрок должен ввести позицию в виде СТРОКАстобец.Пример: A1. В данном случае заполнится 1 срока,1 столбец.")

def start():
    board = Board()
    a = " "
    b = " "
    while a == '--help' or a == " ":
        if a == '--help':
            help()
        print('Введите имя 1 игрока')
        a = input()
    while b == '--help' or b == " ":
        if b == '--help':
            help()
        print('Введите имя 2 игрока')
        b = input()
    player1 = Player(a,"X")
    player2 = Player(b,"O")
    print(board)
    while (not player1.check() and not player2.check()):
        print('Ходит '+player1.name)
        h = input()
        player1.move(h,board)
        print(board)
        if player1.check():
            print(""+player1.name+" победил")
            break
        if board.nec():
            print("Ничья")
            break
        print('Ходит ' + player2.name)
        h = input()
        player2.move(h, board)
        print(board)
        if player2.check():
            print("" + player2.name + " победил")
            break
        if board.nec():
            print("Ничья")
            break


start()
