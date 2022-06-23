# Import
import os,sys,random,ctypes,win32api,win32con,time,subprocess,datetime
from PIL import Image,UnidentifiedImageError
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="0"
import pygame

# Constant
IMAGEDIR="pictures"
SUPPORTEXTS=["jpeg","jpg","png","bmp"]
SCREENSIZE=(800,750)
WHITE=(255,255,255,27)
GRAY=(192,192,192)
sys_lang=hex(ctypes.windll.kernel32.GetSystemDefaultUILanguage())
IsZh_Hans=(sys_lang=="0x804")
DEBUG=False
ONEIMAGE=False
RESTART=True
BOMBTIME="1145141919810"

# Version
major=1
minor=1
releases=0
build=8
typenum=16
x=0

# Language
Lang_Title=""
if IsZh_Hans:
    Lang_Title="抽奖"
else:
    Lang_Title="Scratch Off"

# No pictures error
def noPicturesError():
    quit(1)
    printLog("ERROR","Cannot read pictures file data.")
    if IsZh_Hans:
        if win32api.MessageBox(0,"无法读取图片数据。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。","错误",win32con.MB_ICONWARNING | win32con.MB_YESNO)==6:
            subprocess.run("start website/issues.url",shell=True)
    else:
        if win32api.MessageBox(0,"Cannot read pictures file data.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.","Error",win32con.MB_ICONWARNING | win32con.MB_YESNO)==6:
            subprocess.run("start website/issues.url",shell=True)
    quit(2)

# No icon error
def noIconError():
    quit(1)
    printLog("ERROR","Cannot read icon.")
    if IsZh_Hans:
        if win32api.MessageBox(0,"无法读取图标。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。","错误",win32con.MB_ICONWARNING | win32con.MB_YESNO)==6:
            subprocess.run("start website/issues.url",shell=True)
    else:
        if win32api.MessageBox(0,"Cannot read icon.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.","Error",win32con.MB_ICONWARNING | win32con.MB_YESNO)==6:
            subprocess.run("start website/issues.url",shell=True)
    quit(2)

# No font error
def noFontError():
    quit(1)
    printLog("ERROR","Cannot read font data.")
    if IsZh_Hans:
        if win32api.MessageBox(0,"无法读取字体数据。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。","错误",win32con.MB_ICONWARNING | win32con.MB_YESNO)==6:
            subprocess.run("start website/issues.url",shell=True)
    else:
        if win32api.MessageBox(0,"Cannot read font data.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.","Error",win32con.MB_ICONWARNING | win32con.MB_YESNO)==6:
            subprocess.run("start website/issues.url",shell=True)
    quit(2)

# Cannot write log error
def cannotWriteLogError():
    quit(1)
    if IsZh_Hans:
        if win32api.MessageBox(0,"无法写入日志。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。","错误",win32con.MB_ICONERROR | win32con.MB_YESNO)==6:
            subprocess.run("start website/issues.url",shell=True)
    else:
        if win32api.MessageBox(0,"Cannot write log file.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.","Error",win32con.MB_ICONERROR | win32con.MB_YESNO)==6:
            subprocess.run("start website/issues.url",shell=True)
    quit(3)

# Resize
def resize(size):
    while True:
        if size[0]<800 and size[1]<800:
            size=(size[0]*1.5,size[1]*1.5)
        else:
            break
    while True:
        if size[0]>800 and size[1]>800:
            size=(size[0]*0.5,size[1]*0.5)
        else:
            break
    return size

# Random
def readImageRandomly():
    global SCREENSIZE,ONEIMAGE
    filenames=os.listdir(IMAGEDIR)
    filenames=[f for f in filenames if f.split(".")[-1] in SUPPORTEXTS]
    if len(filenames)==1:
        ONEIMAGE=True
    imgpath=os.path.join(IMAGEDIR,random.choice(filenames))
    img=Image.open(imgpath)
    SCREENSIZE=img.size
    SCREENSIZE=resize(SCREENSIZE)
    return [pygame.transform.scale(pygame.image.load(imgpath),SCREENSIZE),imgpath[9:],img.size]

# Print log
def printLog(logType,logContent):
    if logType!="DEBUG" or DEBUG:
        try:
            with open("log/latest.log","a") as file:
                file.write(time.strftime("[%Y.%m.%d %H:%M:%S] [")+str(logType)+"]: "+str(logContent)+"\n")
                print(" ["+logType+"]: "+logContent)
        except FileNotFoundError:
            cannotWriteLogError()

# Get log time
def getTime(log):
    try:
        with open(log,"r") as file:
            firstLine=file.readline()
            time=""
            for i in firstLine:
                if i=="]":
                    break
                try:
                    time+=str(int(i))
                except ValueError:
                    continue
            return time
    except FileNotFoundError:
        return 1145141919810

# Watermark
def watermark():
    font20=pygame.font.Font("font.ttc",20)
    font15=pygame.font.Font("font.ttc",15)
    font10=pygame.font.Font("font.ttc",10)
    if typenum<=4:
        text1=font20.render("Class Tools 机密",True,(0,0,0))
        text2=font15.render("以任何方式进行未经授权的使用或披露",True,(0,0,0))
        text3=font15.render("可能会招致惩戒处分，最严重的处罚可",True,(0,0,0))
        text4=font15.render("要求承担可能的民事与刑事责任。",True,(0,0,0))
        text5=font15.render("仅用于测试。版本号："+str(major)+"."+str(minor)+"."+str(releases)+"."+str(build)+"."+str(typenum)+"."+str(x),True,(0,0,0))
        screen.blit(text1,(43,0))
        screen.blit(text2,(0,30))
        screen.blit(text3,(0,45))
        screen.blit(text4,(0,60))
        screen.blit(text5,(0,90))
    elif typenum<=8:
        text=font15.render("仅用于测试。版本号："+str(major)+"."+str(minor)+"."+str(releases)+"."+str(build)+"."+str(typenum)+"."+str(x),True,(0,0,0))
        screen.blit(text,(0,0))
    else:
        text=font10.render("版本号："+str(major)+"."+str(minor)+"."+str(releases)+"."+str(build)+"."+str(typenum)+"."+str(x),True,(0,0,0))
        screen.blit(text,(0,0))

# Init
def init():
    global screen
    pygame.init()
    pygame.mixer.init()
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    screen=pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption(Lang_Title)
    try:
        icon=pygame.image.load("SO.png")
        pygame.display.set_icon(icon)
    except FileNotFoundError:
        noIconError()

# Quit
def quit(quittype):
    if quittype==1:
        pygame.quit()
    elif quittype==2:
        printLog("INFO","Exiting ScratchOff.")
        sys.exit(0)
    elif quittype==3:
        sys.exit(0)

# Create log
subprocess.run("md log > temp.txt 2> temp2.txt",shell=True)
subprocess.run("del temp.txt",shell=True)
subprocess.run("del temp2.txt",shell=True)
lastTime=getTime("log/latest.log")
if lastTime!=1145141919810:
    subprocess.run("cd log && ren latest.log "+lastTime+".log",shell=True)
file=open("log/latest.log","w")
file.close()
printLog("INFO","Starting ScratchOff.")

# Timebomb
if typenum<=12:
    if BOMBTIME!="1145141919810":
        now=datetime.datetime.now()
        bomb=datetime.datetime.strptime(BOMBTIME,"%Y.%m.%d %H:%M:%S")
        if now>bomb:
            printLog("INFO","You use the program after the timeless.")
            quit(2)

# Warn
if typenum<=4:
    if win32api.MessageBox(0,"此版本为内部版本，版本号："+str(major)+"."+str(minor)+"."+str(releases)+"."+str(build)+"."+str(typenum)+"."+str(x)+"。\n以任何方式进行未经授权的使用或披露可能会招致惩戒处分，最严重的处罚可要求承担可能的民事与刑事责任。\n若以认真阅读这段文字，请点击否确认。","警告",win32con.MB_ICONWARNING | win32con.MB_YESNO)==6:
        printLog("INFO","You click yes.")
        quit(2)
elif typenum<=8:
    if win32api.MessageBox(0,"此版本为测试版本，仅用于测试，版本号："+str(major)+"."+str(minor)+"."+str(releases)+"."+str(build)+"."+str(typenum)+"."+str(x)+"。\n若以认真阅读这段文字，请点击否确认。","警告",win32con.MB_ICONWARNING | win32con.MB_YESNO)==6:
        printLog("INFO","You click yes.")
        quit(2)


# Read image
while True:
    try:
        image=readImageRandomly()
    except FileNotFoundError:
        noPicturesError()
    except UnidentifiedImageError as errorMsg:
        subprocess.run("del \"pictures\\"+str(errorMsg)[38:-1]+"\"",shell=True)
        printLog("WARNING","You have a unsupported picture, its name is: \""+str(errorMsg)[38:-1]+"\". We delete the picture.")
        continue
    else:
        break
printLog("INFO","Use image "+image[1]+", image size: "+str(image[2]))
printLog("INFO","Set screen size to "+str(SCREENSIZE))

# Init
init()
surface=pygame.Surface(SCREENSIZE).convert_alpha()
surface.fill(GRAY)

# Main
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit(1)
            quit(2)
    mouse_event_flags=pygame.mouse.get_pressed()
    if mouse_event_flags[0]:
        RESTART=False
        pygame.draw.circle(surface,WHITE,pygame.mouse.get_pos(),40)
        printLog("DEBUG","Left button pressed, position: "+str(pygame.mouse.get_pos())+".")
    elif mouse_event_flags[-1]:
        if not RESTART:
            printLog("INFO","Right button pressed, game restart.")
            old=image
            while True:
                try:
                    image=readImageRandomly()
                except FileNotFoundError:
                    noPicturesError()
                except UnidentifiedImageError as errorMsg:
                    subprocess.run("del \"pictures\\"+str(errorMsg)[38:-1]+"\"",shell=True)
                    printLog("WARNING","You have a unsupported picture, its name is: \""+str(errorMsg)[38:-1]+"\". We delete the picture.")
                    continue
                if image[1]!=old[1]:
                    break
                if ONEIMAGE:
                    printLog("WARNING","You only have one image.")
                    break
            printLog("INFO","Use image "+image[1]+", image size: "+str(image[2]))
            printLog("INFO","Set screen size to "+str(SCREENSIZE))
            quit(1)
            init()
            surface=pygame.Surface(SCREENSIZE).convert_alpha()
            surface.fill(GRAY)
            RESTART=True
    screen.blit(image[0],(0,0))
    screen.blit(surface,(0,0))
    try:
        watermark()
    except:
        noFontError()
    pygame.display.update()