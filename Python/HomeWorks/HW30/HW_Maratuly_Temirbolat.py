class Medications:
    name = ''
    description = ''
    price = 0

    def __init__(self,name,description,price):
        self.name = name
        self.description = description
        self.price = price
    
    def __init__(self):
        pass
    
    def set_name(self):
        self.name = input('Введите Наименование лекарства: ')
    
    def display_name(self):
        print('Наименование вашего лекарственного препарата:',self.name)
    
    def set_description(self):
        self.description = input('Введите Описание Лекарства: ')
    
    def display_description(self):
        print('Описание вашего лекарственного препарата:',self.description)

    def set_price(self):
        self.price = int(input('Введиту цену вашего лекарства: '))
        while(self.price < 0):
            print('Извините, но цена не может быть отрицательной!')
            self.price = int(input('Введиту цену вашего лекарства: '))
    
    def display_price(self):
        print('Цена вашего лекарственного препарата:',self.price,'тенге')
    
    def display_all_info(self):
        print('Препарат "{}" с описанием "{}" стоимостью {} тенге'.format(self.name,self.description,self.price))

EXIT_OPTION = '0'
CREATE_MEDICATION_OPTION = '1'
CHANGE_NAME_OPTION = '2'
CHANGE_DESCRIPTION_OPTION = '3'
CHANGE_PRICE_OPTION = '4'
SEE_NAME_OPTION = '5'
SEE_DESCRIPTION_OPTION = '6'
SEE_PRICE_OPTION = '7'
SEE_ALL_INFO_OPTION = '8'
menu_options = (EXIT_OPTION,CREATE_MEDICATION_OPTION,CHANGE_NAME_OPTION,CHANGE_DESCRIPTION_OPTION,CHANGE_PRICE_OPTION,SEE_NAME_OPTION,SEE_DESCRIPTION_OPTION,SEE_PRICE_OPTION,SEE_ALL_INFO_OPTION)


def view_menu_options():
    print('\nВсе возможные опции:')
    print('\t\t 0) Выйти из программы')
    print('\t\t 1) Создать Лекарственный препарат')
    print('\t\t 2) Изменить Название лекарства')
    print('\t\t 3) Изменить Описание лекарства')
    print('\t\t 4) Изменить цену лекарства')
    print('\t\t 5) Увидеть Название лекарства')
    print('\t\t 6) Увидеть Описание лекарства')
    print('\t\t 7) Увидеть Цену лекарства')
    print('\t\t 8) Увидеть Всю информацию о лекарстве')

def start_program():
    print('Здравствуйте! Добро пожаловать в программу, где вы можете ',end = "")
    print('создавать лекарства, изменять информацию, данного лекарства',end = "")
    print(' просматривать информацию о его названии, описании, а также цену. ')
    medication = None
    while(True):
        print('\nПожалуйста, выберите одну из предложенных опций')
        view_menu_options()
        user_option = input('Ваш выбор: ')
        if(user_option not in menu_options):
            print('Вы ввели недоступный символ! Повторите попытку пожалуйста')
            continue
        elif(user_option == EXIT_OPTION):
            print('Спасибо, что использовали нашу программу! До свидания!')
            break
        elif(user_option == CREATE_MEDICATION_OPTION):
            medication = Medications()
            medication.set_name()
            medication.set_description()
            medication.set_price()
            print('Ваше лекарство успешно создано!')
        elif(user_option == CHANGE_NAME_OPTION):
            if(medication == None):
                print('Извините, но сначала надо создать лекарство, чтобы его изменить')
            else:
                medication.set_name()
        elif(user_option == CHANGE_DESCRIPTION_OPTION):
            if(medication == None):
                print('Извините, но сначала надо создать лекарство, чтобы его изменить')
            else:
                medication.set_description()
        elif(user_option == CHANGE_PRICE_OPTION):
            if(medication == None):
                print('Извините, но сначала надо создать лекарство, чтобы его изменить')
            else:
                medication.set_price()
        elif(user_option == SEE_NAME_OPTION):
            if(medication == None):
                print('Вы не можете увидеть название несуществующего лекарства...')
            else:
                medication.display_name()
        elif(user_option == SEE_DESCRIPTION_OPTION):
            if(medication == None):
                print('Вы не можете увидеть описание лекарства, пока не создадите его...')
            else:
                medication.display_description()
        elif(user_option == SEE_PRICE_OPTION):
            if(medication == None):
                print('Вы не можете просмотреть ценю лекарства, пока не создадите его...')
            else:
                medication.display_price()
        elif(user_option == SEE_ALL_INFO_OPTION):
            if(medication == None):
                print('Вы не можете просмотреть информацию, пока не создадите лекарство...')
            else:
                medication.display_all_info()

start_program()