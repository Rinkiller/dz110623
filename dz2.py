# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.
def dublicated(list):
    list_of_dublicated = []
    for el in work_list:
        if work_list.count(el) >= 2: 
            if el not in list_of_dublicated: list_of_dublicated.append(el)
    return list_of_dublicated

work_list = [3,4,3,4,5,7,4,6,8,7,2,0,7,8,12,4,68,5,56457,4,465,6,7,9,23,53]

print('Исходный список: ', work_list)
print('Список дубликатов: ',dublicated(work_list))
