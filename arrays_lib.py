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

def min_id(array: list[int])->int:
    min = array[0]
    for i in range(1, len(array), 1):
        if min > array[i]:
            min = array[i]
    return min

def sum_2d(matrix: list[list[int]])->int:
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
    return sum

def prod_2d(matrix: list[list[int]])->int:
    prod = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            prod *= matrix[i][j]
    return prod

def mean_2d(matrix: list[list[int]])->float:
    sum = 0
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            count += 1
            sum += matrix[i][j]
    sred = sum / count
    return sred

def max_2d(matrix: list[list[int]])->int:
    max = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if max < matrix[i][j]:
                max = matrix[i][j]
    return max

def min_2d(matrix: list[list[int]])->int:
    min = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if min > matrix[i][j]:
                min = matrix[i][j]
    return min
