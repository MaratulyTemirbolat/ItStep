import datetime
ONE_STEP = 1
class User:
    def __init__(self,login,password,user_name):
        self.__login = login
        self.__password = password
        self.__user_name = user_name
    
    def get_login(self):
        return self.__login
    
    def set_login(self,login):
        self.__login = login
    
    def get_password(self):
        return self.__password
    
    def set_password(self,password):
        self.__password = password
    
    def get_user_name(self):
        return self.__user_name
    
    def set_user_name(self,user_name):
        self.__user_name = user_name

class Topic:
    def __init__(self,name,topic_question,date_creation,question_owner):
        self.__name = name
        self.__topic_question = topic_question
        self.__date_creation = date_creation
        self.__question_owner = question_owner
    
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
    
    def get_topic_question(self):
        return self.__topic_question
    
    def set_topic_question(self,topic_question):
        self.__topic_question = topic_question

    def get_date_creation(self):
        return self.__date_creation
    
    def set_date_creation(self,date_creation):
        self.__date_creation = date_creation
    
    def get_question_owner(self):
        return self.__question_owner
    
    def set_question_owner(self,question_owner):
        self.__question_owner = question_owner
    
    def __str__(self):
        return '\nНазвание темы: {}.\n\nВопрос:{}\n\nДата Создания: {}.\
\t  Спросил пользователь: {}\
'.format(self.__name,self.__topic_question,self.__date_creation,self.__question_owner.get_user_name())

class Message:
    def __init__(self,text,date_creation,user_name):
        self.__text = text
        self.__date_creation = date_creation
        self.__user_name = user_name
    
    def get_text(self):
        return self.__text
    
    def set_text(self,text):
        self.__text = text
    
    def get_date_creation(self):
        return self.__date_creation
    
    def set_date_creation(self,date_creation):
        self.__date_creation = date_creation
    
    def get_user_name(self):
        return self.__user_name
    
    def set_user_name(self,user_name):
        self.__user_name = user_name
    
    def __str__(self):
        return '{}.\n\t\t\tОствил пользователь: {} {}\
'.format(self.__text,self.__user_name,self.__date_creation)

class View:
    def input_user_name(self):
        return input('Введите Имя Пользователя: ')
    
    def input_user_login(self):
        return input('Введите Логин Пользователя: ')
    
    def input_date_creation(self):
        return input('Введите дату: ')
    
    def input_user_password(self):
        return input('Введите Пароль Пользователя: ')
    
    def input_topic_name(self):
        return input('Введите название Темы: ')
    
    def input_topic_message(self):
        return input('Введите сообщение для вашей Темы: ')

    def show_options(self,options):
        print('-------------------------------------------')
        print()
        current_option = 1
        for option in options:
            print(current_option,option)
            current_option += ONE_STEP
    
    def show_existed_topics(self,topics):
        print('-------------------------------------------')
        print()
        current_topic = 1
        for topic in topics:
            print(current_topic,topic.get_name())
            current_topic += ONE_STEP

    def input_user_choice(self):
        return int(input('Ваш выбор: '))
    
    def show_non_existed_option_message(self):
        print('\nИзвините, но данной опции не существует')
    
    def show_buy_message(self):
        print('\nСпасибо за использование программы! До свидания!')
    
    def view_existed_user_message(self):
        print('\nДанный пользователь уже существует')
    
    def show_successfully_created_user_message(self):
        print('\nВаш пользователь успешно создан!')
    
    def view_occured_error(self,error):
        print(error)
    
    def view_existed_topic_message(self):
        print('\nИзвините, но данная тема уже поднята в системе!')
    
    def view_non_existed_topic_message(self):
        print('\nИзвините, но такой темы не существует')
    
    def view_welcom_message(self,username):
        print('\nДобро пожаловать в систему',username)
    
    def view_successful_created_message_creation(self,created_item):
        print(created_item,'успешно создана')
    
    def view_created_item_structure(self,item):
        print('\n',item)
    
    def view_topic_messages(self,topic_messages):
        for message in topic_messages:
            print(message)
    

class Controller:
    users = [User('Mara_jc53','12345','temirbolat009kz')]
    topics = []
    topics_messages = dict()
    current_user = None

    menu_options = ['Авторизоваться','Зарегестрироваться','Выйти из программы']
    user_options = ['Создать новую тему','Создать сообщение внутри темы','Вывести список тем','Вывести список сообщений выбранной темы','Выйти в меню авторизациия']

    view = View()

    def __is_topic_exists(self,topic_name):
        for topic in self.topics:
            if(topic.get_name() == topic_name):
                return True
        return False

    def __get_topic(self,topic_name):
        for topic in self.topics:
            if(topic.get_name() == topic_name):
                return topic

    def create_new_topic(self):
        new_topic = self.view.input_topic_name()
        new_topic_question = self.view.input_topic_message()
        date_time = datetime.date.today()
        topic_date_creation = '{}.{}.{}'.format(date_time.day,date_time.month,date_time.year)
        topic_owner = self.current_user
        if(self.__is_topic_exists(new_topic)):
            self.view.view_existed_topic_message()
        else:
            
            new_user_topic = Topic(new_topic,new_topic_question,topic_date_creation, topic_owner)
            self.topics.append(new_user_topic)
            self.topics_messages[new_user_topic] = []
            self.view.view_created_item_structure(new_user_topic)
            self.view.view_successful_created_message_creation('\nНовая тема')
            
    
    def create_new_message_to_topic(self):
        topic_name = self.view.input_topic_name()
        if(self.__is_topic_exists(topic_name) == False):
            self.view.view_non_existed_topic_message()
        else:
            found_topic = self.__get_topic(topic_name)
            message_text = self.view.input_topic_message()
            date_time = datetime.date.today()
            message_date_creation = '{}.{}.{}'.format(date_time.day,date_time.month,date_time.year)
            message_answered_user_name = self.current_user.get_user_name()
            self.topics_messages[found_topic].append(Message(message_text, message_date_creation, message_answered_user_name))
            self.view.view_successful_created_message_creation('Ваше сообщение')
    
    def view_topic_list(self):
        self.view.show_existed_topics(self.topics)
    
    def view_topic_messages(self):
        try:
            self.view_topic_list()
            user_choice = self.view.input_user_choice()
            if(user_choice < 1 or user_choice > len(self.topics)):
                self.view.view_non_existed_topic_message()
            else:
                selected_topic = self.topics[user_choice - ONE_STEP]
                self.view.view_created_item_structure(selected_topic)
                self.view.view_topic_messages(self.topics_messages[selected_topic])
        except Exception as ex:
            self.view.view_occured_error(ex)

    enterred_user_functions = [create_new_topic,create_new_message_to_topic,view_topic_list,view_topic_messages]

    def enterred_user_menu(self):
        self.view.view_welcom_message(self.current_user.get_user_name())
        while True:
            try:
                self.view.show_options(self.user_options)
                user_choice = self.view.input_user_choice()
                if(user_choice < 1 or user_choice > len(self.user_options)):
                    self.view.show_non_existed_option_message()
                    continue
                elif(user_choice == len(self.user_options)):
                    break
                self.enterred_user_functions[user_choice - ONE_STEP](self)
            except Exception as ex:
                self.view.view_occured_error(ex)

    def find_user_by_login_password(self,login,password):
        found_user = None
        for user in self.users:
            if(user.get_login() == login and user.get_password() == password):
                found_user = user
        return found_user 
    
    def __is_user_exist(self,login):
        for user in self.users:
            if(user.get_login() == login):
                return True
        return False
    
    def register_new_user(self):
        login = self.view.input_user_login()
        password = self.view.input_user_password()
        user_name = self.view.input_user_name()
        if(self.__is_user_exist(login)):
            self.view.view_existed_user_message()
        else:
            new_user = User(login,password,user_name)
            self.users.append(new_user)
            self.view.show_successfully_created_user_message()

    def login(self):
        login = self.view.input_user_login()
        password = self.view.input_user_password()
        found_user = self.find_user_by_login_password(login, password)
        if(found_user is None):
            raise TypeError('Данного пользователя не существует!')
        self.current_user = found_user
        self.enterred_user_menu()

    registration_functions = [login,register_new_user]

    def main_menu(self):
        while True:
            try:
                self.view.show_options(self.menu_options)
                user_choice = self.view.input_user_choice()
                if (user_choice < 1 or user_choice > len(self.menu_options)):
                    self.view.show_non_existed_option_message()
                    continue
                elif(user_choice == len(self.menu_options)):
                    self.view.show_buy_message()
                    break
                self.registration_functions[user_choice - ONE_STEP](self)
            except Exception as ex:
                self.view.view_occured_error(ex)

controller = Controller()
controller.main_menu()