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

decades_temperature_july = []
sum_temperatures_decade = 0
DECADE_TERMINAL = 10

for day_index in range(JULY_DAYS):
	sum_temperatures_decade += july_temparatures[day_index]
	if((day_index + INDEX_STEP) % DECADE_TERMINAL == 0 ):
		decades_temperature_july.append(sum_temperatures_decade)
		sum_temperatures_decade = 0

coldest_decade = decades_temperature_july[0]
coldest_decade_index = 0

for decade_index in range(len(decades_temperature_july)):
	if(decades_temperature_july[decade_index] < coldest_decade):
		coldest_decade = decades_temperature_july[decade_index]
		coldest_decade_index = decade_index
print('\nГотово! Самая холодная декада найдена.')
print()
print("Самой холодной декадой является {} с общей температурой {}".format(coldest_decade_index + INDEX_STEP,coldest_decade))
print()