from random import randint


# Сложность алгоритма: O(n^2) - квадратичная.
def check_1(lst_obj):
    min_val = lst_obj[0]  # O(1)
    for j in lst_obj:  # O(n)
        for i in lst_obj:  # O(n)
            if i < j:  # O(1)
                if i < min_val:  # O(1)
                    min_val = i  # O(1)
    return min_val  # O(1)


# Сложность алгоритма: O(n) - линейная.
def check_2(lst_obj):
    min_val = lst_obj[0]  # O(1)
    for i in lst_obj:  # O(n)
        if i < min_val:  # O(1)
            min_val = i  # O(1)
    return min_val  # O(1)


test_list = [randint(1, 100) for i in range(20)]
print(test_list)
print(check_1(test_list))
print(check_2(test_list))
