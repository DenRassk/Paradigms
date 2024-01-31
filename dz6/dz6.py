def binary_search(lst: list[int], val: int) -> int:
    start = 0
    end = len(lst) - 1

    while start <= end:
        middle = start + (end - start) // 2
        if val == lst[middle]:
            return middle
        if val < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1


list1 = [12, 24, 32, 39, 45, 50, 54]
n = 39

result = binary_search(list1, n)

if result != -1:
    print(f"Число {n} имеет индекс {result} в массиве list1")
else:
    print(f"Число {n} отсутствует в массиве list1")
