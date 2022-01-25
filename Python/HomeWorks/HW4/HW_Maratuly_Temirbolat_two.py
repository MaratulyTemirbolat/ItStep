print('\t\t\t\t\tHello! Welcome to the System.')
print('It will ask you to type Three figures that you desire.',end = ' ')
print('Finally, it will show the biggest number among them.')
number_one = float(input('Please, type the first number: '))
max_number = number_one
number_two = float(input('Please, type the second number: '))
if(max_number<number_two):
	max_number = number_two
number_three = float(input('Please, type the third number:'))
if(max_number < number_three):
	max_number = number_three
print('Calculations are over...')
print('Well. The biggest number among {}, {} and {} is {}'.format(number_one,number_two,number_three,max_number))
print('Good Buy!')