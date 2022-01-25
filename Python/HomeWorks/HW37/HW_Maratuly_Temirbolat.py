# Создать собственный итерируемый класс Student, при итерации, класс должен возвращать, по очереди, оценки студента.

ONE_STEP = 1

class Student:
    def __init__(self,name):
        self.__name = name
        self.__subjects = []
        self.__marks = []
    
    def get_marks(self):
        return self.__marks
    
    def get_name(self):
        return self.__name

    def get_subjects(self):
        return self.__subjects
    
    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if(self.__index >= len(self.__marks)):
            raise StopIteration
        else:
            current_subject = self.__subjects[self.__index]
            current_mark = self.__marks[self.__index]
            self.__index += ONE_STEP
            return  (current_subject + ' : ' + str(current_mark))
        
    def __len__(self):
        return len(self.__subjects)

    def __getitem__(self,key):
        if(key == 'name'):
            return self.__name
        else:
            if(key in self.__subjects):
                return self.__marks[self.__subjects.index(key)]
            return IndexError
    
    def __setitem__(self,key,value):
        if(key in self.__subjects):
            key_index = self.__subjects.index(key)
            self.__marks[key_index] = value
        else:
            self.__subjects.append(key)
            self.__marks.append(value)


student_a = Student('Темирболат')
student_a['Философия'] = 5
student_a['Физика'] = 4
student_a['Математика'] = 5
student_a['Физкультура'] = 3 
student_a['Философия'] = 4

print('Оценки студента "{}":'.format(student_a['name']))
for mark in student_a:
    print('\t\t\t',mark)
