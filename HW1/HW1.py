from random import randint


def sort_list_imperative(numbers: list):
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] < numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    return numbers


def sort_list2_declarative(list_to_sort: list):
    list_to_sort.sort(reverse=True)


def start():
    list_sort1 = [randint(0, 50) for i in range(9)]
    list_sort1 = sort_list_imperative(list_sort1)
    print('Сортировка в императивном стиле: ' + str(list_sort1))

    list_sort2 = [randint(0, 50) for i in range(9)]
    list_sort2 = sort_list_imperative(list_sort2)
    print('Сортировка в декларативном стиле: ' + str(list_sort2))



if __name__ == '__main__':
    start()