import os


def get_cook_book(food_list):
    cook_book = {}
    path = os.path.join(os.getcwd(), food_list)
    with open(path, encoding='UTF-8') as file:
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


def shopping_list(dishes, person):
    cook_book = get_cook_book('recipes.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for product in cook_book[dish]:
                name = product['ingredient_name']
                measure = product['measure']
                quantity = product['quantity']
                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity * person}
                else:
                    shop_list[name]['quantity'] += quantity * person
    return shop_list


print(shopping_list(['Омлет', 'Фахитос'], 2))
