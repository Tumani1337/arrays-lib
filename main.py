from logger import log_action
from arrays_lib import filter_greate, filter_equal, filter_less, filter_not_equel


arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 0]


def sum_arrays(arr1, arr2):
    result1 = []
    for i in range(len(arr1)):
        result1.append(arr1[i] + arr2[i])
    log_action("sum_arrays >> " + f"{result1}" + "\r")
    return result1


def diff_arrays(arr1, arr2):
    result2 = []
    for i in range(len(arr1)):
        result2.append(arr1[i] - arr2[i])
    log_action("diff_arrays >> " + f"{result2}" + "\r")
    return result2


def prod_arrays(arr1, arr2):
    result3 = []
    for i in range(len(arr1)):
        result3.append(arr1[i] * arr2[i])
    log_action("prod_arrays >> " + f"{result3}" + "\r")
    return result3


def filter_greate_info(filter_greate, log_action):
    return log_action("filter_greate_info >> " + f"{filter_greate}" + "\r")


def filter_equal_info(filter_equal, log_action):
    return log_action("filter_equal_info >> " + f"{filter_equal}" + "\r")


def filter_less_info(filter_less, log_action):
    return log_action("filter_less_info >> " + f"{filter_less}" + "\r")


def filter_not_equel_info(filter_not_equal, log_action):
    return log_action("filter_not_equal >> " + f"{filter_not_equel}" + "\r")


sum_of_arrays = sum_arrays(arr1, arr2)
diff_of_arrays = diff_arrays(arr1, arr2)
prod_of_arrays = prod_arrays(arr1, arr2)
filter_greate_information = filter_greate_info(filter_greate, log_action)
filter_equal_information = filter_equal_info(filter_equal, log_action)
filter_less_information = filter_less_info(filter_less, log_action)
filter_not_equel_information = filter_not_equel_info(filter_not_equel, log_action)