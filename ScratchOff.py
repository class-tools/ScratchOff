# Import
import os
import sys
import random
import ctypes
import win32api
import win32con
import time
from PIL import Image
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="0"
import pygame

# Constant
IMAGEDIR="pictures"
SUPPORTEXTS=["jpg","png","bmp"]
SCREENSIZE=(800,750)
WHITE=(255,255,255,27)
GRAY=(192,192,192)
sys_lang=hex(ctypes.windll.kernel32.GetSystemDefaultUILanguage())
IsZh_Hans=(sys_lang=="0x804")
DEBUG=False

# Language
Lang_Title=""
if IsZh_Hans:
    Lang_Title="抽奖"
else:
    Lang_Title="Scratch Off"

# No file error
def noFileError():
    printLog("ERROR","Cannot read pictures file data.")
    if IsZh_Hans:
        if win32api.MessageBox(0,"无法读取图片数据。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。","错误",win32con.MB_ICONWARNING | win32con.MB_YESNO)==6:
            os.system("start website/issues.url > temp.txt 2> temp2.txt")
            file=open("temp2.txt","r")
            if file.read()!="":
                printLog("ERROR","Cannot found the issues page in website folder.")
            file.close()
            os.system("del temp.txt")
            os.system("del temp2.txt")
    else:
        if win32api.MessageBox(0,"Cannot read pictures file data.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.","Error",win32con.MB_ICONWARNING)==6:
            os.system("start website/issues.url > temp.txt 2> temp2.txt")
            file=open("temp2.txt","r")
            if file.read()!="":
                printLog("ERROR","Cannot found the issues page in website folder.")
            file.close()
            os.system("del temp.txt")
            os.system("del temp2.txt")
    quit()

# Random
def readImageRandomly():
    global SCREENSIZE
    filenames=os.listdir(IMAGEDIR)
    filenames=[f for f in filenames if f.split(".")[-1] in SUPPORTEXTS]
    imgpath=os.path.join(IMAGEDIR, random.choice(filenames))
    img=Image.open(imgpath)
    SCREENSIZE=img.size
    if SCREENSIZE[0]<800 and SCREENSIZE[1]<750:
        SCREENSIZE=(SCREENSIZE[0]*1.5,SCREENSIZE[1]*1.5)
    return [pygame.transform.scale(pygame.image.load(imgpath),SCREENSIZE),imgpath[9:],img.size]

# Print log
def printLog(logType,logContent):
    if logType!="DEBUG" or DEBUG:
        file=open("log/latest.log","a")
        file.write(time.strftime("[%Y.%m.%d %H:%M:%S] [")+logType+"]: "+logContent+"\n")
        print(" ["+logType+"]: "+logContent)
        file.close()

# Get log time
def getTime(log):
    try:
        file=open(log,"r")
        firstLine=file.readline()
        time=""
        for i in firstLine:
            if i=="]":
                break
            try:
                time+=str(int(i))
            except:
                continue
        file.close()
        return time
    except:
        return 1145141919810

# Quit
def quit():
    printLog("INFO","Exiting ScratchOff.")
    pygame.quit()
    sys.exit(1)

# Create log
os.system("md log > temp.txt 2> temp2.txt")
os.system("del temp.txt")
os.system("del temp2.txt")
lastTime=getTime("log/latest.log")
if lastTime!=1145141919810:
    os.system("cd log && ren latest.log "+lastTime+".log")
file=open("log/latest.log","w")
file.close()
printLog("INFO","Starting ScratchOff.")

# Read image
try:
    image=readImageRandomly()
except:
    noFileError()
else:
    printLog("INFO","Use image "+image[1]+", image size: "+str(image[2]))
    printLog("INFO","Set screen size to "+str(SCREENSIZE))

# Init
pygame.init()
pygame.mixer.init()
pygame.mouse.set_cursor(*pygame.cursors.diamond)
screen=pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(Lang_Title)
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
surface=pygame.Surface(SCREENSIZE).convert_alpha()
surface.fill(GRAY)

# Main
RESTART=False
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
    mouse_event_flags=pygame.mouse.get_pressed()
    if mouse_event_flags[0]:
        if RESTART:
            printLog("INFO","Right button pressed, game restart.")
            printLog("INFO","Use image "+image[1]+", image size: "+str(image[2]))
            printLog("INFO","Set screen size to "+str(SCREENSIZE))
            screen=pygame.display.set_mode(SCREENSIZE)
            surface=pygame.Surface(SCREENSIZE).convert_alpha()
            surface.fill(GRAY)
            RESTART=False
        pygame.draw.circle(surface,WHITE,pygame.mouse.get_pos(),40)
        printLog("DEBUG","Left button pressed, position: "+str(pygame.mouse.get_pos())+".")
    elif mouse_event_flags[-1]:
        RESTART=True
        image=readImageRandomly()
        surface.fill(GRAY)
        printLog("DEBUG","Right button pressed, game restart.")
        printLog("DEBUG","Use image "+image[1])
    screen.blit(image[0],(0,0))
    screen.blit(surface,(0,0))
    pygame.display.update()