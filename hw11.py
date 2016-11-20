#Michael Osorio
#11/26/14

# Vector class
# January 26, 2010
# RLH

import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitude(self):
        """ Returns magnitude of vector """
        return math.sqrt(self.x * self.x + self.y* self.y)

    def normalize(self):
        """ Sets vector magnitude to 1 """
        mag = self.magnitude()
        self.x = self.x/mag
        self.y = self.y/mag

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

# Matrix class
# January 26, 2010
# RLH

from Vector import *

class Matrix:
    """ 2x2 matrix class """

    def __init__(self, a11=0, a12=0, a21=0, a22=0):
        self.array = [[a11, a12], [a21, a22]]

    def set(self, row, column, value):
        """Set element at row and column to given value"""
        self.array[row][column] = value

    def get(self, row, column):
        """Get value at given row and column"""
        return self.array[row][column]

    def __add__(self, other):
        result = Matrix()
        for row in range(0, 2):
            for col in range(0, 2):
                result.set(row, col, self.get(row, col) + other.get(row, col))
        return result

    def __mul__(self, other):
        """ if other is a Matrix, returns a Matrix.  If other is a Vector, returns a Vector."""
        if other.__class__.__name__ == "Matrix":
            result = Matrix()
            for row in range(0, 2):
                for col in range(0, 2):
                    # Compute result matrix in the given row and col
                    entry = 0
                    for i in range(0, 2):
                            entry += self.get(row, i) * other.get(i, col)
                    result.set(row, col, entry)
            return result
        elif other.__class__.__name__ == "Vector":
            result = Vector()
            x = self.get(0, 0) * other.x + self.get(0, 1) * other.y
            y = self.get(1, 0) * other.x + self.get(1, 1) * other.y
            return Vector(x, y)
        else:
            print "Can't multiply a matrix by a ", other.__class__.name__, "!!!"  # !!! is a nice touch

    def __repr__(self):
        return str(self.array[0][0]) + " " + str(self.array[0][1]) + "\n" + str(self.array[1][0]) + " " + str(self.array[1][1])

# Shapes
# January 26, 2010
# RLH

import math
import turtle

from Matrix import *
from Vector import *

class Shape:
    def __init__(self):
        self.points = []
        
    def render(self):
        """Use turtle graphics to render shape"""
        turtle.penup()
        turtle.setposition(self.points[0].x, self.points[0].y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        for vector in self.points[1:]:
            turtle.setposition(vector.x, vector.y)
        turtle.setposition(self.points[0].x, self.points[0].y)
        turtle.end_fill()

    def erase(self):
        """Draw shape in white to effectively erase it from screen"""
        temp = self.color
        self.color = "white"
        self.render()
        self.color = temp
    
    def rotate(self, theta):
        """Rotate shape by theta degrees """
        theta = math.radians(theta)  # THIS IS CORRECT!
        # Python's trig functions expect input in radians
        # so this function converts from degrees into radians.
        RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))
        NewPoints = []
        for vector in self.points:
            newvector = RotationMatrix * vector
            NewPoints.append(newvector)
        self.points = NewPoints
        
class Rectangle(Shape):
    def __init__(self, width, height, center = Vector(0, 0), color = "black"):
        SW = Vector(center.x - width/2.0, center.y - height/2.0)
        NW = Vector(center.x - width/2.0, center.y + height/2.0)
        NE = Vector(center.x + width/2.0, center.y + height/2.0)
        SE = Vector(center.x + width/2.0, center.y - height/2.0)
        self.points = [SW, NW, NE, SE]
        self.color = color

class Square(Rectangle):
    def __init__(self, width, center=Vector(0, 0), color = "black"):
        Rectangle.__init__(self, width, width, center, color)
        
class Circle(Shape):
    def __init__(self, center = Vector(0, 0), radius = 10, color = "black"):
        self.center = center
        self.radius = radius
        self.color = color

    def render(self):
        turtle.penup()
        turtle.setposition(self.center.x, self.center.y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()

    def rotate(self, theta):
        """ theta is in degrees """
        theta = math.radians(theta)
        RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))        
        self.center = RotationMatrix * self.center
