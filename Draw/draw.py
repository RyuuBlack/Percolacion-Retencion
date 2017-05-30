import pygame,sys
from pygame.locals import *
from PIL import Image
import imageio
import os

class draw(object):


    def __init__(self,tamano,tamanoPantalla,suelo,agua):
        self.tamano = tamano
        self.tamanoPantalla = tamanoPantalla
        self.suelo = suelo
        self.agua = agua
        self.sizeScale = 0
        self.terreno = [[0] * self.tamano for i in range(self.tamano)]

    def config(self):
        self.sizeScale = self.tamanoPantalla/self.tamano

        # escalar imagenes de suelo

        imagen = Image.open("Docs/suelo.png")
        scalar = (self.sizeScale,self.sizeScale)
        imagen.thumbnail(scalar)
        imagen.save("data/suelo0.png")

        for i in range(9):
            imagen = Image.open("Docs/suelo"+str(i+1)+".png")
            scalar = (self.sizeScale,self.sizeScale)
            imagen.thumbnail(scalar)
            imagen.save("data/suelo"+str(i+1)+".png")

        # escalar imagen de agua
        imagen = Image.open("Docs/agua.png")
        scalar = (self.sizeScale,self.sizeScale)
        imagen.thumbnail(scalar)
        imagen.save("data/agua.png")

    def simulacionAgua(self):

        pygame.init()
        ventana = pygame.display.set_mode((self.tamanoPantalla,self.tamanoPantalla))
        pygame.display.set_caption("Simulación")

        sueloImage = []


        sueloImage.append(pygame.image.load("data/suelo0.png"))

        for i in range(9):
            sueloImage.append(pygame.image.load("data/suelo"+str(i+1)+".png"))


        imageAgua = pygame.image.load("data/agua.png")

        banderaSimulacion = 0
        finalizar = False
        iteracionFinal = False
        cambio = 0
        contador=1
        x = 0
        y = 0


        while True:


            if contador == 0:
                finalizar = True
            else:
                contador=0
                cambio = 0

            for i in range(self.tamano):
                for j in range(self.tamano):
                    if self.agua[i][j] > 0:
                        self.terreno[i][j] = -1
                    else:
                        self.terreno[i][j] = self.suelo[i][j]



            if finalizar == False:

                if self.agua[y][x]>0:
                    # x, y-1
                    if y != 0 :
                        if self.suelo[y-1][x] < self.suelo[y][x]:
                            self.agua[y-1][x] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                        if self.suelo[y][x] < self.suelo[y-1][x] and self.agua[y][x]>self.suelo[y-1][x]:
                            self.agua[y-1][x] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                    # x+1,y-1
                    if y != 0 and x != self.tamano-1:
                        if self.suelo[y-1][x+1] < self.suelo[y][x]:
                            self.agua[y-1][x+1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                        if self.suelo[y][x] < self.suelo[y-1][x+1] and self.agua[y][x]>self.suelo[y-1][x+1]:
                            self.agua[y-1][x+1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                    # x+1,y
                    if x != self.tamano-1 :
                        if self.suelo[y][x+1] < self.suelo[y][x]:
                            self.agua[y][x+1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                        if self.suelo[y][x] < self.suelo[y][x+1] and self.agua[y][x]>self.suelo[y][x+1]:
                            self.agua[y][x+1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                    # x+1,y+1
                    if y != self.tamano-1 and x != self.tamano-1:
                        if self.suelo[y+1][x+1] < self.suelo[y][x]:
                            self.agua[y+1][x+1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                        if self.suelo[y][x] < self.suelo[y+1][x+1] and self.agua[y][x]>self.suelo[y+1][x+1]:
                            self.agua[y+1][x+1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                    # x,y+1
                    if y != self.tamano-1:
                        if self.suelo[y+1][x] < self.suelo[y][x]:
                            self.agua[y+1][x] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                        if self.suelo[y][x] < self.suelo[y+1][x] and self.agua[y][x]>self.suelo[y+1][x]:
                            self.agua[y+1][x] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                    # x-1,y+1
                    if x != 0 and y != self.tamano-1:
                        if self.suelo[y+1][x-1] < self.suelo[y][x]:
                            self.agua[y+1][x-1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                        if self.suelo[y][x] < self.suelo[y+1][x-1] and self.agua[y][x]>self.suelo[y+1][x-1]:
                            self.agua[y+1][x-1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                    # x-1,y
                    if x != 0:
                        if self.suelo[y][x-1] < self.suelo[y][x]:
                            self.agua[y][x-1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                        if self.suelo[y][x] < self.suelo[y][x-1] and self.agua[y][x]>self.suelo[y][x-1]:
                            self.agua[y][x-1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                    # x-1,y-1
                    if x != 0 and y!=0:
                        if self.suelo[y-1][x-1] < self.suelo[y][x]:
                            self.agua[y-1][x-1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1

                        if self.suelo[y][x] < self.suelo[y-1][x-1] and self.agua[y][x]>self.suelo[y-1][x-1]:
                            self.agua[y-1][x-1] += 1
                            self.agua[y][x] -= 1
                            cambio+=1
                            contador+=1



            x=x+1

            if x == self.tamano:
                y=y+1
                x=0

            if y == self.tamano:
                y=0


            for i in range(self.tamano):
                for j in range(self.tamano):
                    posX = j*self.sizeScale
                    posY = i*self.sizeScale

                    if self.terreno[i][j] == 0:
                        ventana.blit(sueloImage[0],(posX,posY))
                    elif self.terreno[i][j] == 1:
                        ventana.blit(sueloImage[1],(posX,posY))
                    elif self.terreno[i][j] == 2:
                        ventana.blit(sueloImage[2],(posX,posY))
                    elif self.terreno[i][j] == 3:
                        ventana.blit(sueloImage[3],(posX,posY))
                    elif self.terreno[i][j] == 4:
                        ventana.blit(sueloImage[4],(posX,posY))
                    elif self.terreno[i][j] == 5:
                        ventana.blit(sueloImage[5],(posX,posY))
                    elif self.terreno[i][j] == 6:
                        ventana.blit(sueloImage[6],(posX,posY))
                    elif self.terreno[i][j] == 7:
                        ventana.blit(sueloImage[7],(posX,posY))
                    elif self.terreno[i][j] == 8:
                        ventana.blit(sueloImage[8],(posX,posY))
                    elif self.terreno[i][j] == 9:
                        ventana.blit(sueloImage[9],(posX,posY))
                    else:
                        ventana.blit(imageAgua,(posX,posY))


            for i in range(self.tamano):
                for j in range(self.tamano):
                    if self.agua[i][j]>0:
                        self.agua[i][j]-=0.33
                        contador+=1

            for i in range(self.tamano):
                for j in range(self.tamano):
                    if self.agua[i][j] <= 0.33:
                        self.agua[i][j]=0;


            pygame.image.save(ventana,"Simulacion/terreno tiempo "+str(banderaSimulacion)+".png")
            banderaSimulacion = banderaSimulacion + 1


            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if finalizar == True:
                if iteracionFinal == True:
                    cambio=1
                    swang=True
                    images = []
                    bandera = 0
                    while swang:
                        try:
                            im = "Simulacion/terreno tiempo "+str(bandera)+".png"
                            images.append(imageio.imread(im))
                            bandera+=1
                        except:
                            swang=False

                    imageio.mimsave('Gif/Simulacion.gif', images)
                    pygame.quit()
                    sys.exit()
                iteracionFinal = True

            pygame.time.delay(500)
            pygame.display.update()
