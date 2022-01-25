print('Здравсвтуйте! Добро пожаловать в программу, которая покажет вам ', end = '')
print('фигуру, состоящую из 2-ух равносторонних прямоугольников.')
print('Чтобы получить так называемую фигуру, вам необходимо будет ввести' , end = ' ')
print('размер, при котором вы хотите её увидеть.')
print()
given_size = int(input('Пожалуйста, введите размер фигуры: '))
print()
while(given_size < 1):
	print('Размер должен быть не меньше 1. Пожалуйста повторите снова')
	given_size = int(input('Пожалуйста, введите размер фигуры: '))
counter = 0
EVEN_ODD_CHECKER = 2
HALF_TERMINAL = 2
center = given_size // HALF_TERMINAL
ONE_STEP = 1
MINIMAL_VALUE_LIMIT = 1
print('Ваш результат при размере: ' + str(given_size),end = '\n')
if(given_size % EVEN_ODD_CHECKER == 1):
	center += ONE_STEP
for row in range(MINIMAL_VALUE_LIMIT,given_size + ONE_STEP):
	if(row <= center):
		counter += ONE_STEP
	else:
		counter -= ONE_STEP
	for column in range(MINIMAL_VALUE_LIMIT,given_size + ONE_STEP):
		if(column >= counter and column <= given_size - counter + ONE_STEP):
			print('#',end = ' ')
		else:
			print(' ',end = ' ')
	if(row == center and given_size % EVEN_ODD_CHECKER == 0):
		counter += ONE_STEP
	print()
print('\nСпасибо за использование нашей программы! До свидания')

