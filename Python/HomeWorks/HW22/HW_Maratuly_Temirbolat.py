from random import *

array = []

NUMBER_AMOUNT = 40
MIN_NUMBER = 0
MAX_NUMBER = 10
SECOND_ENTERENCE = 2
ONE_STEP = 1
EXIT_OPTION = '0'
ACCEPT_OPTIONS = '1'
UNITY_QUANTITY = 1

def get_enterence_number(array,target_number,option_enterence = SECOND_ENTERENCE):
    index_count = 1
    number_index = array.index(target_number)
    while(index_count != option_enterence):
        if(index_count == option_enterence):
            return number_index
        if(number_index + ONE_STEP < len(array)):
            number_index = array.index(target_number,number_index + ONE_STEP)
        index_count += ONE_STEP
    return number_index

def get_all_enterence(array,targer_number):
    index_count = 1
    answer = ''
    number_index = array.index(targer_number)
    while(index_count < array.count(targer_number)):
        answer += str(number_index) + ' '
        if(number_index + ONE_STEP < len(array)):
            number_index = array.index(targer_number,number_index + ONE_STEP)
        index_count += ONE_STEP
    answer += str(number_index) + ' '
    return answer

print('Здравствуйте! Добро пожаловать в программу, которая заполняет ',end = "")
print('список 40 случайными числами в диапазоне от 0 до 10')
print('После чего, программа находит: ')
print('a) Второе вхождение заданного пользователем числа')
print('б) Предпоследнего вхождения заданного числа в список')
print('с) Всех вхождений.')


user_option = 1
print('\nВы хотите начать работу программу? ')
print('Да (Нажмите 1)')
print('Нет (Нажмите 0)')

user_option = input('Ваш выбор(1 - начать программу, 0 - выйти из программы): ')
while(user_option != EXIT_OPTION and user_option != ACCEPT_OPTIONS):
    print('Вы указали неверную опцию! Повторите ввод')
    user_option = input('Ваш выбор(1 - начать программу, 0 - выйти из программы): ')

print()
if(user_option != EXIT_OPTION):
    for number_index in range(NUMBER_AMOUNT):
        array.append(randint(MIN_NUMBER,MAX_NUMBER))
        print('Число {} успешно\
    под индексом {}'.format(array[number_index],number_index))
    print('\nВаш список чисел: ',end = "")
    print(array)

while(user_option != EXIT_OPTION):
    user_number = int(input('\nПожалуйста, введите ваше число: '))
    if(array.count(user_number) > UNITY_QUANTITY):
        second_enterence = get_enterence_number(array,user_number)
        pre_last_enterence = get_enterence_number(list(reversed(array)),user_number)
        print('а) Индекс второго вхождения числа {} в списке {}'.format(user_number,second_enterence))
        print('б) Индекс предпоследнего вхождения числа {} : {}'.format(user_number,len(array) - ONE_STEP - pre_last_enterence))
        print('с) Все индексы вхождения вашего числа:',get_all_enterence(array,user_number))
    elif(array.count(user_number) == UNITY_QUANTITY):
        print('Число, которое вы ввели всего одно и оно находится на позиции',array.index(user_number))
    else:
        print('Вашего числа нет в списке')
    print('\nЕсли хотите закончить программу, то напечатайте 0, иначе 1')
    user_option = input('Ваша опция(0 - выйти из программы, 1 - продолжить работу): ')

    while(user_option != EXIT_OPTION and user_option != ACCEPT_OPTIONS):
        print('Вы указали неверную опцию! Повторите ввод')
        user_option = input('Ваш выбор(1 - начать программу, 0 - выйти из программы): ')

print('Спасибо за использование программы! До свидания!')

