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

updated_july_temparatures = []
updated_july_temparatures.append(randint(MIN_TEMPERATURE,MAX_TEMPERATURE))
DAYS_MAX_DIFFERENCE_TEMPERATURE = 5

for day_index in range(1,JULY_DAYS):
	previous_day_temperature = updated_july_temparatures[day_index - INDEX_STEP]
	new_random_temperature = randint(previous_day_temperature - DAYS_MAX_DIFFERENCE_TEMPERATURE ,previous_day_temperature + DAYS_MAX_DIFFERENCE_TEMPERATURE)

	while(new_random_temperature < MIN_TEMPERATURE or new_random_temperature > MAX_TEMPERATURE):
		new_random_temperature = randint(previous_day_temperature - DAYS_MAX_DIFFERENCE_TEMPERATURE ,previous_day_temperature + DAYS_MAX_DIFFERENCE_TEMPERATURE)
		
	updated_july_temparatures.append(new_random_temperature)

print('Среднесуточные температуры Июля где температуры рядом стоящих дней',end = " ")
print('не отличается больше чем на +-5 градусов: ')

for day_temperature_index in range(JULY_DAYS):
	current_day = day_temperature_index + INDEX_STEP
	temperature = updated_july_temparatures[day_temperature_index]
	print('Средняя температура за {}-е число составляет {} градусов'.format(current_day,temperature))

