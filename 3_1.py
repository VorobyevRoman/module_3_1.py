calls = 0                 # переменная calls
def count_calls ():       # создание функции count_calls
    global calls          # обозначаем глобальную переменную calls
    calls += 1            # увелечение значения переменной calls
def string_info(string):  # создание функции string_info с параметром string
    count_calls()         # вызывание функции count_calls для функции string_info
    return (len(string), string.upper(), string.lower()) # возврат кортежа из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def  is_contains(string, list_to_search): # создание функции is_contains с параметрами строки и списка
    count_calls()         # # вызывание функции count_calls для функции для функции is_contains
    return string.upper() in [j.upper() for j in list_to_search] # возврат строки верхнего регистра, если строка находится в этом списке
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)