from microbit import *
from random import choice

grid=[[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
bricks = [[9,9],[9,0]],[[9,9],[0,9]],[[9,9],[9,9]],[[9,9],[0,0]]
brick = choice(bricks)
x=3
y=0
frameCount=0


def max(a,b):
    if a>=b:
        return a
    else:
        return b


def hideBrick():
    if x>0:
        display.set_pixel(x-1,y,grid[y][x])
    if x<5:
        display.set_pixel(x+1-1,y,grid[y][x+1])
    if x>0 and y<4:
        display.set_pixel(x-1,y+1,grid[y+1][x])
    if x<5 and y<4:
        display.set_pixel(x+1-1,y+1,grid[y+1][x+1])


def showBrick():
    if x>0:
        display.set_pixel(x-1,y,max(brick[0][0],grid[y][x]))
    if x<5:
        display.set_pixel(x+1-1,y,max(brick[0][1],grid[y][x+1]))
    if x>0 and y<4:
        display.set_pixel(x-1,y+1,max(brick[1][0],grid[y+1][x]))
    if x<5 and y<4:
        display.set_pixel(x+1-1,y+1,max(brick[1][1],grid[y+1][x+1]))


def rotateBrick():
    pixel00 = brick[0][0]
    pixel01 = brick[0][1]
    pixel10 = brick[1][0]
    pixel11 = brick[1][1]

    if not ((grid[y][x]>0 and pixel00>0) or (grid[y+1][x]>0 and pixel10>0) or (grid[y][x+1]>0 and pixel01>0) or (grid[y+1][x+1]>0 and pixel11>0)):
        hideBrick()
        brick[0][0] = pixel10
        brick[1][0] = pixel11
        brick[1][1] = pixel01
        brick[0][1] = pixel00
        showBrick()


def moveBrick(delta_x,delta_y):
    global x,y
    move=False

    if delta_x==-1 and x>0:
        if not ((grid[y][x-1]>0 and brick[0][0]>0) or (grid[y][x+1-1]>0 and brick[0][1]>0) or (grid[y+1][x-1]>0 and brick[1][0]>0) or (grid[y+1][x+1-1]>0 and brick[1][1]>0)):
            move=True
    elif delta_x==1 and x<5:
        if not ((grid[y][x+1]>0 and brick[0][0]>0) or (grid[y][x+1+1]>0 and brick[0][1]>0) or (grid[y+1][x+1]>0 and brick[1][0]>0) or (grid[y+1][x+1+1]>0 and brick[1][1]>0)):
            move=True
    elif delta_y==1 and y<4:
        if not ((grid[y+1][x]>0 and brick[0][0]>0) or (grid[y+1][x+1]>0 and brick[0][1]>0) or (grid[y+1+1][x]>0 and brick[1][0]>0) or (grid[y+1+1][x+1]>0 and brick[1][1]>0)):
            move=True

    if move:
        hideBrick()
        x+=delta_x
        y+=delta_y
        showBrick()

    return move


def checkLines():
    global score
    removeLine=False

    for i in range(0, 5):

        if (grid[i][1]+grid[i][2]+grid[i][3]+grid[i][4]+grid[i][5])==45:
            removeLine = True
            score+=10
            for j in range(i,0,-1):
                grid[j] = grid[j-1]
            grid[0]=[1,0,0,0,0,0,1]
    if removeLine:
        for i in range(0, 5):
            for j in range(0, 5):
                display.set_pixel(i,j,grid[j][i+1])
    return removeLine

gameOn=True
score=0
showBrick()

while gameOn:
    sleep(50)
    frameCount+=1

    if button_a.is_pressed() and button_b.is_pressed():
        rotateBrick()
    elif button_a.is_pressed():
        moveBrick(-1,0)
    elif button_b.is_pressed():
        moveBrick(1,0)


    if frameCount==15 and moveBrick(0,1) == False:
        frameCount=0

        grid[y][x]=max(brick[0][0],grid[y][x])
        grid[y][x+1]=max(brick[0][1],grid[y][x+1])
        grid[y+1][x]=max(brick[1][0],grid[y+1][x])
        grid[y+1][x+1]=max(brick[1][1],grid[y+1][x+1])

        if checkLines()==False and y==0:
            gameOn=False
        else:
            x=3
            y=0
            brick = choice(bricks)
            showBrick()

    if frameCount==15:
        frameCount=0


sleep(2000)
display.scroll("Game Over: Score: " + str(score))