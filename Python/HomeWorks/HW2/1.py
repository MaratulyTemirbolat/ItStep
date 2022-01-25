for number in range(40):
	print('$$',end=' ')
print('\n\t\t\t\t\tGood Day! Welcome to the System!',end = '\n')
for number in range(40):
	print('$$',end = ' ')
print()
inputNumber = int(input('\t\t\t Please, type an integer number that consists of 3 figures: '))
for number in range(40):
	print('$$',end = ' ')
print()
if(inputNumber >=100 and inputNumber<=999):
	print('Part a) ')
	print(' The number of Units in {} is:'.format(inputNumber),inputNumber%10)
	print('Part б) ')
	print(' The number of Tens in {} is:'.format(inputNumber),(inputNumber//10)%10)
	print('Part в) ')
	unitNumber = inputNumber%10
	tenNumber = (inputNumber//10)%10
	hundredNumber = (inputNumber//100)
	print(' The sum of it\'s figures is: {}'.format(unitNumber + tenNumber + hundredNumber))
	print('Part г) ')
	print(' The multiplication of it\'s figures is {}'.format(unitNumber * tenNumber * hundredNumber))
	print('\t\t\t\t\tThank you for using ! Good Buy! ')
else:
	print('You did not type corresponded number! Please, try again.')
for number in range(40):
	print('$$',end = ' ')

