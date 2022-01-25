for current_sign in range(43):
	print('$$',end = " ")
print()
print('\n  Здравствуйте! Добро пожаловать в программу, которая найдёт все ', end = "")
print('двузначные числа, сумма квадратов цифр которых делится на 13\n')
for current_sign in range(43):
	print('$$',end = " ")
ONE_STEP = 1
MIN_TWO_FIGURE_NUMBER = 10
MAX_TWO_FIGURE_NUMBER = 99
DECIMAL_BASE = 10
POWER_SQARE_NUMBER = 2
DIVISION_WITHOUT_REMAINDER_CHECKER = 0
THIRTEEN_TERMINAL_NUMBER = 13
counter = MIN_TWO_FIGURE_NUMBER
print('\n')
while(counter <= MAX_TWO_FIGURE_NUMBER):
	current_number = counter
	last_cur_number_figure = current_number % DECIMAL_BASE
	current_number //=DECIMAL_BASE
	first_cur_number_figure = current_number % DECIMAL_BASE
	sum_sqares_figures = (first_cur_number_figure**POWER_SQARE_NUMBER) + (last_cur_number_figure**POWER_SQARE_NUMBER)

	if(sum_sqares_figures % THIRTEEN_TERMINAL_NUMBER == DIVISION_WITHOUT_REMAINDER_CHECKER):
		print('\t\tДвузначное число ', end = "")
		print('{} подходит, потому что '.format(counter),end = "")
		print(first_cur_number_figure**POWER_SQARE_NUMBER,'+',last_cur_number_figure**POWER_SQARE_NUMBER,end = "")
		print(' =',sum_sqares_figures,'и при делении на 13 остаток = 0',end = "\n")

	counter+=ONE_STEP
print()
for current_sign in range(43):
	print('$$',end = " ")
print('\n\t\t\t\t\tСпасибо за использование ! До свидания!')