import pygame
import os

pygame.init()
pygame.mixer.init()

music_file = "song.mp3" 
if not os.path.exists(music_file):
    print("Music file not found!")
    exit()

