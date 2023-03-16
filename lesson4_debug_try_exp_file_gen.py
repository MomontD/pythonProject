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

shopping_list: list[dict] = []

class Get_shop:
    def __init__(self, name, coast):
        self.name = name
        self.coast = coast


shopping_element = {}
choice = '0'

while choice != '6':

    print('Оберіть будь-ласка опцію :  \n'
          '1. Додати купівлю           \n'
          '2. Вивід куплених речей     \n'
          '3. Пошук (назва,вартість,id \n'
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

                shopping_element = Get_shop(product_name, product_coast)
                shopping_list.append(shopping_element.__dict__)

                try:
                     with open('shopping_book.txt', 'w') as file:
                         json.dump(shopping_list, file)

                except Exception as err:
                     print(err)

                choice_shop = input('Додати ще купівлю ? (y/n) : ')

        case '2':
            try:
                with open('shopping_book.txt', 'r') as file:
                    shopping_list = json.load(file)
                    print(shopping_list)

            except Exception as err:
                print(err)

        case _:
            pass
