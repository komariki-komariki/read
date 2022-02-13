def my_cook_book():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, numb_ingredients, *products = txt.split('\n')
            ingredients_list = []
            for values in products:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, values.split(' | '))
                ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = ingredients_list
    return cook_book
#print(my_cook_book())

def get_shop_list_by_dishes(dishes, person_count):
    coock_dict = {}
    cook_book = my_cook_book()
    for dish in dishes:
        for key, value in cook_book.items():
            if key == dish:
                for ing in value:
                    if ing['ingredient_name'] in coock_dict:
                        i = int(ing['quantity']) * person_count
                        coock_dict.update({ing['ingredient_name']:{'measure': ing.get('measure'), 'quantity': ing.get('quantity') * person_count + i}})
                    else:
                        coock_dict.setdefault(ing.get('ingredient_name'),
                                            {'measure': ing.get('measure'), 'quantity': ing.get('quantity') * person_count})
    return(coock_dict)

print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))