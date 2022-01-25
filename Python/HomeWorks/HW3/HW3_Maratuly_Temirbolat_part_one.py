for number in range(64):
	print('$$',end = ' ')
print('\n\nGood Afternoon! Welcome to the system', end = ' ')
print('that will take your monthly income, bank credit per month',end = ' ')
print('as well as you utility bills and',end = ' ')
print('finally will illustrate the remainded money after all payments.')
print()
for number in range(64):
	print('$$',end = ' ')
print('\n')
income_per_month = float(input('Please, type you salary which you earns monthly: '))
credit_debt_per_month = float(input('Please, type the sum of your monthly bank credit: '))
utility_bills_per_momth = float(input('Please, type your utility bills: '))
remainded_money_after_payments = income_per_month - (credit_debt_per_month + utility_bills_per_momth)
print()
for number in range(64):
	print('$$',end = ' ')
print('\nWell, this is your remainded money after payments for bank credit alond with the utility bills:',remainded_money_after_payments)
print('Thank you for usage! Good Buy!')