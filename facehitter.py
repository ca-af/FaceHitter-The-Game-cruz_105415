from graphics import *
from random import randrange
import time
from math import sqrt

def isClicked(circle, point):
    center = circle.getCenter()
    distance = ((point.getX() - center.getX()) ** 2 + (point.getY() - center.getY()) ** 2) ** 0.5
    
    return distance < circle.radius

def main():
    win = GraphWin('Face Hitter!', 300, 300)
    win.setBackground("blue")
    
    face1 = Circle(Point(150, 150), 100)
    face1.setFill("pink")
    face1.draw(win)
    
    eye1 = Circle(Point(100, 130), 30)
    eye1.setFill("white")
    eye1.draw(win)
    eye2 = Circle(Point(200, 130), 30)
    eye2.setFill("white")
    eye2.draw(win)
    
    pupil1 = Circle(Point(100, 130), 10)
    pupil1.setFill("black")
    pupil1.draw(win)
    
    pupil2 = Circle(Point(200, 130), 10)
    pupil2.setFill("black")
    pupil2.draw(win)
    
    nose = Circle(Point(150, 150), 10)
    nose.setFill("red")
    nose.draw(win)
    
    mouth = Circle(Point(150, 200), 30)
    mouth.setFill("black")
    mouth.draw(win)
    
    message = Text(Point(150, 30), "Click the left eye twice to start the game")
    message.draw(win)
    message.setFace("arial")
    message.setStyle("bold italic")
    message.setTextColor('white')
    win.getMouse()

    face = 0
    
    clickCounter = randrange(10)
    
    
    while (face < 7):    
            mousePos = win.getMouse()
            if isClicked(eye1, mousePos):
                message.undraw()
                message = Text(Point(150, 30), "Click the left eye " + str(clickCounter) +" times!")
                message.setFace("arial")
                message.setStyle("bold italic")
                message.setTextColor('white')
                message.draw(win)
                clickCounter -= 1
                if clickCounter < 0:
                    eye1.undraw()
                    eye2.undraw()
                    pupil1.undraw()
                    pupil2.undraw()
                    nose.undraw()
                    mouth.undraw()
                    face1.undraw()
                    message.undraw()
                    message = Text(Point(150, 150), "You did it!")
                    message.draw(win)
                    win.getMouse()
                    win.close()

    
main()
