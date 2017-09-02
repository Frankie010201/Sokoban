#coding=utf-8

'''
PushBoxes pygame
Version: 2.0
加入图片
Author: Frank
Created: 09/01/2017
'''
import pygame
import sys
import logging
from pygame.locals import *
import time

keyBuff = None  # 上一次按键记录
logger =0 #for logging

#图形尺寸
blockwidth = 50
blockheight = 50
Unitwidth = 10
Unitheight = 7
size = width, height = blockwidth * Unitwidth , blockheight * Unitheight

#图形颜色（1.5 version 用彩色小块代替不同）
'''
bg = (255,255,255)
wallcolor = (25,25,25)
wallcolorlight = (100,100,100)
workercolor = (0,255,0)
workercolorlight = (0,100,0)
boxescolor = (0,0,255)
boxescolorlight = (0,0,200)
blankspacecolor = (255,255,255)
blankspacecolorlight = (200,200,200)
targetpositioncolor = (0,200,200)
targetpositioncolorlight = (0,100,100)
screen = 0
'''
'''
workerimage = None
wallimage = None
targetimage = None
blankspaceimage = None
boximage = None
'''

# list0-6 and Boxlayout for layout (x 为 纵坐标，y 为横坐标)
list0 = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
list1 = ['#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#']
list2 = ['#', '#', 'O', '#', '#', '#', ' ', ' ', ' ', '#']
list3 = ['#', ' ', 'S', ' ', 'O', ' ', ' ', 'O', ' ', '#']
list4 = ['#', ' ', '*', '*', '#', ' ', 'O', ' ', '#', '#']
list5 = ['#', '#', '*', '*', '#', ' ', ' ', ' ', '#', '#']
list6 = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
Boxlayout = [list0, list1, list2, list3, list4, list5, list6]

    #   'S'表示工作的小人
    #   '#'表示墙体
listx = [2, 3, 3, 4]  # listx, listy 为箱子'O'的坐标，共四个箱子
listy = [2, 4, 7, 6]

listxa = [4, 4, 5, 5]  # listxa,listys 为最终箱子的位置'*'的坐标，共四个
listya = [2, 3, 2, 3]

Boxesleftout = 4  # 未推到最终位置的箱子个数

x = 3  # (3,2)为工作小人最初位置
y = 2

Order = 0


def load_images():
    global workerimage,wallimage,targetimage, blankspaceimage, boximage, congratulation,Exit
    workerimage=pygame.image.load('workerimage.png').convert()
    wallimage = pygame.image.load('wallimage.png').convert()
    targetimage = pygame.image.load('targetimage.png').convert()
    blankspaceimage = pygame.image.load('blankspaceimage.png').convert()
    boximage = pygame.image.load('boximage.png').convert()
    congratulation = pygame.image.load('congratulation.jpg').convert()
    Exit = pygame.image.load('exit.png').convert()

def printTxt(content, x, y, font, screen, color=(255, 255, 255)):
    '''显示文本
    args:
        content:待显示文本内容
        x,y:显示坐标
        font:字体
        screen:输出的screen
        color:颜色
    '''
    imgTxt = font.render(content, True, color)
    screen.blit(imgTxt, (x, y))

def draw_wall():

    for i in range (Unitheight):
        for j in range (Unitwidth):
            if Boxlayout [i][j] == '#':
                #pygame.draw.rect(screen, wallcolor, ((j*blockwidth), (i*blockheight), blockwidth, blockheight),0)
                #pygame.draw.rect(screen, wallcolorlight, ((j*blockwidth)+1, (i*blockheight)+1, blockwidth-2, blockheight-2),0)
                screen.blit(wallimage,((j*blockwidth), (i*blockheight)))

def draw_boxes():
    for i in range (4):
        #pygame.draw.rect(screen, boxescolor, ((listy[i]*blockwidth), (listx[i]*blockheight), blockwidth, blockheight),0)
        #pygame.draw.rect(screen, boxescolorlight, ((listy[i]*blockwidth)+1, (listx[i]*blockheight)+1, blockwidth-2, blockheight-2),0)
        screen.blit(boximage, ((listy[i]*blockwidth), (listx[i]*blockheight)))

def draw_target():
    global targetimage
    for i in range (4):
        #pygame.draw.rect(screen, targetpositioncolor, ((listya[i]*blockwidth), (listxa[i]*blockheight), blockwidth, blockheight),0)
        #pygame.draw.rect(screen, targetpositioncolorlight, ((listya[i] * blockwidth)+1, (listxa[i] * blockheight)+1, blockwidth-2, blockheight-2), 0)
        screen.blit(targetimage, ((listya[i]*blockwidth), (listxa[i]*blockheight)))

def draw_worker():
    #pygame.draw.rect(screen, workercolor,((y * blockwidth), (x * blockheight), blockwidth, blockheight), 0)
    #pygame.draw.rect(screen, workercolorlight, ((y * blockwidth)+1, (x * blockheight)+1, blockwidth-2, blockheight-2), 0)
    global workerimage
    screen.blit(workerimage, ((y * blockwidth), (x * blockheight)))

def draw_blankspace():
    global blankspaceimage
    for i in range (Unitheight):
        for j in range (Unitwidth):
            if Boxlayout [i][j] == ' ':
                #pygame.draw.rect(screen, blankspacecolor, ((j*blockwidth), (i*blockheight), blockwidth, blockheight),0)
                #pygame.draw.rect(screen, blankspacecolorlight, ((j * blockwidth)+1, (i * blockheight)+1, blockwidth-2, blockheight-2), 0)
                screen.blit(blankspaceimage, ((j * blockwidth), (i * blockheight)))

def movedown():
    global x, y

    if Boxlayout[x + 1][y] != '#' and Boxlayout[x + 1][y] != 'O':  # 判断前方格是否是墙体或箱子，如否，则小人前进一格
        Boxlayout[x][y] = ' '
        x = x + 1
        Boxlayout[x][y] = 'S'
    elif Boxlayout[x + 1][y] == 'O' and Boxlayout[x + 2][y] != '#' and Boxlayout[x + 2][y] != 'O':  # 判断前方格是否为箱子，且前方第二格不是墙体或另一箱子。如否，则小人前进一格
        Boxlayout[x][y] = ' '
        x = x + 1
        Boxlayout[x][y] = 'S'
        for i in range(4):
            if listx[i] == x and listy[i] == y:  # 判断前方箱子为哪一个箱子
                Boxlayout[x + 1][y] = 'O'  # 箱子前进一格，并相应修改listx表示的箱子位置
                listx[i] = listx[i] + 1

def moveup():
    global x, y

    if Boxlayout[x - 1][y] != '#' and Boxlayout[x - 1][y] != 'O':
        Boxlayout[x][y] = ' '
        x = x - 1
        Boxlayout[x][y] = 'S'
    elif Boxlayout[x - 1][y] == 'O' and Boxlayout[x - 2][y] != '#' and Boxlayout[x - 2][y] != 'O':
        Boxlayout[x][y] = ' '
        x = x - 1
        Boxlayout[x][y] = 'S'
        for i in range(4):
            if listx[i] == x and listy[i] == y:
                Boxlayout[x - 1][y] = 'O'
                listx[i] = listx[i] - 1


def moveleft():
    global x, y

    if Boxlayout[x][y - 1] != '#' and Boxlayout[x][y - 1] != 'O':
        Boxlayout[x][y] = ' '
        y = y - 1
        Boxlayout[x][y] = 'S'
    elif Boxlayout[x][y - 1] == 'O' and Boxlayout[x][y - 2] != '#' and Boxlayout[x][y - 2] != 'O':
        Boxlayout[x][y] = ' '
        y = y - 1
        Boxlayout[x][y] = 'S'
        for i in range(4):
            if listx[i] == x and listy[i] == y:
                Boxlayout[x][y - 1] = 'O'
                listy[i] = listy[i] - 1

def moveright():
    global x, y

    if Boxlayout[x][y + 1] != '#' and Boxlayout[x][y + 1] != 'O':
        Boxlayout[x][y] = ' '
        y = y + 1
        Boxlayout[x][y] = 'S'
    elif Boxlayout[x][y + 1] == 'O' and Boxlayout[x][y + 2] != '#' and Boxlayout[x][y + 2] != 'O':
        Boxlayout[x][y] = ' '
        y = y + 1
        Boxlayout[x][y] = 'S'
        for i in range(4):
            if listx[i] == x and listy[i] == y:
                Boxlayout[x][y + 1] = 'O'
                listy[i] = listy[i] + 1



def main():

    global blockwidth, blockheight,Unitwidth, Unitheight, size, bg, wallcolor ,workercolor ,boxescolor,blankspacecolor,targetpositioncolor,screen
    global Boxlayout, listx ,listy, listxa ,listya,Boxesleftout , x, y
    global Order, keyBuff, wallimage, workerimage, blankspaceimage, targetimage, workerimage

    # 第一步，创建一个logger
    global logger

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关

    # 第二步，创建一个handler，用于写入日志文件
    # logfile = './log/logger.txt'
    # fh = logging.FileHandler(logfile, mode='w')
    # fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

    # 第三步，再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

    # 第四步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    # fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 第五步，将logger添加到handler里面
    # logger.addHandler(fh)
    logger.addHandler(ch)

    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('PushBoxes')

    load_images()


    clock = pygame.time.Clock()

    draw_wall()
    Exitcode = 0


    while Boxesleftout != 0 :

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w or event.key == K_UP:
                    if keyBuff != K_UP:
                        keyBuff = K_UP
                        moveup()
                        msg = "event type : %s   key:  %s  x: %s  y: %s" % ( str(event.type), str(event.key), str(x), str(y))
                        logger.warning(msg)
                elif event.key == K_s or event.key == K_DOWN:
                    if keyBuff != K_DOWN:
                        keyBuff = K_DOWN
                        movedown()
                elif event.key == K_a or event.key == K_LEFT:
                    if keyBuff != K_LEFT:
                        keyBuff = K_LEFT
                        moveleft()
                elif event.key == K_d or event.key == K_RIGHT:
                    if keyBuff != K_RIGHT:
                        keyBuff = K_RIGHT
                        moveright()
                elif event.key == K_x or event.key == K_ESCAPE:
                    Exitcode = 1
                    break
            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_DOWN or event.key == K_UP:
                    keyBuff = None
        if Exitcode == 1:
            break

                #elif event.type == KEYUP:
                    #Order = 'z'
        # 用w 上，s 下， a 左，d 右
        # 表示工作小人的移动方向
        # 用x 退出游戏
        # 每次输入后需要按回车确认


        # 避免因小人和箱子的移动而覆盖箱子最终位置'*'的显示
        for i in range(4):
            if Boxlayout[listxa[i]][listya[i]] != 'O' and Boxlayout[listxa[i]][listya[i]] != 'S':
                Boxlayout[listxa[i]][listya[i]] = '*'

        # 判断箱子是否已经全部被推到最终位置
        Boxesleftout = 4
        for i in range(4):
            for j in range(4):
                if listx[i] == listxa[j] and listy[i] == listya[j]:
                    Boxesleftout = Boxesleftout - 1

        draw_blankspace()
        draw_target()
        draw_boxes()
        draw_worker()

        pygame.display.update()
        clock.tick(30)
        # 清屏
        #print('\n' * 30)
    # 判断是成功或是中途退出
    #defaultFont = pygame.font.Font("yh.ttf", 16)  # yh.ttf这个字体文件请自行上网搜索下载，如果找不到就随便用个ttf格式字体文件替换一下。
    backSurface = pygame.Surface((screen.get_rect().width, screen.get_rect().height))
    if Boxesleftout == 0:
        #printTxt("Congratulation", 320, 40, defaultFont, backSurface, (255,255,255))
        screen.blit(congratulation,(((screen.get_rect().width - congratulation.get_rect().width)/2,(screen.get_rect().height - congratulation.get_rect().height)/2)))
    else:
        #printTxt("Exit" , 320, 40, defaultFont, backSurface, (255,255,255))
        screen.blit(Exit, ((screen.get_rect().width - Exit.get_rect().width)/2,(screen.get_rect().height - Exit.get_rect().height)/2))
    pygame.display.update()
    pygame.time.delay(3000)

main()