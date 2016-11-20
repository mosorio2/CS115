#Michael Osorio
#I pledge my honor that I have abided by the Stevens Honor System.
#11/26/14

import math
import turtle

from Matrix import *
from Vector import *

class Shape:
    def __init__(self):
        """initializes Shape class"""
        self.points = []
        
    def render(self):
        """Use Turtle graphics to render shape"""
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

    def translate(self, vector):
        """translates any current shapes by a vector"""
        for i in self.points:
            i.x += vector.x
            i.y += vector.y
    
    def rotate(self, theta, rotateAbout = Vector(0,0)):
        """Rotate shape by theta degrees """
        for i in self.points:
            i.x -= rotateAbout.x
            i.y -= rotateAbout.y
        theta = math.radians(theta)  # THIS IS CORRECT!
        # Python's trig functions expect input in radians
        # so this function converts from degrees into radians.
        RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))
        NewPoints = []
        for vector in self.points:
            newvector = RotationMatrix * vector
            NewPoints.append(newvector)
        self.points = NewPoints
        for i in self.points:
            i.x += rotateAbout.x
            i.y += rotateAbout.y
        
class Rectangle(Shape):
    def __init__(self, width, height, center = Vector(0, 0), color = "red"):
        """initializes Rectangle class"""
        SW = Vector(center.x - width/2.0, center.y - height/2.0)
        NW = Vector(center.x - width/2.0, center.y + height/2.0)
        NE = Vector(center.x + width/2.0, center.y + height/2.0)
        SE = Vector(center.x + width/2.0, center.y - height/2.0)
        self.points = [SW, NW, NE, SE]
        self.color = color

class Square(Rectangle):
    def __init__(self, width, center=Vector(0, 0), color = "green"):
        """initializes Square class"""
        Rectangle.__init__(self, width, width, center, color)
        
class Circle(Shape):
    def __init__(self, center = Vector(0, 0), radius = 100, color = "blue"):
        """initializes Circle class"""
        self.center = center
        self.radius = radius
        self.color = color

    def render(self):
        """renders shape using Turtle graphics"""
        turtle.penup()
        turtle.setposition(self.center.x, self.center.y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()

    def translate(self, vector):
        """translates any current shapes by a vector"""
        self.center = Vector(self.center.x + vector.x, self.center.y + vector.y)
        
    def rotate(self, theta):
        """ theta is in degrees """
        theta = math.radians(theta)
        RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))        
        self.center = RotationMatrix * self.center

class Triangle(Shape):
    def __init__(self, width, height, center = Vector(0, 0), color = "yellow"):
        """initializes Triangle class"""
        self.center = center
        self.width = width
        self.height = height
        self.color = color
        N = Vector(center.x, center.x + height/2)
        SW = Vector(center.x - width/2, center.x - height/2)
        SE = Vector(center.x + width/2, center.x - height/2)
        self.points = [N, SW, SE]

#main function
def main():
    """main function that returns desired result"""
    r = Rectangle(50,70)
    s = Square(50)
    t = Triangle(70, 120)
    c = Circle()

    r.rotate(40, Vector(20, 70))
    r.translate(Vector(100, 150))
    r.render()

    s.rotate(40, Vector(60, 120))
    s.translate(Vector(-150, -100))
    s.render()

    t.rotate(50)
    t.render()

    c.translate(Vector(-40, 70))
    c.rotate(10)
    c.render()

    turtle.exitonclick()

if __name__ == "__main__":
    main()
