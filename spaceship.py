import time
from threading import Thread

class spaceship:

    speed=1 #in m/s
    direction=[0,0]
    coords = [0,0]


    def __init__(self, name="testName", coords=[0,0]):
        self.name = name   
        self.coords = coords
        self.inFlight = False


    def getName(self):
        return self.name


    def getPosition(self):
        return self.coords


    def setSpeed(self,speed):
        self.speed = speed


    def getSpeed(self):
        return self.speed


    def flyForX(self,direction,duration):
        self.direction = direction
        for i in range(duration):
            self.coords[0] += self.direction[0]*self.speed
            self.coords[1] += self.direction[1]*self.speed


    def start(self,x,y):
        self.inFlight = True
        self.direction = [x,y]
        while (self.inFlight):
            self.coords[0] += self.direction[0]
            self.coords[1] += self.direction[1]
            time.sleep(1.0)
    
    def stop(self):
        self.inFlight=False
