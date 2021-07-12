# Рекурсивная функция для подсчета элементов в списке:

def element_counter(arr):
    if len(arr) == 0:               # если список пустой (базовый случай)
        return 0
    else:
        arr = arr[:-1]
        return 1 + element_counter(arr)        # если не пустой снова вызываем функию и убираем один элем. из списка


a = [4, 1, 3, 5]
print(element_counter(a))

# Рекурсивная функция для нахождения максимального числа в списке:
def max_search(arr):
    if len(arr) == 1:
        return arr[0]
    if arr[0] > arr[1]:
        arr[1] = arr[0]
        arr = arr[1:]
        return max_search(arr)
    if arr[0] < arr[1]:
        arr = arr[1:]
        return max_search(arr)


b = [12, 41, 83, 95, 115, 8, 93, 55, 0, 18]
print(max_search(b))
