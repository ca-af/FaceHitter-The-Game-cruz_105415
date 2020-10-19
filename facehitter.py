from graphics import *
import random
import time
from math import sqrt

# Esta función es utilizado para determinar cuando el usuasio
# hace clic con el mouse en una parte específica de la cara
def mouseClick(circle, point):
    center = circle.getCenter()
    distance = ((point.getX() - center.getX()) ** 2 + (point.getY() - center.getY()) ** 2) ** 0.5
    
    return distance < circle.radius

# Esta función decide un cara basado en la dificultad
# que escoge el usuario.
def randomFacePicker():
    x = 1
    
# Esta función decide cuantos clicks aleatorios necesita hacer
# en cada parte de la cara elegida.
def randomClicksPicker():
    clickCounter = random.randint(1, 20)
    return clickCounter

# Esta función decide aleatoriamente qué partes de la cara el usuario
# debe hacer click para ganar el juego.
def randomPicker():
    clickCounter = random.randint(1, 4)
    return clickCounter

# Esta función empieza el juego con la cara elegida.
def faceSelector(win):
    return faceDrawer(win)

# Esta función dibuja las carras (faltan tres).
def faceDrawer(win):
    face1 = Circle(Point(150, 150), 100)
    face1.setFill("pink")
    face1.draw(win)
    
    # Se dibuja el ojo izquierdo y derecho
    eye1 = Circle(Point(100, 130), 30)
    eye1.setFill("white")
    eye1.draw(win)
    eye2 = Circle(Point(200, 130), 30)
    eye2.setFill("white")
    eye2.draw(win)
    
    # Se dibuja el pupila del ojo izquerdo y derecho
    pupil1 = Circle(Point(100, 130), 10)
    pupil1.setFill("black")
    pupil1.draw(win)
    pupil2 = Circle(Point(200, 130), 10)
    pupil2.setFill("black")
    pupil2.draw(win)
    
    # Se dibuja la nariz
    nose = Circle(Point(150, 150), 10)
    nose.setFill("red")
    nose.draw(win)
    
    # Se dibuja la boca
    mouth = Circle(Point(150, 200), 30)
    mouth.setFill("black")
    mouth.draw(win)
    
    # Se llama las reglas del juego
    gameRules(win, face1, eye1, eye2, pupil1, pupil2, nose, mouth)

# Las reglas del juego son mostrados al jugador.
def gameRules(win, face1, eye1, eye2, pupil1, pupil2, nose, mouth):
    #Escribe las reglas al usuario
    message = Text(Point(150, 30), "Click anywhere to start the game")
    message.setFace("arial")
    message.setStyle("bold italic")
    message.setTextColor('white')
    message.draw(win)
    
    win.getMouse()
    
    gameSession(win, face1, eye1, eye2, pupil1, pupil2, nose, mouth, message)
    
# El juego se empienza aquí.
def gameSession(win, face1, eye1, eye2, pupil1, pupil2, nose, mouth, message):
    
    # El juego aleatoriamente elige la cantidad de clicks que el usuario 
    # debe hacer en una parte específica de la cara.
    clickCounter = randomClicksPicker()
    numberPick = randomPicker()
    part1 = True
    part2 = True
    part3 = True
    part4 = True
    
    # El juego verifica si se ha hecho clic en una determinada parte de la 
    # cara la cantidad de veces especificada.
    while (part1 == True or part2 == True or part3 == True or part4 == True):
        # El juego verifica si el ojo izquiero fue elegido y dado unas cuantas
        # veces.
        if (numberPick == 1 and part1 == True):
            message.undraw()
            message = Text(Point(150, 30), "Click the left eye " + str(clickCounter) + " times!")
            message.setFace("arial")
            message.setStyle("bold italic")
            message.setTextColor('white')
            message.draw(win)
            if mouseClick(eye1, win.getMouse()):
                clickCounter -= 1
                message.undraw()
                message = Text(Point(150, 30), "Click the left eye " + str(clickCounter) + " times!")
                message.setFace("arial")
                message.setStyle("bold italic")
                message.setTextColor('white')
                message.draw(win)
                while (clickCounter == 0):
                    eye1.undraw()
                    pupil1.undraw()
                    clickCounter = randomPicker()
                    numberPick = randomPicker()
                    part1 = False
                    continue
        # El juego verifica si el ojo izquierdo ha sido borrada de la cara 
        # por el jugador.
        elif (numberPick == 1 and part1 == False):
            numberPick = randomPicker()
            clickCounter = randomPicker()
            continue
        # El juego verifica si el ojo derecho fue elegido y dado unas cuantas
        # veces.
        elif (numberPick == 2 and part2 == True):
            message.undraw()
            message = Text(Point(150, 30), "Click the right eye " + str(clickCounter) + " times!")
            message.setFace("arial")
            message.setStyle("bold italic")
            message.setTextColor('white')
            message.draw(win)
            if mouseClick(eye2, win.getMouse()):
                clickCounter -= 1
                message.undraw()
                message = Text(Point(150, 30), "Click the right eye " + str(clickCounter) + " times!")
                message.setFace("arial")
                message.setStyle("bold italic")
                message.setTextColor('white')
                message.draw(win)
                while (clickCounter == 0):
                    eye2.undraw()
                    pupil2.undraw()
                    clickCounter = randomPicker()
                    numberPick = randomPicker()
                    part2 = False
                    continue
        # El juego verifica si el ojo derecho ha sido borrada de la cara 
        # por el jugador.
        elif (numberPick == 2 and part2 == False):
            numberPick = randomPicker()
            clickCounter = randomPicker()
            continue
        # El juego verifica si la nariz fue elegido y dado unas cuantas
        # veces.
        elif (numberPick == 3 and part3 == True):
            message.undraw()
            message = Text(Point(150, 30), "Click the nose " + str(clickCounter) + " times!")
            message.setFace("arial")
            message.setStyle("bold italic")
            message.setTextColor('white')
            message.draw(win)
            if mouseClick(nose, win.getMouse()):
                clickCounter -= 1
                message.undraw()
                message = Text(Point(150, 30), "Click the nose " + str(clickCounter) + " times!")
                message.setFace("arial")
                message.setStyle("bold italic")
                message.setTextColor('white')
                message.draw(win)
                while (clickCounter == 0):
                    nose.undraw()
                    clickCounter = randomPicker()
                    numberPick = randomPicker()
                    part3 = False
                    continue
        # El juego verifica si la nariz ha sido borrada de la cara 
        # por el jugador.
        elif (numberPick == 3 and part3 == False):
            numberPick = randomPicker()
            clickCounter = randomPicker()
            continue
        # El juego verifica si la boca fue elegido y dado unas cuantas
        # veces.
        elif (numberPick == 4 and part4 == True):
            message.undraw()
            message = Text(Point(150, 30), "Click the mouth " + str(clickCounter) + " times!")
            message.setFace("arial")
            message.setStyle("bold italic")
            message.setTextColor('white')
            message.draw(win)
            if mouseClick(mouth, win.getMouse()):
                clickCounter -= 1
                message.undraw()
                message = Text(Point(150, 30), "Click the mouth " + str(clickCounter) + " times!")
                message.setFace("arial")
                message.setStyle("bold italic")
                message.setTextColor('white')
                message.draw(win)
                while (clickCounter == 0):
                    mouth.undraw()
                    clickCounter = randomPicker()
                    numberPick = randomPicker()
                    part4 = False
                    continue
        # El juego verifica si la boca ha sido borrada de la cara 
        # por el jugador.
        elif (numberPick == 4 and part4 == False):
            numberPick = randomPicker()
            clickCounter = randomPicker()
            continue
        else:
            break
                
    endGame(win, face1, message)

# El juego se acaba si el usuario gana o no
def endGame(win, face1, message):
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
            
#Aqui se hace la pantalla del juego
def main():
    #Se crea un window nuevo para el juego
    win = GraphWin('Face Hitter!', 300, 300)
    win.setBackground("blue")
    
    #Se escribe el mensaje de bienvenida para el usuario
    intro = Text(Point(150, 140), "Hello! Welcome to Face Hitter!")
    intro.setFace("times roman")
    intro.setStyle("bold italic")
    intro.setTextColor("yellow")
    intro.draw(win)
    
    message = Text(Point(150, 160), "Click anywhere to continue.")
    message.setTextColor("white")
    message.draw(win)
    win.getMouse()
    message.undraw()
    intro.undraw()
    
    #Llama a una cara random
    faceSelector(win)
    
    win.close()
    
main()
