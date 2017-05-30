import random

class terreno(object):

    def __init__(self,p,suelo,agua):
        self.p = p
        self.suelo = suelo
        self.agua = agua


    def darProbabilidad(self):
        return self.p

    def crearSuelo(self):
        for i in range(len(self.suelo)):
            for j in range(len(self.suelo)):
                self.suelo[i][j] = random.randint(0, 9)
        return self.suelo

    def rociarAgua(self):
        for i in range(len(self.agua)):
            for j in range(len(self.agua)):
                numero = random.random()
                if numero < self.p:
                    self.agua[i][j] = random.randint(1, 8)
                else:
                    self.agua[i][j] = 0
        return self.agua

    def __str__(self):
        return "Probabilidad de que haya agua %s" % (self.p)
