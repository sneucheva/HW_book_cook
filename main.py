## ЗАДАНИЕ 1.

with open ('recipes.txt', encoding='utf-8') as f:
    book_cook = {}
    for line in f:
        bk_dish = line
        bk_count = int(f.readline())
        bk_product = []
        for i in range(bk_count):
            bkp = f.readline().strip()
            ingridient, quantity, gauge = bkp.split(' | ')
            bk_product.append({
                'ingridient': ingridient,
                'quantity': quantity,
                'gauge': gauge
            })
        f.readline()
        book_cook[bk_dish] = bk_product
for x in book_cook:
    print(x, bk_count)
    for y in book_cook[x]:
        print(y)




## ЗАДАНИЕ 2.


#def get_shop_list_by_dishes(dishes, person_count):
    #dishes = input('Напишите блюда через запятую: ') \
    #.lower().split(',')
    #person_count = int(input('Введите количество человек:  '))
    #for dishes in book_cook:
     #   res = f'{bk_dish}:\n' + '\n'.join(f'{ingridient}, {quantity * person_count} {gauge}' for ingridient, quantity, gauge in bk_product)
#print(res)

#get_shop_list_by_dishes(dishes, person_count)




## ЗАДАНИЕ 3.










