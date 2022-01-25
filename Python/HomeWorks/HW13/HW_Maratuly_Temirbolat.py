from random import *

MAX_ELEMENT_NUMBER = 4.0
current_element = 0

MIN_NUMBER = -10
MAX_NUMBER = 10

random_numbers = []

print('Здравствуйте! Добро пожаловать в программу, которая заполняет ', end = "")
print('список целыми числами в диапазоне от -10 до 10, выводит содержимое ', end = "")
print('списка на экран. Также она считает она покажет сумму всех чисел в ',end = " ")
print('списке, их среднее арифметическое, сравнит эти данные списка со ', end = "")
print('средним арифметическим и если оно больше, то заменит это число на 0.')
print()

while(current_element < MAX_ELEMENT_NUMBER):
    random_numbers.append(randint(MIN_NUMBER,MAX_NUMBER))
    print('Случайное число {} успешно добавлено в список.'.format(random_numbers[current_element]))
    current_element += 1

print('\nГотово. Ваш список успешно заполнен всеми случайными переменными.')
sum_numbers = 0

print('Ваш список на данный момент: ',end = "")
for number in random_numbers:
	print(number,end = ", ")
	sum_numbers += number

average_number = sum_numbers/MAX_ELEMENT_NUMBER

print()
print('Сумма всех чисел в списке: {}, а среднее арифметическое: {}'.format(sum_numbers,average_number))

for index in range(len(random_numbers)):
	if(random_numbers[index] < average_number):
		random_numbers[index] = 0

print('Сравнив все числа списка со средним арифметическим мы получили: ',end = "")
for number in random_numbers:
	print(number, end = ", ")

print('\n')
print('Спасибо за использование данной программы! До свидания!')
