from random import *

ONE_STEP = 1
NEGATIVE_INDEX = -1
HALF_ARRAY = 0.5

def binary_search(my_array,target_number):
    left_border = 0
    right_border = len(my_array) - ONE_STEP
    while(left_border < right_border):
        middle = int((left_border + right_border)*HALF_ARRAY)
        if(my_array[middle] < target_number):
            left_border = middle + ONE_STEP
        else:
            right_border = middle
    if(my_array[right_border] == target_number):
        return right_border
    return NEGATIVE_INDEX

def show_dollars():
	MAX_DOLLARS = 40
	print()
	for dollar_index in range(MAX_DOLLARS):
		print('$$',end = " ")

def selected_sort(array):
    for current_number in range(len(array) - ONE_STEP):
        min_element = current_number
        next_number = current_number + ONE_STEP
        while next_number < len(array):
            if(array[next_number] < array[min_element]):
                min_element = next_number
            next_number += ONE_STEP
        array[current_number],array[min_element] = array[min_element],array[current_number]


print('Здравсвтуйте! Добро пожаловать в программу, которая:')
print('Заполняет список 20 целыми числами в диапазоне от 0 до 100.')
print('Затем программа отсортирует полученный список',end = " ")
print('с помощью сортировки выбором, выведет результат "до"',end = " ")
print('и "после".') 
print('Пользователь вводит число, которое он хочет найти в данном списке,',end =' ')
print('и программа выведет индекс местонахождения данного числа,',end = " ")
print('либо сообщит, что данного числа в списке нет.')
my_list = []

MAX_NUMBERS = 20

SMALLEST_NUMBER = 0
MAX_NUMBER = 100

show_dollars()


print('\n\nНачнем заполнение вашего пустого списка')
print()
for number_index in range(MAX_NUMBERS):
	my_list.append(randint(SMALLEST_NUMBER,MAX_NUMBER))
	print('Число {} под индексом {} успешно добавлено в список'.format(my_list[number_index],number_index + ONE_STEP))

print('Список успешно заполнен случайными целыми числами.')
print('\nВаш неотсортированный список:',my_list)
print()

print('Теперь отсортируем ваш список, чтобы элементы шли в порядке возрастания...')
selected_sort(my_list)
print('\nВаш список успешно отсортирован в порядке возрастания')

print('\nВаш отсортированный список целых чисел:',my_list)

show_dollars()

print('\n\nТеперь, пожалуйста введите число, которое вы желаете найти')
find_number = int(input('Число, для поиска в списке: '))

found_number_index = binary_search(my_list,find_number)

if(found_number_index != NEGATIVE_INDEX):
    print('Ваше число найдено! Оно находится под индексом:',found_number_index + ONE_STEP)
else:
    print('Извините, но вашего числа нет в списке.')

show_dollars()

print('\n\nСпасибо за использование программы! До свидания!')


