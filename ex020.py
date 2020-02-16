import time
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex020.mp3')
pygame.mixer.music.play(0, 0.0)
time.sleep(5)
pygame.mixer.music.stop()