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

########################################################################################
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
    def __init__(self, name, age, found_shoe_size:int):
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

    def __init__(self, name, age, shoe_size:int):
        super().__init__(name, age)
        self.shoe_size = shoe_size
    def __str__(self):
        return f'Попелюшка : {self.name} Вік :  {self.age}  Розмір туфельки : {self.shoe_size}'

cin1 = Cinderella('Nastya', 22, 32)
cin2 = Cinderella('Yaryna', 20, 34)
cin3 = Cinderella('Olya', 28, 43)

princ = Prince('Fedya', 36, 34)

print(princ.searhc_cinderella([cin1, cin2, cin3]))

# print(type([cin1, cin2, cin3]))
#
# list_cin = [cin1, cin2, cin3]
#
# print(list_cin)
#
# for cin in list_cin :
#     print(cin)






# питання на консультацію :
# 1)print(rec1.__lt__)  - що це ? Чи можемо ми мати окремий доступ до меджік функції ?
# 2) Чи можемо ми описати всі математичні дії в одній меджік функції і реторном повернути тапл результатів?


