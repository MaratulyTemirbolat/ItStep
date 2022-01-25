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

def __view_dollars_controller(function):
    def add_dollars():
        print('\n$$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$')
        print()
        function()
        print('\n$$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$ $$')
    return add_dollars
    
def __view_mines_controller(function):
    def add_mines():
        print('\n-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --')
        print()
        function()
        print('\n-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --')
    return add_mines
