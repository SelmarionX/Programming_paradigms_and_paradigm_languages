from utils import collect_name, who_start, user_move
from display import BoardPrinter, Messenger
from board import Board
from response import Response


"""Крестики нолики"""

"""Нумерация поля
       A   B   C  
      ╔═══╤═══╤═══╗
    1 ║ O │ 3 │ 6 ║
      ╟───┼───┼───╢
    2 ║ 1 │ 4 │ 7 ║
      ╟───┼───┼───╢
    3 ║ 2 │ 5 │ 8 ║
      ╚═══╧═══╧═══╝
      
      'X' - Человек
      'O' - Компьютер
"""


def main():
    
    user_name = (collect_name()).upper()
    message = Messenger(user_name)
    game_counter = 0  
    score = [0, 0, 0] 
    game_start = [0, 0] 

    

    while True:
        board = Board() 
        display = BoardPrinter(board)
        answer = Response(board)
        display.display_board("")
        game_counter += 1

        def win_score(win):
            message.win_message(win)
            if win:
                if win == "X":
                    score[0] += 1
                elif win == "O":
                    score[1] += 1
                elif win == "ничья":
                    score[2] += 1

       

        print("\n" + "═" * 35, "\n     Крестики нолики     \n" + "═" * 35, "\n")

        start = who_start()

        if start == "O":
            answer.response()  
            display.display_board("O")  
            game_start[1] += 1
        else:
            game_start[0] += 1

        while True:

            
            move = user_move(board)  

            board.insert(move, "X")  

            display.display_board("X")  

            win = board.check_win()
            if win:
                win_score(win)
                board.reset_board()
                break

            
            answer.response() 

           
            display.display_board("O")  

            win = board.check_win()
            if win:
                win_score(win)
                board.reset_board()
                break

        print("Мы сыграли {} раундов и наш текущий результат:".format(game_counter))
        print("           {0:^15}  {1:^15}  {2:^15}".format(user_name, "Компьютер", "Ничья"))
        print("Побед      {0:^15}  {1:^15}  {2:^15}".format(score[0], score[1], score[2]))
        print("Начато игр {0:^15}  {1:^15}\n".format(game_start[0], game_start[1]))

        while not input("нажми Enter для продолжения"):
            break


if __name__ == "__main__":
    main()