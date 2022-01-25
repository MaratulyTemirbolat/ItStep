for number in range(50):
	print('##',end = ' ')
print()
print('\n\t\t\tHello! Welcome to the system that reverses',end = ' ')
print('provided number consisting of 4 figures.')
print('\n')
for number in range(50):
	print('##',end = ' ')
print()
given_four_gifures_number = int(input('\n\t\t\tPlease, type your number consisting of 4 figures starting not from zero: '))
if(given_four_gifures_number>=1000 and given_four_gifures_number<=9999):
	units_number = given_four_gifures_number%10
	given_four_gifures_number//=10
	tens_number = given_four_gifures_number%10
	given_four_gifures_number//=10
	hundreds_number = given_four_gifures_number%10
	given_four_gifures_number//=10
	thousands_number = given_four_gifures_number%10
	print('\t\t\t\t',end = '')
	print('The input number was {0}{1}{2}{3} and its reverse view is {3}{2}{1}{0}'.format(thousands_number,hundreds_number,tens_number,units_number))
	print()
else:
	print('Sorry, but made a mistake typing the number!')
for number in range(50):
	print('##',end = ' ')
print('\n\t\t\t\t\t\tGood Buy! Have a good Day!')