################################################################################################
# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com'
#   '(Хеш то що з ліва записувати не потрібно)

# Читання з файлу + фільтрація адресів по @gmail.com
try:
    with open('emails.txt', 'r') as file:

        arr_emails: list[str] = []

        while file.readline():
            line = file.readline().split()
            if line[1].endswith('@gmail.com'):
                arr_emails.append(line[1] + '\n')  # додаємо '\n' щоб був роздільник між мейлами при записі і новий файл

except Exception as err:
    print(err)

# Запис у файл фдресів '@gmail.com'

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

def write_file(file_name,list):
    try:
        with open(file_name, 'w') as file:
            json.dump(list, file)

    except Exception as err:
        print(err)



def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

    except Exception as err:
        write_file('shopping_book.txt',shopping_list)

    return data

shopping_list = []
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
                    product_id = product_id + shopping_list[-1]['id']

                shopping_element = Get_shop(product_name, product_coast, product_id)
                shopping_list.append(shopping_element.__dict__)

                write_file('shopping_book.txt',shopping_list)

                choice_shop = input('Додати ще купівлю ? (y/n) : ')

        case '2':

            print(shopping_list)

        case _:
            pass
