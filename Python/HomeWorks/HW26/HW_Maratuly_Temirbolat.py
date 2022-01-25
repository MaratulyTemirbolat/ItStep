import time
EXIT_PROGRAM_OPTION = 'exit'
FIRST_EXERCISE_OPTION = '1'
SECOND_EXERCISE_OPTION = '2'
THIRD_EXERCISE_OPTION = '3'
FOURTH_EXERCISE_OPTION = '4'
menu_options = (FIRST_EXERCISE_OPTION,SECOND_EXERCISE_OPTION,THIRD_EXERCISE_OPTION,FOURTH_EXERCISE_OPTION,EXIT_PROGRAM_OPTION)

# Exercise 1
def start_exercise_one():
    print()
    print('Здравствуйте! Добро пожаловать в программу, которая принимает',end = " ")
    print('от пользователя формат времени в котором он/она хочет увидеть ',end = "")
    print('текущее время')

    print('\nПеред тем как писать соответствующий формат, пишите %')
    user_time_format = input('Пожалуйста, введите желаемый формат времени: ')

    print('Время в желаемом вами формате:',time.strftime(user_time_format))


#Exercise 2
def start_exercise_two():
    print()
    print('Здравствуйте! Добро пожаловать в программу, которая',end = " ")
    print('принимает от пользователя количество секунд, прошедшее',end = " ")
    print('с начала эпохи UNIX, а затем выведет на экран время в ',end = "")
    print('формате текущей локализации.')

    user_passed_seconds = int(input('\nПожалуйста, введите пройденные секунды: '))
    print('Дата соответсвующая количеству секунд указанных вами:',time.ctime(user_passed_seconds))


#Execise 3

def get_passed_seconds_to_origin():    
    user_format = input('\nПожалуйста, введите формат времени: ')
    user_day_time = input('Пожалуйста, введите время соответствующее вашему формату: ')

    user_day_time_struct = time.strptime(user_day_time,user_format)
    passed_seconds_origin = time.mktime(user_day_time_struct)
    return passed_seconds_origin

def start_exercise_three():
    print()
    print('Здравствуйте! Добро пожаловать в программу, которая',end = " ")
    print('примет от пользователя формат даты и времени,',end = " ")
    print('затем дату и время,в заданному пользователем формате.')
    print('Программа выведет на экран количество секунд, которое ',end = "")
    print('прошло с начала эпохи UNIX.')

    passed_seconds = get_passed_seconds_to_origin()

    print('\nКоличество секунд, прошедшее от начала эпохи UNIX ',end = "")
    print('согласно вашим данным: ',passed_seconds,'секунд')

#Exercise 4
def start_exercise_four():
    print()
    print('Здравствуйте! Добро пожаловать в программу, которая', end = " ")
    print('примет от пользователя формат даты и времени,', end = " ")
    print('затем дату и время, в заданном вами формате.')
    print('Программа выведет на экран количество секунд, прошедшее ',end = "" )
    print('с начала эпохи UNIX, а также время прошедшее от заданного ', end = "")
    print('времени до текущего.')

    passed_seconds = get_passed_seconds_to_origin()
    print('\nКоличество секунд, прошедшее от начала эпохи UNIX ',end = "")
    print('согласно вашим данным: ',passed_seconds,'секунд.')
    print('\nСекунды, прошедшие с указанного времени до текущего:',end = " ")
    print(int(time.mktime(time.gmtime()) - passed_seconds),'секунд.')

def view_available_exercises():
    print('\nНапечатайте цифру одну из показанных ниже, или "exit",чтобы выйти:')
    print('\t\t\t 0) Напечатайте "exit", чтобы выйти из программы')
    print('\t\t\t 1) Напечатайте 1, чтобы запустить первое задание')
    print('\t\t\t 2) Напечатайте 2, чтобы запустить второе задание')
    print('\t\t\t 3) Напечатайте 3, чтобы запустить третье задание')
    print('\t\t\t 4) Напечатайте 4, чтобы запустить четвёртое задание')

def start_main_program():
    print('\nЗдравствуйте! Добро пожаловать в программу!')
    print('Вы можете запустить 1 из 4 домашних заданий на ваш выбор.',end = " ")
    print('Ниже будут представлены все инструкции...')
    while(True):
        view_available_exercises()
        user_option = input('Введите необходимый номер задачи: ')
        if(user_option not in menu_options):
            print('Вы выбрали не ту опцию... Повторите ввод!')
            continue
        elif(user_option == FIRST_EXERCISE_OPTION):
            start_exercise_one()
        elif(user_option == SECOND_EXERCISE_OPTION):
            start_exercise_two()
        elif(user_option == THIRD_EXERCISE_OPTION):
            start_exercise_three()
        elif(user_option == FOURTH_EXERCISE_OPTION):
            start_exercise_four()
        elif(user_option == EXIT_PROGRAM_OPTION):
            break
    print('\nСпасибо за использование программы! До свидания!')

start_main_program()