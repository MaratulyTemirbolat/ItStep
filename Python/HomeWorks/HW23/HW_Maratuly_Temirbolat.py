
countries_capitals = {
    'Казахстан':'Астана',
    'Индия':'Дели',
    'Россия':'Москва'
}

def view_all():
    print()
    for key in countries_capitals.keys():
        print('Стране "{}" соответствует столица "{}"'.format(key,countries_capitals[key]))
    print()

def add_pair():
    print()
    country = input('Пожалуйста, введите Страну: ')
    capital = input('Пожалуйста, введите Столицу для вашей Страны: ')
    while(country in countries_capitals):
        print('Извините, но данная страна уже существует в вашем списке.')
        country = input('Пожалуйста, введите Страну: ')
    
    countries_capitals.setdefault(country,capital)
    print('Страна "{}" со столицей "{}" успешно добавлены!'.format(country,capital))
    print()

def delete_pair():
    print()
    country = input('Пожалуйста, введите Страну, которую хотите удалить: ')
    while(country not in countries_capitals):
        print('Страны "{}" нет в вашем словаре. Пожалуйста, повторите ввод.'.format(country))
        country = input('Пожалуйста, введите Страну, которую хотите удалить: ')
    
    capital = countries_capitals[country]
    del countries_capitals[country]
    print('Пара в виде "{}" --> "{}" успешна была удалена'.format(country,capital))
    print()

def correct_capital():
    print()
    country = input('Пожалуйста, введите страну, чью столицу вы хотите исправить: ')
    while(country not in countries_capitals):
        print('Страны "{}" нет в вашем словаре. Пожалуйста, повторите ввод.'.format(country))
        country = input('Пожалуйста, введите страну, чью столицу вы хотите исправить: ')
    
    old_capital = countries_capitals[country]
    print('Текущей столицей "{}" является "{}"'.format(country,old_capital))
    new_capital = input('Введите новую столицу для "{}": '.format(country))
    
    countries_capitals[country] = new_capital
    print('Ваш словарь успешно обновлен!')
    print()

def correct_country():
    print()
    country = input('Введите текущую страну, которую вы хотите изменить: ')
    while(country not in countries_capitals):
        print('Страны "{}" нет в вашем словаре. Пожалуйста, повторите ввод.'.format(country))
        country = input('Введите текущую страну, которую вы хотите изменить: ')
    current_capital = countries_capitals[country]
    new_country = input('Введите новую страну для столицы "{}": '.format(current_capital))
    while(new_country in countries_capitals):
        print('Извините, но страна "{}" уже занята в словаре. Введите другую!'.format(new_country))
        new_country = input('Введите новую страну для столицы "{}": '.format(current_capital))
    countries_capitals[new_country] = countries_capitals.pop(country)
    print('Страна с "{}" была успешно заменена на "{}"'.format(country,new_country))
    print()

def view_all_options():
    print('Все доступные опции: ')
    print('\t\t  0)Выйти из программы')
    print('\t\t  1)Просмотреть все доступные Страны и их Столицы')
    print('\t\t  2)Добавить новую Страну со Столицей')
    print('\t\t  3)Удалить Страну вместе с её Столицей')
    print('\t\t  4)Заменить Столицу у Страны')
    print('\t\t  5)Поменять текущую Страну на другую')

print('Здравствуйте! Добро пожаловать в программу, которая будет ',end = "")
print('отображать вам набор пар в виде Страна --> Столица')
print('Вы будете иметь возможность: добавлять, удалять, заменять страны',end = " ")
print('и их столицы.')

print('\nВы хотите начать программу? Если да, то напечатайте 1, в ',end ="")
print('противном случае напечатайте 0, чтобы выйти из программы')

EXIT_OPTION = '0'
ACCEPT_OPTION = '1'
VIEW_OPTION = '1'
INSERT_OPTION = '2'
DELETE_OPTION = '3'
CORRECT_CAPITAl_OPTION = '4'
CORRECT_COUNTRY_OPTION = '5'



user_option = input('Ваш выбор(1-начать программу, 0-завершить работу): ')
while(user_option != EXIT_OPTION and user_option != ACCEPT_OPTION):
    print('Вы напечатали несуществующую опцию. Пожалуйста, повторите попытку')
    user_option = input('Ваш выбор(1-начать программу, 0-завершить работу): ')

while(user_option != EXIT_OPTION):
    view_all_options()
    user_option = input('Ваш выбор в виде соответствующей цифры: ')
    while(user_option != EXIT_OPTION and user_option != VIEW_OPTION and 
    user_option != INSERT_OPTION and user_option != DELETE_OPTION and 
    user_option != CORRECT_CAPITAl_OPTION and user_option != CORRECT_COUNTRY_OPTION):
        print('Вы напечатали несуществующую опцию. Пожалуйста, повторите попытку')
        view_all_options()
        user_option = input('Ваш выбор в виде соответствующей цифры: ')
    
    if(user_option == VIEW_OPTION):
        view_all()
    elif(user_option == INSERT_OPTION):
        add_pair()
    elif(user_option == DELETE_OPTION):
        delete_pair()
    elif(user_option == CORRECT_CAPITAl_OPTION):
        correct_capital()
    elif(user_option == CORRECT_COUNTRY_OPTION):
        correct_country()

print('Спасибо за использование программы! До свидания!')