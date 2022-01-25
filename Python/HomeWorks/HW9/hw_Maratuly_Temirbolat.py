print('Здравсвтуйте! Добро пожаловать в программу которая принимает значения,',end = " ")
print('вводимые с клавиатуры пользователем и заполняет ими список. Всего 10 попыток.')
number = []
current_number = 1
MAX_NUMBER = 10
ONE_STEP = 1
while(current_number <= MAX_NUMBER):
	user_number = float(input('Введите пожалуйста {}-е ваше число: '.format(current_number)))
	if(user_number == int(user_number)):
		user_number = int(user_number)
	number.append(user_number)
	print('Число {} успешно добавлено в текущий список!'.format(user_number))
	current_number += ONE_STEP

print('Все числа, которыми вы заполнили ваш список: ',end = "")
index = 0
while(index < len(number)):
	if(index != len(number) - ONE_STEP):
		print(number[index],end = ", ")
	else:
		print(number[index])
	index += ONE_STEP
print('Спасибо за использование! До свидания!')
