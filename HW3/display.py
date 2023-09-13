
class BoardPrinter:

    def __init__(self, board):
        self.board = board

    def display_board(self, who):

        if who == "X":
            message = "◀◀◀  ( X )  Это твой ход."
        elif who == "O":
            message = "◀◀◀  ( O )  Это мой ход."
        else:
            message = "◀◀◀  Это наша игровая доска"

        print("        A   B   C  ".format(self.board.state))
        print("      ╔═══╤═══╤═══╗")
        print("    1 ║ {0[0]:^{1}} │ {0[3]:^{1}} │ {0[6]:^{1}} ║".format(
            self.board.state, 1))
        print("      ╟───┼───┼───╢")
        print("    2 ║ {0[1]:^{1}} │ {0[4]:^{1}} │ {0[7]:^{1}} ║   {2}".format(
            self.board.state, 1, message))
        print("      ╟───┼───┼───╢")
        print("    3 ║ {0[2]:^{1}} │ {0[5]:^{1}} │ {0[8]:^{1}} ║".format(
            self.board.state, 1))
        print("      ╚═══╧═══╧═══╝")


class Messenger:
    def __init__(self, name):
        self.name = name

    def win_message(self, who):  
        if who == "X":
            print("Поздавляю {}! Ты смог победить меня\n"
                  "В следующий раз ты точно проиграешь !".format(self.name))

        elif who == "O":
            print(
                "Я выиграл! {}, ты проигравший. Дни человечества сочтены! ха-ха-ха\n".format(self.name))

        elif who == 'ничья':
            print("─" * 8, "Ничья!! {}, Серьёзно ?? Ты даже не смог победить обычный компьютер!".format(self.name), "─" * 8)
