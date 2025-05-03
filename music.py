import pygame
import os

pygame.init()
pygame.mixer.init()

music_file = "song.mp3" 
if not os.path.exists(music_file):
    print("Music file not found!")
    exit()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

print("Playing music... Press Enter to stop.")
input() 

pygame.mixer.music.stop()

