from random import *

ONE_STEP = 1

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


print('Здравсвтуйте! Добро пожаловать в программу, которая:\na)Заполняет ',end = "")
print('список целыми числами в диапазоне от -10 до + 20')
print('b)Выводит на экран значения неотсортированного списка')
print('c)Отсортирует список методом сортировка "выбором"')
print('d)Выводит на экран отсортированный конечный список')

my_list = []

MAX_NUMBERS = 10

SMALLEST_NUMBER = -10
MAX_NUMBER = 20

show_dollars()


print('\n\na)Начнем заполнение вашего пустого списка')
print()
for number_index in range(MAX_NUMBERS):
	my_list.append(randint(SMALLEST_NUMBER,MAX_NUMBER))
	print('Число {} под индексом {} успешно добавлено в список'.format(my_list[number_index],number_index + ONE_STEP))

print('Список успешно заполнен случайными целыми числами.')
print('\nb)Ваш неотсортированный список:',my_list)
print()

print('c)Теперь отсортируем ваш список, чтобы элементы шли в порядке возрастания...')
selected_sort(my_list)
print('\nВаш список успешно отсортирован в порядке возрастания')

print('\nd)Ваш отсортированный список целых чисел:',my_list)

show_dollars()

print('\n\nСпасибо за использование программы! До свидания!')


