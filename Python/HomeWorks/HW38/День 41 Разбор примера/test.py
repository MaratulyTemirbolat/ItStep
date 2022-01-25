class Events:
    def __init__(self):
        self.__time =[]
        self.__details = []

    def add_event(self, time, details):
        self.__time.append(time)
        self.__details.append(details)

    def __str__(self):
        i = 0
        str_ = ''
        while i < len (self.__time):
            str_ += self.__time[i] + \
                    ' | ' + \
                    self.__details[i] + '\n'
            i += 1
        return str_

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        if self.__i > len(self.__time) - 1:
            raise StopIteration
        else:
            event = self.__time[self.__i] + \
                    ' | ' + \
                    self.__details[self.__i]
            self.__i += 1
            return event

class DiaryNote:
    def __init__(self):
        self.__dates = []
        self.__events = []

    def add_date(self, dates):
        try:
            return self.__dates.index(dates)
        except ValueError:
            self.__dates.append(dates)
            self.__events.append(Events())
            return self.__dates.index(dates)
        
    def add_event(self, dates, time, detail):
        key = self.add_date(dates)
        self.__events[key].add_event(time, detail)

    def get_dates(self):
        dates = ''
        for i in self.__dates:
            dates += i +'\n'
        return dates

    def get_day_events(self, date):
        key = self.__dates.index(date)
        return self.__events[key]

    def __getitem__(self, date):
        try:
            return self.get_day_events(date)
        except ValueError:
            raise IndexError

test = DiaryNote()
test.add_date('26.10.2021')
print(test.get_dates())
test.add_event('25.10.2021','00:00:00', 'Начало времён')
test.add_event('25.10.2021','13:00:00', 'Обед')
print(test['26.10.2021'])
print(test['25.10.2021'])

#print(test)
