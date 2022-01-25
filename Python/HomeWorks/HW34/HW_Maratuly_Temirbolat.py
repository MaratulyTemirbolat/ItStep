class MemoryEquipment:
    def __init__(self,ram_size,disk_space):
        self.__ram_size = ram_size
        self.__disk_space = disk_space
    
    def get_ram_size(self):
        return self.__ram_size
    
    def set_ram_size(self,ram_size):
        self.__ram_size = ram_size
    
    def get_disk_space(self):
        return self.__disk_space
    
    def set_disk_space(self,disk_space):
        self.__disk_space = disk_space

    def __str__(self):
        return 'Размер оперативной памяти: {} мб. Объем диска: {} гб.\
'.format(self.__ram_size,self.__disk_space)

class ComputerEquipment:
    def __init__(self,processor,maternal_memory,power_supply_power):
        self.__processor = processor
        self.__material_memory = maternal_memory
        self.__power_supply_power = power_supply_power
    
    def get_processor(self):
        return self.__processor
    
    def set_processor(self,processor):
        self.__processor = processor
    
    def get_maternal_memory(self):
        return self.__material_memory
    
    def set_maternal_memory(self,maternal_memory):
        self.__material_memory = maternal_memory
    
    def get_power_supply(self):
        return self.__power_supply_power
    
    def set_power_supply(self,power_supply):
        self.__power_supply_power = power_supply
    
    def __str__(self):
        return 'Процессор: {}. Объем Материнской памяти: {} мб. \
Мощность блока питания: {} Вт.\
'.format(self.__processor,self.__material_memory,self.__power_supply_power)

class CameraEquipment:
    def __init__(self,matrix_resolution):
        self.__matrix_resolution = matrix_resolution
    
    def get_matrix_resolution(self):
        return self.__matrix_resolution
    
    def set_matrix_resolution(self,matrix_resolution):
        self.__matrix_resolution = matrix_resolution
    
    def __str__(self):
        return 'Разрешение матрицы: {} пикселей.\
'.format(self.__matrix_resolution)

class VideoEquipment(CameraEquipment):
    def __init__(self,matrix_resolution,frame_frequency,stabilization_type):
        CameraEquipment.__init__(self,matrix_resolution)
        self.__frame_frequency = frame_frequency
        self.__stabilization_type = stabilization_type
    
    def get_frame_frequency(self):
        return self.__frame_frequency
    
    def set_frame_frequency(self,frame_frequenct):
        self.__frame_frequency = frame_frequenct
    
    def get_stabilization_type(self):
        return self.__stabilization_type
    
    def set_stabilization_type(self,stabilization_type):
        self.__stabilization_type = stabilization_type
    
    def __str__(self):
        return CameraEquipment.__str__(self) + ' Частота кадров: {} Гц. \
Тип стабилизации: {}.'.format(self.__frame_frequency,self.__stabilization_type)
        
class Computer(ComputerEquipment,MemoryEquipment):
    def __init__(self,processor,maternal_memory,power_supply_power,ram_size,disk_space):
        ComputerEquipment.__init__(self,processor,maternal_memory,power_supply_power)
        MemoryEquipment.__init__(self,ram_size,disk_space)
    
    def __str__(self):
        return 'Компьютер: ' + ComputerEquipment.__str__(self) + ' ' + MemoryEquipment.__str__(self)
        
class Camera(CameraEquipment,MemoryEquipment):
    def __init__(self,matrix_resolution,ram_size,disk_space):
        CameraEquipment.__init__(self,matrix_resolution)
        MemoryEquipment.__init__(self,ram_size,disk_space)

    def __str__(self):
        return 'Камера: ' + CameraEquipment.__str__(self) + ' ' + MemoryEquipment.__str__(self)

class VideoCamera(VideoEquipment,MemoryEquipment):
    def __init__(self,matrix_resolution,frame_frequency,stabilization_type,ram_size,disk_space):
        VideoEquipment.__init__(self,matrix_resolution,frame_frequency,stabilization_type)
        MemoryEquipment.__init__(self,ram_size,disk_space)
    
    def __str__(self):
        return 'Видеокамера: ' + VideoEquipment.__str__(self) + ' ' + MemoryEquipment.__str__(self)

class Smartphone(ComputerEquipment,VideoEquipment,MemoryEquipment):
    def __init__(self,processor,maternal_memory,power_supply_power,matrix_resolution,frame_frequency,stabilization_type,ram_size,disk_space):
        ComputerEquipment.__init__(self,processor,maternal_memory,power_supply_power)
        VideoEquipment.__init__(self,matrix_resolution,frame_frequency,stabilization_type)
        MemoryEquipment.__init__(self,ram_size,disk_space)
    
    def __str__(self):
        return 'Смартфон: ' + ComputerEquipment.__str__(self) + ' ' + VideoEquipment.__str__(self) + ' ' + MemoryEquipment.__str__(self)

ONE_STEP = 1

class View:
    def input_processor(self):
        return input('Введите ваш процессор: ')
    
    def input_maternal_memory(self):
        return int(input('Введите объем материнской памяти: '))
    
    def input_power_supply_power(self):
        return int(input('Введите Мощность блока питания: '))
    
    def input_ram_size(self):
        return int(input('Введите объем оперативной памяти: '))
    
    def input_disk_space(self):
        return int(input('Введите объем диска: '))
    
    def input_matrix_resolution(self):
        return input('Введите разрешение матрицы: ')
    
    def input_frame_frequency(self):
        return int(input('Введите частоту кадров: '))
    
    def input_stabilization_type(self):
        return input('Введите тип стабилизации: ')
    
    def input_user_choice(self):
        return input('Ваш выбор: ')
    
    def view_device_info(self,device):
        print(device)
    
    def show_items(self,items):
        print()
        item_number = 1
        for item in items:
            print(item_number,item)
            item_number += ONE_STEP
        print()

    def view_all_added_devices(self,all_devices):
        print()
        item_number = 1
        for device in all_devices:
            print(item_number,device)
            item_number += ONE_STEP
        print()
    
    def show_wrong_user_input_error(self):
        print('Извините, но вы ввели недопустимый символ!')
    
    def show_good_buy_message(self):
        print('Спасибо за использование программы! До свидания!')
    
    def show_successful_added_created_device(self):
        print('Созданный вами девайс успешно добавлен!')

ADD_NEW_COMPUTER_OPTION = '1'
ADD_NEW_CAMERA_OPTION = '2'
ADD_NEW_VIDEOCAMERA_OPTION = '3'
ADD_NEW_SMARTPHONE_OPTION = '4'
VIEW_ALL_ADDED_DEVICES_OPTION = '5'
EXIT_OPTION = '6'

class Controller:
    menu_items = ['Добавить новый Компьютер',
                  'Добавить новый Фотоаппарат',
                  'Добавить новую Видеокамеру',
                  'Добавить новый Смартфон',
                  'Просмотреть все добавленные девайсы',
                  'Выход']

    devices = []
    view = View()

    def add_new_computer(self):
        processor = self.view.input_processor()
        maternal_memory = self.view.input_maternal_memory()
        power_supply_power = self.view.input_power_supply_power()
        ram_size = self.view.input_ram_size()
        disk_space = self.view.input_disk_space()
        computer = Computer(processor,maternal_memory,power_supply_power,ram_size,disk_space)
        self.devices.append(computer)

    def add_new_camera(self):
        matrix_resolution = self.view.input_matrix_resolution()
        ram_size = self.view.input_ram_size()
        disk_space = self.view.input_disk_space()
        camera = Camera(matrix_resolution,ram_size,disk_space)
        self.devices.append(camera)

    def add_new_videocamera(self):
        matrix_resolition = self.view.input_matrix_resolution()
        frame_frequency = self.view.input_frame_frequency()
        stabilization_type = self.view.input_stabilization_type()
        ram_size = self.view.input_ram_size()
        disk_space = self.view.input_disk_space()
        videocamera = VideoCamera(matrix_resolition,frame_frequency,stabilization_type,ram_size,disk_space)
        self.devices.append(videocamera)

    def add_new_smartphone(self):
        processor = self.view.input_processor()
        maternal_memory = self.view.input_maternal_memory()
        power_supply_power = self.view.input_power_supply_power()
        matrix_resolution = self.view.input_matrix_resolution()
        frame_frequency = self.view.input_frame_frequency()
        stabilization_type = self.view.input_stabilization_type()
        ram_size = self.view.input_ram_size()
        disk_space = self.view.input_disk_space()
        smartphone = Smartphone(processor,maternal_memory,power_supply_power,matrix_resolution,frame_frequency,stabilization_type,ram_size,disk_space)
        self.devices.append(smartphone)

    def main_menu(self):
        while True:
            self.view.show_items(self.menu_items)
            user_choice = self.view.input_user_choice()
            if user_choice == ADD_NEW_COMPUTER_OPTION:
                self.add_new_computer()
            elif user_choice == ADD_NEW_CAMERA_OPTION:
                self.add_new_camera()
            elif user_choice == ADD_NEW_VIDEOCAMERA_OPTION:
                self.add_new_videocamera()
            elif user_choice == ADD_NEW_SMARTPHONE_OPTION:
                self.add_new_smartphone()
            elif user_choice == VIEW_ALL_ADDED_DEVICES_OPTION:
                self.view.view_all_added_devices(self.devices)
            elif user_choice == EXIT_OPTION:
                self.view.show_good_buy_message()
                break
            else:
                self.view.show_wrong_user_input_error()

controller = Controller()
controller.main_menu()