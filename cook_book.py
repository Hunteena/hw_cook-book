import os
from pprint import pprint


def read_cook_book_from_file(file_name):
    '''
    Читает книгу рецептов из файла в словарь
    '''
    path = os.getcwd()
    file_path = f'{path}/{file_name}'
    cook_book = {}
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            dish = line.strip()
            cook_book[dish] = []
            ingredients_number = int(file.readline())            
            for counter in range(ingredients_number):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredient_dict = {
                    'ingredient_name': ingredient_name.strip(),
                    'quantity': int(quantity),
                    'measure': measure.strip()
                    }
                cook_book[dish].append(ingredient_dict)
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    '''
    Составляет список покупок для блюд из списка dishes на количество персон person_count
    '''
    shop_list = {}
    cook_book = read_cook_book_from_file('recipes.txt')
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity, measure = ingredient['quantity'], ingredient['measure']
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity * person_count
            else:
                shop_list[ingredient_name] = {
                    'measure': measure,
                    'quantity': quantity * person_count
                    }
    return shop_list


pprint(read_cook_book_from_file('recipes.txt'))
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
