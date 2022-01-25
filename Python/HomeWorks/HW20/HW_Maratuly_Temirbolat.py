from random import *

MAX_ASKED_QUESTIONS = 7
MAX_QUESTION = 14
MIN_QUESTION = 0
ONE_STEP = 1
MAX_ANSWERS = 3
NON_USED_INDEX = -1
ALL_CORRECT_ANSWERS_PERCENTS = 100

def get_answer_index(question_index,answer_index_a = NON_USED_INDEX,answer_index_b = NON_USED_INDEX):
	answer_index = randint(MAX_ANSWERS * question_index,(MAX_ANSWERS * question_index) + ONE_STEP + ONE_STEP)
	while(answer_index == answer_index_a or answer_index == answer_index_b):
		answer_index = randint(MAX_ANSWERS * question_index,(MAX_ANSWERS * question_index) + ONE_STEP + ONE_STEP)
	return answer_index

print('Здравсвтуйте! Добро пожаловать в программу, которая проверит ',end = "")
print('ваши теоретические познания в области основ программирования.')
print('Всего в программе будет 15 вопросов, вам же из них попадуться ',end = "")
print('только 7 на которые вам нужно дать ответ.')
print('На каждый вопрос будет дано 3 ответа, один из которых только верный.')
print('После ответа на все выданные вопросы, вам будет выдан процент ',end= "")
print('верно отвеченных вопросов, а также неправильных.')
print('Чтобы ответить на вопрос выбирайте между символами: а,б или с')

questions = []
questions.append('Какой оператор позволяет досрочно прервать выполнение действий в цикле и досрочно выйти из него?') #break
questions.append('Дизъюнкция это какая логическая операция?') #Бинарная
questions.append('Инверсия это какая логическая операция?') #Унарная
questions.append('Какое руководство по коду используют в Python?') # PEP8
questions.append('Какой символ программисты используют, чтобы указать комментарий?') #
questions.append('Когда мы хотим написать условие, с чего мы его всегда начинаем писать согласно синтаксису(Первое условие)?') # if
questions.append('Что такое список?') 
questions.append('Какой цикл не используется в Python из ниже приведенных?') # do while
questions.append('Что такое Конкатенация строк?')
questions.append('Что из ниже приведенных не может быть по типу Булевым?') # 5
questions.append('Что из ниже приведенных по типу данных являетя строкой?') # "Temirbolat"
questions.append('Конъюнкция это какая логическая операция?') #Бинарная
questions.append('Какие операторы называются тернарными?')
questions.append('Какой оператор позволяет досрочно прервать выполнение текущей итерации и перейти к проверке условия?') #continue
questions.append('Какая специальная инструкция позволяет использовать функции, находящиеся в разных модулях?') #import

answers = []

answers.append('break')
answers.append('stop')
answers.append('continue')

answers.append('Бинарная')
answers.append('Унарная')
answers.append('Тернарная')

answers.append('Унарная')
answers.append('Бинарная')
answers.append('Тернарная')

answers.append('PEP8')
answers.append('PY2')
answers.append('SNAKE3')

answers.append('#')
answers.append('//')
answers.append('/**/')

answers.append('if')
answers.append('elif')
answers.append('else')

answers.append('Именнованный набор пронмерованных переменных')
answers.append('Именованный, функционально завершённый блок программы, который можно вызвать из любого места программы')
answers.append('Любой файл с программным кодом')

answers.append('do while')
answers.append('while')
answers.append('for')

answers.append('Это операция склеивания строк')
answers.append('Это операция получения адреса текущей строки')
answers.append('Это операция разделения строк')

answers.append('5')
answers.append('False')
answers.append('True')

answers.append('\'Temirbolat\'')
answers.append('5.5')
answers.append('False')

answers.append('Бинарная')
answers.append('Унарная')
answers.append('Тернарная')

answers.append('Операторы, которым необходимо 3 операнда')
answers.append('Операторы, которым необходим 1 операнд')
answers.append('Операторы, которым необходимо 2 операнда')

answers.append('continue')
answers.append('skip')
answers.append('break')

answers.append('import')
answers.append('download')
answers.append('use')

POSSIBLE_ANSWER_A = 'а'
POSSIBLE_ANSWER_B = 'б'
POSSIBLE_ANSWER_C = 'с'


used_questions = []

correct_answers_number = 0

print()

for current_question_index in range(MAX_ASKED_QUESTIONS):
	question_index = randint(MIN_QUESTION,MAX_QUESTION)
	while(question_index in used_questions):
		question_index = randint(MIN_QUESTION,MAX_QUESTION)

	print('Вопрос #{}:'.format(current_question_index + ONE_STEP),questions[question_index])
	print('\nВарианты ответов: ')

	answer_a_index = get_answer_index(question_index = question_index)
	print('\na)',answers[answer_a_index])
	
	answer_b_index = get_answer_index(question_index = question_index,answer_index_a = answer_a_index)
	print('б)',answers[answer_b_index])

	answer_c_index = get_answer_index(question_index = question_index,answer_index_a = answer_a_index,answer_index_b = answer_b_index)
	print('c)',answers[answer_c_index])

	user_answer = input('\nВаш вариант ответа: ')
	while(user_answer != POSSIBLE_ANSWER_A and user_answer != POSSIBLE_ANSWER_B and user_answer != POSSIBLE_ANSWER_C):
		print('Нужно выбирать между а,б или с.Пожалуйста повторите попытку.')
		user_answer = input('\nВаш вариант ответа: ')

	correct_answer_index = question_index * MAX_ANSWERS
	
	user_index = answer_a_index
	if(user_answer == POSSIBLE_ANSWER_B):
		user_index = answer_b_index
	elif(user_answer == POSSIBLE_ANSWER_C):
		user_index = answer_c_index

	if(user_index == correct_answer_index):
		correct_answers_number += ONE_STEP

	used_questions.append(question_index)
	print()

final_correct_percents = (correct_answers_number * ALL_CORRECT_ANSWERS_PERCENTS)/MAX_ASKED_QUESTIONS
print('Тест завершен. Мои поздравления! Вот ваши результаты: ')
print('Количество правильных вами ответов',correct_answers_number,end = " ")
print('из 7, что составляет {} процентов.'.format(final_correct_percents))
