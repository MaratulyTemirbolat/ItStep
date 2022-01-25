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

#2
decades_temperature_july = []
sum_temperatures_decade = 0
DECADE_TERMINAL = 10

for day_index in range(JULY_DAYS):
	sum_temperatures_decade += july_temparatures[day_index]
	if((day_index + INDEX_STEP) % DECADE_TERMINAL == 0 ):
		decades_temperature_july.append(sum_temperatures_decade)
		sum_temperatures_decade = 0 # Что по поводу Последнего 31-го дня? Куда отнести и что с ним сделать?

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
#3
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
print('не отличается больше чем на 5 градусов: ',end = "")

for day_temperature in updated_july_temparatures:
	print(day_temperature, end = ", ")


