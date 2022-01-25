ONE_STEP = 1
class Student:
    def __init__(self,first_name,last_name,middle_name,id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__middle_name = middle_name
        self.__id = id
    
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self,first_name):
        self.__first_name = first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self,last_name):
        self.__last_name = last_name
    
    def get_middle_name(self):
        return self.__middle_name
    
    def set_middle_name(self,middle_name):
        self.__middle_name = middle_name
    
    def get_id(self):
        return self.__id
    
    def set_id(self,id):
        self.__id = id

    def __str__(self):
        return 'ФИО студента: "{} {} {}". ИИН: "{}"\
'.format(self.__last_name,self.__first_name,self.__middle_name,self.__id)

students = []
file_students = open(r"students.txt","a+")

def show_menu_options():
    print('\n1. Создать нового студента\n\
2. Просмотреть всех существующих студентов\n\
3. Выйти из программы')

def get_user_option():
    return int(input('Ваш выбор: '))

def get_student_first_name():
    return input('Введите Имя студента: ')

def get_student_last_name():
    return input('Введите Фамилию студента: ')

def get_student_middle_name():
    return input('Введите Отчество студента: ')

def get_student_id():
    return int(input('Введите ИИН студента: '))

def create_new_student():
    student_first_name = get_student_first_name()
    student_last_name = get_student_last_name()
    student_middle_name = get_student_middle_name()
    student_id = get_student_id()
    student = Student(student_first_name,student_last_name,student_middle_name,student_id)
    students.append(student)
    student_full_name = student_last_name + ' ' + student_first_name + ' ' + student_middle_name
    student_id = str(student_id)
    student_info = student_full_name + ',' + student_id + "\n"
    file_students.write(student_info)
    print('\nСтудент успешно создан!')

def load_students():
    student_lines = []
    with open("students.txt") as f:
        student_lines = f.readlines()
    
    for line in student_lines:
        student_info = line.split(",")
        student_full_name = student_info[0].split(" ")
        student_last_name = student_full_name[0]
        student_first_name = student_full_name[1]
        student_middle_name = student_full_name[2]
        student_id = student_info[1].replace("\n","")
        student = Student(student_first_name,student_last_name,student_middle_name,student_id)
        students.append(student)

def view_all_students():
    current_student = 1
    for student in students:
        print(current_student,student)
        current_student += ONE_STEP

menu_functions = [create_new_student,view_all_students]

def main_menu():
    while True:
        try:
            show_menu_options()
            user_choice = get_user_option()
            if(user_choice < 1 or user_choice > len(menu_functions) + ONE_STEP):
                print('\nИзвините, но такой опции нет!')
                continue
            elif(user_choice == len(menu_functions) + ONE_STEP):
                print('\nСпасибо за использование программы! До свидания!')
                break
            menu_functions[user_choice - ONE_STEP]()
        except ValueError:
            print('Извините, но вы ввели не число!')
        except Exception as ex:
            print(type(ex))
            print(ex)

load_students()
main_menu()

file_students.close()