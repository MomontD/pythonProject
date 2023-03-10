################################## ЗАВДАННЯ 1 ######################################################
# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

class Rectangle:
    __slots__ = ('x', 'y')

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other) -> float:
        return (self.x * self.y) + (other.x * other.y)

    def __sub__(self, other) -> float:
        return (self.x * self.y) - (other.x * other.y)

    def __lt__(self, other) -> tuple:
        __equal = (self.x * self.y) == (other.x * other.y)
        __more = (self.x * self.y) > (other.x * other.y)
        __less = (self.x * self.y) < (other.x * other.y)
        return __equal, __more, __less

    def __len__(self):
        return self.x + self.y

    def __str__(self):
        return f'сторона х : {self.x} , сторона y : {self.y} , Площина : {self.x * self.y})\n'

rec1 = Rectangle(2, 5)
rec2 = Rectangle(3, 6)

print(rec1, rec2)
print('Сума площин прямокутників : ', rec1 + rec2)
print('Різниця площин прямокутників : ', rec1 - rec2)
print('Рівність площин прямокутників : ', rec1 == rec2)
print('Площина першого прямокутника більша ? : ', Rectangle.__lt__(rec1, rec2)[1])
print('Площина першого прямокутника менша ? : ', Rectangle.__lt__(rec1, rec2)[2])
print('Сума сторін прямокутників :', Rectangle.__len__(rec1),' та ',Rectangle.__len__(rec2))

################################## ЗАВДАННЯ 2 ######################################################
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:

    __slots__ = ('name', 'age')
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

class Prince(Human):
    __slots__ = ('name', 'age','_found_shoe_size')
    def __init__(self, name:str, age:int, found_shoe_size:int):
        super().__init__(name,age)
        self._found_shoe_size = found_shoe_size
    def searhc_cinderella (self, list_Cinderellas:list):
        res=''
        for cinderella in list_Cinderellas:
            if self._found_shoe_size == cinderella.shoe_size:
                res = f'Cinderella found : {cinderella.name}'
        if res:
            return res
        else: return 'Cinderella not found'

    def __str__(self):
        return f'Принц : {self.name} Вік :  {self.age} Знайдений розмір туфельки : {self._found_shoe_size}'

class Cinderella(Human):
    __slots__ = ('name', 'age', 'shoe_size')

    count = 0
    def __init__(self, name:str, age:int, shoe_size:int):
        super().__init__(name, age)
        self.shoe_size = shoe_size
        Cinderella.count +=1

    def __str__(self):
        return f'Попелюшка : {self.name} Вік :  {self.age}  Розмір туфельки : {self.shoe_size}'


cin1 = Cinderella('Nastya', 22, 32)
cin2 = Cinderella('Yaryna', 20, 34)
cin3 = Cinderella('Olya', 28, 43)

princ = Prince('Fedya', 36, 34)

print(princ.searhc_cinderella([cin1, cin2, cin3]))
print('К-сть створених попелюшок : ', Cinderella.count)

##################################### ЗАВДАННЯ 3#######################################################################
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:

# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

# !!!! РІШЕННЯ З КУРСІВ , САМ НЕ ЗМІГ ЗРОБИТИ.

from abc import ABC, abstractmethod  # імпортуємо абстрактний клас ABC та метод abstractmethod
class Printable(ABC):          # Декларуємо абстрактний метод
    @abstractmethod            # Ставимо декоратор
    def print(self) -> None:
        pass

class Magazine(Printable):     # Декларуємо клас Magazine(наслідує клас Printable)  , який буде приймати значення - "Назву"
    def __init__(self, name: str) -> None:
        self.__name = name

    def print(self) -> None:   # Функція абстрактного класу Printable - виводимо дані
        print(f'{self.__class__.__name__} - {self.__name}')

class Book(Printable):         # Декларуємо клас Book (наслідує клас Printable) , який буде приймати значення - "Назву"
    def __init__(self, name: str) -> None:
        self.__name = name

    def print(self) -> None:   # Функція абстрактного класу Printable - виводимо дані
        print(f'{self.__class__.__name__} - {self.__name}')

class Main:
    __printable_list: list[Book | Magazine] = []  #список , в якому будуть зберігатись введені назви Magazine та Book
                                                  # введені назви будуть мати тип class Magazine або Book.
                                                  # Далі ми будемо робити перевірку(isinstance) приналежності назви в списку до типу.
    @classmethod                                  # використовуючи декор @classmethod , ми приймаємо class Main  через
    def add(cls, item: Book | Magazine) -> None:  # аргумент cls та змінну яка належить до класу(типу) Book або Magazine
        # if isinstance(item, Magazine) or isinstance(item, Book):
        if isinstance(item, (Book, Magazine)):    # перевіряємо до якого класу(типу) належить змінна і додаємо її в список
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls) -> None:
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls) -> None:
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book2'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book3'))
Main.add(Magazine('Magazine3'))
Main.add(Book('Book1'))
Main.add(Book('Book4'))

Main.show_all_magazines()
print('*' * 50)
Main.show_all_books()





# питання на консультацію :
# 1)print(rec1.__lt__)  - що це ? Чи можемо ми мати окремий доступ до меджік функції ?
# 2) Чи можемо ми описати всі математичні дії в одній меджік функції і реторном повернути тапл результатів?


