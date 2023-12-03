cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}

with open('receprs.txt', 'w', encoding='utf-8') as f:
    for i, j in cook_book.items():
        f.write(f'{i}\n')
        f.write(f'{len(j)}\n')
        for k in j:
            str1 = f"{' | '.join(map(str, k.values()))}\n"
            f.write(str1)
        f.write("\n")


def get_shop_list_by_dishes(dishes, person_count):
    new_cook_book = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            new_cook_book[ing['ingredient_name']] = {'measure': ing['measure'],
                                                     'quantity': ing['quantity'] * person_count}
    return dict(sorted(new_cook_book.items()))


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), sep='\n')
