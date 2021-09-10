import pygame
import sys
import time
import TronHighscore
from TronMainboard import *
import mysql.connector
global mydb
mydb = mysql.connector.connect(user='root', password='wildfactor', host='127.0.0.1',port=3306,database='tron',
auth_plugin='mysql_native_password')
global mycursor
mycursor = mydb.cursor()
pygame.init()

sql = ("SELECT width FROM main")
mycursor.execute(sql)

i = mycursor.fetchall()
i = ','.join(str(o) for o in i)
i = i.replace("(","")
i = i.replace(")","")
i = i.replace(",","")
i = i.replace("'","")
i = i.replace("[","")
i = i.replace("]","")

sql = ("SELECT height FROM main")
mycursor.execute(sql)

a = mycursor.fetchall()
a = ','.join(str(o) for o in a)
a = a.replace("(","")
a = a.replace(")","")
a = a.replace(",","")
a = a.replace("'","")
a = a.replace("[","")
a = a.replace("]","")

width = int(i)
height = int(a) 
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tron Legacy")
clock = pygame.time.Clock()

background = (27, 79, 114)
white = (236, 240, 241)
TronEnginePatternBlue = (125, 253, 254)
tronEngineBlue = (36, 25, 244)
TronEnginePatternRed = (241, 148, 138)
TronEngineRed = (255,0,0)
darkBlue = (40, 116, 166)

font = pygame.font.SysFont("Agency FB", 65)

w = 10


class tronBike:
    def __init__(self, name, color, darkColor, side):
        self.w = w
        self.h = w
        self.x = abs(side - 100)
        self.y = height/2 - self.h
        self.speed = 10
        self.color = color
        self.darkColor = darkColor
        self.history = [[self.x, self.y]]
        self.name = name
        self.length = 1
        
    
    def draw(self):
        
        for i in range(len(self.history)):
            if i == self.length - 1:
                pygame.draw.rect(display, self.darkColor, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:    
                pygame.draw.rect(display, self.color, (self.history[i][0], self.history[i][1], self.w, self.h))

    
    def move(self, xdir, ydir):
        
        self.x += xdir*self.speed
        self.y += ydir*self.speed
        self.history.append([self.x, self.y])
        self.length += 1
        if self.x < 0 or self.x > width or self.y < 0 or self.y > height:
            gameOver(self.name)

    
    def checkIfHit(self, opponent):
        
        if abs(opponent.history[opponent.length - 1][0] - self.history[self.length - 1][0]) < self.w and abs(opponent.history[opponent.length - 1][1] - self.history[self.length - 1][1]) < self.h:
            gameOver(0)
        for i in range(opponent.length):
            if abs(opponent.history[i][0] - self.history[self.length - 1][0]) < self.w and abs(opponent.history[i][1] - self.history[self.length - 1][1]) < self.h:
                gameOver(self.name)

        for i in range(len(self.history) - 1):
            if abs(self.history[i][0] - self.x) < self.w and abs(self.history[i][1] - self.y) < self.h and self.length > 2:
                gameOver(self.name)

def gameOver(name):
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    tron()
        sql = ("SELECT name1 FROM imena")
        mycursor.execute(sql)
        a = mycursor.fetchall()
        a = ','.join(str(o) for o in a)
        a = a.replace("(","")
        a = a.replace(")","")
        a = a.replace(",","")
        a = a.replace("'","")
        a = a.replace("[","")
        a = a.replace("]","")
        name1 = str(a)
        sql = ("SELECT name2 FROM imena")
        mycursor.execute(sql)
        a = mycursor.fetchall()
        a = ','.join(str(o) for o in a)
        a = a.replace("(","")
        a = a.replace(")","")
        a = a.replace(",","")
        a = a.replace("'","")
        a = a.replace("[","")
        a = a.replace("]","")
        name2 = str(a)
        if name == 0:
            text = font.render("Both the Players Collided!", True, white)
        elif name == 1:
            
                sql = ("SELECT points FROM highscore")
                mycursor.execute(sql)
                num= mycursor.fetchall()
                for i in num:
                        c = "".join(map(str,i))

                        a = int(c)
                tempPoints = int(a)
                points = 1
                points+= tempPoints
                sql = ("UPDATE highscore SET points = %s WHERE name = %s ")
                val = (points,name2)
                mycursor.execute(sql, val)
                mydb.commit()


                text = font.render(" %s Lost the Tron!"%(name1), True, white)
        elif name == 2:
                sql = ("SELECT points FROM highscore")
                mycursor.execute(sql)
                num= mycursor.fetchall()
                for i in num:
                    c = "".join(map(str,i))

                    a = int(c)
                tempPoints = a
                points = 1 
                points += tempPoints
                sql = ("UPDATE highscore SET points = %s WHERE name = %s ")
                val = (points,name1)
                mycursor.execute(sql, val)
                mydb.commit()
                text = font.render(" %s Lost the Tron!"%(name2), True, white)
                
        else:
            text = font.render("Error has occured",True,white)


        display.blit(text, (width/4, height/2))
        
        pygame.display.update()
        
        clock.tick(60)
        
        time.sleep(3)
        close()
def drawGrid():
    
    squares = 50
    for i in range(int(width/squares)):
        pygame.draw.line(display, darkBlue, (i*squares, 0), (i*squares, height))
        pygame.draw.line(display, darkBlue, (0, i*squares), (width, i*squares))

def close():
    pygame.quit()
    sys.exit()



def music():
    pygame.mixer.init()
    pygame.mixer.music.load(str("Derezzed.mp3"))
    pygame.mixer.music.play()
    

def tron():
    loop = True
    

    bike1 = tronBike(1, TronEnginePatternRed, TronEngineRed, 0)
    bike2 = tronBike(2, TronEnginePatternBlue, tronEngineBlue, width)

    x1 = 1
    y1 = 0
    x2 = -1
    y2 = 0
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_UP:
                    if not (x2 == 0 and y2 == 1):
                        x2 = 0
                        y2 = -1
                if event.key == pygame.K_DOWN:
                    if not (x2 == 0 and y2 == -1):
                        x2 = 0
                        y2 = 1
                if event.key == pygame.K_LEFT:
                    if not (x2 == 1 and y2 == 0):
                        x2 = -1
                        y2 = 0
                if event.key == pygame.K_RIGHT:
                    if not (x2 == -1 and y2 == 0):
                        x2 = 1
                        y2 = 0
                if event.key == pygame.K_w:
                    if not (x1 == 0 and y1 == 1):
                        x1 = 0
                        y1 = -1
                if event.key == pygame.K_s:
                    if not (x1 == 0 and y1 == -1):
                        x1 = 0
                        y1 = 1
                if event.key == pygame.K_a:
                    if not (x1 == 1 and y1 == 0):
                        x1 = -1
                        y1 = 0
                if event.key == pygame.K_d:
                    if not (x1 == -1 and y1 == 0):
                        x1 = 1
                        y1 = 0
                
                
            
        
        drawGrid()
        bike1.draw()
        bike2.draw()

        bike1.move(x1, y1)
        bike2.move(x2, y2)

        bike1.checkIfHit(bike2)
        bike2.checkIfHit(bike1)
        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    music()
    tron()