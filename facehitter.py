from graphics import *
import random
import time
from math import sqrt

class FaceHitter:
    # Esta función es utilizado para determinar cuando el usuasio
    # hace clic con el mouse en una parte específica de la cara
    def mouseClick(self, circle, point):
        self.center = circle.getCenter()
        self.distance = ((point.getX() - self.center.getX()) ** 2 
                         + (point.getY() - self.center.getY()) ** 2) ** 0.5

        return self.distance < circle.radius

    # Esta función decide un cara basado en la dificultad
    # que escoge el usuario.
    def randomFacePicker(self):
        self.x = 1

    # Esta función decide cuantos clicks aleatorios necesita hacer
    # en cada parte de la cara elegida.
    def randomClicksPicker(self):
        self.clickCounter = random.randint(1, 20)
        return self.clickCounter

    # Esta función decide aleatoriamente qué partes de la cara el usuario
    # debe hacer click para ganar el juego.
    def randomPicker(self):
        self.clickCounter = random.randint(1, 4)
        return self.clickCounter

    def setScore(self, x):
        self.score += x

    def getScore(self):
        return self.score

    # Esta función dibuja las carras (faltan tres).
    def faceDrawer(self):
        self.face1 = Circle(Point(150, 150), 100)
        self.face1.setFill("pink")
        self.face1.draw(self.win)

        # Se dibuja el ojo izquierdo y derecho
        self.eye1 = Circle(Point(100, 130), 30)
        self.eye1.setFill("white")
        self.eye1.draw(self.win)
        self.eye2 = Circle(Point(200, 130), 30)
        self.eye2.setFill("white")
        self.eye2.draw(self.win)

        # Se dibuja el pupila del ojo izquerdo y derecho
        self.pupil1 = Circle(Point(100, 130), 10)
        self.pupil1.setFill("black")
        self.pupil1.draw(self.win)
        self.pupil2 = Circle(Point(200, 130), 10)
        self.pupil2.setFill("black")
        self.pupil2.draw(self.win)

        # Se dibuja la nariz
        self.nose = Circle(Point(150, 150), 10)
        self.nose.setFill("red")
        self.nose.draw(self.win)

        # Se dibuja la boca
        self.mouth = Circle(Point(150, 200), 30)
        self.mouth.setFill("black")
        self.mouth.draw(self.win)

    # Las reglas del juego son mostrados al jugador.
    def gameRules(self):
        # Escribe las reglas al usuario
        self.message = Text(Point(150, 30), "Click anywhere to start the game")
        self.message.setFace("arial")
        self.message.setStyle("bold italic")
        self.message.setTextColor('white')
        self.message.draw(self.win)

        self.win.getMouse()
        
     # El juego se acaba si el usuario gana o no
    def endGame(self):
        self.face1.undraw()
        self.message.undraw()
        self.message = Text(Point(150, 150), "You did it!")
        self.message.setFace("arial")
        self.message.setStyle("bold italic")
        self.message.setTextColor('white')
        self.message.draw(self.win)

        self.messageScore.undraw()
        self.messageScore = Text(Point(140, 100), "Score: ")
        self.messageScore.setFace("arial")
        self.messageScore.setStyle("bold italic")
        self.messageScore.setTextColor('white')
        self.messageScore.draw(self.win)

        self.displayScore = Text(Point(175, 100), str(self.score))
        self.displayScore.setFace("arial")
        self.displayScore.setStyle("bold italic")
        self.displayScore.setTextColor('yellow')
        self.displayScore.draw(self.win)

        self.message2 = Text(Point(150, 170), "Click again to close the game!")
        self.message2.setFace("arial")
        self.message2.setStyle("bold italic")
        self.message2.setTextColor('white')
        self.message2.draw(self.win)

        self.win.getMouse()

    # El juego se empienza aquí.
    def gameSession(self):

        # El juego aleatoriamente elige la cantidad de clicks que el usuario 
        # debe hacer en una parte específica de la cara.
        self.clickCounter = self.randomClicksPicker()
        self.numberPick = self.randomPicker()
        self.part1 = True
        self.part2 = True
        self.part3 = True
        self.part4 = True
        self.score = 0

        self.messageScore = Text(Point(145, 272), "Score: " + str(self.score))
        self.messageScore.setFace("helvetica")
        self.messageScore.setStyle("bold italic")
        self.messageScore.setTextColor('yellow')
        self.messageScore.draw(self.win)

        # El juego verifica si se ha hecho clic en una determinada parte de la 
        # cara la cantidad de veces especificada.
        while (self.part1 == True or self.part2 == True or self.part3 == True or self.part4 == True):
            # El juego verifica si el ojo izquiero fue elegido y dado unas cuantas
            # veces.
            if (self.numberPick == 1 and self.part1 == True):
                self.message.undraw()
                self.message = Text(Point(150, 30), "Click the left eye " + str(self.clickCounter) + " times!")
                self.message.setFace("arial")
                self.message.setStyle("bold italic")
                self.message.setTextColor('white')
                self.message.draw(self.win)
                if self.mouseClick(self.eye1, self.win.getMouse()):
                    self.clickCounter -= 1
                    self.message.undraw()
                    self.message = Text(Point(150, 30), "Click the left eye " + str(self.clickCounter) + " times!")
                    self.message.setFace("arial")
                    self.message.setStyle("bold italic")
                    self.message.setTextColor('white')
                    self.message.draw(self.win)
                    self.score += 5
                    self.messageScore.undraw()
                    self.messageScore = Text(Point(145, 272), "Score: " + str(self.score))
                    self.messageScore.setFace("helvetica")
                    self.messageScore.setStyle("bold italic")
                    self.messageScore.setTextColor('yellow')
                    self.messageScore.draw(self.win)
                    while (self.clickCounter == 0):
                        self.eye1.undraw()
                        self.pupil1.undraw()
                        self.clickCounter = self.randomPicker()
                        self.numberPick = self.randomPicker()
                        self.part1 = False
                        continue
            # El juego verifica si el ojo izquierdo ha sido borrada de la cara 
            # por el jugador.
            elif (self.numberPick == 1 and self.part1 == False):
                self.numberPick = self.randomPicker()
                self.clickCounter = self.randomPicker()
                continue
            # El juego verifica si el ojo derecho fue elegido y dado unas cuantas
            # veces.
            elif (self.numberPick == 2 and self.part2 == True):
                self.message.undraw()
                self.message = Text(Point(150, 30), "Click the right eye " + str(self.clickCounter) + " times!")
                self.message.setFace("arial")
                self.message.setStyle("bold italic")
                self.message.setTextColor('white')
                self.message.draw(self.win)
                if self.mouseClick(self.eye2, self.win.getMouse()):
                    self.clickCounter -= 1
                    self.message.undraw()
                    self.message = Text(Point(150, 30), "Click the right eye " + str(self.clickCounter) + " times!")
                    self.message.setFace("arial")
                    self.message.setStyle("bold italic")
                    self.message.setTextColor('white')
                    self.message.draw(self.win)
                    self.score += 5
                    self.messageScore.undraw()
                    self.messageScore = Text(Point(145, 272), "Score: " + str(self.score))
                    self.messageScore.setFace("helvetica")
                    self.messageScore.setStyle("bold italic")
                    self.messageScore.setTextColor('yellow')
                    self.messageScore.draw(self.win)
                    while (self.clickCounter == 0):
                        self.eye2.undraw()
                        self.pupil2.undraw()
                        self.clickCounter = self.randomPicker()
                        self.numberPick = self.randomPicker()
                        self.part2 = False
                        continue
            # El juego verifica si el ojo derecho ha sido borrada de la cara 
            # por el jugador.
            elif (self.numberPick == 2 and self.part2 == False):
                self.numberPick = self.randomPicker()
                self.clickCounter = self.randomPicker()
                continue
            # El juego verifica si la nariz fue elegido y dado unas cuantas
            # veces.
            elif (self.numberPick == 3 and self.part3 == True):
                self.message.undraw()
                self.message = Text(Point(150, 30), "Click the nose " + str(self.clickCounter) + " times!")
                self.message.setFace("arial")
                self.message.setStyle("bold italic")
                self.message.setTextColor('white')
                self.message.draw(self.win)
                if self.mouseClick(self.nose, self.win.getMouse()):
                    self.clickCounter -= 1
                    self.message.undraw()
                    self.message = Text(Point(150, 30), "Click the nose " + str(self.clickCounter) + " times!")
                    self.message.setFace("arial")
                    self.message.setStyle("bold italic")
                    self.message.setTextColor('white')
                    self.message.draw(self.win)
                    self.score += 5
                    self.messageScore.undraw()
                    self.messageScore = Text(Point(145, 272), "Score: " + str(self.score))
                    self.messageScore.setFace("helvetica")
                    self.messageScore.setStyle("bold italic")
                    self.messageScore.setTextColor('yellow')
                    self.messageScore.draw(self.win)
                    while (self.clickCounter == 0):
                        self.nose.undraw()
                        self.clickCounter = self.randomPicker()
                        self.numberPick = self.randomPicker()
                        self.part3 = False
                        continue
            # El juego verifica si la nariz ha sido borrada de la cara 
            # por el jugador.
            elif (self.numberPick == 3 and self.part3 == False):
                self.numberPick = self.randomPicker()
                self.clickCounter = self.randomPicker()
                continue
            # El juego verifica si la boca fue elegido y dado unas cuantas
            # veces.
            elif (self.numberPick == 4 and self.part4 == True):
                self.message.undraw()
                self.message = Text(Point(150, 30), "Click the mouth " + str(self.clickCounter) + " times!")
                self.message.setFace("arial")
                self.message.setStyle("bold italic")
                self.message.setTextColor('white')
                self.message.draw(self.win)
                if self.mouseClick(self.mouth, self.win.getMouse()):
                    self.clickCounter -= 1
                    self.message.undraw()
                    self.message = Text(Point(150, 30), "Click the mouth " + str(self.clickCounter) + " times!")
                    self.message.setFace("arial")
                    self.message.setStyle("bold italic")
                    self.message.setTextColor('white')
                    self.message.draw(self.win)
                    self.score += 5
                    self.messageScore.undraw()
                    self.messageScore = Text(Point(145, 272), "Score: " + str(self.score))
                    self.messageScore.setFace("helvetica")
                    self.messageScore.setStyle("bold italic")
                    self.messageScore.setTextColor('yellow')
                    self.messageScore.draw(self.win)
                    while (self.clickCounter == 0):
                        self.mouth.undraw()
                        self.clickCounter = self.randomPicker()
                        self.numberPick = self.randomPicker()
                        self.part4 = False
                        continue
            # El juego verifica si la boca ha sido borrada de la cara 
            # por el jugador.
            elif (self.numberPick == 4 and self.part4 == False):
                self.numberPick = self.randomPicker()
                self.clickCounter = self.randomPicker()
                continue
            else:
                break
            
    def __init__(self):
        #Se crea un window nuevo para el juego
        self.win = GraphWin('Face Hitter!', 300, 300)
        self.win.setBackground("blue")

        #Se escribe el mensaje de bienvenida para el usuario
        self.intro = Text(Point(150, 140), "Hello! Welcome to Face Hitter!")
        self.intro.setFace("times roman")
        self.intro.setStyle("bold italic")
        self.intro.setTextColor("yellow")
        self.intro.draw(self.win)

        self.message = Text(Point(150, 160), "Click anywhere to continue.")
        self.message.setTextColor("white")
        self.message.draw(self.win)
        self.win.getMouse()
        self.message.undraw()
        self.intro.undraw()

        self.faceDrawer()
        # Se llama las reglas del juego
        self.gameRules()
        self.gameSession()
        self.endGame()
        #Aqui se hace la pantalla del juego
        
        self.win.getMouse()
        self.win.close()

def main():
    faceHitter = FaceHitter()
    
if __name__ == "__main__":
    main()
