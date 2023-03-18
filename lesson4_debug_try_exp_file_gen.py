################################################################################################
# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com'
#   '(Хеш то що з ліва записувати не потрібно)

try:
    with open('emails.txt', 'r') as file:

        arr_emails: list[str] = []

        while file.readline():
            line = file.readline().split()
            if line[1].endswith('@gmail.com'):
                arr_emails.append(line[1] + '\n')  # додаємо '\n' щоб був роздільник між мейлами при записі і новий файл

except Exception as err:
    print(err)

try:
    with open('emails_gmail.txt', 'w') as file:
        file.writelines(arr_emails)

except Exception as err:
    print(err)

#################################################################################################################
# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

import json


class Get_shop:
    def __init__(self, name, coast, id):
        self.name = name
        self.coast = coast
        self.id = id


def write_file(file_name, list):
    try:
        with open(file_name, 'w') as file:
            json.dump(list, file)

    except Exception as err:
        print(err)


def read_file(file_name):

    data = []

    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

    except Exception as err:
        write_file('shopping_book.txt', data)

    return data

def search (position, key, list):

    res = ''
    find_index = int

    for index, el in enumerate(list):
        if el[key] == position:
            res = el
            find_index = index
            print('Знайдено позицію :', res)
    if res == '':
        print('Позицію не знайдено')

    return find_index

shopping_list : list[dict] = []
choice = '0'

while choice != '6':

    shopping_list = read_file('shopping_book.txt')
    shopping_element = {}

    print('Оберіть будь-ласка опцію :   \n'
          '1. Додати купівлю            \n'
          '2. Вивід куплених речей      \n'
          '3. Пошук (назва,вартість,id) \n'
          '4. Найдорожча купівля \n'
          '5. Видалення по id    \n'
          '6. Вихід              \n')

    choice = input('Введіть свій вибір : ')

    match choice:
        case '1':
            choice_shop = 'y'
            while choice_shop == 'y':

                product_name = input('Введіть назву купівлі : ')
                product_coast = int(input('Введіть вартість купівлі : '))

                if len(shopping_list) == 0:
                    product_id = 1
                else:
                    product_id = shopping_list[-1]['id'] + 1     # розраховуємо id запису (id попер. запису + 1)

                shopping_element = Get_shop(product_name, product_coast, product_id)
                shopping_list.append(shopping_element.__dict__)

                write_file('shopping_book.txt', shopping_list)

                choice_shop = input('Додати ще купівлю ? (y/n) : ')

        case '2':

            print(shopping_list)

        case '3':

            print('Вкажіть параметр по якому здійснити пошук : \n'
                  '1 - за назвою    \n'
                  '2 - за вартістю  \n'
                  '3 - за id ')

            user_choice = input('Введіть Ваш вибір : ')

            if user_choice == '1':
                element = input('Введіть назву купівлі: ')
                search(element, 'name', shopping_list)

            elif user_choice == '2':
                element = int(input('Введіть вартість купівлі: '))
                search(element, 'coast', shopping_list)

            elif user_choice == '3':
                element = int(input('Введіть номер id: '))
                search(element, 'id', shopping_list)

            else: print('Ви ввели невірний параметр , здійснено перехід на головне меню.')

        case '4':
            coasts_array = [el['coast'] for el in shopping_list if el['coast']]

            search(max(coasts_array), 'coast', shopping_list)

        case '5':
            user_delete_choice = int(input('Введіть номер id для видалення : '))

            del_index = search(user_delete_choice, 'id', shopping_list)
            shopping_list.pop(del_index)
            write_file('shopping_book.txt', shopping_list)

        case _:
            print('Ви ввели не вірний пункт меню')

############################################################################################################
# !!! Не робоче , не превіряти

# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то
# брати наступне з того ж підсписку
#
# в результат має записатись тільки 5 id
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122]

# data = [
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1111, "field": {}},
#         {"id": 1112, "field": {}},
#         {"id": 1113, "field": {}},
#         {"id": 1114, "field": {}},
#         {"id": 1115, "field": {}},
#     ],
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1120, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1123, "field": {}},
#         {"id": 1124, "field": {}},
#         {"id": 1125, "field": {}},
#
#     ],
#     [
#         {"id": 1130, "field": {}},
#         {"id": 1131, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1132, "field": {}},
#         {"id": 1133, "field": {}},
#
#     ]
# ]
#
# list1, list2, list3 = [*data]
# res = []
# iteration_loop = max(len(list1), len(list2), len(list3))
# count = 0
#
# while count <= iteration_loop:
#
#     if count < len(list1):
#         if list1[count]['id'] not in res :
#             res.append(list1[count]['id'])
#     if count < len(list2):
#         if list2[count]['id'] not in res :
#             res.append(list2[count]['id'])
#     if count < len(list3):
#         if list3[count]['id'] not in res :
#             res.append(list3[count]['id'])
#
#     count+=1
#
# print(res)

