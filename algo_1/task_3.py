
# сложность O(n)
# данное решение является оптимальнее первого, т.к. перебор выполняется в 1 цикл
def method_2(company):
    list_name = [0, 0, 0]
    list_values = [0, 0, 0]
    best_company = {}
    for key, value in company.items():  # O(n)
        if int(value) > int(list_values[2]):
            list_values[2] = value
            list_name[2] = key
        if int(list_values[2]) > int(list_values[1]):
            tmp = list_values[1]
            list_values[1] = list_values[2]
            list_values[2] = tmp
            tmp = list_name[1]
            list_name[1] = list_name[2]
            list_name[2] = tmp
        if int(list_values[1]) > int(list_values[0]):
            tmp = list_values[0]
            list_values[0] = list_values[1]
            list_values[1] = tmp
            tmp = list_name[0]
            list_name[0] = list_name[1]
            list_name[1] = tmp
    for it in range(3):  # O(n)
        best_company[list_name[it]] = list_values[it]
    return best_company


# сложность O(n^2)
def method_1(company):
    best_company = {}
    sort_list = list(company.values())
    sort_list.sort()
    sort_list = sort_list[-3:]
    for key, value in company.items():  # O(n)
        if value in sort_list:  # O(n)
            best_company[key] = value
    return best_company


all_company = {'компания_1': '100',
               'компания_2': '900',
               'компания_3': '200',
               'компания_4': '800',
               'компания_5': '300',
               'компания_6': '700',
               'компания_7': '400',
               'компания_8': '600',
               'компания_9': '500', }
print(all_company)
print(method_1(all_company))
print(method_2(all_company))
