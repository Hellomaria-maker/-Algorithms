# функция получает отсортированный массив и значение,
# если значение есть в массиве, то функция возвращает позицию(индекс значения)

def binary_search(my_list, my_item):
    first_item = 0
    last_item = len(my_list) - 1

    while first_item <= last_item:
        mean_item = (first_item + last_item) // 2
        if my_item == my_list[mean_item]:
            return mean_item
        elif my_item < my_list[mean_item]:
            last_item = mean_item - 1
        else:
            first_item = mean_item + 1
    return 'Такого значения нет в списке!'


print(binary_search([1, 2, 3, 4], 4))
print(binary_search([1, 2, 3, 4], 7))

