products_list = []

i = 1
print("Пожалуйста введите название, цену и количество товара через пробел, для выхода введите 'exit'")
while True:
    new_item = input(': ')
    if new_item == 'exit':
        break
    item_list = new_item.split()
    product = (i, {'name': item_list[0], 'cost': item_list[1], 'count': item_list[2]})
    products_list.append(product)
    i += 1
    print("Товар добавлен")

print(products_list)
print("")


analytics = {
    'name': [],
    'cost': [],
    'count': []
}

for i in products_list:
    analytics['name'].append(i[1]['name'])
    analytics['cost'].append(i[1]['cost'])
    analytics['count'].append(i[1]['count'])

print(analytics)

