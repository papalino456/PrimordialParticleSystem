import pygame
import numpy as np
import random
import math

width, height = 900, 500
winSize = (width, height)
array = []

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode(winSize)
pygame.display.set_caption("The game of life")

clock = pygame.time.Clock()

class Cell():
    def __init__(self, x, y, a, b, v, r, color,phi):
        self.x = x
        self.y = y
        self.a = a #alpha angle
        self.b = b #beta angle
        self.v = v #velocity
        self.r = r #sensor radius
        self.color = color
        self.phi = phi
        self.R = 0
        self.L = 0
        self.N = 0
    def draw(self):
        circle = pygame.draw.circle(screen,(self.color),(self.x,self.y),10)
    def updateCol(self, N):
        if (N > 15 and N <= 35):
            self.color = (0,0,255)
        if (N > 35):
            self.color = (255,255,0)
        if (N >= 13 and N <= 15):
            self.color = (140,70,20)
        if (N > 15):
            self.color = (255,0,255)
        else:
            self.color = (0,255,50)

def spawn():
    for i in range(200):
        cell = Cell(random.randrange(10,890),random.randrange(10,490),180,17,2,60,(0,255,50),0)
        cell.draw()
        array.append(cell)

def calculat_new_xy(x,y,speed,angle_in_radians):
    new_x = x + (speed*math.cos(angle_in_radians))
    new_y = y + (speed*math.sin(angle_in_radians))
    return new_x, new_y

def isInside(circle_x, circle_y, rad, x, y):
    #Compare radius of circle with distance 
    #of its center from given point
    if ((x - circle_x) * (x - circle_x) + (y - circle_y) * (y - circle_y) <= rad * rad):
        return True
    else:
        return False

        
def main():
    running = True
    spawn()
    while running:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                running = False
        screen.fill((0,0,0))
        for cell in array:
            cell.N = 0
            cell.R = 0
            cell.L = 0
            for Ecell in array:
                if Ecell != cell:
                    if isInside(cell.x,cell.y,cell.r,Ecell.x,Ecell.y):
                        if(math.tan(cell.phi)*Ecell.x + Ecell.y < 0):    #no funciona
                            cell.L = cell.L + 1
                        if(math.tan(cell.phi)*Ecell.x + Ecell.y > 0):    #no funciona
                            cell.R = cell.R + 1   
            cell.N = cell.L + cell.R
            cell.phi = cell.phi + cell.a + cell.b * cell.N * np.sign(cell.R-cell.L)
            cell.x, cell.y = calculat_new_xy(cell.x,cell.y,cell.v, math.radians(cell.phi))
            cell.updateCol(cell.N)
            cell.draw()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()



if __name__ == "__main__":
    main()