import pygame
import tkinter as tkr
import os
from tkinter.filedialog import askdirectory

# box configuration
music_player = tkr.Tk()
music_player.title("Sangeet App")
music_player.geometry("450x350")
directory = askdirectory() # ask for directory
os.chdir(directory)  # change directory of computer 
song_list = os.listdir() 

# add song in list
play_list = tkr.Listbox(music_player,font="Arial 12 bold",bg="yellow",selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos,item)
    pos += 1
pygame.init()
pygame.mixer.init()

# function for player
def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()
    
def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()
    
Button1 = tkr.Button(music_player,width=5,height=3,font="Helvetica 12 bold",text="PLAY",command=play,bg="blue",fg="white")    
Button2 = tkr.Button(music_player,width=5,height=3,font="Helvetica 12 bold",text="PLAY",command=stop,bg="red",fg="white")    
Button3 = tkr.Button(music_player,width=5,height=3,font="Helvetica 12 bold",text="PLAY",command=pause,bg="purple",fg="white")    
Button4 = tkr.Button(music_player,width=5,height=3,font="Helvetica 12 bold",text="PLAY",command=unpause,bg="orange",fg="white")    
    
var = tkr.StringVar()
song_title = tkr.Label(music_player,font="Helvetica 12 bold",textvariable=var)
song_title.pack()

# To show Button in box
Button1.pack(fill="X")
Button2.pack(fill="X")
Button3.pack(fill="X")
Button4.pack(fill="X")

play_list.pack(fill="both",expand="yes")

# main program
music_player.mainloop()