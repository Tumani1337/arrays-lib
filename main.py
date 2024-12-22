from logger import log_action


arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 0]


def sum_arrays(arr1, arr2):
    result1 = []
    for i in range(len(arr1)):
        result1.append(arr1[i] + arr2[i])
    log_action(f"{result1}" + "\r")
    return result1


def diff_arrays(arr1, arr2):
    result2 = []
    for i in range(len(arr1)):
        result2.append(arr1[i] - arr2[i])
    log_action(f"{result2}" + "\r")
    return result2


def prod_arrays(arr1, arr2):
    result3 = []
    for i in range(len(arr1)):
        result3.append(arr1[i] * arr2[i])
    log_action(f"{result3}" + "\r")
    return result3

sum_of_arrays = sum_arrays(arr1, arr2)
diff_of_arrays = diff_arrays(arr1, arr2)
prod_of_arrays = prod_arrays(arr1, arr2)