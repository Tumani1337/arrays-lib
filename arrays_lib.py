def sum_1d(array: list[int]) -> int:
    summ = 0
    for i in range(len(array)):
        summ += array[i]
    return summ

def prod_1d(array: list[int]) -> int:
    prod = 1
    for i in range(len(array)):
        prod *= array[i]
    return prod

def mean_1d(array: list[int]) -> float:
    summ = 0
    for i in range(len(array)):
        summ += array[i]
    sred = summ / len(array)
    return sred

def max_1d(array: list[int])->int:
    max = array[0]
    for i in range(1, len(array), 1):
        if max < array[i]:
            max = array[i]
    return max
