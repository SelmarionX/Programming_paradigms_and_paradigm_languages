from random import choice
from collections import Counter

class Response:

    def __init__(self, board):
        self.board = board
        self.lines = board.LINES
        self.state = board.state
        self.corners = board.CORNERS
        self.out_centers = board.OUT_CENTERS

    def corner_put(self,
                   empty_cor):  
        if self.state[4] in ("O", "X"):  
            # print(444)
            for diagonal in ([0, 8], [2, 6]):  
                for i in range(2):
                    if self.state[diagonal[i]] in ("O", "X"):  
                        self.state[diagonal[i - 1]] = "O"
                        # print(3)
                        return
        self.state[choice(empty_cor)] = "O"  
        # print(4)
        return

    def response(self):  

        o_move = self.potential_win("O")  

        
        if type(o_move) == int:  
            self.state[o_move] = "O"
            return

        
        empty_cor = self.board.empty_corner()  
        x_move = self.potential_win("X") 
        move_X_no = self.state.count("X")  
        move_O_no = self.state.count("O")  

        if move_X_no >= 2 and type(x_move) == int:  
            self.state[x_move] = "O"
            # print(1)
            return

        elif move_X_no == 1 and move_O_no == 0 and self.state[4] == " ":  
            self.state[4] = "O"  
            # print(2)
            return

        
        elif move_X_no == 2 and move_O_no == 1 and self.state[4] == "O" and \
            "X" in (self.state[self.corners[0]], self.state[self.corners[1]],
                    self.state[self.corners[2]], self.state[self.corners[3]]):
            x_in_center = False  
            line = ()
            for line in self.lines[0:3]:  
                if self.state[line[1]] == "X":  
                    x_in_center = line
                    break

            if x_in_center:  
                self.two_lines("O", 0)  
            else:
                self.state[line[1]] = "O"  
                return

        elif move_X_no <= 1 and empty_cor:  
            # print(555)
            self.corner_put(empty_cor)
            return

        elif self.state.count(" ") == 1: 
            self.state[self.state.index(" ")] = "O"
            # print(5)
            return

        elif self.state.count(" ") == 2:  
            self.state[self.state.index(" ")] = "O"
            # print(6)
            return

        else:
            two = self.two_lines("O", 0)
            # print(7777, two)
            if not two:
                self.state[self.state.index(" ")] = "O"
                # print(8)
            return

    def two_lines(self, who, level):  

        empty = []  
        level += 1  
        for line in self.lines:  
            line_values = [self.state[line[0]], self.state[line[1]], self.state[line[2]]]
            if line_values.count(who) == 1 and line_values.count(" ") == 2:  
                for i in line:
                    if self.state[i] == " ":  
                        empty.append(i)
        empty_indexes = Counter(empty)  
        print(level, empty_indexes)
        if not all(val == 1 for val in empty_indexes.values()):  
            self.state[(empty_indexes.most_common(1)[0][0])] = "O"  
            # print("222")
            checked = True
            return checked  
        elif level == 2:  
            # print("111")
            checked = False
            return checked  
        # print("рекурсия")
        return self.two_lines("X", level)  

    def potential_win(self, who_in):

        potential_fields = []  

        
        for line in self.lines:
            line_values = [self.state[line[0]], self.state[line[1]], self.state[line[2]]]

           
            if line_values.count(who_in) == 2 and line_values.count(" ") == 1:
               
                potential_fields.append(line[line_values.index(" ")])

        if len(potential_fields) > 0:  
            return potential_fields[0]  