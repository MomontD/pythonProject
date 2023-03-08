# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання

from typing import Callable


# tuple[Callable[[str], None], Callable[[],list[str]]]
# Дана функція - замикання , повертає результати двох внутрішніх ф-й
#                перша - приймає як аргумент значення яке додається до внутрішньої змінної cases
#                друга - повертає список cases (його вміст)
# Результати цих двох ф-й повертаються tuplle : return add_case, show_case
# Відповідно прописується tuple [ функція 1(Callable[[str], None, функція 2 (Callable[[],list[str]]]
def case_list() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    cases: list[str] = []

    def add_case(new_case: str) -> None:
        nonlocal cases
        cases.append(new_case)

    def show_case() -> list[str]:
        nonlocal cases
        return cases

    return add_case, show_case


add_case, show_case = case_list()

print_case = show_case()

add_case('Hello')
add_case('By')

print(print_case)
add_case('4521')
print(print_case)

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція
# продекорована цим декоратором, та буде виводити це значення після виконання функцій

def decor (func) :
    count=0
    def inner (*args,**kwargs):
        nonlocal count
        count +=1
        print('Кількість викликів :' , count)
        return func(*args, **kwargs)
    return inner

@decor
def div_num (num):
    # len_num = len(str(num))-1
    counter = 0
    mass_nums = []

    for el in str(num):
        if el != '0':
            mass_nums.append(el + '0'*(len(str(num))-1-counter))
            counter += 1
    return '+'.join(mass_nums)
    #  рішення з курсів :
    #  return ' + '.join(ch + '0' * (len(st) - i - 1) for i, ch in enumerate(st) if ch != '0') + f' = {st}'

print(div_num(136))
print(div_num(512))

