def exponential_search(arr, target):
    # длина массива
    n = len(arr)
    if n == 0:
        return -1

    # отдельная проверка на первый элемент
    if arr[0] == target:
        return 0

    # постепенно увеличиваем диапазон поиска
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # бинарный поиск в найденных границах
    return binary_search(arr, target, i // 2, min(i, n - 1))


def binary_search(arr, target, left, right):
    # простая бинарка
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# вывод без слов
def test_exponential_search():
    arr = [2, 3, 4, 10, 15, 18, 20, 23, 35, 40, 45, 50, 60, 70, 80, 90, 100]
    targets = [10, 35, 100, 5, 95]

    print(arr)
    for t in targets:
        print(exponential_search(arr, t))

test_exponential_search()
