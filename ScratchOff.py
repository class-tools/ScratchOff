# Import
from _tkinter import TclError
from PIL import Image, UnidentifiedImageError
import tkinter.messagebox
import tkinter
import datetime
import subprocess
import time
import ctypes
import random
import sys
import pygame
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "0"

# Constant
IMAGEDIR = "pictures"
SUPPORTEXTS = ["jpeg", "jpg", "png", "bmp"]
SCREENSIZE = (800, 750)
WHITE = (255, 255, 255, 27)
GRAY = (192, 192, 192)
sys_lang = hex(ctypes.windll.kernel32.GetSystemDefaultUILanguage())
IsZh_Hans = (sys_lang == "0x804")
DEBUG = False
BOMBTIME = "2022.8.1 00:00:00"

# Version
major = 1
minor = 2
releases = 0
build = 12
typenum = 6
x = 1

# Language
if IsZh_Hans:
    Lang_Title = "刮刮乐"
    Lang_Quit = "退出"
    Lang_About = "关于"
    Lang_About_Message = "本程序受 MIT 许可证保护\nCopyright © 2022 Class Tools Develop Team. All rights reserved.\nGithub 存储库：https://github.com/class-tools/ScratchOff\n"
    Lang_About_Confidential = "Class Tools 机密\n以任何方式进行未经授权的使用或披露可能会招致惩戒处分，\n最严重的处罚可要求承担可能的民事与刑事责任。\n"
    Lang_About_Test = "仅用于测试。版本号："
    Lang_About_Releases = "版本号："
else:
    Lang_Title = "Scratch Off"
    Lang_Quit = "Quit"
    Lang_About = "About"
    Lang_About_Message = "This program uses MIT License\nCopyright © 2022 Class Tools Develop Team. All rights reserved.\nGithub Repository: https://github.com/class-tools/ScratchOff\n"
    Lang_About_Confidential = "Class Tools Confidential\nUnauthorized use or disclosure in any way may result in disciplinary action, \nand the most serious punishment may require possible civil and criminal liability.\n"
    Lang_About_Test = "Only for test. Version: "
    Lang_About_Releases = "Version: "


def noPicturesError():
    """No pictures error"""
    quit(1)
    root.wm_attributes('-topmost', 1)
    printLog("ERROR", "Cannot read pictures file data.")
    if IsZh_Hans:
        if tkinter.messagebox._show(
            "错误",
            "无法读取图片数据。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。",
            tkinter.messagebox.ERROR,
                tkinter.messagebox.YESNO) == "yes":
            subprocess.run("start website/issues.url", shell=True)
    else:
        if tkinter.messagebox._show(
            "Error",
            "Cannot read pictures file data.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.",
            tkinter.messagebox.ERROR,
                tkinter.messagebox.YESNO) == "yes":
            subprocess.run("start website/issues.url", shell=True)
    quit(3)


def noIconError():
    """No icon error"""
    quit(1)
    root.wm_attributes('-topmost', 1)
    printLog("ERROR", "Cannot read icon.")
    if IsZh_Hans:
        if tkinter.messagebox._show(
            "错误",
            "无法读取图标。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。",
            tkinter.messagebox.ERROR,
                tkinter.messagebox.YESNO) == "yes":
            subprocess.run("start website/issues.url", shell=True)
    else:
        if tkinter.messagebox._show(
            "Error",
            "Cannot read icon.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.",
            tkinter.messagebox.ERROR,
                tkinter.messagebox.YESNO) == "yes":
            subprocess.run("start website/issues.url", shell=True)
    quit(3)


def noFontError():
    """No font error"""
    quit(1)
    root.wm_attributes('-topmost', 1)
    printLog("ERROR", "Cannot read font data.")
    if IsZh_Hans:
        if tkinter.messagebox._show(
            "错误",
            "无法读取字体数据。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。",
            tkinter.messagebox.ERROR,
                tkinter.messagebox.YESNO) == "yes":
            subprocess.run("start website/issues.url", shell=True)
    else:
        if tkinter.messagebox._show(
            "Error",
            "Cannot read font data.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.",
            tkinter.messagebox.ERROR,
                tkinter.messagebox.YESNO) == "yes":
            subprocess.run("start website/issues.url", shell=True)
    quit(3)


def cannotWriteLogError():
    """Cannot write log error"""
    quit(1)
    root.wm_attributes('-topmost', 1)
    if IsZh_Hans:
        if tkinter.messagebox._show(
            "错误",
            "无法写入日志。\n如果你认为这是程序的问题，你可以点击“是”跳转到 Issues 界面反馈。",
            tkinter.messagebox.ERROR,
                tkinter.messagebox.YESNO) == "yes":
            subprocess.run("start website/issues.url", shell=True)
    else:
        if tkinter.messagebox._show(
            "Error",
            "Cannot write log file.\nIf you think it is a bug, you can click \"yes\" to skip to the issues page.",
            tkinter.messagebox.ERROR,
                tkinter.messagebox.YESNO) == "yes":
            subprocess.run("start website/issues.url", shell=True)
    quit(4)


def resize(size):
    while True:
        if size[0] < 800 and size[1] < 800:
            size = (size[0] * 1.5, size[1] * 1.5)
        else:
            break
    while True:
        if size[0] > 800 and size[1] > 800:
            size = (size[0] * 0.5, size[1] * 0.5)
        else:
            break
    size = (int(size[0]), int(size[1]))
    return size


def readImageRandomly():
    """Random a image."""
    global SCREENSIZE, ONEIMAGE
    filenames = os.listdir(IMAGEDIR)
    filenames = [f for f in filenames if f.split(".")[-1] in SUPPORTEXTS]
    if len(filenames) == 1:
        ONEIMAGE = True
    else:
        ONEIMAGE = False
    imgpath = os.path.join(IMAGEDIR, random.choice(filenames))
    img = Image.open(imgpath)
    SCREENSIZE = img.size
    SCREENSIZE = resize(SCREENSIZE)
    return [pygame.transform.scale(pygame.image.load(
        imgpath), SCREENSIZE), imgpath[9:], img.size]


def printLog(logType, logContent):
    """Print log"""
    if logType != "DEBUG" or DEBUG:
        try:
            with open("log/latest.log", "a") as file:
                file.write(
                    time.strftime("[%Y.%m.%d %H:%M:%S] [") +
                    str(logType) +
                    "]: " +
                    str(logContent) +
                    "\n")
                print(" [" + logType + "]: " + logContent)
        except FileNotFoundError:
            cannotWriteLogError()


def getTime(log):
    """Get log time"""
    try:
        with open(log, "r") as file:
            firstLine = file.readline()
            time = ""
            for i in firstLine:
                if i == "]":
                    break
                try:
                    time += str(int(i))
                except ValueError:
                    continue
            return time
    except FileNotFoundError:
        return 1145141919810


def watermark():
    font20 = pygame.font.Font("font.ttc", 20)
    font15 = pygame.font.Font("font.ttc", 15)
    if typenum <= 4:
        text1 = font20.render("Class Tools 机密", True, (0, 0, 0))
        text2 = font15.render("以任何方式进行未经授权的使用或披露", True, (0, 0, 0))
        text3 = font15.render("可能会招致惩戒处分，最严重的处罚可", True, (0, 0, 0))
        text4 = font15.render("要求承担可能的民事与刑事责任。", True, (0, 0, 0))
        text5 = font15.render(
            "仅用于测试。版本号：" +
            str(major) +
            "." +
            str(minor) +
            "." +
            str(releases) +
            "." +
            str(build) +
            "." +
            str(typenum) +
            "." +
            str(x),
            True,
            (0,
             0,
             0))
        screen.blit(text1, (43, 0))
        screen.blit(text2, (0, 30))
        screen.blit(text3, (0, 45))
        screen.blit(text4, (0, 60))
        screen.blit(text5, (0, 90))
    elif typenum <= 8:
        text = font15.render(
            "仅用于测试。版本号：" +
            str(major) +
            "." +
            str(minor) +
            "." +
            str(releases) +
            "." +
            str(build) +
            "." +
            str(typenum) +
            "." +
            str(x),
            True,
            (0,
             0,
             0))
        screen.blit(text, (0, 0))


def Menu_About():
    """About in menu bar"""
    printLog("INFO", "Use menu command \"About\".")
    about = tkinter.Toplevel()
    try:
        about.iconbitmap("SO.ico")
    except TclError:
        noIconError()
    about.title(Lang_About)
    about.resizable(width=False, height=False)
    about.wm_attributes('-topmost', 1)
    image = tkinter.PhotoImage(file="about.png")
    icon = tkinter.Label(about, image=image)
    icon.image = image
    icon.pack()
    if typenum <= 4:
        message = tkinter.Label(
            about, text=Lang_About_Message)
        messageConfidential = tkinter.Label(
            about, text=Lang_About_Confidential, fg="red")
        messageVersion = tkinter.Label(about,
                                       text=Lang_About_Test +
                                       str(major) +
                                       "." +
                                       str(minor) +
                                       "." +
                                       str(releases) +
                                       "." +
                                       str(build) +
                                       "." +
                                       str(typenum) +
                                       "." +
                                       str(x))
        message.pack()
        messageConfidential.pack()
        messageVersion.pack()
    elif typenum <= 8:
        message = tkinter.Label(about,
                                text=Lang_About_Message)
        messageVersion = tkinter.Label(about,
                                       text=Lang_About_Test +
                                       str(major) +
                                       "." +
                                       str(minor) +
                                       "." +
                                       str(releases) +
                                       "." +
                                       str(build) +
                                       "." +
                                       str(typenum) +
                                       "." +
                                       str(x))
        message.pack()
        messageVersion.pack()
    else:
        message = tkinter.Label(about,
                                text=Lang_About_Message)
        messageVersion = tkinter.Label(about,
                                       text=Lang_About_Releases +
                                       str(major) +
                                       "." +
                                       str(minor) +
                                       "." +
                                       str(releases) +
                                       "." +
                                       str(build) +
                                       "." +
                                       str(typenum) +
                                       "." +
                                       str(x))
        message.pack()
        messageVersion.pack()


def Menu_Quit():
    """Quit in menu bar"""
    printLog("INFO", "Use menu command \"Quit\".")
    quit(2)


def init(inittype):
    if inittype == 1:
        global root, embed
        root = tkinter.Tk()
        title = ""
        if typenum == 1:
            title += "[内部预览版] "
        elif typenum == 2:
            title += "[内部调试版] "
        elif typenum == 4:
            title += "[内部测试版] "
        elif typenum == 6:
            title += "[公共预览版] "
        elif typenum == 8:
            title += "[公共测试版] "
        elif typenum == 10:
            title += "[预先发布版] "
        if DEBUG:
            title += "[开发人员模式] "
        root.title(title + Lang_Title)
        root.geometry(str(SCREENSIZE[0]) +
                      "x" +
                      str(SCREENSIZE[1]) +
                      "+" +
                      str(int(root.winfo_screenwidth() /
                              2 -
                              SCREENSIZE[0] /
                              2)) +
                      "+" +
                      str(int(root.winfo_screenheight() /
                              2 -
                              SCREENSIZE[1] /
                              2)))
        root.resizable(width=False, height=False)
        try:
            root.iconbitmap("SO.ico")
        except TclError:
            noIconError()
        menubar = tkinter.Menu(root)
        root["menu"] = menubar
        menubar.add_command(label=Lang_About, command=Menu_About)
        menubar.add_command(label=Lang_Quit, command=Menu_Quit)
        embed = tkinter.Frame(root, width=SCREENSIZE[0], height=SCREENSIZE[1])
        embed.grid(columnspan=(600), rowspan=500)
        embed.pack(side=tkinter.LEFT)
        os.environ["SDL_WINDOWID"] = str(embed.winfo_id())
        os.environ["SDL_VIDEODRIVER"] = "windib"
    elif inittype == 2:
        global screen
        pygame.init()
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
        screen = pygame.display.set_mode(SCREENSIZE)


def quit(quittype):
    """Quit the program."""
    if quittype == 1:
        pygame.quit()
    elif quittype == 2:
        root.destroy()
    elif quittype == 3:
        printLog("INFO", "Exiting ScratchOff.")
        sys.exit(0)
    elif quittype == 4:
        sys.exit(0)


# Create log
subprocess.run("md log > temp.txt 2> temp2.txt", shell=True)
subprocess.run("del temp.txt", shell=True)
subprocess.run("del temp2.txt", shell=True)
lastTime = getTime("log/latest.log")
if lastTime != 1145141919810:
    subprocess.run("cd log && ren latest.log " + lastTime + ".log", shell=True)
file = open("log/latest.log", "w")
file.close()
printLog("INFO", "Starting ScratchOff.")

# Timebomb
if typenum <= 12:
    if BOMBTIME != "1145141919810":
        now = datetime.datetime.now()
        bomb = datetime.datetime.strptime(BOMBTIME, "%Y.%m.%d %H:%M:%S")
        if now > bomb:
            printLog("INFO", "You use the program after the timeless.")
            quit(3)


# Read image
while True:
    try:
        image = readImageRandomly()
    except FileNotFoundError:
        init(1)
        noPicturesError()
    except IndexError:
        init(1)
        noPicturesError()
    except UnidentifiedImageError as errorMsg:
        subprocess.run(
            "del \"pictures\\" +
            str(errorMsg)[
                38:-
                1] +
            "\"",
            shell=True)
        printLog(
            "WARNING",
            "You have a unsupported picture, its name is: \"" +
            str(errorMsg)[
                38:-
                1] +
            "\". We delete the picture.")
        continue
    else:
        break
printLog("INFO", "Use image " + image[1] + ", image size: " + str(image[2]))
printLog("INFO", "Set screen size to " + str(SCREENSIZE))

# Init window
init(1)

# Warn
if typenum <= 4:
    root.wm_attributes('-topmost', 1)
    if tkinter.messagebox._show(
        "警告",
        "此版本为内部版本，版本号：" +
        str(major) +
        "." +
        str(minor) +
        "." +
        str(releases) +
        "." +
        str(build) +
        "." +
        str(typenum) +
        "." +
        str(x) +
        "。\n以任何方式进行未经授权的使用或披露可能会招致惩戒处分，最严重的处罚可要求承担可能的民事与刑事责任。\n若以认真阅读这段文字，请点击否确认。",
        tkinter.messagebox.WARNING,
            tkinter.messagebox.YESNO) == "yes":
        printLog("INFO", "You click yes.")
        quit(1)
        quit(3)
elif typenum <= 8:
    root.wm_attributes('-topmost', 1)
    if tkinter.messagebox._show(
        "警告",
        "此版本为测试版本，仅用于测试，版本号：" +
        str(major) +
        "." +
        str(minor) +
        "." +
        str(releases) +
        "." +
        str(build) +
        "." +
        str(typenum) +
        "." +
        str(x) +
        "。\n若以认真阅读这段文字，请点击否确认。",
        tkinter.messagebox.WARNING,
            tkinter.messagebox.YESNO) == "yes":
        printLog("INFO", "You click yes.")
        quit(1)
        quit(3)
root.wm_attributes('-topmost', 0)

# Init game
init(2)
surface = pygame.Surface(SCREENSIZE).convert_alpha()
surface.fill(GRAY)

# Main
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(1)
            quit(3)
    mouse_event_flags = pygame.mouse.get_pressed()
    if mouse_event_flags[0]:
        pygame.draw.circle(surface, WHITE, pygame.mouse.get_pos(), 40)
        printLog("DEBUG", "Left button pressed, position: " +
                 str(pygame.mouse.get_pos()) + ".")
    elif mouse_event_flags[-1]:
        printLog("INFO", "Right button pressed, game restart.")
        old = image
        while True:
            try:
                image = readImageRandomly()
            except FileNotFoundError:
                noPicturesError()
            except UnidentifiedImageError as errorMsg:
                subprocess.run(
                    "del \"pictures\\" +
                    str(errorMsg)[
                        38:-
                        1] +
                    "\"",
                    shell=True)
                printLog(
                    "WARNING",
                    "You have a unsupported picture, its name is: \"" +
                    str(errorMsg)[
                        38:-
                        1] +
                    "\". We delete the picture.")
                continue
            if image[1] != old[1]:
                break
            if ONEIMAGE:
                printLog("WARNING", "You only have one image.")
                break
        printLog("INFO", "Use image " +
                 image[1] + ", image size: " + str(image[2]))
        printLog("INFO", "Set screen size to " + str(SCREENSIZE))
        quit(1)
        quit(2)
        init(1)
        init(2)
        surface = pygame.Surface(SCREENSIZE).convert_alpha()
        surface.fill(GRAY)
    screen.blit(image[0], (0, 0))
    screen.blit(surface, (0, 0))
    try:
        watermark()
    except FileNotFoundError:
        noFontError()
    pygame.display.update()
    try:
        root.update()
    except TclError:
        quit(1)
        quit(3)
