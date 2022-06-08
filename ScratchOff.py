# Import
import os
import sys
import random
import ctypes
import win32api
import win32con
import time
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="0"
import pygame

# Constant
IMAGEDIR = 'pictures'
SUPPORTEXTS = ['jpg', 'png', 'bmp']
SCREENSIZE = (800, 750)
WHITE = (255, 255, 255, 27)
GRAY = (192, 192, 192)
sys_lang = hex(ctypes.windll.kernel32.GetSystemDefaultUILanguage())
IsZh_Hans = (sys_lang == "0x804")
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
        if win32api.MessageBox(0, "无法读取图片数据。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。", "错误", win32con.MB_ICONWARNING | win32con.MB_YESNO)==6:
            os.system("start website/issues.url")
    else:
        if win32api.MessageBox(0, "Cannot read pictures file data.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.", "Error", win32con.MB_ICONWARNING)==6:
            os.system("start website/issues.url")

# Random
def readImageRandomly():
    filenames=os.listdir(IMAGEDIR)
    filenames=[f for f in filenames if f.split('.')[-1] in SUPPORTEXTS]
    imgpath=os.path.join(IMAGEDIR, random.choice(filenames))
    return pygame.transform.scale(pygame.image.load(imgpath), SCREENSIZE)

# Print log
def printLog(logType,logContent):
    if logContent!="DEBUG" or DEBUG==True:
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

# Init
pygame.init()
pygame.mixer.init()
pygame.mouse.set_cursor(*pygame.cursors.diamond)
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(Lang_Title)
surface = pygame.Surface(SCREENSIZE).convert_alpha()
surface.fill(GRAY)

# Read image
try:
    image_used = readImageRandomly()
except:
    noFileError()
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

# Main
printLog("INFO","Starting ScratchOff.")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            printLog("INFO","Exiting ScratchOff.")
            pygame.quit()
            sys.exit(-1)
    mouse_event_flags = pygame.mouse.get_pressed()
    if mouse_event_flags[0]:
        pygame.draw.circle(surface, WHITE, pygame.mouse.get_pos(), 40)
    elif mouse_event_flags[-1]:
        surface.fill(GRAY)
        image_used = readImageRandomly()
    screen.blit(image_used, (0, 0))
    screen.blit(surface, (0, 0))
    pygame.display.update()
