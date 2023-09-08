
#   Использовано процедурное программирование
#      - простота и удобство, как написания кода, так и его чтение


def get_number():
    flag = True
    message = 'Ошибка ввода значения! Введите целое число от 1 до 9'
    while flag:
        number = input('Введите целое число от 1 до 9: ')
        try:
            number = int(number)
            if 0 < number < 10:
                flag = False
            else:
                print(message)
        except ValueError:
            print(message)
    return number


def print_multiplication_table(number: int):
    for i in range(1, number + 1):
        for j in range(1, 10):
            print(f'{i} x {j} = {i * j}')
        print()


def main():
    print_multiplication_table(get_number())


if __name__ == '__main__':
    main()
