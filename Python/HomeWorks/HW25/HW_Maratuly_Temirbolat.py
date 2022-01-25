car_catalog = {
    'TOYOTA':['Автоматическая',3.5,20000],
    'LEXUS':['Механическая',4.0,35000],
    'BMW':['Автоматическая',2.2,50000],
    'BUGATTI':['Автоматическая',5.5,100000],
    'AUDI':['Механическая',1.4,15000]
}
DELETE_WHOLE_MEDICATION = '1'
DELETE_DESCRIPTION = '2'
DELETE_PRICE = '3'
DELETE_QUANTITY = '4'
delete_options = (DELETE_WHOLE_MEDICATION,DELETE_DESCRIPTION,DELETE_PRICE,DELETE_QUANTITY)

CORRECT_NAME = '1'
CORRECT_DESCRIPTION = '2'
CORRECT_PRICE = '3'
CORRECT_REMAINED_QANTITY = '4'
correct_options = (CORRECT_NAME,CORRECT_DESCRIPTION,CORRECT_PRICE,CORRECT_REMAINED_QANTITY)

GO_OUT_MENU = 'EXIT'

def view_cars():
    print()
    for car in car_catalog:
        print('Марка:',car,'\tТип передачи:',car_catalog[car][0],'\tОбъем двигателя:',end = " ")
        print(car_catalog[car][1],'литров','\tЦена:',car_catalog[car][2],'$')
    print()

FIND_BY_MARK_OPTION = '1'
FIND_BY_TRANSMISSION_OPTION = '2'
FIND_BY_BOTH = '3'
find_options = (FIND_BY_MARK_OPTION,FIND_BY_TRANSMISSION_OPTION,FIND_BY_BOTH)

def view_find_options():
	print('\nВсе доступные опции по поиску автомобиля')
	print('\t\t\t 1) Найти по Марке Автомобиля')
	print('\t\t\t 2) Найти по Коробке Передач автомобиля')
	print('\t\t\t 3) Найти по Марке и по Коробке Передач')

def get_cars_by_transmission():
	print('Пожалуйста, укажите коробку передач автомобиля')
	car_transmission_type_find = (input('Введите Тип Коробки передач: ')).capitalize()
	found_marks = []
	for mark_car, car_description in car_catalog.items():
		if(car_transmission_type_find in car_description):
			found_marks.append(mark_car)
	return found_marks

def view_car_by_mark():
	print('Пожалуйста, укажите Марку Автомобиля')
	car_mark_find = (input('Введите Марку Автомобиля: ')).upper()
	if(car_mark_find in car_catalog):
		transmission_car = car_catalog[car_mark_find][0]
		volume_engine = car_catalog[car_mark_find][1]
		price_found = car_catalog[car_mark_find][2]
		print('\nИнформация о найденной модели "{}": '.format(car_mark_find),end = "")
		print('\tТип передачи: "{}". Объем двигателя: "{}" литров. \tСтоимость: "{}" $'.format(transmission_car,volume_engine,price_found))
	else:
		print('Извините, по вашему запросу найденных автомобилей нет.')

def get_car_by_transmission_mark():
	user_mark = (input('Введите Марку Автомобиля: ')).upper()
	if(user_mark in get_cars_by_transmission()):
		transmission_car = car_catalog[user_mark][0]
		volume_engine = car_catalog[user_mark][1]
		price_found = car_catalog[user_mark][2]
		print('\nИнформация о найденной модели "{}": '.format(user_mark),end = "")
		print('\tТип передачи: "{}". \tОбъем двигателя: "{}" литров. \tСтоимость: "{}" $'.format(transmission_car,volume_engine,price_found))
	else:
		print('Извините, но автомобиль по вашему запросу не найден.')

def find_car():
	print('Пожалуйста, выберите одну из опций по поиску автомобиля')
	print('Если вы хотите вернутся в Меню, напечатйте: "EXIT"')
	view_find_options()
	user_find_option = input('Ваш выбор: ')
	if(user_find_option == GO_OUT_MENU):
		print('Возвращаемся в Главное Меню...')
		print()
		return
	while(user_find_option not in find_options):
		print('Извините, но вы выбрали недоступную опцию.Повторите попытку')
		view_find_options()
		user_find_option = input('Ваш выбор: ')
	if(user_find_option == FIND_BY_MARK_OPTION):
		view_car_by_mark()
	elif(user_find_option == FIND_BY_TRANSMISSION_OPTION):
		found_cars_marks = get_cars_by_transmission()
		if(len(found_cars_marks) == 0):
			print('Извините, но по вашему запросу автомобили не найдены.')
		else:
			print('\nВсе что найдено:')
			for mark in found_cars_marks:
				print('Марка автомобиля: "{}"\tТип Передачи: "{}"'.format(mark,car_catalog[mark][0]),end = "")
				print('\tОбъем двигателя: "{}" литров\tЦена: "{}" $'.format(car_catalog[mark][1],car_catalog[mark][2]))
	else:
		get_car_by_transmission_mark()
	print()

def view_correct_options():
    print('\nВсе доступные ваши опции: ')
    print('\t\t\t 1) Изменить марку автомобиля')
    print('\t\t\t 2) Изменить тип передачи автомобиля')
    print('\t\t\t 3) Изменить объем двигателя')
    print('\t\t\t 4) Изменить цену автомобиля')

def correct_car_mark(car_name):
    print('Введите новую марку: ')
    new_name = (input('Имя новой марки: ')).upper()
    while(new_name in car_catalog):
        print('Извините, марка автомобиля занята. Введите другую')
        new_name = (input('Имя новой марки автомобиля: ')).upper()
    print('\nМеняем марку автомобиля с "{}" на "{}"'.format(car_name,new_name))
    car_catalog[new_name] = car_catalog.pop(car_name)
    print('Марка автомобиля успешно изменена!')

def correct_car_price(car_name):
    print('Введите новую цену на автомобиль в долларах($) "{}": '.format(car_name))
    new_quantity = int(input('Новая цена на "{}": '.format(car_name)))
    print('Меняем старую цену "{}"'.format(car_name))
    car_catalog[car_name][2] = new_quantity
    print('Новая цена на автомобиль успешно обновлена!')

def correct_car_volume(car_name):
    print('Введите новый объем двигателя в литрах для "{}": '.format(car_name))
    new_volume = float(input('Новый объем двигателя для "{}": '.format(car_name)))
    print('Меняем объем двигателя автомобиля "{}"'.format(car_name))
    car_catalog[car_name][1] = new_volume
    print('Объем двигателя успешно изменен')

def correct_car_transmission(car_name):
    print('Введите обновленный Тип Передачи Автомобиля "{}": '.format(car_name))
    new_transmission_type = (input('Новый Тип Передачи для "{}": '.format(car_name))).capitalize()
    print('Меняем тип передачи автомобиля "{}"'.format(car_name))
    car_catalog[car_name][0] = new_transmission_type
    print('Информация о Типе Передачи успешно обновлена')

def correct_information():
    print('Если вы хотите вернутся в Меню, напечатйте: "EXIT"')
    car_name = (input('Пожалуйста, введите Марку Автомобиля, которую вы хотите найти: ')).upper()
    if(car_name == GO_OUT_MENU):
        print('Возвращаемся в Главное Меню...')
        print()
        return
    while(car_name not in car_catalog):
        print('Извините, данного автомобиля нет в Базе. Повторите попытку')
        car_name = (input('Пожалуйста, введите Марку Автомобиля, которую вы хотите найти: ')).upper()
    print('Что вы хотите именно изменить?')
    view_correct_options()
    user_option = input('Ваш выбор: ')

    while(user_option not in correct_options):
        print('Такой доступной опции нет. Повторите пожалуйста попытку.')
        user_option = input('Ваш выбор: ')
        
    if(user_option == CORRECT_NAME):
        correct_car_mark(car_name)
    elif(user_option == CORRECT_DESCRIPTION):
        correct_car_transmission(car_name)
    elif(user_option == CORRECT_PRICE):
        correct_car_volume(car_name)
    else:
        correct_car_price(car_name)
    print()
def delete_car_completely(car_name):
    del car_catalog[car_name]
    print('Автомобиль марки "{}" успешно удален с Базы...'.format(car_name))

def delete_car_transmission_type(car_name):
    car_catalog[car_name][0] = "Нет описания"
    print('Описание типа передачи успешно удалено!')

def delete_car_volume(car_name):
    car_catalog[car_name][1] = 0.0
    print('Объем двигателя успешно обнулен')

def delete_car_price(car_name):
    car_catalog[car_name][2] = 0
    print('Цена автомобиля успешно обнулена')

def view_delete_options():
    print('\nВсе доступные ваши опции: ')
    print('\t\t\t 1) Удалить автомобиль полностью')
    print('\t\t\t 2) Удалить описания типа передачи автомобиля')
    print('\t\t\t 3) Удалить объем двигателя автомобиля')
    print('\t\t\t 4) Удалить цену автомобиля')

def delete_car_opt():
    print('Если вы хотите вернутся в Меню, напечатйте: "EXIT"')
    car_name = (input('Пожалуйста, введите Марку Автомобиля, которую вы хотите найти: ')).upper()
    if(car_name == GO_OUT_MENU):
        print('Возвращаемся в Главное Меню...')
        print()
        return
    while(car_name not in car_catalog):
        print('Извините, данного автомобиля нет в Базе. Повторите попытку')
        car_name = (input('Пожалуйста, введите Марку Автомобиля, которую вы хотите найти: ')).upper()
    print('Что вы хотите удалить именно?')
    view_delete_options()
    user_option = input('Ваш выбор: ')
    while(user_option not in delete_options):
        print('Извините, такой опции нет. Повторите ваш выбор')
        view_delete_options()
        user_option = input('Ваш выбор: ')
    
    if(user_option == DELETE_WHOLE_MEDICATION):
        delete_car_completely(car_name)
    elif(user_option == DELETE_DESCRIPTION):
        delete_car_transmission_type(car_name)
    elif(user_option == DELETE_PRICE):
        delete_car_volume(car_name)
    else:
        delete_car_price(car_name)
    print()

def add_car():
    print('Если вы хотите вернуться в Меню, напечатйте: "EXIT"')
    car_name = (input('Пожалуйста, введите Марку Автомобиля, которую вы хотите добавить: ')).upper()
    if(car_name == GO_OUT_MENU):
        print('Возвращаемся в Главное Меню...')
        print()
        return
    while(car_name in car_catalog):
        print('Извините, данный товар уже есть в базе. Повторите попытку')
        car_name = (input('Пожалуйста, введите Марку Автомобиля, которую вы хотите добавить: ')).upper()
    
    car_transmission_type = (input('Введите Тип Передачи Автомобиля: ')).capitalize()
    car_volume = float(input('Введите Объем Двигателя Автомобиля: '))
    car_price = int(input('Введите Цену данной марки автомобиля: '))
    print('\nДобавляем вашу марку автомобиля...')
    car_catalog.setdefault(car_name,[car_transmission_type,car_volume,car_price])
    print('\nВаша Марка Автомобиля успешно добавлена!')
    print()    

EXIT_MENU_OPTION = '0'
ADD_MENU_OPTION = '1'
DELETE_MENU_OPTION = '2'
CORRECT_MENU_OPTION = '3'
VIEW_GOODS_OPTION = '4'
FIND_GOOD_OPTION = '5'
menu_options = (EXIT_MENU_OPTION,ADD_MENU_OPTION,DELETE_MENU_OPTION,CORRECT_MENU_OPTION,VIEW_GOODS_OPTION,FIND_GOOD_OPTION)

def view_menu_options():
    print('Все доступные опции: ')
    print('\t\t\t 0) Выйти из программы')
    print('\t\t\t 1) Добавить новый автомобиль')
    print('\t\t\t 2) Удалить информацию')
    print('\t\t\t 3) Изменить информацию')
    print('\t\t\t 4) Просмотреть список автомобилей')
    print('\t\t\t 5) Найти автомобиль')

while(True):
    print('Вы находитесь в главном меню, пожалуйста, напечатайте одну из опций')
    view_menu_options()
    user_choice = input('Ваш выбор: ')
    while(user_choice not in menu_options):
        print('Извините, такой опции нет. Повторите выбор.')
        user_choice = input('Ваш выбор: ')
    if(user_choice == ADD_MENU_OPTION):
        add_car()
    elif(user_choice == DELETE_MENU_OPTION):
        delete_car_opt()
    elif(user_choice == CORRECT_MENU_OPTION):
        correct_information()
    elif(user_choice == VIEW_GOODS_OPTION):
        view_cars()
    elif(user_choice == FIND_GOOD_OPTION):
        find_car()
    else:
        break
    
print('Спасибо за использование программы! До свидания!')