import os
from pprint import pprint


def get_cook_book(food_list):
    cook_book = {}
    path = os.path.join(os.getcwd(), food_list)
    with open(path, 'r', encoding='UTF-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            else:
                ingredients_quantity = int(file.readline().strip())
                ingredients_list = []
                for i in range(ingredients_quantity):
                    ingredients_dict = {}
                    temp = file.readline().strip().split(' | ')
                    ingredients_dict['ingredient_name'] = temp[0]
                    ingredients_dict['quantity'] = int(temp[1])
                    ingredients_dict['measure'] = temp[2]
                    ingredients_list.append(ingredients_dict)
                file.readline()
            cook_book[dish_name] = ingredients_list
        return cook_book


pprint(get_cook_book('recipes.txt'))
