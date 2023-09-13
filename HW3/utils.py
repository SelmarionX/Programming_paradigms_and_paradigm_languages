
def collect_name():  
    name = input("Пожалуйста введите своё имя: ").upper()
    return name


def who_start(): 
    while True:
        start = input("Я буду играть за 'O' , а ты за 'X'.\n"
                      "Пожалуйста напишите 'O' или 'X' чтобы выбрать, кто начинает игру и подтвердите клавишей 'Enter'. ").upper()
        if start not in ("O", "X"):
            print("Ошибка! Неправильный ввод! Попробуйте ещё раз.")
        else:
            return start  


def user_move(board): 
    while True:
        move = input("Введите координаты, куда поставить 'X' (например: A1) ")
        move = move.upper()
        if len(move) != 2 or move[0] not in ("A", "B", "C") or move[1] not in (
                "1", "2", "3"):  
            print("Ошибка ввода! Попробуй ещё раз.")
        elif board.check_field(move) != " ":  
            print(" '{}' в этом поле. Попробуй ещё раз.".format(board.check_field(move)))
        else:
            return move  