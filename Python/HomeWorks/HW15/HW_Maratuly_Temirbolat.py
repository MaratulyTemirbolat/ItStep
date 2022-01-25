from random import *


print('Здравсвтуйте! Добро пожаловать в программу, которая заполняет ',end = "")
print('список рейтинго 20-ти студентов.')
print('Рейтинг будет в диапазоне от 0 до 50.\nПрограмма определит:')
print('1.Самый низкий рейтинг\n2.Индексы студентов с низким рейтингом')
print('3.Индексы 3-х студентов, имеющие самые высокие рейтинги')

print()
for sign_index in range(40):
	print('$$',end = " ")

student_ratings = []

STUDENT_NUMBER = 20

MIN_RATING = 0
MAX_RATING = 50

INDEX_STEP = 1

print('\n\nНачинаем заполнять рейтинг всех студентов...\n')

for student_index in range(STUDENT_NUMBER):
	student_ratings.append(randint(MIN_RATING,MAX_RATING))
	print('Студент под индексом {} обладает рейтингом {}'.format(student_index + INDEX_STEP,student_ratings[student_index]))

print('\nУх...Все рейтинги успешно добавлены в список. Определим самый низкий')

#1
print()
for sign_index in range(40):
	print('$$',end = " ")

lowest_rating = student_ratings[0]

for student_index in range(STUDENT_NUMBER):
	if(student_ratings[student_index] < lowest_rating):
		lowest_rating = student_ratings[student_index]

print('\n\n1.Самый низкий рейтинг студента составляет',lowest_rating)

print()
for sign_index in range(40):
	print('$$',end = " ")

#2

print('\n\n2.Индексы(номера) студентов с самым низким рейтингом являются: ')
for student_index in range(STUDENT_NUMBER):
	if(student_ratings[student_index] == lowest_rating):
		print("\t\t\t\t\t\t\tСтудент под номером",student_index + INDEX_STEP)

#3
print('\nТак, теперь найдем индексы 3-х студентов, имеющие самые высокие рейтинги')

max_rating_a_index = student_ratings.index(max(student_ratings[0],student_ratings[1],student_ratings[2]))
max_rating_c_index = student_ratings.index(min(student_ratings[0],student_ratings[1],student_ratings[2]))
max_rating_b = student_ratings[0] + student_ratings[1] + student_ratings[2] - (student_ratings[max_rating_a_index] + student_ratings[max_rating_c_index])
max_rating_b_index = student_ratings.index(max_rating_b)

for student_index in range(STUDENT_NUMBER):
	if(student_ratings[student_index] > student_ratings[max_rating_a_index]):
		max_rating_c_index = max_rating_b_index
		max_rating_b_index = max_rating_a_index
		max_rating_a_index = student_index
	else:
		if(student_ratings[student_index] > student_ratings[max_rating_b_index]):
			max_rating_c_index =max_rating_b_index
			max_rating_b_index = student_index
		else:
			if(student_ratings[student_index] > student_ratings[max_rating_c_index]):
				max_rating_c_index = student_index

print()
for sign_index in range(40):
	print('$$',end = " ")

print('\n\n3.Индексы(номера) 3-х студентов, чьи рейтинги самые высокие: ')
print('Студент под номером {} с рейтингом {}.'.format(max_rating_a_index + INDEX_STEP,student_ratings[max_rating_a_index]))
print('Студент под номером {} с рейтингом {}.'.format(max_rating_b_index + INDEX_STEP,student_ratings[max_rating_b_index]))
print('Студент под номером {} с рейтингом {}.'.format(max_rating_c_index + INDEX_STEP,student_ratings[max_rating_c_index]))

print()
for sign_index in range(40):
	print('$$',end = " ")

print('\n\nСпасибо за использование программы! До свидания!')

