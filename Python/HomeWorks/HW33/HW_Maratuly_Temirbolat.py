class Device:
    
    def __price_validation(self,price):
        if(price < 0):
            self.__price = 0
        else:
            self.__price = price

    def __volume_validation(self,volume):
        if(volume < 0):
            self.__volume = 0
        else:
            self.__volume = volume

    def __init__(self,brand,volume,date_production,price,description):
        self.__brand = brand
        self.__volume = volume
        self.__date_production = date_production
        self.__price = price
        self.__description = description
        self.__volume_validation(volume)
        self.__price_validation(price)
    
    def __is_volume_correct(self,volume):
        if(volume < 0):
            return False
        return True
    
    def __is_price_correct(self,price):
        if(price < 0):
            return False
        return True
    
    def set_brand(self,brand):
        self.__brand = brand
        return True
    
    def get_brand(self):
        return self.__brand
    
    def set_volume(self,volume):
        if(self.__is_volume_correct(volume)):
            self.__volume = volume
            return True
        return False
    
    def get_volume(self):
        return self.__volume
    
    def set_date_production(self,date_production):
        self.__date_production = date_production
        return True
    
    def get_date_production(self):
        return self.__date_production
    
    def set_price(self,price):
        if(self.__is_price_correct(price)):
            self.__price = price
            return True
        return False
    
    def get_price(self):
        return self.__price
    
    def set_description(self,description):
        self.__description = description
        return True
    
    def get_description(self):
        return self.__description
    
    def get_all_info(self):
        return 'Бренд: {}, Объем: {}, Дата создания: {}, Цена: {} тенге, Описание: {}\
'.format(self.__brand,self.__volume,self.__date_production,self.__price,self.__description)

class CoffeeMachine(Device):

    def __quantity_coffee_production_validation(self,quantity_coffee):
        if(quantity_coffee < 1):
            self.__number_coffee_production_types = 1
        else:
            self.__number_coffee_production_types = quantity_coffee
    
    def __cups_capacity_validation(self,cups_capacity):
        if(cups_capacity < 1):
            self.__cups_capacity = 1
        else:
            self.__cups_capacity = cups_capacity
    
    def __milk_boiler_there_validation(self,is_milk_boiler_there):
        if(is_milk_boiler_there != False or is_milk_boiler_there != True):
            self.__is_milk_boiler_there = False
        else:
            self.__is_milk_boiler_there = is_milk_boiler_there

    def __init__(self,brand,volume,date_production,price,description,number_coffee_production_options,cups_capacity,is_milk_boiler_there):
        super().__init__(brand,volume,date_production,price,description)
        self.__number_coffee_production_options = number_coffee_production_options
        self.__cups_capacity = cups_capacity
        self.__is_milk_boiler_there = is_milk_boiler_there
        self.__quantity_coffee_production_validation(number_coffee_production_options)
        self.__cups_capacity_validation(cups_capacity)
        self.__milk_boiler_there_validation(is_milk_boiler_there)
    
    def __is_valid_number_coffee_production_options(self,number_coffee_production_options):
        if(number_coffee_production_options >= 1):
            return True
        return False

    def set_number_coffee_production_options(self,number_coffee_production_options):
        if(self.__is_valid_number_coffee_production_options(number_coffee_production_options)):
            self.__number_coffee_production_options = number_coffee_production_options
            return True
        return False
    
    def get_number_coffee_production_options(self):
        return self.__number_coffee_production_options
    
    def __is_valid_cups_capacity(self,cups_capacity):
        if(cups_capacity > 0):
            return True
        return False

    def set_cups_capacity(self,cups_capacity):
        if(self.__is_valid_cups_capacity(cups_capacity)):
            self.__cups_capacity = cups_capacity
            return True
        return False
    
    def get_cups_capacity(self):
        return self.__cups_capacity
    
    def __is_valid_milk_boiler_there(self,is_milk_boiler_there):
        if(is_milk_boiler_there == True or is_milk_boiler_there == False):
            return True
        return False

    def set_milk_boiler_there_state(self,is_milk_boiler_there):
        if(self.__is_valid_milk_boiler_there(is_milk_boiler_there)):
            self.__is_milk_boiler_there = is_milk_boiler_there
            return True
        return False
    
    def get_milk_boiler_there_state(self):
        return self.__is_milk_boiler_there
    
    def get_all_info(self):
        return 'Кофемашинка: ' + super().get_all_info() + ' \
, Количество типов кофи: {}, Емкость для чашек: {}, Бойлер для молока: {}\
'.format(self.__number_coffee_production_options,self.__cups_capacity,self.__is_milk_boiler_there)


class Blender(Device):
    __MIN_BLENDER_POWER = 220
    __MAX_BLENDER_POWER = 700
    
    __MIN_FUNCTION_NUMBER = 1

    __MIN_SPEED_NUMBER = 2
    __MAX_SPEED_NUMBER = 5

    __MIN_BOWL_VOLUME = 1.5
    def __power_validation(self,power):
        if(power >= self.__MIN_BLENDER_POWER and power <= self.__MAX_BLENDER_POWER):
            self.__power_blender = power
        else:
            self.__power_blender = self.__MIN_BLENDER_POWER
    
    def __function_number_validation(self,number_function):
        if(number_function > self.__MIN_FUNCTION_NUMBER):
            self.__function_number = number_function
        else:
            self.__function_number = self.__MIN_FUNCTION_NUMBER

    def __number_speeds_validation(self,number_speeds):
        if(number_speeds >= self.__MIN_SPEED_NUMBER and number_speeds <= self.__MAX_SPEED_NUMBER):
            self.__number_speeds = number_speeds
        else:
            self.__number_speeds = self.__MIN_SPEED_NUMBER

    def __bowl_volume_validation(self,bowl_volume):
        if(bowl_volume >= self.__MIN_BOWL_VOLUME ):
            self.__bowl_volume = bowl_volume
        else:
            self.__bowl_volume = self.__MIN_BOWL_VOLUME

    def __init__(self,brand,volume,date_production,price,description,power_blender,function_number,number_speeds,bowl_volume):
        super().__init__(brand,volume,date_production,price,description)
        self.__power_blender = power_blender
        self.__function_number = function_number
        self.__number_speeds = number_speeds
        self.__bowl_volume = bowl_volume
        self.__power_validation(power_blender)
        self.__function_number_validation(function_number)
        self.__number_speeds_validation(number_speeds)
        self.__bowl_volume_validation(bowl_volume)
    
    def __is_blender_power_valid(self,power_blender):
        if(power_blender >= self.__MIN_BLENDER_POWER and power_blender <= self.__MAX_BLENDER_POWER):
            return True
        return False

    def get_blender_power(self):
        return self.__power_blender

    def set_blender_power(self,power_blender):
        if(self.__is_blender_power_valid(power_blender)):
            self.__power_blender = power_blender
            return True
        return False
    
    def __is_function_number_valid(self,function_number):
        if(function_number >= self.__MIN_FUNCTION_NUMBER):
            return True
        return False

    def get_function_number(self):
        return self.__function_number
    
    def set_function_number(self,function_number):
        if(self.__is_function_number_valid(function_number)):
            self.__function_number = function_number
            return True
        return False
    
    def __is_number_speeds_valid(self,number_speeds):
        if(number_speeds >= self.__MIN_SPEED_NUMBER and number_speeds <= self.__MAX_SPEED_NUMBER):
            return True
        return False

    def get_number_speeds(self):
        return self.__number_speeds
    
    def set_number_speeds(self,speed_number):
        if(self.__is_number_speeds_valid(speed_number)):
            self.__number_speeds = speed_number
            return True
        return False
    
    def __is_bowl_volume_valid(self,bowl_volume):
        if(bowl_volume >= self.__MIN_BOWL_VOLUME):
            return True
        return False

    def get_bowl_volume(self):
        return self.__bowl_volume
    
    def set_bowl_volume(self,bowl_volume):
        if(self.__is_bowl_volume_valid(bowl_volume)):
            self.__bowl_volume = bowl_volume
            return True
        return False
    
    def get_all_info(self):
        return 'Блендер: ' + super().get_all_info() + '\
 , Мощность: {} Вт, Кол-во функций: {}, Кол-во скоростей: {}, Объем чаши: {} л\
'.format(self.__power_blender,self.__function_number,self.__number_speeds,self.__bowl_volume)



class MeatGrinder(Device):

    __MIN_NUMBER_SPEEDS = 0
    __MAX_NUMBER_SPEEDS = 2
    
    def __number_speeds_validation(self,number_speeds):
        if(number_speeds >= self.__MIN_NUMBER_SPEEDS and number_speeds <= self.__MAX_NUMBER_SPEEDS):
            self.__number_speeds = number_speeds
        else:
            self.__number_speeds = self.__MIN_NUMBER_SPEEDS
    
    def __init__(self,brand,volume,date_production,price,description,material,number_speeds,transmission_mechanism_auger):
        super().__init__(brand,volume,date_production,price,description)
        self.__material = material
        self.__number_speeds = number_speeds
        self.__transmission_mechanism_auger = transmission_mechanism_auger
        self.__number_speeds_validation(number_speeds)
    
    def get_material(self):
        return self.__material
    
    def set_material(self,material):
        self.__material = material
        return True
    
    def __is_valid_number_speeds(self,number_speeds):
        if(number_speeds >= self.__MIN_NUMBER_SPEEDS and number_speeds <= self.__MAX_NUMBER_SPEEDS):
            return True
        return False

    def get_number_speeds(self):
        return self.__number_speeds
    
    def set_number_speeds(self,number_speeds):
        if(self.__is_valid_number_speeds(number_speeds)):
            self.__number_speeds = number_speeds
            return True
        return False

    def get_all_info(self):
        return 'Мясорубка: ' + super().get_all_info() + '\
 , Материал: {}, Кол-во скоростей: {}, Механизм передачи: {}\
'.format(self.__material, self.__number_speeds,self.__transmission_mechanism_auger)

coffee_machine = CoffeeMachine('Mitsubishi',0.5,'01.01.2001',50000,'Кофемашина, для вкусного напитка',4,2,True)
blender = Blender('Toyota',0.9,'05.10.2021',80000,'Супер пупер блендер',400,3,4,3)
meat_grinder = MeatGrinder('Lexus',1,'30.09.2021',100000,'Мясорубка 2.0','Нержавеющая сталь',2,'Пластиковый механизм')

print(coffee_machine.get_all_info())
print()
print(blender.get_all_info())
print()
print(meat_grinder.get_all_info())