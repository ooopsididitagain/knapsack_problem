# 0/1 example for bag

import random
import pprint

bag_weight = 15  # Задаю вес рюкзака
bag = []


def gen_list(list_lenght=10, random_start=1, random_end=12):
    '''

        Функция генерирует список неповторяющихся чисел от random_start до random_end.
        Числа используются для определения веса и цены товара.

        Возвращает: список чисел длинной list_lenght.

    '''
    # Определение типов аргументов передаваемых в функции
    list_lenght: int
    random_start: int
    random_end: int
    name = []
    while len(name) < list_lenght:
        i = random.randint(random_start, random_end)
        if i not in name:
            name.append(i)
    return name


def gen_product_name(list_lenght=10):
    '''

        Функция генерирует название товаров.

        Возвращает: список чисел длинной list_lenght.

    '''
    # Определение типов аргументов передаваемых в функции
    list_lenght: int
    product_name = []
    count = 1
    while len(product_name) < list_lenght:
        product_name.append(f'{count}_Product')
        count += 1
    return product_name


def gen_dict():
    '''

        Функция генерирует словарь, используемый в дальнейшем как описание товара (цена, валюта, вес, мера измерения).
        Словарь используется как значение ключа. Ключ - это название продукта (например: '1_Product').

        Возвращает: словарь.

    '''
    product_info = {}
    while len(product_info) == 0:
        weight = dict(zip(['Weight'], gen_list()))
        price = dict(zip(['Price'], gen_list()))
        currency_code = dict(zip(['Сurrency_code'], ['$']))
        Weight_measure = dict(zip(['Weight_measure'], ['kg']))
        product_info.update(weight)
        product_info.update(price)
        product_info.update(currency_code)
        product_info.update(Weight_measure)
    return product_info


product_name = gen_product_name()


def gen_data():
    '''

        Функция генерирует словарь со списков товаров и их свойствами.

        Возращает: словарь длинной gen_product_name(list_lenght=...).

    '''
    data = {}
    for i in product_name:
        data[i] = gen_dict()
    return data


pp = pprint.PrettyPrinter(indent=2)
pp.pprint(gen_data())

# print(data.get('Product1'))
#
# for i in sorted(data.items(), key=lambda it: (it[1][1], it[1][0]), reverse=True):
#     print(i)
#     while bag_weight > 0:
#         if bag_weight - int(i[1][0][0]) > 0:
#             print(int(i[1][0][0]))
#             bag_weight -= int(i[1][0][0])
#             bag.append(i)
#             print(bag_weight)
#
# print(bag)
