print('Здравствуйте! Добро пожаловать в программу "Тест "Зануда или ',end = "")
print('экстремал ?""\nОна будет задавать вам по очереди вопросы с ',end = "")
print('вариантами ответов (А,Б или В) и вы сможете выбрать только 1 ответ', end ="")
print(' из возможных, введя соответсвующую букву.')
print('За каждый ответ вы получите соответсвующую балл, сумма которых ',end = "")
print('по окончанию выдаст вам результат\n')

questions = []
questions.append('Какое впечатление произвело на вашу вторую половину первое свидание с вами?')
questions.append('Каким способом вы привыкли зарабатывать на жизнь?')
questions.append('Любите ли вы поспорить? Если когда-нибудь вы совершали неординарные поступки в связи с проигрышем, на что из перечисленного ниже это было похоже?')
questions.append('Что вы делали вчера вечером?')
questions.append('Какую одежду вы обычно носите?')
questions.append('Что вы надели, собираясь на первый экзамен при поступлении в вуз?')
questions.append('Вообразите, что вам вдруг представился уникальный шанс превратиться в великого творца всего сущего, то есть в самого Бога. Каковы будут ваши первые действия после свершения метаморфозы?')

answers = []
answers.append('A. Он(а) выразил(а) свои ощущения примерно так: "Кайф! Просто здорово! Я хочу повторить это, и не раз"')
answers.append('Б. Он(а) смутно об этом помнит')
answers.append('В. У меня нет второй половины')
answers.append('А. Один из способов - продажа ненужных вещей, второй - работа менеджером, а третий зависит от обстоятельств')
answers.append('Б. Вот уже несколько лет я гну спину над станком на своем заводе и довольствуюсь тем, что имею')
answers.append('В. До нелегальной перевозки наркотиков через границу я еще не дорос, но занимаюсь одним очень интересным делом, о котором по понятным причинам не желаю распространяться')
answers.append('А. Скорее нет, чем да. Но фруктовое мыло все же пришлось попробовать')
answers.append('Б. Куда же без них? Прыжки с большой высоты, ныряние на приличную глубину, покорение деревьев... А почему же, по-вашему, у меня рука в гипсе')
answers.append('В. Вы бы видели лицо моего декана лет пять тому назад, в тот самый день открытых дверей, когда каждый, подходивший к его кабинету, мог прочесть надпись: «Продаю места абитуриентам! Большой выбор: бюджетные и коммерческие, очное и заочное отделения! Первым пяти клиентам скидка!!!»')
answers.append('А. Странный вопрос. Понятное дело: играл(а) в компьютерные игры и смотрел(а) телевизор')
answers.append('Б. Лучше не спрашивайте. Это напоминает о головной боли, от которой не помогает даже огуречный рассол')
answers.append('В. Гонял(а) по шоссе на своем «харлее»')
answers.append('A. Брюки, пиджаки и туфли… В основном классику, я ведь интеллигентный человек')
answers.append('Б. Неважно какую, главное – моднее, чем у всех окружающих')
answers.append('B. В зависимости от того, куда направляюсь. Впрочем, мне ничего не стоит прийти на работу в майке с надписью: «Хочу быть начальником!»')
answers.append('А. Обычные вещи: в таких случаях не церемонюсь. Правда, в этот раз я взял(а) с собой цветы')
answers.append('Б. Конечно, строгий костюм и до блеска начищенные туфли, ведь мне нужно было произвести выгодное впечатление')
answers.append('В. Специально для такого случая сделал(а) временную татуировку на руке с внешней стороны, на шею повесил(а) цепь, надел(а) черную куртку с заклепками, уложил(а) волосы соответствующим образом… Словом, сразил(а) всех наповал')
answers.append('А. Наконец-то я смогу осуществить свои самые заветные желания! Куплю себе пару островов, две яхты, три самые крутые тачки, слетаю в космос')
answers.append('Б. Забью «стрелу» нечистому и «сделаю» его, чтобы до народа не «докапывался»')
answers.append('В. Превращу всю морскую воду в пиво! Вот здорово было бы: и много, и бесплатно, и не заканчивается')

points = [3,2,1,2,1,3,1,3,2,1,2,3,1,2,3,2,1,3,2,3,1]

ANSWER_ONE_OPTION = 'А'
ANSWER_TWO_OPTION = 'Б'
ANSWER_THREE_OPTION = 'В'

sum_user_points = 0
index = 0
MAX_NUMBER_QUESTIONS = 7
ONE_STEP = 1
ANSWERS_PER_QUESTION = 3
ANSWER_A_OPTION = 0
ANSWER_B_OPTION = 1
ANSWER_C_OPTION = 2
while(index < MAX_NUMBER_QUESTIONS):
	print('Вопрос # {}:'.format(index + ONE_STEP),questions[index])
	print('Ваши возможные варинаты ответов:',end = "\n")
	minimum_answer_option = index * ANSWERS_PER_QUESTION
	maximum_answer_option = (index * ANSWERS_PER_QUESTION) + ANSWERS_PER_QUESTION 
	for answer_index in range(minimum_answer_option,maximum_answer_option):
		print(answers[answer_index],end = "\n")
	print('Пожалуйста, введите А,Б или В')

	user_answer = input('Пожалуйста, введите свой ответ (А, Б или В): ')

	while(user_answer != ANSWER_ONE_OPTION and user_answer != ANSWER_TWO_OPTION and user_answer != ANSWER_THREE_OPTION):
		user_answer = input('Нет такого варианта ответа, пожалуйста выберите между А, Б или В: ')

	print()

	index_point = index * ANSWERS_PER_QUESTION
	if(user_answer == ANSWER_ONE_OPTION):
		index_point += ANSWER_A_OPTION
	elif(user_answer == ANSWER_TWO_OPTION):
		index_point += ANSWER_B_OPTION
	elif(user_answer == ANSWER_THREE_OPTION):
		index_point += ANSWER_C_OPTION
	sum_user_points += points[index_point]
	index += ONE_STEP

MAX_POINTS_LOWER_EXTREME = 9

MIN_POINTS_MIDDLE_EXTREME = 10
MAX_POINTS_MIDDLE_EXTREME = 15

MIN_POINTS_HARD_EXTREME = 16
MAX_POINTS_HARD_EXTREME = 21

print('Ваши баллы составляют: ' + str(sum_user_points))

if(sum_user_points <= MAX_POINTS_LOWER_EXTREME ):
	print('Как ни крути, но экстремала из вас не выйдет... Нужно признать', end = "")
	print(', что вы самый настоящий зануда. И как только вас друзья ',end = "")
	print('терпят? Так, пожалуй, и умереть можно от скуки!')
	print('\nНе стоит подвергать риску своих ближних, поэтому ждем ', end = "")
	print('исправления, пусть вам в помощь будут следующие советы.')
	print('\n1. Включите фантазию. Найдите ее, даже если она закрыта ',end = "")
	print('слишком глубоко и кажется недосягаемой. Она у вас есть, мы в это верим!')
	print('\n2. Вспомните о том? что в жизни можно многое попробовать, ',end = "")
	print('и поставьте себе определенные цели (не противоречащие закону,', end = "")
	print('моральным нормам и кодексу чести настоящих друзей).')
	print('\n3. Откройте глаза шире: на свете столько всего интересного ',end ="")
	print('и полезного!')
elif(sum_user_points >= MIN_POINTS_MIDDLE_EXTREME and 
	sum_user_points <= MAX_POINTS_MIDDLE_EXTREME):
	print('Нет, вы тоже не экстримал, хотя кое в чем на него все-таки ',end = "")
	print('похожи. В целом вы выглядите вполне прилично. Надо признать,',end = "")
	print('что с вами не соскучишься, но и отвлечься от ежедневной ', end = "")
	print('рутины тоже нечасто удается. Однако умерененность - это ', end = "")
	print('хорошее качество, тем более для того, кто общается с людьми ',end = "")
	print('в меру темпераментными и по своей натуре довольно серьезен.')
elif(sum_user_points >= MIN_POINTS_HARD_EXTREME and 
	sum_user_points <= MAX_POINTS_HARD_EXTREME):
	print('Вот он, настоящий экстремал с большой буквы! Живость и ',end = "")
	print('подвижность, сумасбродство и постоянное стремление вперед ',end = "")
	print('навстречу приключениям, любовь к опасностям и постоянное ',end = "")
	print('желание получить дозу адреналина - основа вашей бурной жизни.')
	print('\nХотя, возможно, это только ее часть. Экстремальная сущность',end = "")
	print(' не исключает серьезности, а вот с ощущением меры у вас ',end = "")
	print('могут возникать проблемы.')
	print('\nЖивите и радуйтесь, только постарайтесь не перегнуть палку,',end = "")
	print(' то есть, проще говоря, не сломайте себе шею. И прислушайтесь',end = "")
	print(' к совету родственников и друзей: они ничего плохого ',end = "")
	print('не пожелают!')
print('\nСпасибо за использование программы! До свидания!')