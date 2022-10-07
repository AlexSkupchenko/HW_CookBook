cook_book = {}

with open('recipes.txt', 'rt', encoding='utf8') as file:
    for l in file:
        dish_name = l.strip()
        book = {dish_name: []}
        ingredients_count = file.readline()
        for i in range(int(ingredients_count)):
            ing = file.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ')
            book[dish_name].append({'ingredient_name': ingredient_name,
                                       'quantity': quantity,
                                       'measure': measure})
        blank_line = file.readline()
        cook_book.update(book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient['quantity'] = int(ingredient['quantity'])
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))