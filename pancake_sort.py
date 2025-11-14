def pancake_sort(arr):
    # основная длина массива
    ln = len(arr)

    # идём с конца, уменьшая рабочую область
    for size in range(ln, 1, -1):
        # ищем индекс самого большого элемента в текущей части
        max_pos = arr.index(max(arr[:size]))

        # если он стоит не на финальной позиции — делаем два переворота
        if max_pos != size - 1:
            # переворот до максимального
            flip(arr, max_pos)
            # переворот до конца рабочей области
            flip(arr, size - 1)

    return arr


def flip(arr, k):
    # переворачиваем участок от 0 до k
    left = 0
    right = k
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


# вывод без слов
arr = [23, 10, 20, 11, 12, 6, 7]
print(arr)
print(pancake_sort(arr.copy()))
