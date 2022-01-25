import re
# ^[a-zA-Z]+[0-9]*@[a-z]+\.[a-z]{2}$  
# ^[0-9]{2}-[0-9]{2}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}$

EXIT_OPTION = '0'
EXERCISE_ONE_OPTION = '1'
EXERCISE_TWO_OPTION = '2'
menu_options = (EXIT_OPTION,EXERCISE_ONE_OPTION,EXERCISE_TWO_OPTION)

MIN_DAY = 1
MAX_DAY = 31

MIN_MONTH = 1
MAX_MONTH = 12

MAX_HOURS = 23
MAX_MINUTES = 59
MAX_SECONDS = 59

def is_correct_date_range(day,month,year):
    day = int(day)
    month = int(month)
    year = int(year)
    if((day >= MIN_DAY and day <= MAX_DAY) and (month >= MIN_MONTH and month <= MAX_MONTH)):
        return True
    return False


def is_correct_time_range(hours,minutes,seconds):
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    if(hours <= MAX_HOURS and minutes <= MAX_MINUTES and seconds <= MAX_SECONDS):
        return True
    return False

def is_correct_date_time(user_date_time):
    user_date_time = user_date_time.split(' ')
    date_part = user_date_time[0].split('-')
    time_part = user_date_time[1].split(':')
    date_checker = is_correct_date_range(date_part[0],date_part[1],date_part[2])
    time_checker = is_correct_time_range(time_part[0],time_part[1],time_part[2])
    if(date_checker == True and time_checker == True):
        return True
    return False

def start_exercise_one():
    print('\nВы решили запустить первое задание...')
    print('\nПожалуйста, напечатайте строку email, учитывая следующее:')
    print('1) Все должно быть написано латиницей')
    print('2) Обязательно должны содержаться символы "@" и "."')
    print('3) После точки должно быть два символа')
    print('Пример валидного email: Temirbolatm2001@kbtu.kz')
    user_email = input('\nПожалуйста, введите ваш email: ')
    result = re.fullmatch('^[a-zA-Z]+[0-9]*@[a-z]+\.[a-z]{2}$',user_email)
    print()
    if(result):
        print('Поздравляем! Ваш email соответствует нашим стандартам')
    else:
        print('Извините, но вы совершили ошибку. Повторите попытку')

def start_exercise_two():
    print('\nВы решили запустить второе задание...')
    print('Пожалуйста, напечатайте дату и время, соответствующая формату ',end = "")
    print('"ДД-MM-ГГГГ ЧЧ:ММ:СС"')
    user_date_time = input('Пожалуйста, введите дату и время: ')
    result = re.fullmatch('^[0-9]{2}-[0-9]{2}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}$',user_date_time)
    print()
    if(result):
        if(is_correct_date_time(user_date_time) == True):
            print('Поздравляем! Ваш Дата и Время введены правильно')
        else:
            print('Формат Правильный! Но вы вышли за диапазон допустимых значений!')
    else:
        print('Извините, но вы совершили ошибку. Повторите попытку')

def view_menu_options():
    print('\nВсе возможные опции:')
    print('\t\t0) Выйти из программы.')
    print('\t\t1) Запустить первое задание.')
    print('\t\t2) Запустить второе задание.')

def start_main_program():
    print('\nЗдравствуйте! Добро пожаловать в программу с домашним заданием.')
    print('Здесь будут представлены 2 задачи, каждую из которых вы ',end = "")
    print('можете запустить.')
    while(True):
        print('\nПожалуйста, выберите одну из представленных опций ниже')
        view_menu_options()
        user_option = input('Ваш выбор: ')
        if(user_option not in menu_options):
            print('Извините, но такой опции нет. Повторите попытку')
            continue
        elif(user_option == EXIT_OPTION):
            print('Спасибо за использование программы! До свидания!')
            break
        elif(user_option == EXERCISE_ONE_OPTION):
            start_exercise_one()
        elif(user_option == EXERCISE_TWO_OPTION):
            start_exercise_two()

start_main_program()