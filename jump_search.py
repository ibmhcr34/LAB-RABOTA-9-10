import math

def jump_search(arr, target):
    # длина массива
    n = len(arr)
    if n == 0:
        return -1

    # считаем примерный размер шага
    step = int(math.sqrt(n))

    # ищем примерный блок, где может быть число
    start = 0
    while arr[min(step, n) - 1] < target:
        start = step
        step += int(math.sqrt(n))
        if start >= n:
            return -1

    # обычный линейный поиск внутри найденного блока
    while arr[start] < target:
        start += 1
        if start == min(step, n):
            return -1

    # проверяем совпадение
    if arr[start] == target:
        return start
    return -1


# вывод без слов
def test_jump_search():
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    targets = [13, 1, 144, 100]

    print(arr)
    for t in targets:
        print(jump_search(arr, t))

test_jump_search()
