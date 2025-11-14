def bead_sort(arr):
    # если массив пустой, просто возвращаем его
    if not arr:
        return arr

    # ищем самое большое число — понадобится для высоты "абака"
    max_num = max(arr)

    # создаём абак (типа таблица с нулями)
    board = [[0] * len(arr) for _ in range(max_num)]

    # раскладываем "бусинки" по абаку
    for i, val in enumerate(arr):
        for h in range(val):
            board[h][i] = 1

    # имитация падения бусинок вниз
    for row in range(max_num):
        # считаем сколько единичек в строке
        count = sum(board[row])
        # сначала ставим 1, потом 0 — как будто бусины упали
        for col in range(len(arr)):
            board[row][col] = 1 if col < count else 0

    # собираем отсортированные значения обратно
    result = []
    for col in range(len(arr)):
        # считаем сколько "бусин" стоит в колонке
        s = sum(board[row][col] for row in range(max_num))
        result.append(s)

    return result


# вывод без слов
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(arr)
print(bead_sort(arr))
