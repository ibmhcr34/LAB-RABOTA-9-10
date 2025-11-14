def bucket_sort(nums):
    # Если массив пустой, то просто возвращаем его
    if len(nums) == 0:
        return nums

    # Примерное количество корзин (берём по длине массива)
    b_count = len(nums)
    max_num = max(nums)
    min_num = min(nums)

    # Шаг, который помогает понять куда класть число
    step = (max_num - min_num) / b_count

    # Создаём список корзин
    buckets = [[] for _ in range(b_count + 1)]

    # Раскладываем числа по корзинам
    for value in nums:
        idx = int((value - min_num) / step)
        buckets[idx].append(value)

    # Сюда соберём всё после сортировки
    sorted_list = []

    # Сортируем каждую корзину и добавляем в итог
    for b in buckets:
        # Тут простая сортировка вставками, чтобы не городить что-то сложное
        insertion_sort(b)
        sorted_list.extend(b)

    return sorted_list


def insertion_sort(items):
    # Обычный алгоритм вставками
    for i in range(1, len(items)):
        cur = items[i]
        j = i - 1

        while j >= 0 and items[j] > cur:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = cur


# Пример работы
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
print("Стартовый список:", arr)
res = bucket_sort(arr)
print("После сортировки:", res)
