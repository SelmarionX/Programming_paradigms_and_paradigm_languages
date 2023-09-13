"""Крестики нолики

Нумерация поля
   A   B   C
  ╔═══╤═══╤═══╗
1 ║ O │ 3 │ 6 ║
  ╟───┼───┼───╢
2 ║ 1 │ 4 │ 7 ║
  ╟───┼───┼───╢
3 ║ 2 │ 5 │ 8 ║
  ╚═══╧═══╧═══╝

'X' - Человек
'O' - Компьютер"""


class Board:
    STATE = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    FIELD_COORDS = (
        "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")
    LINES = (
            (0, 1, 2), (2, 5, 8), (0, 3, 6), (6, 7,
                                              8), (3, 4, 5), (1, 4, 7), (0, 4, 8),
            (2, 4, 6))
    CORNERS = (0, 2, 6, 8)
    OUT_CENTERS = (1, 3, 5, 7)

    def __init__(self):
        self.state = Board.STATE.copy()

    def set_board(self):
        return Board.STATE.copy()

    def check_win(self):

        def x_or_o():
            for line in self.LINES:
                if self.state[line[0]] == self.state[line[1]] == self.state[line[2]] in (
                        "X", "O"):
                    print(
                        "─" * 34, " '{0}' Победил! ".format(self.state[line[0]]), "─" * 33)
                    return self.state[line[0]]

        if self.state.count(" ") == 0 and not x_or_o():
            return "ничья"
        else:
            return x_or_o()

    def insert(self, coodrs, who):
        self.state[self.FIELD_COORDS.index(coodrs)] = who

    def check_field(self, coodrs):
        field = self.state[self.FIELD_COORDS.index(coodrs)]
        return field

    def empty_corner(self):
        corners = (0, 8, 2, 6)
        empty_cor = []
        for i in corners:
            if self.state[i] == " ":
                empty_cor.append(i)
        return empty_cor

    def current_state(self):
        return self.state

    def reset_board(self):
        self.state = self.set_board()
