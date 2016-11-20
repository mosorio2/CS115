class Shape(object):
    def __init__(self, x, y, name="Shape"):
        self.__x=x
        self.__y=y
        self.__name=name

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x<0:
            raise ValueError("x coordinate must be >= 0")
        self.__x=x


    def __eq__(self, rhs):
        return self.__x == rhs.__x and self.__y == rhs.__y and \
               self.__name == rhs.__name

        
    def __str__(self):
        return self.__name + ' at (' + str(self.__x) + ', ' + \
               str(self.__y) + ')'
    
class Rectangle(Shape):
    def __init__(self, x, y, length, width, name = "Rectangle"):
        Shape.__init__(self, x, y, name)
        self.__length=length
        self.__width=width

    def __eq__(self, rhs):
        return self.__length == rhs.__length and self.__width == rhs.__width
    
if __name__=='__main__':
    s=Shape(3,2,"MyShape")
    print s
    s.x=4
    print s


x=Rectangle(1,1,1,1, "rectangle")
y=Rectangle(1,1,1,1, "rectangle")
print x==y

