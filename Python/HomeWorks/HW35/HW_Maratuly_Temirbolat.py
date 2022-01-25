
import math

class CorrectFigure:

    def __init__(self,side):
        self.__side = side 
    
    def get_side(self):
        return self.__side
    
    def set_side(self,side):
        self.__side = side
    
class Circle(CorrectFigure):
    __PERIMETER_TERMINAL = 2
    def __init__(self,side):
        CorrectFigure.__init__(self,side)
    
    def get_perimeter(self):
        return self.__PERIMETER_TERMINAL * math.pi * super().get_side()
    
    def get_area(self):
        return math.pi * super().get_side() * super().get_side()
    
    def __str__(self):
        return 'Радиус Круга: {} см. Периметр Круга: {} см. \
Площадь Круга: {}см^2\
'.format(super().get_side(),self.get_perimeter(),self.get_area())

class Square(CorrectFigure):

    __PERIMETER_TERMINAL = 4
    def __init__(self, side):
        super().__init__(side) 

    def get_perimeter(self):
        return self.__PERIMETER_TERMINAL * super().get_side()

    def get_area(self):
        return super().get_side() * super().get_side()

    def __str__(self):
        return 'Сторона Квадрата: {} см. Периметр Квадрата: {} см. \
Площадь Квадрата: {} см^2\
'.format(super().get_side(),self.get_perimeter(),self.get_area())

class EquilateralTriangle(CorrectFigure):

    __PERIMETER_TERMINAL = 3
    __AREA_TERMINAL = 4

    def __init__(self, side):
        super().__init__(side)
    
    def get_perimeter(self):
        return self.__PERIMETER_TERMINAL * super().get_side()

    def get_area(self):
        return (super().get_side()*super().get_side() * math.sqrt(self.__PERIMETER_TERMINAL))/self.__AREA_TERMINAL

    def __str__(self):
        return 'Сторона Треугольника: {} см. Периметр: {} см. \
Площадь: {} см^2\
'.format(super().get_side(),self.get_perimeter(),self.get_area())

ONE_STEP = 1

class View:
    def input_square_side(self):
        return float(input('Введите сторону Квадрата: '))
    
    def input_circle_side(self):
        return float(input('Введите сторону Круга: '))
    
    def input_triangle_side(self):
        return float(input('Введите длину стороны Треугольника: '))
    
    def input_user_choice(self):
        return input('Ваш выбор: ')
    
    def view_all_options(self,options):
        current_option = 1
        for option in options:
            print(current_option,option)
            current_option += ONE_STEP 
    
    def view_non_created_figure_error(self):
        print('Извините, Но вы не создали еще фигуру!')
    
    def view_wrong_option_message(self):
        print('Извините, такой опции нет! Повторите попытку')

    def show_buy_message(self):
        print('Спасибо за использование программы! До свидания!')
    
    def input_figure_shape(self):
        return input('Введите тип геометрической фигуры: ')
    
    def view_figure_options(self,figure_variants):
        current_variant = 1
        for variant in figure_variants:
            print(current_variant,variant)
            current_variant += ONE_STEP
    
    def show_non_existed_shape_message(self):
        print('Извините, но такой фигуры не существует!')
    
    def show_successfull_creation_shape_message(self):
        print('Ваша геометрическая фигура успешно создана!')
    
    def show_figure_area(self,area):
        print('Площадь вашей геометрической фигуры составляет: {} см^2'.format(area))

    def show_figure_perimeter(self,perimetr):
        print('Периметр вашей геометрической фигуры составляет: {} см'.format(perimetr))

CREATE_FIGURE_OPTION = '1'
INPUT_FIGURE_DATA_OPTION = '2'
SHOW_FIGURE_PERIMETER_OPTION = '3'
SHOW_FIGURE_AREA_OPTION = '4'
EXIT_OPTION = '5'

CIRCLE_OPTION = '1'
SQUARE_OPTION = '2'
TRIANGLE_OPTION = '3'
figure_shape_options = (CIRCLE_OPTION,SQUARE_OPTION,TRIANGLE_OPTION)

menu_options = (CREATE_FIGURE_OPTION,INPUT_FIGURE_DATA_OPTION,SHOW_FIGURE_PERIMETER_OPTION,SHOW_FIGURE_AREA_OPTION,EXIT_OPTION)
class Controller:
    view = View()

    menu_options = ['Выбрать фигуру',
                    'Ввести/Изменить размер фигуры',
                    'Вывести периметр фигуры',
                    'Вывести площадь фигуры',
                    'Выйти из программы']

    figure_variants = ['Круг','Квадрат','Правильный треугольник']
    figure = None

    def __is_figure_created(self):
        if(self.figure == None):
            return False
        return True
    
    def create_circle(self):
        circle_radius = self.view.input_circle_side()
        self.figure = Circle(circle_radius)
        self.view.show_successfull_creation_shape_message()

    def create_square(self):
        square_side = self.view.input_square_side()
        self.figure = Square(square_side)
        self.view.show_successfull_creation_shape_message()
    
    def create_triangle(self):
        triangle_side = self.view.input_triangle_side()
        self.figure = EquilateralTriangle(triangle_side)
        self.view.show_successfull_creation_shape_message()
    
    shape_creation_options = [create_circle,create_square,create_triangle]

    def start_first_option(self):
        self.view.view_figure_options(self.figure_variants)
        user_choice = self.view.input_figure_shape()
        if(user_choice not in figure_shape_options):
            self.view.show_non_existed_shape_message()
        else:
            self.shape_creation_options[int(user_choice) - ONE_STEP](self)
            
    def start_second_option(self):
        if(self.__is_figure_created()):
            if(type(self.figure) == Circle):
                self.figure.set_side(self.view.input_circle_side())
            elif(type(self.figure) == Square):
                self.figure.set_side(self.view.input_square_side())
            elif(type(self.figure) == EquilateralTriangle):
                self.figure.set_side(self.view.input_triangle_side())
        else:
            self.view.view_non_created_figure_error()

    def start_third_option(self):
        if(self.__is_figure_created()):
            self.view.show_figure_perimeter(self.figure.get_perimeter())
        else:
            self.view.view_non_created_figure_error()
    
    def start_fourth_option(self):
        if(self.__is_figure_created()):
            self.view.show_figure_area(self.figure.get_area())
        else:
            self.view.view_non_created_figure_error()

    functions = [start_first_option,start_second_option,start_third_option,start_fourth_option]
    
    def main_menu(self):
        while True:
            self.view.view_all_options(self.menu_options)
            user_choice = self.view.input_user_choice()
            if(user_choice not in menu_options):
                self.view.view_wrong_option_message()
                continue
            elif(user_choice == EXIT_OPTION):
                self.view.show_buy_message()
                break
            self.functions[int(user_choice) - ONE_STEP](self)
                
controller = Controller()
controller.main_menu()
