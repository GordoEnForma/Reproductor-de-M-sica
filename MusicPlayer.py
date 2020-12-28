#Importing neccesary Modules
import pygame
import tkinter as tkr

from tkinter.filedialog import askdirectory
import os

#Create app window

musicplayer= tkr.Tk()

#Setting the title name
musicplayer.title("Music Player") 

#Setting the dimensions
musicplayer.geometry("450x350")

#Asking for music Directory
directory = askdirectory()

#Setting music directory to the current working directory
os.chdir(directory)

#Creating our songlist
#os.listdir() returns a list containing the names of the entries in the directory given by the path
songlist = os.listdir()

#Creating the playlist
playlist = tkr.Listbox(musicplayer, font ="Cambria 14 bold", bg = "cyan2", selectmode= tkr.SINGLE)

#Adding songs from the songlist to the playlist
for item in songlist:
    pos = 0
    playlist.insert(pos,item)
    pos+=1
#initializing modules

pygame.mixer.init()

#function for play button
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

#function for stop button
def ExitMusicPlayer():
    pygame.mixer.music.stop()
#function for pause button
def pause():
    pygame.mixer.music.pause()
#function for resume button
def resume():
    pygame.mixer.music.unpause()


#Creating buttons
Button_play = tkr.Button(musicplayer,height =3 , width =5,text = "Play Music",font ="Cambria 14 bold", command = play ,bg ="lime green", fg = "Black")
Button_stop = tkr.Button(musicplayer,height =3 , width =5,text = "Stop Music",font ="Cambria 14 bold", command = ExitMusicPlayer ,bg ="red", fg = "Black")
Button_pause = tkr.Button(musicplayer,height =3 , width =5,text = "Pause Music",font ="Cambria 14 bold", command = pause ,bg ="yellow", fg = "Black")
Button_resume = tkr.Button(musicplayer,height =3 , width =5,text = "Resume Music",font ="Cambria 14 bold", command = resume ,bg ="blue", fg = "Black")


Button_play.pack(fill ="x")
Button_stop.pack(fill ="x")
Button_pause.pack(fill ="x")
Button_resume.pack(fill ="x")


playlist.pack(fill ="both",expand ="yes")


var = tkr.StringVar()
songTitle = tkr.Label(musicplayer, font ="Cambria 12 bold", textvariable = var)
songTitle.pack()
musicplayer.mainloop()