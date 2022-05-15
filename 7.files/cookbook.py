import os
from pprint import pprint
file_path = os.path.join(os.getcwd(), 'recipes.txt')
def cookbook():
    cookbook = {}
    with open(file_path) as file:
        while True:
            rec_name = file.readline().strip()
            if rec_name == '':
                break
            cookbook[rec_name] = []
            amount = file.readline()
            for i in range(int(amount)):
                column = file.readline().split(" | ")
                cookbook[rec_name].append({'ingredient_name': column[0], 'quantity': column[1], 'measure': column[2]},)
            file.readline()
    return cookbook
print("cook_book = ", cookbook())
print("# -----------------------------------")

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = cookbook()
    ingredient_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingredient_name'] in ingredient_list.keys():
                update_dict = {ingridient['ingredient_name']: {'measure': ingridient['measure'],\
                 'quantity': (ingredient_list[ingridient['quantity']] + int(ingridient['quantity']) * person_count)}}
                ingredient_list.update(update_dict)    
            else:               
                update_dict = {ingridient['ingredient_name']: {'measure': ingridient['measure'],\
                 'quantity': int(ingridient['quantity']) * person_count}}
                ingredient_list.update(update_dict)
                # ingredient_list = sorted(ingredient_list).sort()
    return ingredient_list
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 1))
