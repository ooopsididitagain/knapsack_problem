#!/usr/bin/python3
# Date: 17.12.2019
# Status: Done
# Author: Glebov I.A.

import random

bag_weight_max = 15
bag_weight_now = 0
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
        weight_measure = dict(zip(['Weight_measure'], ['kg']))
        product_info.update(weight)
        product_info.update(price)
        product_info.update(currency_code)
        product_info.update(weight_measure)
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


def sort_and_append(Param1='Price', Param2='Weight'):
    '''

        Функция сортирует полученные данные по двум параметрам (в нашем случае Цена и Вес) и
            добавляет подходящие товары в bag. (Пока вместимость сумки не превысит 15 кг).
            Вместимость сумки задается переменной bag_weight_max

        Возвращает словарь.

    '''

    global bag_weight_now
    for i in sorted(gen_data().items(), key=lambda it: (it[1].get(Param1), it[1].get(Param2)), reverse=True):
        if (bag_weight_now + i[1].get(Param2)) != bag_weight_max and (
                bag_weight_now + i[1].get(Param2)) < bag_weight_max:
            bag.append(i)
            bag_weight_now += i[1].get(Param2)
    return dict(bag)


if __name__ == '__main__':
    sort_and_append()
