# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.
import random
def list_of_box_counts(list_of_joy,index_of_mass, massa,list_rezult,old_massa):
    if massa >= index_of_mass: 
        list_rezult.pop()
        return list_rezult, massa-old_massa
    elif massa == index_of_mass: return list_rezult, massa
    while True:
        key = random.choice(list(list_of_joy.keys()))
        if key not in list_rezult:
            massa += list_of_joy.get(key)
            old_massa = list_of_joy.get(key)
            list_rezult.append(key)
            break 
    return list_of_box_counts(list_of_joy,index_of_mass, massa,list_rezult,old_massa)


def get_all_items_of_box(list_of_box, max_massa_in):
    max_massa = 0
    list_of_all_items_of_box = []
    for massa in list_of_box.values():
        max_massa += massa
    if max_massa_in >= max_massa: 
        return list_of_box_counts(list_of_box,max_massa_in,0,[],0)
    else:
        
        for _ in range(len(list_of_box ) * 2) :
            lst = list_of_box_counts(list_of_box,max_massa_in,0,[],0)
            if lst not in list_of_all_items_of_box:
                list_of_all_items_of_box.append(lst)
        return list_of_all_items_of_box

list_of_box = {'нож':2,'фонарик':5,'паек':15,'топор':3,'спички':1,'котелок':5,'одежда':4,'палатка':9,\
               'GPS-навигатор':3,'матрс':9,'веревка':3,'аптечка':3}

for el in get_all_items_of_box(list_of_box,30):
    print(el)

 