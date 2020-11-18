import pygame
import random
import time

class Params:
    rules={}
    size = 10
    screen = pygame.display.set_mode((2500, 1000))
    id = 0
    network = []
    numCon = 3
    nSize = 1000/size
    curXPoint = 0

    @staticmethod
    def GetRect():
        for n in Params.network:
            if n.Value == 1:
                pygame.draw.rect(Params.screen, (0, 255, 0), n.Rect)
            else:
                pygame.draw.rect(Params.screen, (0, 0, 255), n.Rect)

    @staticmethod
    def CreateRules(numCon):
        d = dict()
        for i in range(pow(2,numCon)):
            tmp = str(bin(i)).replace("0b","")
            d[tmp] = random.randint(0,1)
            while len(tmp)!=numCon:
                tmp = "0"+tmp
                d[tmp] = random.randint(0, 1)


        Params.rules = d
        Params.numCon = numCon

    @staticmethod
    def Tick():
        print("TICK")
        for n in Params.network:
            result = ""
            for con in n.Connections:
                conVal = Params.GetNodeValueOfId(con)
                if conVal is not None:
                    result += str(conVal)
            n.Value = Params.rules[result]
            n.Rect.x+=Params.size
        Params.curXPoint += Params.size

    @staticmethod
    def GetNodeValueOfId(id):
        for n in Params.network:
            if n.ID == id:
                return n.Value
        return None


class Node:
    def __init__(self, posX, posY):
        self.Rect = pygame.Rect(posX, posY, Params.size, Params.size)
        self.ID = Params.id
        Params.id += 1
        self.Connections = []
        c = random.randint(1, Params.numCon)
        for i in range(c):
            r = random.randint(0, Params.nSize-1)
            if r != self.ID:
                self.Connections.append(r)
            else:
                self.Connections.append(0)
        self.Value = random.randint(0, 1)

Params.CreateRules(6)
for i in range(int(1000 / Params.size)):
    Params.network.append(Node(0, i * Params.size))

print("Created network with __{}__ number of nodes".format(Params.network.__len__()))
screenActive = True
nextTick = 0

while screenActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screenActive = False
        if event.type == pygame.MOUSEBUTTONDOWN or nextTick<time.time():
            nextTick = time.time()+0.1
            Params.Tick()
    Params.GetRect()
    pygame.display.flip()
