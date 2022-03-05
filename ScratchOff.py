import os
import sys
import random
import ctypes
import win32api
import win32con

# Import pygame
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "0"
import pygame

# Constant
IMAGEDIR = 'pictures'
SUPPORTEXTS = ['jpg', 'png', 'bmp']
SCREENSIZE = (800, 600)
WHITE = (255, 255, 255, 27)
GRAY = (192, 192, 192)
sys_lang = hex(ctypes.windll.kernel32.GetSystemDefaultUILanguage())
IsZh_Hans = (sys_lang == "0x804")

# Language
Lang_Title = ""
if IsZh_Hans:
    Lang_Title = "抽奖"
else:
    Lang_Title = "Scratch Off"

# Error
def errno_1():
    print("ERROR: [Errno 1] Cannot read pictures file data.")
    win32api.MessageBox(0, "[Errno 1] Cannot read pictures file data.", "Error", win32con.MB_ICONWARNING)

# Random
def readImageRandomly():
    filenames = os.listdir(IMAGEDIR)
    filenames = [f for f in filenames if f.split('.')[-1] in SUPPORTEXTS]
    imgpath = os.path.join(IMAGEDIR, random.choice(filenames))
    return pygame.transform.scale(pygame.image.load(imgpath), SCREENSIZE)

# Main
pygame.init()
pygame.mixer.init()
pygame.mouse.set_cursor(*pygame.cursors.diamond)
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(Lang_Title)
surface = pygame.Surface(SCREENSIZE).convert_alpha()
surface.fill(GRAY)
try:
    image_used = readImageRandomly()
except FileNotFoundError:
    errno_1()
    pygame.quit()
    sys.exit(1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
