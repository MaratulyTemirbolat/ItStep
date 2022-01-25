import math
ONE_STEP = 1
class Circle:
    __LENGTH_TERMINAL = 2

    def __radius_validation(self,radius):
        if(radius < 0):
            raise ValueError("Радиус не может быть отрицательным!")
        self.__radius = radius
    
    def __init__(self, radius):
        self.__radius_validation(radius)
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self,radius):
        self.__radius_validation(radius)

    def __str__(self):
        return 'Радиус окружности: {} см'.format(self.__radius)
    
    def get_circle_length(self):
        return self.__LENGTH_TERMINAL * math.pi * self.__radius

    def __add__(self,object):
        if not isinstance(object,Circle):
            raise TypeError("Правый операнд должен быть типом 'Circle'")
        return self.__radius + object.get_radius()
    
    def __radd__(self,object):
        if not isinstance(object,Circle):
            raise TypeError("Левый операнд должен быть по типу 'Circle'")
        
        return object.get_radius() - self.get_radius()

    def __sub__(self,object):
        if not isinstance(object,Circle):
            raise ArithmeticError("Правый операнд должен быть типом 'Circle'")
        return self.__radius - object.get_radius()
    
    def __rsub__(self,object):
        if not isinstance(object,Circle):
            raise TypeError("Левый операнд должен быть по типу 'Circle'")
        return object.get_radius() - self.__radius
    
    def __iadd__(self,object):
        if not isinstance(object,Circle):
            raise TypeError("Все операнды должны быть по типу 'Circle'")
        self.__radius += object.get_radius()
        return self
    
    def __isub__(self,object):
        if not isinstance(object,Circle):
            raise TypeError("Все операнды должны быть по типу 'Circle'")
        self.__radius -= object.get_radius()
        return self

    def __eq__(self,object):
        if not isinstance(object,Circle):
            raise TypeError("Все операнды должны быть по типу 'Circle'")
        return self.__radius == object.get_radius()
    
    def __ne__(self,object):
        return not self.__eq__(object)
    
    def __lt__(self,object):
        if not isinstance(object,Circle):
            raise TypeError("Все операнды должны быть по типу 'Circle'")
        return self.get_circle_length() < object.get_circle_length()

    def __gt__(self,object):
        if not isinstance(object,Circle):
            raise TypeError("Все операнды должны быть по типу 'Circle'")
        return self.get_circle_length() > object.get_circle_length()
    
    def __le__(self,object):
        return self.__lt__(object) or self.get_circle_length() == object.get_circle_length() 
    
    def __ge__(self,object):
        return  self.__gt__(object) or self.get_circle_length() == object.get_circle_length() 
    
class View:

    def __view_dollars_controller(function):
        def add_dollars(self):
            print('\n$$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$')
            print()
            function(self)
            print('\n$$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$')
        return add_dollars
    
    def __view_mines_controller(function):
        def add_mines(self):
            print('\n-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --')
            print()
            function(self)
            print('\n-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --')
        return add_mines

    def input_radius(self):
        return float(input('Пожалуйста, введите радиус окружности: '))

    @__view_mines_controller
    def view_non_created_circle_error(self):
        print('Извините, но вы еще не создали обе окружности, что выполнить что то')
    
    def show_stars(self):
        print('\n** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **')

    def input_user_choice(self):
        return int(input('Ваш выбор: '))
    
    def view_options(self,options):
        print()
        current_option = 1
        for option in options:
            print(current_option,option)
            current_option += ONE_STEP
    
    @__view_mines_controller
    def view_non_available_option_message(self):
        print('Извините, но такой опции нет.')
    
    @__view_dollars_controller
    def view_buy_message(self):
        print('Спасибо за использование программы! До свидания!')
    
    @__view_dollars_controller
    def view_successful_circle_creation_message(self):
        print('Ваша окружность успешно создана')
    
    def view_sum_radius_result(self,result):
        print('Результат суммы радиусов двух окружностей:',result)
    
    def view_subtraction_radius_result(self,circle_a,circle_b,result):
        print('{} - {} = {} '.format(circle_a,circle_b,result))
    
    def view_circle_radius(self,circle,result):
        print('\nРадиус {} окружности составляeт: {} см'.format(circle,result))
    
    @__view_mines_controller
    def view_non_availabe_radius(self):
        print('Длина радиуса не может быть отрицательной!')
    
    @__view_dollars_controller
    def show_equal_radiuses_message(self):
        print('Радиусы ваших окружностей равны друг другу!')
    
    @__view_mines_controller
    def show_non_equal_radiuses_message(self):
        print('Радиусы ваших окружностей НЕ равны друг другу!')
    
    @__view_dollars_controller
    def show_less_left_length_circle_message(self):
        print('Длина окружности слева МЕНЬШЕ длины окружности справа')
    
    @__view_dollars_controller
    def show_higher_rigth_length_circle_message(self):
        print('Длина окружности слева БОЛЬШе длины окружности справа')
    
    @__view_dollars_controller
    def show_less_equal_left_length_circle_message(self):
        print('Длина окружности слева МЕНЬШЕ или РАВНА длине окружности справа')
    
    @__view_dollars_controller
    def show_higher_equal_left_length_circle_message(self):
        print('Длина окружности слева БОЛЬШЕ или РАВНА длине окружности справа')
    
    def view_both_circles_info(self,circle_a,circle_b):
        print('Ваши Созданные Окружности: ')
        print('\t Первая:',circle_a)
        print('\t Вторая:',circle_b,end = "")
    
    def view_error_message(self,error):
        print(error)

LESS_OPTION = 2
MORE_OPTION = 3
LESS_EQUAL_OPTION = 4
MORE_EQUAL_OPTION = 5    

class Controller:
    
    menu_options = ['Создать Первую Окружность',
                    'Создать Вторую Окружность',
                    'Операция ( Первая окружность + Вторая окружность )',
                    'Операция ( Первая окружность - Вторая окружность )',
                    'Операция ( Вторая окружность - Первая окружность )',
                    'Операция ( Увеличить Первую окружность значением Второй окружности)',
                    'Операция ( Увеличить Вторую окружность значением Первой окружности)',
                    'Операция ( Уменьшить Первую окружность значением Второй окружности)',
                    'Операция ( Уменьшить Вторую окружность значением Первой окружности)',
                    'Сранивить Окружности оператором сравнения',
                    'Выйти из программы']

    condition_options = ['Радиус Первой Окружности == Радиус Второй Окружности',
                        'Длина Первой Окружности < Длина Второй Окружности',
                        'Длина Первой Окружности > Длина Второй Окружности',
                        'Длина Первой Окружности <= Длина Второй Окружности',
                        'Длина Первой Окружности >= Длина Второй Окружности']
    view = View()
    circle_a = None
    circle_b = None

    def __create_circle(self):
        self.view.show_stars()
        radius = self.view.input_radius()
        self.view.show_stars()
        circle = Circle(radius)
        self.view.view_successful_circle_creation_message()
        return circle
        
    def create_first_circle(self):
        self.circle_a = self.__create_circle()
    
    def create_second_circle(self):
        self.circle_b = self.__create_circle()
    
    def make_plus_operation(self):
        if(self.circle_a is None or self.circle_b is None):
            self.view.view_non_created_circle_error()
        else:
            sum_result = self.circle_a + self.circle_b
            self.view.show_stars()
            self.view.view_sum_radius_result(sum_result)
            self.view.show_stars()
    
    def make_subtraction_first_second_circles(self):
        if(self.circle_a is None or self.circle_b is None):
            self.view.view_non_created_circle_error()
        else:
            subtraction_result = self.circle_a - self.circle_b
            self.view.show_stars()
            self.view.view_subtraction_radius_result('Радиус Первой окружности','Радиус Второй окружности',subtraction_result)
            self.view.show_stars()
    
    def make_subtraction_second_first_circles(self):
        if(self.circle_a is None or self.circle_b is None):
            self.view.view_non_created_circle_error()
        else:
            subtraction_result = self.circle_b - self.circle_a
            self.view.show_stars()
            self.view.view_subtraction_radius_result('Радиус Второй окружности','Радиус Первой окружности',subtraction_result)
            self.view.show_stars()

    def increase_first_circle_radius(self):
        if(self.circle_a is None or self.circle_b is None):
            self.view.view_non_created_circle_error()
        else:
            self.circle_a += self.circle_b
            self.view.show_stars()
            self.view.view_circle_radius('Первой',self.circle_a.get_radius())
            self.view.show_stars()
    
    def increase_second_circle_radius(self):
        if(self.circle_a is None or self.circle_b is None):
            self.view.view_non_created_circle_error()
        else:
            self.circle_b += self.circle_a
            self.view.show_stars()
            self.view.view_circle_radius('Второй',self.circle_b.get_radius())
            self.view.show_stars()
    
    def decrease_first_circle_radius(self):
        if(self.circle_a is None or self.circle_b is None):
            self.view.view_non_created_circle_error()
        else:
            if(self.circle_a - self.circle_b < 0):
                self.view.view_non_availabe_radius()
            else:
                self.circle_a -= self.circle_b
                self.view.show_stars()
                self.view.view_circle_radius('Первой',self.circle_a.get_radius())
                self.view.show_stars()

    def decrease_second_circle_radius(self):
        if(self.circle_a is None or self.circle_b is None):
            self.view.view_non_created_circle_error()
        else:
            if(self.circle_b - self.circle_a < 0):
                self.view.view_non_availabe_radius()
            else:
                self.circle_b -= self.circle_a
                self.view.show_stars()
                self.view.view_circle_radius('Второй',self.circle_b.get_radius())
                self.view.show_stars()


    def compare_radiuses(self):
        if(self.circle_a == self.circle_b):
            self.view.show_equal_radiuses_message()
        else:
            self.view.show_non_equal_radiuses_message()

    def compare_circle_lengths(self,option):
        if(option == LESS_OPTION):
            if(self.circle_a < self.circle_b):
                self.view.show_less_left_length_circle_message()
            else:
                self.view.show_higher_rigth_length_circle_message()
        elif(option == MORE_OPTION):
            if(self.circle_a > self.circle_b):
                self.view.show_higher_rigth_length_circle_message()
            else:
                self.view.show_less_left_length_circle_message()
        elif(option == LESS_EQUAL_OPTION):
            if(self.circle_a <= self.circle_b):
                self.view.show_less_equal_left_length_circle_message()
            else:
                self.view.show_higher_equal_left_length_circle_message()
        elif(option == MORE_EQUAL_OPTION):
            if(self.circle_a >= self.circle_b):
                self.view.show_higher_equal_left_length_circle_message()
            else:
                self.view.show_less_equal_left_length_circle_message()

    def compare_two_circles(self):
        if(self.circle_a is not None and self.circle_b is not None):
            self.view.view_options(self.condition_options)
            user_choice = self.view.input_user_choice()
            if(user_choice == 1):
                self.compare_radiuses()
            else:
                self.compare_circle_lengths(user_choice)
        else:
            self.view.view_non_created_circle_error()

    
    functions = [create_first_circle,create_second_circle,make_plus_operation,
                make_subtraction_first_second_circles,make_subtraction_second_first_circles,
                increase_first_circle_radius,increase_second_circle_radius,
                decrease_first_circle_radius,decrease_second_circle_radius,compare_two_circles]

    def start_menu(self):
        while True:
            try:
                if(self.circle_a is not None and self.circle_b is not None):
                    self.view.view_both_circles_info(self.circle_a,self.circle_b)
                self.view.view_options(self.menu_options)
                user_choice = self.view.input_user_choice()
                if(user_choice < 1 or user_choice > len(self.menu_options)):
                    self.view.view_non_available_option_message()
                    continue
                elif(user_choice == len(self.menu_options)):
                    self.view.view_buy_message()
                    break
                self.functions[user_choice - ONE_STEP](self)
            except TypeError as te:
                print('asd')
                self.view.view_error_message(te)
            except ValueError as ve:
                self.view.view_error_message(ve)
            except Exception as ex:
                self.view.view_error_message(ex)

controller = Controller()
controller.start_menu()
