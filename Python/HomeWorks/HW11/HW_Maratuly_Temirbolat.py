print('Здравствуйте! Добро пожаловать в программу, которая имитирует ', end = "")
print('работу кассового аппарата для магазина, торгующего новогодними ', end = "")
print('товарами. Вы увидите список товаров с соответсвующими ценами.')
print('Вам нужно будет: \nA) Выбрать товар из предлагаемого списка магазином.')
print('B) Ввести желаемое количество этого товара, который вы хотите приобрести.')
print('C) Выбрать следующий товар')
goods_list = ['Хлеб','Шоколад','Чипсы','Вода','Сахар']
price_list = [150,400,230,140,800]
client_final_sum = 0.0
work_shift_final_sum = 0.0
TAX = 0.12
work_shift_total_tax = 0.0
client_tax_price = 0.0
good_index = 0
MIN_INDEX_GOOD = 0
MAX_INDEX_GOOD = 4
is_closed_work_shift = False
is_client_served = False
index = 0
ONE_INDEX_SHIFT = 1
DENY_OPTION = '-1'
CONTINUE_OPTION = '1'
NOT_FINISHED_WORK = False

while(is_closed_work_shift == NOT_FINISHED_WORK):
	while(is_client_served == NOT_FINISHED_WORK):
		print('\nВсе доступные товары в магазине: ')
		while(index <= MAX_INDEX_GOOD):
			print('#' + str(index + ONE_INDEX_SHIFT) + ':',goods_list[index],end = ". ")
			print('Цена за 1 товар составляет: {} тенге'.format(price_list[index]))
			index += 1

		good_index = int(input('Пожалуйста, напишите номер понравившегося товара: '))

		while(good_index < MIN_INDEX_GOOD + ONE_INDEX_SHIFT or good_index > MAX_INDEX_GOOD + ONE_INDEX_SHIFT):
			good_index = int(input('Вы совершили ошибку. Повторите еще раз ввод номера: '))
		good_number = int(input('Пожалуйста, введите количество понравившегося товара: '))

		client_final_sum += (price_list[good_index - ONE_INDEX_SHIFT] * good_number)
		client_tax_price += (price_list[good_index - ONE_INDEX_SHIFT] * good_number) * TAX

		print()
		print('Вы выбрали товар #{}: {} '.format(good_index,goods_list[good_index - ONE_INDEX_SHIFT]),end = "")
		print('на сумму {} тенге'.format(price_list[good_index - ONE_INDEX_SHIFT] * good_number))
		print('Вы желаете совершить еще покупки?')
		client_choice = input('Если нет, то напишите -1, в противном случае напишите 1: ')

		while(client_choice != DENY_OPTION and client_choice != CONTINUE_OPTION):
			print('Вы выбрали не ту опцию. Пожалуйста, повторите ввод.')
			client_choice = input('Если нет, то напишите -1, в противном случае напишите 1: ')

		if(client_choice == DENY_OPTION):
			is_client_served = True
		index = 0

	print('\nБлагодарим вас за покупку наших товаров. Ваша итоговая цена', end = " ")
	print('без НДС составит ' + str(client_final_sum) + ' тенге')
	print('Сумма НДС составит: ' + str(client_tax_price) + ' тенге')
	print('А с учетом НДС цена будет {} тенге'.format(client_final_sum + client_tax_price))
	print('\nПродавец, вы желаете продолжить рабочую смену?')

	work_shift_final_sum += client_final_sum
	work_shift_total_tax += client_tax_price
	seller_choice = input('Если нет, то напишите -1, в противном случае напишите 1: ')

	while(seller_choice != DENY_OPTION and seller_choice != CONTINUE_OPTION):
		print('Вы выбрали не ту опцию, пожалуйста повторите ввод.')
		seller_choice = input('Если нет, то напишите -1, в противном случае напишите 1: ')
	if(seller_choice == DENY_OPTION):
		is_closed_work_shift = True
		print('\nВаша сумма проданного товара за сегодняшнюю смену составляет: ', end = "")
		print(work_shift_final_sum,'тенге без учета НДС.')
		print('Общая сумма НДС за сегодняшнюю смену составит : ' + str(work_shift_total_tax))
	elif(seller_choice == CONTINUE_OPTION):
		is_client_served = False
		client_final_sum = 0.0
		client_tax_price = 0.0
		
print('Спасибо за использование программы! До свидания!')