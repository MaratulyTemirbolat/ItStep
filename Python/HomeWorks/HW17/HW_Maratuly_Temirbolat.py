HOUR_SECONDS = 3600
MINUTE_SECONDS = 60
ONE_MINUTE_COST = 3
MAX_HOURS = 23
MAX_MINUTES = 59
MAX_SECONDS = 59
def get_seconds(hours,minutes,seconds):
	seconds += ((hours * HOUR_SECONDS) + (minutes * MINUTE_SECONDS))
	return seconds

def get_time_difference(seconds_begin,seconds_end):
	return (seconds_end - seconds_begin)

def calculate_call_cost(hours_begin,minutes_begin,seconds_begin,hours_end,minutes_end,seconds_end):
	seconds_duration_begin = get_seconds(hours_begin,minutes_begin,seconds_begin)
	seconds_duration_end = get_seconds(hours_end,minutes_end,seconds_end)
	total_seconds_duration = get_time_difference(seconds_duration_begin,seconds_duration_end)
	return (total_seconds_duration // MINUTE_SECONDS) * ONE_MINUTE_COST

def is_legal_time_range(hours,minutes,seconds):
	if(hours > MAX_HOURS or minutes > MAX_MINUTES or seconds > MAX_SECONDS):
		return False
	return True

def is_legal_time(hours_begin,minutes_begin,seconds_begin,hours_end,minutes_end,seconds_end):
	seconds_duration_begin = get_seconds(hours_begin,minutes_begin,seconds_begin)
	seconds_duration_end = get_seconds(hours_end,minutes_end,seconds_end)
	if(seconds_duration_end > seconds_duration_begin and 
		is_legal_time_range(hours_begin,minutes_begin,seconds_begin) == True and 
		is_legal_time_range(hours_end,minutes_end,seconds_end) == True):
		return True
	return False

print('Здравсвтуйте! Добро пожаловать в программу, которая будет ',end = "")
print('принимать время начала и время завершения телефонного разговора ',end = "")
print('в формате (часы,минуты,секунды).')
print('Далее, будет выведена общая стоимость за время, которое ',end = "")
print('вы использовали во время разговора.')
print('Стоимость одной минуты = 3 тенге.')

hour_begin = int(input('\nПожалуйста, введите часы начала разговора: '))
minute_begin = int(input('Пожалуйста, введите минуты начала разговора: '))
seconds_begin = int(input('Пожалуйста, введите секунды начала разговора: '))

hour_end = int(input('\nПожалуйста, введите часы конца разговора: '))
minute_end = int(input('Пожалуйста, введите минуты конца разговора: '))
second_end = int(input('Пожалуйста, введите секунды конца разговора: '))

while(is_legal_time(hour_begin,minute_begin,seconds_begin,hour_end,minute_end,second_end) == False):
	print('Вы совершили ошибку в заполнении данных, пожалуйста повторите попытку')
	hour_begin = int(input('\nПожалуйста, введите часы начала разговора: '))
	minute_begin = int(input('Пожалуйста, введите минуты начала разговора: '))
	seconds_begin = int(input('Пожалуйста, введите секунды начала разговора: '))

	hour_end = int(input('\nПожалуйста, введите часы конца разговора: '))
	minute_end = int(input('Пожалуйста, введите минуты конца разговора: '))
	second_end = int(input('Пожалуйста, введите секунды конца разговора: '))


final_call_cost = calculate_call_cost(hour_begin,minute_begin,seconds_begin,hour_end,minute_end,second_end)
print()
print('Общее количество времени потраченное на разговор составляет:',final_call_cost // ONE_MINUTE_COST,end = " ")
print('минут')
print('Общая сумма, которую вам необходимо заплатить составляет: {} тенге'.format(final_call_cost))

print('Спасибо за использование программы! До свидания!')

