
TEN_BARS_CHOCOLATE = 10
FIVE_LITTERS_JUICE = 5

def is_correct_data(input_cost_amount):
	if(input_cost_amount < 0):
		return False
	return True

def get_product_cost(product_basic_cost,desired_product_amount,product_basic_number):
	product_final_cost = (desired_product_amount * product_basic_cost)/product_basic_number
	return product_final_cost

def show_title():
	print('Здравствуйте! Добро пожаловать в программу, которая принимает ',end = "")
	print('от пользователя цены 10-ти плиток шоколада, а также 5 литров ',end = "")
	print('сока.')
	print('В итоге программа вычислит стоимость общей покупки, которая ',end = "")
	print('включает n-ое количество плиток шоколада и n литров сока,',end = " ")
	print('которые пользователь решил приобрести.')	

def take_cost_data():
	ten_bars_chocolate_cost = int(input('Пожалуйста, введите стоимость 10 плиток шоколада: '))
	five_litters_juice_cost = int(input('Пожалуйста, введите стоимость 5 литров сока: '))
	
	while(is_correct_data(ten_bars_chocolate_cost) == False or is_correct_data(five_litters_juice_cost) == False):
		print('Кажется вы указали отрицательную стоимость у какого-то товара.',end = "")
		print(' Повторите ввод заново!')
		ten_bars_chocolate_cost = int(input('Пожалуйста, введите стоимость 10 плиток шоколада: '))
		five_litters_juice_cost = int(input('Пожалуйста, введите стоимость 5 литров сока: '))

	return ten_bars_chocolate_cost,five_litters_juice_cost

def take_desired_amount():
	desired_chocolate_bars = int(input('Какое количество плиток шоколада вы хотите купить: '))
	desired_juice_litters = int(input('Сколько литров сока вы хотите купить: '))	

	while(is_correct_data(desired_chocolate_bars) == False or is_correct_data(desired_juice_litters) == False):
		print('Кажется вы указали отрицательное количество у какого-то товара.',end = "")
		print(' Повторите ввод заново!')
		desired_chocolate_bars = int(input('Какое количество плиток шоколада вы хотите купить: '))
		desired_juice_litters = int(input('Сколько литров сока вы хотите купить: '))
		
	return desired_chocolate_bars,desired_juice_litters

def show_dollars():
	DOLLAR_AMOUNT = 40
	for star_index in range(DOLLAR_AMOUNT):
		print('$$',end = " ")

def show_final_bill(*goods_costs,desired_chocolate_bars,desired_juice_litters):
	total_goods_cost = goods_costs[0] + goods_costs[1]
	print('\n\nПокупка завершена:')
	print('Ваша финальная стоимость {} плиток шоколада составляет: {}'.format(desired_chocolate_bars,goods_costs[0]))
	print('Ваша финальная стоимость {} литров сока составляет {}'.format(desired_juice_litters,goods_costs[1]))
	print('КОНЕЧНАЯ стоимость {} плиток шоколада и {} литров сока будет: {}'.format(desired_chocolate_bars,desired_juice_litters,total_goods_cost))
	print('Спасибо за использование! До свидания!')

show_dollars()
print('\n')

show_title()

print()
show_dollars()
print('\n')

ten_bars_chocolate_cost,five_litters_juice_cost = take_cost_data()
print()
desired_chocolate_bars,desired_juice_litters = take_desired_amount()

final_cost_chocolate = get_product_cost(ten_bars_chocolate_cost,desired_chocolate_bars,TEN_BARS_CHOCOLATE)
final_cost_juice = get_product_cost(five_litters_juice_cost,desired_juice_litters,FIVE_LITTERS_JUICE)

show_dollars()
show_final_bill(final_cost_chocolate,final_cost_juice,desired_chocolate_bars = desired_chocolate_bars, desired_juice_litters = desired_juice_litters)