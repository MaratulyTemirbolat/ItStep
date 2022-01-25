MECHANIC_TRANSMISSION = 'Механическая'
AUTO_TRANSMISSION = 'Автоматическая'
CONTINUOUSLY_VARIABLE_TRANSMISSION = 'Вариатор'
ROBOT_TRANSMISSION = 'Робот'
transmission_types = (MECHANIC_TRANSMISSION,AUTO_TRANSMISSION,CONTINUOUSLY_VARIABLE_TRANSMISSION,ROBOT_TRANSMISSION)

class Car:
    __name = ''
    __wheelbase = ''
    __transmission = ''

    def __init__(self,name,wheelbase,transmission):
        set_car_name(name)
        set_car_wheelbase(wheelbase)
        set_car_transmission(transmission)
        
    def __is_wheelbase_correct(self,wheelbase):
        MIN_WHEELBASE = 1500
        MAX_WHEELBASE = 3000
        if(int(wheelbase) >= MIN_WHEELBASE and int(wheelbase) <= MAX_WHEELBASE):
            return True
        return False

    def __raise_wheelbase_error(self):
        print('Ошибка! Колесная база должна быть в промежтке от 1500 до 3000')
    
    def __view_wheelbase_successful_message(self):
        print('Колесная база Успешно установлена!')

    def __view_car_name_successful_message(self):
        print('Наименование автомобиля успешно установлено')

    def __is_transmission_correct(self,transmission):
        if(transmission in transmission_types):
            return True
        return False

    def __view_transmission_error(self):
        print('Ошибка! Неправильно указанный тип Коробки передач!')
    
    def __view_transmission_successful_message(self):
        print('Тип Коробки передач успешно Установлен!')

    def set_car_name(self,name):
        self.__name = name
        __view_car_name_successful_message()
    
    def get_car_name(self):
        return __name
    
    def set_car_wheelbase(self,wheelbase):
        if(__is_wheelbase_correct(wheelbase) == True):
            self.__wheelbase = wheelbase
            __view_wheelbase_successful_message()
        else:
            __raise_wheelbase_error()
    
    def get_car_wheelbase(self):
        return self.__wheelbase
    
    def set_car_transmission(self,transmission):
        if(__is_transmission_correct(transmission)):
            self.__transmission = transmission
            __view_transmission_successful_message()
        else:
            __view_transmission_error()
    
    def get_car_transmission(self):
        return self.__transmission

    def view_car_info(self):
        print('Автомобиль с наименованием: "{}", \
колёсной базой: "{}", коробкой \
передач: "{}"'.format(self.__name,self.__wheelbase,self.__transmission))

def ask_car_new_name():
    print('\nПожалуйста, введите Наименование автомобиля!')
    car_name = input('Введите наименование автомобиля: ')
    return car_name

def ask_car_new_wheelbase():
    print('\nПожалуйста, введите колесную базу автомобиля. Например: 1856')
    print('Допустимая колёсная база: от 1500 до 3000')
    car_wheelbase = int(input('Введите колесную базу автомобиля: '))
    return car_wheelbase

def view_transmisiion_options():
    print('\nВозможные типы коробки передач, которые вы можете выбрать:',end =" ")
    print('"Механическая", "Автоматическая", "Вариатор", "Робот"')

def ask_car_new_transission():
    print('\nПожалуйста, введите тип коробки передач')
    view_transmisiion_options()
    car_transmision = input('Ввидели тип коробки передач: ')   
    return car_transmision

EXIT_OPTION = '0'
CREATE_CAR_OPTION = '1'
CHANGE_NAME_OPTION = '2'
CHANGE_WHEEL_BASE_OPTION = '3'
CHANGE_TRANSMISSION_OPTION = '4'
VIEW_NAME_OPTION = '5'
VIEW_WHEEL_BASE_OPTION = '6'
VIEW_TRANSMISSION_OPTION = '7'
VIEW_ALL_CAR_INFO_OPTION = '8'

program_options = (EXIT_OPTION,CREATE_CAR_OPTION,CHANGE_NAME_OPTION,CHANGE_WHEEL_BASE_OPTION,CHANGE_TRANSMISSION_OPTION,VIEW_NAME_OPTION,VIEW_WHEEL_BASE_OPTION,VIEW_TRANSMISSION_OPTION,VIEW_ALL_CAR_INFO_OPTION)

def view_program_options():
    print('Все возможные опции:')
    print('\t\t0) Выйти из программы')
    print('\t\t1) Создать новый автомобиль')
    print('\t\t2) Изменить Наименование существующего автомобиля')
    print('\t\t3) Изменить Колесную базу существующего автомобиля')
    print('\t\t4) Изменить Коробку передач существующего автомобиля')
    print('\t\t5) Просмотреть Наименование автомобиля')
    print('\t\t6) Просмотреть колёсную базу автомобиля')
    print('\t\t7) Просмотреть Тип коробки передач автомобиля')
    print('\t\t8) Просмотреть всю информацию автомобиля')

def start_main_program():
    print('Здравствуйте! Добро пожаловать в программу, которая может ',end = "")
    print('создать АВТОМОБИЛЬ, изменить его наименование, колёсную базу,',end = " ")
    print('тип коробки передач, а также просмотреть каждый аттрибут и всю информацию')
    car = None

    while(True):
        print('\nПожалуйста, выберите одну из возможных опций')
        view_program_options()
        user_option = input('Ваш выбор: ')
        if(user_option not in program_options):
            print('Извините, но такой опции нет. Повторите еще раз!')
            continue
        elif(user_option == EXIT_OPTION):
            print('Спасибо за использование программы! До свидания!')
            break
        elif(user_option == CREATE_CAR_OPTION):
            car_name = ask_car_new_name()
            car_wheelbase = ask_car_new_wheelbase()
            car_transmision = ask_car_new_transission()
            car = Car(car_name,car_wheelbase,car_transmision)
        elif(user_option == CHANGE_NAME_OPTION):
            if(car == None):
                print('Извините, но сначала надо создать автомобиль!')
            else:
                car_name = ask_car_new_name()
                car.set_car_name(car_name)
        elif(user_option == CHANGE_WHEEL_BASE_OPTION):
            if(car == None):
                print('Извините, но сначала надо создать автомобиль!')
            else:
                car_wheelbase = ask_car_new_wheelbase()
                car.set_car_wheelbase(car_wheelbase)
        elif(user_option == CHANGE_TRANSMISSION_OPTION):
            if(car == None):
                print('Извините, но сначала надо создать автомобиль!')
            else:
                car_transmision = ask_car_new_transission()
                car.set_car_transmission(car_transmision)
        elif(user_option == VIEW_NAME_OPTION):
            if(car == None):
                print('Извините, но сначала надо создать автомобиль!')
            else:
                print('Наименование вашего автомобиля:',car.get_car_name())
        elif(user_option == VIEW_WHEEL_BASE_OPTION):
            if(car == None):
                print('Извините, но сначала надо создать автомобиль!')
            else:
                print('Колёсная база вашего автомобиля составляет:',car.get_car_wheelbase())
        elif(user_option == VIEW_TRANSMISSION_OPTION):
            if(car == None):
                print('Извините, но сначала надо создать автомобиль!')
            else:
                print('Тип Коробки передач вашего автомобиля:',car.get_car_transmission())
        elif(user_option == VIEW_ALL_CAR_INFO_OPTION):
            if(car == None):
                print('Извините, но сначала надо создать автомобиль!')
            else:
                car.view_car_info() 
                
start_main_program()