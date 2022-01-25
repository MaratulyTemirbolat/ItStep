class Events:
    def __init__(self):
        self.__time = []
        self.__details = []
    
    def get_time_details(self,time):
        if(time in self.__time):
            key = self.__time.index(time)
            return self.__details[key]
        else:
            raise ValueError
    
    def __getitem__(self,time):
        try:
            return self.get_time_details(time)
        except ValueError:
            raise IndexError
    
    def __setitem__(self,key,value):
        try:
            key = self.__time.index(key)
            self.__details[key] = value
        except Exception:
            self.__time.append(key)
            self.__details.append(value)

    def __str__(self):
        i = 0
        comma = ', '
        str_ = ""
        while i < len(self.__time):
            if(i == len(self.__time) - 1):
                comma = ' '
            str_ += self.__time[i] + \
                    " | " + \
                    self.__details[i] + comma
            i+=1
        return str_

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        if self.__i > len(self.__time)-1:
            raise StopIteration
        else:
            event = self.__time[self.__i] + \
                    "| " + \
                    self.__details[self.__i]
            self.__i += 1
            return event
    
class DiaryNote:
    def __init__(self):
        self.__dates = []
        self.__events = []

    def add_date(self,dates):
        try:
            return self.__dates.index(dates)
        except ValueError:
            self.__dates.append(dates)
            self.__events.append(Events())
            return self.__dates.index(dates)

    def add_event(self,dates,time,detail):
        key = self.add_date(dates)
        self.__events[key][time] = detail

    def get_dates(self):
        dates = ""
        for i in self.__dates:
            dates += i + "\n"
        return dates
    
    def get_day_events(self,date):
        key = self.__dates.index(date)
        # print(key)
        return self.__events[key]

    def __getitem__(self,date):
        try:
            return self.get_day_events(date)
        except ValueError:
            raise IndexError
    
    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if(self.__index > len(self.__dates) - 1):
            raise StopIteration
        else:
            result = '[' + self.__dates[self.__index] + ', [' + str(self.__events[self.__index]) + ']'
            self.__index += 1
            return result
    
    def __len__(self):
        return len(self.__dates)

class View:
    def input_date(self):
        return input('Пожалуйста, введите дату события: ')
    
    def input_time(self):
        return input('Пожалуйста, введите время события: ')
    
    def input_detail(self):
        return input('Пожалуйста, введите событие: ')
    
    def view_options(self,options):
        print()
        option_number = 1
        for option in options:
            print(option_number,option)
            option_number += 1
    
    def input_user_choice(self):
        return int(input('Ваш выбор: '))

    def view_wrong_message(self,error):
        print('Ошибка:',error)
    
    def view_buy_message(self):
        print('Спасибо за использование программы! До свидания!')
    
    def view_date_events(self,date,events):
        print('События для даты "{}":'.format(date))
        print(events)
    
    def view_all_dairy_note_info(self,dairy_note):
        print('[',end = "")
        comma = ', '
        current_date = 1
        for date in dairy_note:
            if(current_date == len(dairy_note)):
                comma = ''
            print(date,end = "]{}".format(comma))
            current_date += 1
        print(']')

class Controller:
    view = View()
    diary_note = DiaryNote()
    menu_options = ['Создать событие','Просмотреть события данного дня','Просмотреть все события','Выйти из программы']
    
    def create_event(self):
        event_date = self.view.input_date()
        event_time = self.view.input_time()
        event_details = self.view.input_detail()
        self.diary_note.add_event(event_date,event_time,event_details)
    
    def view_date_events(self):
        event_date = self.view.input_date()
        self.view.view_date_events(event_date, self.diary_note[event_date])

    def view_all_dates_events(self):
        self.view.view_all_dairy_note_info(self.diary_note)

    menu_functions = [create_event,view_date_events,view_all_dates_events]

    def main_program(self):
        while(True):
            try:
                self.view.view_options(self.menu_options)
                user_choice = self.view.input_user_choice()
                if(user_choice <= 0 or user_choice > len(self.menu_options)):
                    self.view.view_wrong_message('такой опции нет!')
                    continue
                elif(user_choice == len(self.menu_options)):
                    self.view.view_buy_message()
                    break
                self.menu_functions[user_choice - 1](self)
            except ValueError as ex:
                # print(type(ex))
                self.view.view_wrong_message('Вам надо написать число, а не что то другое')
            except IndexError as ex:
                # print(type(ex))
                self.view.view_wrong_message('Извините, но таких данных нет')
            except Exception as ex:
                # print(type(ex))
                self.view.view_wrong_message(ex)
                
            
controller = Controller()
controller.main_program()
