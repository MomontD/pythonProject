# strings
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'
digit_st=''

for el in st :
    if el.isdigit() :
        digit_st += el + ','
print(digit_st.rstrip(','))

# рішення з курсів
# digit_str = ','.join([char for char in st if char.isdigit()])
# print(digit_str)

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі


st = 'as 23 fdfdg544 34 a'
arr=[]
digit_element=''

for el in st :
    if el.isdigit() :
        digit_element+=el
    if el == ' ' and digit_element != '' :
        arr.append(digit_element)
        digit_element=''
print(','.join(arr))

# рішення з курсів :
# res =','.join(''.join([el if el.isdigit() else ' ' for el in st ]).split())
# print(res)

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
res = [el.upper() for el in greeting]
print(res)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

res = [pow(el,2) for el in range(0,50) if el%2 ]
print(res)

# рішення з курсів :
# print([i ** 2 for i in range(50) if i % 2])

# #################################################################################
# function
#
# - створити функцію яка виводить ліст
array = [1,2,3,4,5]
def print_array (in_array) :
    return in_array

print(print_array(array))

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def max_number (num1,num2,num3) :
    print("Отримані числа числа : ",num1,num2,num3 ,sep=' ')
    return max(num1,num2,num3)

print('Найбільше число : ',max_number(3,7,5))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def min_max_num(*args) :
    print('Найбільше число :' , max(*args))
    return min(*args)

print('Найменше число : ',min_max_num(1, 2, 6, 9, 4, 1, 15))
# - створити функцію яка повертає найбільше число з ліста
# - створити функцію яка повертає найменьше число з ліста
arr_of_nums = [1,4,7,45,23,43,7,55,4,7]
def min_max_num_list (list) :
    min_num= min(list)
    max_num= max(list)
    return (min_num,max_num)

print(min_max_num_list(arr_of_nums))
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
arr_of_nums = [1,4,7,45,23,43,7,55]
def calc_el_list(list) :
    sum_list = sum(list)
    average_num = sum_list/len(list)
    return (sum_list,average_num)

print(calc_el_list(arr_of_nums))

# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
list = [22, 3,5,2,10,2,-23, 8,23,5]

def actions_of_list (list) :
    min_num = min(list)
    dub_of  = set(list)
    return (min_num,dub_of)

def change_list (list) :
    for i in range(3,len(list),4) :
        list[i]='X'
    return list

print(actions_of_list(list))

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square (size) :
    for pix in range(1,size+1) :
        if pix==1 or pix == size : print('*'*size)
        else : print ('*' + ' '*(size-2) + '*')

square(5)

# 3) вывести табличку множення за допомогою цикла while
def multiplication_table() :
    count=1
    while count in range(1,10) :
        count2=1
        while count2 in range(1,10) :
            print(f'{(count*count2):3}',end=' ')
            count2+=1
        print()
        count+=1

# 4) переробити це завдання під меню

choice=int
while choice != 6 :
    print('1) Знайти min число \n'
          '2) Видалити дублікати \n'
          "3) Змінити кожне 4-те значення на 'X' \n"
          '4) Вивести на екран квадрат з "*" сторону якого необхідно вказати  \n'
          '5) Сформувати табличку множення\n'
          '6) Вихід ')

    choice=int(input('Введіть Ваш вибір : '))
    print()

    if choice   == 1:
        print('Мінімальне значення масиву :',min_max_num_list(arr_of_nums)[0],'\n')
    elif choice == 2:
        print('Масив без дублікатів : ',actions_of_list(arr_of_nums)[1],'\n')
    elif choice == 3:
        print("Кожне 4-те значення змінене на 'X' :", change_list(arr_of_nums),'\n')
    elif choice == 4:
        print('Надрукований квадрат')
        square(5)
    elif choice == 5:
        print('Табличка множення :')
        multiplication_table()
