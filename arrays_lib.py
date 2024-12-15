def sum_1d(array: list[int]) -> int:
    summ = 0
    for i in range(len(array)):
        summ += array[i]
    return summ
