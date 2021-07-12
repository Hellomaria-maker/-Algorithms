# Алгоритм быстрой сортировки списка по позрастанию
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]                           # первый элемент списка выбираем как опорный
        less = [i for i in arr[1:] if i <= pivot]
        greather = [i for i in arr[1:] if i >= pivot]
        return quicksort(less) + [pivot] + quicksort(greather)


a = [45, 16, 88, 3, 9, 15, 8]
print(quicksort(a))