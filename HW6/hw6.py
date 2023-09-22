def binary_search(list, find_num):
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:
        mid = low + (high - low) // 2
        if list[mid] == find_num:
            return mid
        elif list[mid] < find_num:
            low = mid + 1
        else:
            high = mid - 1
    return -1


mas = [1, 3, 4, 6, 7, 8, 10, 13, 14]
find_num = 3

result = binary_search(mas, find_num)

if result != -1:
    print(f"Индекс элемента {find_num} в списке {mas} ---> {str(result)} ")
else:
    print("-1 Элемент не найден")
