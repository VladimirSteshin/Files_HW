import os


def get_cook_book(food_list):
    cook_book = {}
    path = os.path.join(os.getcwd(), food_list)
    with open(path, 'r', encoding='UTF-8') as file:
        work = file


get_cook_book('recipes.txt')
