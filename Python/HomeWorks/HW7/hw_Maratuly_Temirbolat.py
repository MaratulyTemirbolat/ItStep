print('Здравсвтуйте! Добро пожаловать в систему, которая принимает ', end = '')
print('натуральное число, введеннное с компьютера делает следующее: ')
print('a) Определяет его максимальное и минимальное цифры в нём')
print('b) Определяет, на сколько его максимальняа цифра превышает минимальное')
print('c) Находит сумму его максимальной и минимальной цифр')
natural_user_number = int(input('Пожалуйста, введите ваше натуральное число: '))
while(natural_user_number <= 0):
	print('Неправильно! Натуральное число должно быть больше 0.Повторите попытку')
	natural_user_number = int(input('Пожалуйста, введите ваше натуральное число: '))
DECIMAL_SYSTEM = 10
max_number = 0
min_number = 10
last_number_remainder = 0
while(natural_user_number != 0):
	last_number_remainder = natural_user_number % DECIMAL_SYSTEM
	if(last_number_remainder > max_number):
		max_number = last_number_remainder
	if(last_number_remainder < min_number):
		min_number = last_number_remainder
	natural_user_number //=DECIMAL_SYSTEM
max_min_figure_difference = max_number - min_number
max_min_figure_sum = max_number + min_number
print('а) Максимальным цифрой будет ялвяться {}, а минимальной {}'.format(max_number,min_number))
print('b) Максимальная цифра {} превышает минимальную цифру {} на {}'.format(max_number,min_number,max_min_figure_difference))
print('c) Сумма между максимальной цифрой {} и минимальной {} составляет {}'.format(max_number,min_number,max_min_figure_sum))