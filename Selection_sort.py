# сортировка списка по возрастанию

def find_smallest(my_list):
    smallest_item = my_list[0]
    smallest_index = 0
    for i in range(1, len(my_list)):
        if my_list[i] < smallest_item:
            smallest_item = my_list[i]
            smallest_index = i
    return smallest_index


def selection_sort(my_list):
    new_list = []
    for i in range(len(my_list)):
        smallest_item = find_smallest(my_list)
        new_list.append(my_list.pop(smallest_item))
    return new_list


print(selection_sort([4, 5, 67, 98, 12, 0]))


