import pygame
import random
import time

# You need the zil.ttf for the game

pygame.init()

height = 600
width = 700
cellSize = 100

rows = 3
cols = 3

screen = pygame.display.set_mode((height, width))

pygame.display.set_caption("???")

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 100, 0)

grid = pygame.Surface(((height), width))
grid.fill(white)

gridState = [[white for _ in range(rows)] for _ in range(cols)]

gridMatriz = [[0,0,0],[0,0,0],[0,0,0]]

gridLevel = [[False,False,False],[False, False, False],[False, False, False]]

resList = [[0,0,0],[0,0,0]]

def paintNumber(x, y, number):
    global gridMatriz
    gridMatriz[x][y] = number
    text = str(number)
    font = pygame.font.Font("zil.ttf", 50)
    textSurface = font.render(text, True, (15, 25, 150))
    textRect = textSurface.get_rect()
    textRect.center = ((cellSize // 2)+cellSize*y, (cellSize // 2)+cellSize*x)
    grid.blit(textSurface, textRect)

def paintRes(x, y, number):
    text = str(number)
    font = pygame.font.Font("zil.ttf", 50)
    textSurface = font.render(text, True, (0, 0, 0))
    textRect = textSurface.get_rect()
    textRect.center = ((cellSize // 2)+cellSize*y, (cellSize // 2)+cellSize*x)
    grid.blit(textSurface, textRect)

def paintWin():
    text = str("You Won!")
    font = pygame.font.Font("zil.ttf", 60)
    textSurface = font.render(text, True, (255, 0, 0))
    textRect = textSurface.get_rect()
    textRect.center = ((height//2)-100, (width//2)+100)
    grid.blit(textSurface, textRect)


def generateLevel():
    global gridMatriz, resList, gridLevel
    tempList = [[0,0,0],[0,0,0],[0,0,0]]

    conditon = False

    for i in range(3):
        for j in range(3):
            tempList[i][j] = random.randint(1,9)


    resList[0][0] = calculateSum(tempList, 0,0,0)
    resList[0][1] = calculateSum(tempList, 1,0,0)
    resList[0][2] = calculateSum(tempList, 2,0,0)

    resList[1][0] = calculateSum(tempList, 0,0,1)
    resList[1][1] = calculateSum(tempList, 0,1,1)
    resList[1][2] = calculateSum(tempList, 0,2,1)


    for i in range(3):
        conditon = False
        while(conditon == False):
            indexOne = random.randint(0,2)
            indexTwo = random.randint(0,2)

            if gridMatriz[indexOne][indexTwo] == 0:
                conditon = True

        gridLevel[indexOne][indexTwo] = True
        gridMatriz[indexOne][indexTwo] = tempList[indexOne][indexTwo]




def calculateSum(matriz, x, y, flag):

    totalSum = 0

    if flag == 0:
        for i in range(3):
            totalSum+= matriz[x][y+i]

    if flag == 1:
        for i in range(3):
            totalSum+= matriz[x+i][y]

    return totalSum





def incrementOrDecrement(mouseX, mouseY, operator):
    global gridMatriz
    if mouseX >= (height//4) + cellSize*1 and mouseX <= (height//4) + cellSize *2 and mouseY <= cellSize*3:
        if mouseY <= cellSize:
            if gridMatriz[0][1] == 0 and operator == -1 or gridMatriz[0][1] == 9 and operator == 1:
                return
            
            if flag(0,1):
                gridMatriz[0][1] +=operator

        elif mouseY >= cellSize*1 and mouseY <= cellSize*2:
            if gridMatriz[1][1] == 0 and operator == -1 or gridMatriz[1][1] == 9 and operator == 1:
                return
            
            if flag(1,1):
                gridMatriz[1][1] +=operator

        elif mouseY >= cellSize*2 and mouseY <= cellSize*3:
            if gridMatriz[2][1] == 0 and operator == -1 or gridMatriz[2][1] == 9 and operator == 1:
                return
            
            if flag(2,1):
                gridMatriz[2][1] +=operator
    
    elif mouseX >= (height//4) and mouseX <= (height//4) + cellSize *2 and mouseY <= cellSize*3:
        if (gridMatriz[0][0] == 0 and gridMatriz[1][0] == 0 and gridMatriz[2][0] == 0)and operator == -1:
            return
        if mouseY <= cellSize:
            if gridMatriz[0][0] == 0 and operator == -1 or gridMatriz[0][0] == 9 and operator == 1:
                return
            
            if flag(0,0):
                gridMatriz[0][0] +=operator
            
        elif mouseY >= cellSize*1 and mouseY <= cellSize*2:
            if gridMatriz[1][0] == 0 and operator == -1 or gridMatriz[1][0] == 9 and operator == 1:
                return
            
            if flag(1,0):
                gridMatriz[1][0] +=operator

        elif mouseY >= cellSize*2 and mouseY <= cellSize*3:
            if gridMatriz[2][0] == 0 and operator == -1 or gridMatriz[2][0] == 9 and operator == 1:
                return
            
            if flag(2,0):
                gridMatriz[2][0] +=operator
    
    elif mouseX >= (height//4) + cellSize*2 and mouseX <= (height//4) + cellSize *3 and mouseY <= cellSize*3:
        if (gridMatriz[0][2] == 0 and gridMatriz[1][2] == 0 and gridMatriz[2][2] == 0)and operator == -1:
            return
        if mouseY <= cellSize:
            if gridMatriz[0][2] == 0 and operator == -1 or gridMatriz[0][2] == 9 and operator == 1:
                return
            if flag(0,2):
                gridMatriz[0][2] +=operator

        elif mouseY >= cellSize*1 and mouseY <= cellSize*2:
            if gridMatriz[1][2] == 0 and operator == -1 or gridMatriz[1][2] == 9 and operator == 1:
                return
            
            if flag(1,2):
                gridMatriz[1][2] +=operator

        elif mouseY >= cellSize*2 and mouseY <= cellSize*3:
            if gridMatriz[2][2] == 0 and operator == -1 or gridMatriz[2][2] == 9 and operator == 1:
                return
            
            if flag(2,2):
                gridMatriz[2][2] +=operator

def flag(x, y):
    global gridLevel

    if gridLevel[x][y] == True:
        return False
    return True

def calculateWin():
    global resList
    contador=0
    tempMatriz = [[0,0,0],[0,0,0]]

    tempMatriz[0][0] = calculateSum(gridMatriz, 0,0,0)
    tempMatriz[0][1] = calculateSum(gridMatriz, 1,0,0)
    tempMatriz[0][2] = calculateSum(gridMatriz, 2,0,0)

    tempMatriz[1][0] = calculateSum(gridMatriz, 0,0,1)
    tempMatriz[1][1] = calculateSum(gridMatriz, 0,1,1)
    tempMatriz[1][2] = calculateSum(gridMatriz, 0,2,1)

    for i in range(2):
        for j in range(3):
            if tempMatriz[i][j] == resList[i][j]:
                contador+=1
    

    if contador >= 6:
        return True
    else:
        return False




running = True
generateLevel()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            
            mouseX = pos[0]
            mouseY = pos[1]


            if event.button == 1:
                incrementOrDecrement(mouseX,mouseY,+1)
            if event.button == 3:
                incrementOrDecrement(mouseX,mouseY,-1)




    paintNumber(0, 0, gridMatriz[0][0])
    paintNumber(0, 1, gridMatriz[0][1])
    paintNumber(0, 2, gridMatriz[0][2])

    paintNumber(1, 0, gridMatriz[1][0])
    paintNumber(1, 1, gridMatriz[1][1])
    paintNumber(1, 2, gridMatriz[1][2])

    paintNumber(2, 0, gridMatriz[2][0])
    paintNumber(2, 1, gridMatriz[2][1])
    paintNumber(2, 2, gridMatriz[2][2])

    paintRes(0, 3, resList[0][0])
    paintRes(1, 3, resList[0][1])
    paintRes(2, 3, resList[0][2])

    paintRes(3, 0, resList[1][0])
    paintRes(3, 1, resList[1][1])
    paintRes(3, 2, resList[1][2])


    screen.fill(white)
    screen.blit(grid, (height//4, 0))

    for fila in range(rows):
        for columna in range(cols):
            cellX = columna * cellSize
            cellY = fila * cellSize
            pygame.draw.rect(grid, gridState[columna][fila], (cellX, cellY, cellSize, cellSize), 0)
            pygame.draw.rect(grid, black, (cellX, cellY, cellSize, cellSize), 1)


    pygame.display.flip()

    if calculateWin():
        screen.fill(white)
        paintWin()
        


    

pygame.quit()


