from random import *

print('Здравсвтуйте! Добро пожаловать в программу, которая заполняет ',end = "")
print('список данными о средней температуре каждого дня июля ',end = "")
print('случайными числами в диапазоне от +15 до +42.')
print('В последствии она выводит информацию о средней температуре ',end = "")
print('каждого дня в Июле, а также выводит даты двух самых теплых дней',end = " ")
print('вместе с их датами.')

JULY_DAYS = 31

MIN_TEMPERATURE = 15
MAX_TEMPERATURE = 42

INDEX_STEP = 1

july_temparatures = []

for day_index in range(JULY_DAYS):
	july_temparatures.append(randint(MIN_TEMPERATURE,MAX_TEMPERATURE))
	print('Средняя температура за {}-е число составляет {} градусов'.format(day_index + INDEX_STEP,july_temparatures[day_index]))

#1
warmest_day_a = 0
warmest_day_b = 0

warmest_day_a_index = 0
warmest_day_b_index = 0

for day_index in range(JULY_DAYS):
	if(july_temparatures[day_index] > warmest_day_a):
		warmest_day_a = july_temparatures[day_index]
		warmest_day_a_index = day_index

for day_index in range(JULY_DAYS):
	if(july_temparatures[day_index] > warmest_day_b and july_temparatures[day_index] < warmest_day_a):
		warmest_day_b = july_temparatures[day_index]
		warmest_day_b_index = day_index

print('\nГотово! Выдаю результаты: ')
print()

print("Самыми жаркими днями являются {} июля с температурой {}".format(warmest_day_a_index + INDEX_STEP,warmest_day_a), end = " ")
print("и {} июля с температурой {}".format(warmest_day_b_index + INDEX_STEP, warmest_day_b))