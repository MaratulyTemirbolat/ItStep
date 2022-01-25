import datetime

DATE_TIME_FORMAT = '%d.%m.%Y %H:%M:%S'

SECONDS_PER_DAY = 86400
SECONDS_PER_MINUTE = 60

EXIT_PROGRAM = '0'
FIRST_TASK_OPTION = '1'
SECOND_TASK_OPTION = '2'
THIRD_TASK_OPTION = '3'
FOURTH_TASK_OPTION = '4'
program_options = (EXIT_PROGRAM,FIRST_TASK_OPTION,SECOND_TASK_OPTION,THIRD_TASK_OPTION,FOURTH_TASK_OPTION)


def input_date_time():
    print('\nПожалуйста, введите желаемое время и дату в формате: ',end = "")
    print('dd.mm.YYYY HH:MM:SS')
    user_time_date = input('Введите дату и время в формате "dd.mm.YYYY HH:MM:SS": ')
    user_time_date = datetime.datetime.strptime(user_time_date,DATE_TIME_FORMAT)
    return user_time_date

def calculate_time_difference(start_time,end_time):
    passed_seconds = end_time.timestamp() - start_time.timestamp()
    return passed_seconds

def view_passed_days(start_time,end_time,passed_seconds):
    passed_days = int(passed_seconds // SECONDS_PER_DAY)
    print('\nКоличество дней прошедших \
с {} по {} составляет {} дней/дня/день'.format(start_time,end_time,passed_days))

def view_passed_seconds(start_time,end_time,passed_seconds):
    print('\nКоличество секунд, прошедших \
с {} по {} составляет {} секунд'.format(start_time,end_time,int(passed_seconds)))

def view_passed_minutes(start_time,end_time,passed_seconds):
    passed_minutes = int(passed_seconds // SECONDS_PER_MINUTE)
    print('\nКоличество минут прошедших \
с {} по {} составляет {} минут'.format(start_time,end_time,passed_minutes))

def view_program_options():
    print('\nВсе возможные опции программы:')
    print('\t\t\t0) Выйти из программы')
    print('\t\t\t1) Вывести количество дней прошедших между датами')
    print('\t\t\t2) Вывести количество секунд прошедших между датами')
    print('\t\t\t3) Вывести количеству минут дней прошедших между датами')
    print('\t\t\t4) Ввести другие даты со временем')

def view_program_description():
    print('Здравствуйте! Добро пожаловать в программу, которая принимает',end = " ")
    print('от пользователя две даты и времени, затем программа: ')
    print('\t\t\t 1. Выведет количество дней прошедших между первым и ',end = '')
    print('вторым введённым временами')
    print('\t\t\t 2. Выведет количество секунд, прошедших между первым ',end = '')
    print('и вторым временем')
    print('\t\t\t 3. Выведете количество минут, прошедших между первым ',end = '')
    print('и вторым временем')

def start_main_program():
    view_program_description()
    time_date_beginning,time_date_end = input_date_time(),input_date_time()
    time_date_beginning,time_date_end = min(time_date_beginning,time_date_end),max(time_date_beginning,time_date_end)
    while(True):
        print('\nПожалуйста введите одну из представленных опций')
        view_program_options()
        user_option = input('Ваш выбор: ')
        if(user_option not in program_options):
            print('\nИзвините, такой опции нет...Повторите попытку')
            continue
        elif(user_option == EXIT_PROGRAM):
            print('Спасибо за использование программы. До свидания!')
            break
        elif(user_option == FOURTH_TASK_OPTION):
            time_date_beginning,time_date_end = input_date_time(),input_date_time()
            time_date_beginning,time_date_end = min(time_date_beginning,time_date_end),max(time_date_beginning,time_date_end)
        else:
            passed_seconds = calculate_time_difference(time_date_beginning,time_date_end)
            if(user_option == FIRST_TASK_OPTION):
                view_passed_days(time_date_beginning,time_date_end,passed_seconds)
            elif(user_option == SECOND_TASK_OPTION):
                view_passed_seconds(time_date_beginning,time_date_end,passed_seconds)
            elif(user_option == THIRD_TASK_OPTION):
                view_passed_minutes(time_date_beginning,time_date_end,passed_seconds)

start_main_program()