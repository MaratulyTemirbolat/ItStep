EXIT_OPTION = '0'
ACCEPT_OPTION = '1'

ADD_CLASS_OPTION = '1'
SHOW_ALL_CLASSES_OPTION = '2'
FIND_CLASS_OPTION = '3'
menu_options = (EXIT_OPTION,ADD_CLASS_OPTION,SHOW_ALL_CLASSES_OPTION,FIND_CLASS_OPTION)

ADD_STUDENT_OPTION = '1'
FIND_STUDENT_OPTION = '2'
DELETE_CLASS_OPTION = '3'
class_options = (ADD_STUDENT_OPTION,FIND_STUDENT_OPTION,DELETE_CLASS_OPTION)

CHANGE_STUDENT_INFO_OPTION = '1'
DELETE_STUDENT_OPTION = '2'
student_options = (CHANGE_STUDENT_INFO_OPTION,DELETE_STUDENT_OPTION)

GO_OUT_OPTION = 'exit'

classes = {
    "1a":['Темирболат','Александр','Тамерлан'],
    "2a":['Темирлан']
}

def view_menu_options():
    print('\nВсе опции в данном разделе: ')
    print('\t\t\t0) Выйти из меню')
    print('\t\t\t1) Добавить новый класс')
    print('\t\t\t2) Вывести список всех классов')
    print('\t\t\t3) Найти класс')

def view_student_options(student_name):
    print('\nВсе опции для студента "{}": '.format(student_name))
    print('\t\t\t1) Изменить ФИО "{}"'.format(student_name))
    print('\t\t\t2) Удалить ученика "{}" из его класса'.format(student_name))

def view_class_options():
    print('\nВсе опции для вашего класс: ')
    print('\t\t\t 1) Добавить нового студента')
    print('\t\t\t 2) Найти ученика в Классе по ФИО')
    print('\t\t\t 3) Удалить данный класс')

def view_all_classes():
    print('\nВсе существующие классы: ')
    print()
    for class_key in classes.keys():
        print('\t\tКласс "{}" состоит из: "{}"'.format(class_key,classes[class_key]))
    print()

def add_class():
    print('\nВы решили добавить новый класс...')
    print('Пожалуйста, создайте название класса: ')
    print('Если вы хотите выйти из данного раздела, то напишите: "exit"')
    new_class = input('Ваш новый класс: ')
    if(new_class == GO_OUT_OPTION):
        print('Выход...')
        print()
        return 
    while(new_class in classes):
        print('\nИзвините, но такой класс уже существует. Повторите попытку.')
        print('Если вы хотите выйти из данного раздела, то напишите: "exit"')
        new_class = input('Ваш новый класс: ')
        if(new_class == GO_OUT_OPTION):
            print('Выход...')
            print()
            return 
    print('Начинаю создавать новый класс...')
    classes.setdefault(new_class,[])
    print('Класс "{}" успешно создан'.format(new_class))
    print()

def change_student_info(class_name,student_info):
    print('Введите новые данные "{}"'.format(student_info))
    student_new_info = input('Введите новое ФИО студента: ')
    old_student_index = classes[class_name].index(student_info)
    print('Начинаем менять данные...')
    classes[class_name][old_student_index] = student_new_info
    print('Данные студента успешно изменены...')
    print()

def delete_student(class_name,student_info):
    old_student_index = classes[class_name].index(student_info)
    print('Студент "{}" успешно удален из класса'.format(classes[class_name].pop(old_student_index)))
    print()

def find_student(class_name):
    print('\nВы решили найти ученика...')
    print('Введите пожалуйста ФИО данного ученика')
    print('Если вы хотите выйти из данного раздела, то напишите: "exit"')
    student_data = input('ФИО ученика: ')
    if(student_data == GO_OUT_OPTION):
        print('Выход...')
        return 
    while(student_data not in classes[class_name]):
        print('\nИзвините, такого ученика нет в "{}". Повторите попытку'.format(class_name))
        print('Если вы хотите выйти из данного раздела, то напишите: "exit"')
        student_data = input('ФИО ученика: ')
        if(student_data == GO_OUT_OPTION):
            print('Выход...')
            print()
            return
    
    print('Ученик "{}" успешно найден.'.format(student_data))
    print('Что вы хотите с ним сделать?')
    view_student_options(student_data)
    student_option_choice = input('Ваш выбор: ')
    while(student_option_choice not in student_options):
        print('Извините, но такой опции нет. Пожалуйста выбирайте из предложенных.')
        view_student_options(student_data)
        student_option_choice = input('Ваш выбор: ')
    if(student_option_choice == CHANGE_STUDENT_INFO_OPTION):
        change_student_info(class_name, student_data)
    elif(student_option_choice == DELETE_STUDENT_OPTION):
        delete_student(class_name,student_data)

def add_student(class_name):
    print('Пожалуйста, введите имя учника')
    print('Если вы хотите выйти из данного раздела, то напишите: "exit"')
    student_name = input('Имя ученика: ')
    if(student_name == GO_OUT_OPTION):
        print('Выход...')
        print()
        return
    classes[class_name].append(student_name)
    print('Студент "{}" успешно добавлен в класс "{}"'.format(student_name,class_name))

def delete_class(class_name):
    del classes[class_name]
    print('Класс "{}" успешно удален'.format(class_name))
    print()

def find_class():
    print('\nПожалуйста, введите класс, который вы хотите найти: ')
    print('Если вы хотите выйти из данного раздела, то напишите: "exit"')
    find_class = input('Ваш класс: ')
    if(find_class == GO_OUT_OPTION):
        print('Выход...')
        return 
    while(find_class not in classes):
        print('\nИзвините, но такого класса нет. Повторите пожалуйста попытку.')
        print('Если вы хотите выйти из данного раздела, то напишите: "exit"')
        find_class = input('Ваш класс: ')
        if(find_class == GO_OUT_OPTION):
            print('Выход...')
            print()
            return 
    
    print('\nВсе ученики, обучающиеся в классе "{}": '.format(find_class),end = "")
    print(sorted(classes[find_class]))
    
    print('\nЧто вы желаете сделать с классом "{}"?'.format(find_class))
    view_class_options()
    class_choise = input('Ваш выбор: ')
    while(class_choise not in class_options):
        print('Извините, но такой опции нет.Повторите попытку')
        view_class_options()
        class_choise = input('Ваш выбор: ')
    
    if(class_choise == ADD_STUDENT_OPTION):
        add_student(find_class)
    elif(class_choise == FIND_STUDENT_OPTION):
        find_student(find_class)
    elif(class_choise == DELETE_CLASS_OPTION):
        delete_class(find_class)
    print()

repeat = ACCEPT_OPTION
while repeat != EXIT_OPTION:
    print('Выберите пожалуйста одну из предложенных опций: ')
    view_menu_options()
    menu_choice = input('Ваш выбор: ')
    while(menu_choice not in menu_options):
        print('Извините, но такой опции нет. Повторите пожалуйста попытку.')
        view_menu_options()
        menu_choice = input('Ваш выбор: ')
    if(menu_choice == ADD_CLASS_OPTION):
        add_class()
    elif(menu_choice == SHOW_ALL_CLASSES_OPTION):
        view_all_classes()
    elif(menu_choice == FIND_CLASS_OPTION):
        find_class()
    else:
        repeat = EXIT_OPTION
print('Спасибо за использование программы! До свидания!')