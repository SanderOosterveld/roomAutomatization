# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 17:05:03 2018

@author: Sander Oosterveld
"""
import pygame
from MainScreen import MainScreen
from queue import Queue

q = Queue()
screen = MainScreen(q)
musicFile = 'disturbed.ogg'
pygame.mixer.init()
pygame.mixer.music.load(musicFile)
pygame.mixer.music.play()
screen.start()
pygame.mixer.quit()