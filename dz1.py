# ✔Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
#  Ответьте на вопросы: 
# ✔Какие вещи взяли все три друга 
# ✔Какие вещи уникальны, есть только у одного друга 
# ✔Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует 
# ✔Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

# Функция возвращеет словарь из: 
# 1)списка вещей которые есть у всех 
# 2) список уникальных вещей, есть только у одного друга
# 3) словарь вещей которые есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
#  Повышенный расход памяти, но компактный код и быстродействие O(n)
def what_get_all_items_sec(dictionary_of_items):
    new_list = []
    list_of_all_elements = []
    list_of_unicum_elements = []
    list_of_luser_elements = {}
    for key, el in dictionary_of_items.items():
        for e in el:
            new_list.append(e)

    for key, el in dictionary_of_items.items():
        for e in el:
            if new_list.count(e) == 1 : 
                if e not in list_of_unicum_elements:list_of_unicum_elements.append(e)
            if new_list.count(e) >= len(dictionary_of_items): 
                if e not in list_of_all_elements: list_of_all_elements.append(e)
            if new_list.count(e) == len(dictionary_of_items) - 1: 
                for key_failed, el_failed in dictionary_of_items.items(): 
                    if e not in el_failed:
                        list_of_luser_elements[key_failed] = e
                        break

    return list_of_all_elements,list_of_unicum_elements,list_of_luser_elements




# Функция возвращеет словарь из: 
# 1)списка вещей которые есть у всех 
# 2) список уникальных вещей, есть только у одного друга
# 3) словарь вещей которые есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
#  память не расходуется, но неудобочитаемый(сложный(возможно избыточный)) код и (скорее всего) низкое быстродействие o(n**2) сложность квадратичная

def what_get_all_items(dictionary_of_items):
    
    all_items = True
    unicum_items = False
    list_of_all_elements = []
    list_of_unicum_elements = []
    list_of_luser_elements = {}
    key_of_luser = ''
    count = 0
    num = 0
    for ferst_element in dictionary_of_items.values():
        
        for el in ferst_element:
            for key_of_other_element, other_element in dictionary_of_items.items():
                if el not in other_element: 
                    all_items = False
                    unicum_items = True
                    key_of_luser = key_of_other_element
                else: 
                    count += 1 
                    if num == 0: 
                        unicum_items = True
                        num =1
                    else:
                        unicum_items = False 
                    
            if unicum_items == False and all_items == False and count == len(dictionary_of_items) - 1:
                if el not in list_of_luser_elements:
                    list_of_luser_elements[key_of_luser] = el

            if all_items == True:
                if el not in list_of_all_elements: list_of_all_elements.append(el)
            else:
                all_items = True

            if unicum_items == True :
                list_of_unicum_elements.append(el)
                unicum_items = False
            key_of_luser = ''    
            count = 0
            num = 0    
    return list_of_all_elements , list_of_unicum_elements, list_of_luser_elements


my_dict = {'Максим':('knife' , '2' ,'3','4','20'),'Рома':('3', '5', 'knife','4'),'Никита':('knife','7','3','9'),'Артем':('4','3','2','11','knife'),'Маша':('4','knife','3')}

print(what_get_all_items(my_dict))
print(what_get_all_items_sec(my_dict))

