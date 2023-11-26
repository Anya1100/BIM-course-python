# TODO Напишите функцию для поиска индекса товара
def find_index(spisok, tovar):
    try:
        elem_idx = spisok.index(tovar)
    except ValueError:
        print(f"Товар '{tovar}' не найден в списке.")
    else:
        print(f"Первое вхождение товара '{tovar}' имеет индекс {elem_idx}.")



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
find_index(items_list, 'банан')
find_index(items_list, 'груша')
find_index(items_list, 'персик')


#for find_item in ['банан', 'груша', 'персик']:
 #   index_item = find_index(items_list,find_item)   # TODO Вызовите функцию, что получить индекс товара
  #  if index_item is not None:
   #     print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    #else:
     #   print(f"Товар '{find_item}' не найден в списке.")
