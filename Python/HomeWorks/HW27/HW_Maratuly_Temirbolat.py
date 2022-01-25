import datetime
import time

TIME_FORMAT = '%d.%m.%Y %H:%M'
CHANGED_TIME_FORMAT_DATE = '%d.%m.%Y'
CHANGED_TIME_FORMAT = '%H:%M'

FIND_BY_NAME_OPTION = '1'
FIND_BY_DATE_TIME_OPTIONS = '2'
find_options = (FIND_BY_NAME_OPTION,FIND_BY_DATE_TIME_OPTIONS)

DELETE_EVENT_OPTION = '1'
CHANGE_EVENT_OPTION = '2'
event_otions = (DELETE_EVENT_OPTION,CHANGE_EVENT_OPTION)

CHANGE_DATE_OPTION = '1'
CHANGE_TIME_OPTION = '2'
change_options = (CHANGE_DATE_OPTION,CHANGE_TIME_OPTION)

events = {

}
GO_OUT_OPTION = "exit"
days = [ "Понедельник", "Вторник", "Среда", "Четверг", "Пятница","Суббота", "Воскресенье" ]
months = [ "", "января", "февраля", "марта", "апреля", "мая", "июня",
"июля", "августа", "сентября", "октября", "ноября", "декабря" ]

def get_todays_time_gate():
    return time.localtime()

def view_todays_time_date():
    time_date = get_todays_time_gate()
    week_day_index = time_date[6]
    month_index = time_date[1]
    day_number = time_date[2]
    year = time_date[0]
    print()
    print('Сегодня: {} {} {} {} года '.format(days[week_day_index],day_number,months[month_index],year))
    print('Текущее время: {}:{}:{}'.format(time_date[3],time_date[4],time_date[5]))
    print()

def get_left_time_event(event_date_time):
    todays_passed_seconds = int(time.mktime(time.localtime()))
    event_passed_seconds = int(time.mktime(event_date_time))
    time_difference_seconds = event_passed_seconds - todays_passed_seconds
    return time_difference_seconds

def get_formated_time(event_time_seconds):
    left_time = str(datetime.timedelta(seconds = event_time_seconds))
    if('days' in left_time):
        left_time = left_time.replace('days', 'дней/дня')
    return left_time

def view_all_set_events():
    if(len(events) != 0):
        print('\nВсе ваши назначенные события:')
        for event in events:
            print('Событие: "{}" с датой {} {} {} {} года'.format(event,days[events[event][6]],events[event][2],months[events[event][1]],events[event][0]),end = ' ')
            print('и временем: {}:{}'.format(events[event][3],events[event][4]),'Описание:',end = "")
            left_time_event = get_left_time_event(events[event])
            if(left_time_event > 0):
                print('\tосталось времени до события: ' + get_formated_time(left_time_event))
            else:
                print('\tсобытие прошло')
    else:
        print('\nИзвините, ваш список событий пуст')

def view_change_event_options():
    print('Все возможные опции:')
    print('\t\t\t 1) Поменять Дату события')
    print('\t\t\t 2) Поменять Время события')

def change_time_event(event_name):
    print('\nВы решили изменить ВРЕМЯ события "{}"'.format(event_name))
    print('Пожалуйста введите новое ВРЕМЯ для события "{}"'.format(event_name))
    new_time = input('Введите новое время для события в формате "HH:MM": ')
    new_time = '{}.{}.{}'.format(events[event_name][2],events[event_name][1],events[event_name][0]) + ' ' + new_time
    new_time = time.strptime(new_time,TIME_FORMAT)
    events[event_name] = new_time
    print('Время события "{}" успешно изменено!'.format(event_name))

def change_date_event(event_name):
    print('\nВы решили изменить ДАТУ события "{}"'.format(event_name))
    print('Пожалуйста введите новую дату для события "{}"'.format(event_name))
    new_date = input('Введите новую дату события в формате "dd.mm.YYYY": ')
    new_date = new_date + ' ' + '{}:{}'.format(events[event_name][3],events[event_name][4])
    new_date = time.strptime(new_date,TIME_FORMAT)
    events[event_name] = new_date
    print('Ваша дата успешно изменена!')

def delete_event(event_name):
    print('\nВы решили удалить событие')
    del events[event_name]
    print('Событие "{}" успешно удалено!'.format(event_name))
    print()

def view_find_options():
    print('\nВсе возможные опции по поиску:')
    print('\t\t\t 1) Найти событие по Имени')
    print('\t\t\t 2) Найти событие по Дате и Времени')

def view_event_options():
    print('\nВсе возможные опции: ')
    print('\t\t\t 1) Удалить событие')
    print('\t\t\t 2) Изменить событие')

def modify_event(event_name):
    print('\nЧто вы хотите сделать с событием "{}"?'.format(event_name))
    view_event_options()
    user_option = input('Ваш выбор: ')
    while(user_option not in event_otions):
        print('Извините, но такой опции нет. Повторите пожалуйста ввод')
        view_event_options()
        user_option = input('Ваш выбор: ')
    if(user_option == DELETE_EVENT_OPTION):
        delete_event(event_name)
    else:
        print('Что вы хотите изменить?')
        view_change_event_options()
        user_choice = input('Ваш выбор: ')
        while(user_choice not in change_options):
            print('Извините, но такой опции нет. Повторите попытку')
            view_change_event_options()
            user_choice = input('Ваш выбор: ')
        if(user_choice == CHANGE_DATE_OPTION):
            change_date_event(event_name)
        else:
            change_time_event(event_name)


def fint_event_by_date():
    print('\nВы решили найти событие по указанной вами дате и времени')
    user_find_time = ask_time_event()
    all_dates = list(events.values())
    if(user_find_time in all_dates):
        event_index = all_dates.index(user_find_time)
        counter = 0
        found_event = ''
        for event in events:
            if(counter == event_index):
                found_event = event
                break
            counter += 1
        modify_event(found_event)
    else:
        print('Извините, но такого события нет')

def find_event_by_name():
    print('\nПожалуйста, укажите название события, которое вы хотите найти')
    event_name = input('Укажите название события либо "exit", чтобы выйти в главное меню: ')
    while(event_name not in events and event_name != GO_OUT_OPTION):
        print('Извините, такого события нет...Повторите попытку или',end = " ")
        print('напечатайте "exit" чтобы вернуться в главное меню')
        event_name = input('Укажите название события либо "exit", чтобы выйти в главное меню: ')
    if(event_name == GO_OUT_OPTION):
        print('Возвращаемся в главное меню...')
        return
    
    modify_event(event_name)


def ask_time_event():
    print('\nУкажите интересующее вас время и дату в формате dd.mm.YYYY HH:MM',end = ', ')
    print('где dd - номер дня, mm - номер месяца, YYYY - номер года',end = " ")
    print('HH - часы, MM - число минут')
    user_given_time = input('Укажите время и дату в формате "dd.mm.YYYY HH:MM": ')
    user_time = time.strptime(user_given_time,TIME_FORMAT)
    return user_time


def add_new_event():
    print('\nВы решили добавить новое событие')
    print('Пожалуйста, укажите название для нового события или напишите',end = ' ')
    print('"exit", чтобы вернуться в главное меню')
    new_event_name = input('Название для нового события: ')
    while(new_event_name in events and new_event_name != GO_OUT_OPTION):
        print('Извините, такое событие уже существует. Придумайте ',end = "")
        print('пожалуйста другое Название для события. Либо ',end = '')
        print('напишите "exit", чтобы вернуться в главное меню')
        new_event_name = input('Название для нового события: ')
    if(new_event_name == GO_OUT_OPTION):
        print('\nВозвращаемся в главное меню...')
        return
    print('Пожалуйста, укажите дату и время для предстоящего события')
    new_event_date_time = ask_time_event()
    events.setdefault(new_event_name,new_event_date_time)
    print('Ваше событие "{}" успешно добавлено!'.format(new_event_name))

def find_event():
    print('\nВы решили найти событие. Пожалуйста, выберите метод поиска события')
    print('Если вы хотите вернуться в главное меню, то напишите "exit"')
    view_find_options()
    user_option = input('Ваш выбор: ')
    while(user_option not in find_options and user_option != GO_OUT_OPTION):
        print('Извините, но такой опции нет. Пожалуйста повторите ',end = "")
        print('запрос или напишите "exit" для выхода в главное меню')
        view_find_options()
        user_option = input('Ваш выбор: ')
    is_found_event = False
    found_event_index = -1
    if(user_option == GO_OUT_OPTION):
        print('Возвращаемся в главное меню...')
        return
    elif(user_option == FIND_BY_NAME_OPTION):
        is_found_event = find_event_by_name()
    else:
        found_event_index = fint_event_by_date()

EXIT_OPTION = '0'
ADD_NEW_EVENT_OPTION = '1'
FIND_EVENT = '2'
VIEW_ALL_EVENTS_OPTION = '3'
VIEW_TODAY_DATE_TIME_OPTION = '4'
main_program_options = (EXIT_OPTION,ADD_NEW_EVENT_OPTION,FIND_EVENT,VIEW_ALL_EVENTS_OPTION,VIEW_TODAY_DATE_TIME_OPTION)
def view_main_options():
    print('\nВсе доступные опции:')
    print('\t\t\t 0) Выйти из программы')
    print('\t\t\t 1) Добавить новое событие')
    print('\t\t\t 2) Найти событие')
    print('\t\t\t 3) Просмотреть все события')
    print('\t\t\t 4) Просмотреть сегодняшнюю Дату и Время')
    
def start_main_program():
    print('Здравствуйте! Добро пожаловать в программу, которая выводит все',end = " ")
    print('предстоящии события, дату и время наступления события. Программа',end = " ")
    print('выводит сколько времени (дней, часов, минут, секунд) осталось до',end = " ")
    print('того или иного события.')

    is_start_program = True
    print('\nНачнем программу...')
    while(is_start_program):
        print('\nПожалуйста, выберите одну из доступных опций')
        view_main_options()
        user_option = input('Ваш выбор: ')
        if(user_option not in main_program_options):
            print('Извините, такой опции нет. Повторите попытку')
            continue
        elif(user_option == EXIT_OPTION):
            print('Спасибо за использование программы.До свидания')
            break
        elif(user_option == ADD_NEW_EVENT_OPTION):
            add_new_event()
        elif(user_option == VIEW_ALL_EVENTS_OPTION):
            view_all_set_events()
        elif(user_option == VIEW_TODAY_DATE_TIME_OPTION):
            view_todays_time_date()
        else:
            find_event()

start_main_program()