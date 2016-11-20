class Student(object):

    def __init__(self, first_name, last_name, sid):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__sid = sid
        self.__grades = [100,50]

    def name_length(self):
        return len(self.__first_name) + len(self.__last_name)


    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if first_name == 'Troy':
            raise ValueError('DO NOT CHANGE NAME TO TROY')
        self.__first_name= first_name

    @property
    def grades(self):
        return self.__grades
        
    def __repr__(self):
        return self.__class__.__name__ + '(' + self.__first_name + ', ' + \
               self.__last_name + ', ' + self.__sid + ')'

    def __str__(self):
        return self.__first_name + ' ' + self.__last_name + ', ' + str(self.__grades)


if __name__ == '__main__':
    s1 = Student('Stephen', 'McArdle', '12345678')
    print repr(s1)
    print s1.first_name
    s1.first_name='Tom'
    print s1
    s1._Student__first_name = 'Troy'
    print s1
    grades=s1.grades
    grades[1]=100
    print s1
