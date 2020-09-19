from graphics import *
from random import randrange
import time
from math import sqrt

#Esta función es utilizado para determinar si el usuario le está dando al ojo izquierdo.
def isClicked(circle, point):
    center = circle.getCenter()
    distance = ((point.getX() - center.getX()) ** 2 + (point.getY() - center.getY()) ** 2) ** 0.5
    
    return distance < circle.radius
#Aqui se hace la pantalla del juego
def main():
    win = GraphWin('Face Hitter!', 300, 300)
    win.setBackground("blue")
    
    #Se dibuja la cara
    face1 = Circle(Point(150, 150), 100)
    face1.setFill("pink")
    face1.draw(win)
    
    #Se dibuja el ojo izquierdo y derecho
    eye1 = Circle(Point(100, 130), 30)
    eye1.setFill("white")
    eye1.draw(win)
    eye2 = Circle(Point(200, 130), 30)
    eye2.setFill("white")
    eye2.draw(win)
    
    #Se dibuja el pupila de ojo izquerdo y derecho
    pupil1 = Circle(Point(100, 130), 10)
    pupil1.setFill("black")
    pupil1.draw(win)
    pupil2 = Circle(Point(200, 130), 10)
    pupil2.setFill("black")
    pupil2.draw(win)
    
    #Se dibuja la nariz
    nose = Circle(Point(150, 150), 10)
    nose.setFill("red")
    nose.draw(win)
    
    #Se dibuja la boca
    mouth = Circle(Point(150, 200), 30)
    mouth.setFill("black")
    mouth.draw(win)
    
    #Escribe las reglas al usuario
    message = Text(Point(150, 30), "Click the left eye twice to start the game")
    message.draw(win)
    message.setFace("arial")
    message.setStyle("bold italic")
    message.setTextColor('white')
    win.getMouse()

    face = 0
    
    #El programa escoje un numero random para
    #la cantidad de veces que el usuario tiene que hacer clic en el ojo izquierdo.
    clickCounter = randrange(100)
    
    while (face < 7):    
            #Aquí se verifica si el usuario esta haciendo click al ojo izquierdo.
            mousePos = win.getMouse()
            if isClicked(eye1, mousePos):
                message.undraw()
                message = Text(Point(150, 30), "Click the left eye " + str(clickCounter) +" times!")
                message.setFace("arial")
                message.setStyle("bold italic")
                message.setTextColor('white')
                message.draw(win)
                clickCounter -= 1
                #Cuando el usuario termina los clicks, el juego borra la cara y se cierra.
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
                    message.setFace("arial")
                    message.setStyle("bold italic")
                    message.setTextColor('white')
                    message.draw(win)
                    message2 = Text(Point(150, 170), "Click again to close the game!")
                    message2.setFace("arial")
                    message2.setStyle("bold italic")
                    message2.setTextColor('white')
                    message2.draw(win)
                    win.getMouse()
                    win.close()
    
main()
