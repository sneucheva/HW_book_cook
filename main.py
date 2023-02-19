with open ('recipes.txt', encoding='utf-8') as f:
    book_cook = {}
    for line in f:
        bk_dish = line
        bk_count = int(f.readline())
        bk_product = []
        for i in range(bk_count):
            bkp = f.readline().strip()
            ingredient, quantity, gauge = bkp.split(' | ')
            bk_product.append({
                'ingredient': ingredient,
                'quantity': quantity,
                'gauge': gauge
            })
        f.readline()
        book_cook[bk_dish] = bk_product
for x in book_cook:
    print(x)
    for y in book_cook[x]:
        print(y)



#def get_shop_list_by_dishes(dishes, person_count):
 #   dishes = input('Введите названия блюд из заказа: ')
  #  person_count = int(input('Введите количество персон: '))

   # return(get_shop_list_by_dishes(dishes, person_count))
#print(get_shop_list_by_dishes(dishes, person_count))


