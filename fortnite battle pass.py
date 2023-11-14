from tkinter import *
import pygame
import os
import random
from PIL import Image, ImageTk
import shutil
from pytube import Playlist
from pytube import YouTube
from gtts import gTTS
from io import BytesIO
from os import path 
from pydub import AudioSegment
import subprocess
from moviepy.editor import *
import glob
from pathlib import Path
from time import sleep

base = Tk()
base.title('pluh')
base.geometry("500x600")
player = pygame.image.load('images\\player.png')
play_img = PhotoImage(file="images\play.png")
skip_img = PhotoImage(file="images\skipF.png")
back_img = PhotoImage(file="images\\skipB.png")
pause_img = PhotoImage(file="images\\pause.png")
shuffle_img = PhotoImage(file="images\\shuffle.png")
move_img = PhotoImage(file="images\\move.png")
nvm_img = PhotoImage(file="images\\nvm.png")
loop_img = PhotoImage(file="images\\loop.png")
chiefkeef = Image.open("images\\chiefkeef.jpg")
chiefkeef = chiefkeef.resize((50,50))
chiefkeef = ImageTk.PhotoImage(chiefkeef)
music_list = []
current_song = []
path = "music\\"
i = 0
x = 0
global paused
paused = False
global looped
looped = True

pygame.mixer.init()
pygame.mixer.music.set_endevent(69)
def leftKey(event):
    goBack()
base.bind('<Left>', leftKey)

def rightKey(event):
    skip()
base.bind('<Right>', rightKey)

def play2():
    global current
    pygame.mixer.music.load(path + music_list[i-1])
    for i in range(len(music_list),):
        current = music_list[i-1]
        pygame.mixer.music.queue(path + music_list[i])
        print(music_list[i])
        pygame.mixer.music.play(0)

def play():
        global i
        pygame.mixer.music.load(path + music_list[i])
        pygame.mixer.music.play()

        queue()
        
def pause(is_paused):
    global paused

    
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def search(input):
    index = music_list.index(input)
    return index

def print_input():
    global i 
    inp = input_text.get(1.0, "end-1c")
    index = search(inp)
    i = index
    print(i)
    music_box.select_clear(0, END)
    music_box.activate(i)
    music_box.selection_set(i, last=None)
    pygame.mixer.music.load(path + music_list[i])
    pygame.mixer.music.play()
    queue()
    
def skip():
    global i
    if music_list[i] != music_list[-1]:
        add()
        next_one = music_box.curselection()
        next_one = next_one[0] + 1
        music_box.selection_clear(0, END)
        music_box.activate(next_one)
        music_box.selection_set(next_one, last=None)
        pygame.mixer.music.load(path + music_list[i])
        pygame.mixer.music.play()
    else:
        print("fortnite")
        
def goBack():
    global i
    if music_list[i] != music_list[0]:
        subtract()
        next_one = music_box.curselection()
        next_one = next_one[0] - 1
        music_box.selection_clear(0, END)
        music_box.activate(next_one)
        music_box.selection_set(next_one, last=None)
        pygame.mixer.music.load(path + music_list[i])
        pygame.mixer.music.play()
    else:
        print("fortnite")

def queue():
    global i, music_list
    pos = pygame.mixer.music.get_pos()
    if int(pos) == -1:
        i += 1
        next_one = music_box.curselection()
        next_one = next_one[0] + 1
        music_box.selection_clear(0, END)
        music_box.activate(next_one)
        music_box.selection_set(next_one, last=None)
        pygame.mixer.music.load(path + music_list[i])
        pygame.mixer.music.play(0)
    base.after(1, queue)
    
def add():
    global i
    i += 1
    play()
    
def subtract():
    global i
    if i == len(music_list) - 1:
        i -= 2
        play()
    else:
        i -= 1
        play()

def stop():
    pygame.mixer.music.stop()
    
def mixemupcuh():
    global i
    music_list.clear()
    music_box.delete(0,END)
    i = 0
    print(music_list)
    shovethatshitincuh2()
    music_box.select_clear(0, END)
    music_box.activate(i)
    music_box.selection_set(i, last=None)
    pygame.mixer.music.load(path + music_list[i])
    pygame.mixer.music.play()
    queue()
    return

def move():
    for files in os.listdir("temp"):
        shutil.move("temp\\" + files, "music\\" + files)
    for files in os.listdir("music"):
        music_list.append(files)
    music_list.clear()
    music_box.delete(0,END)
    input_playlist.delete(0,END)
    input_text.delete('1.0', END)
    file_list.clear()
    shovethatshitincuh()

def loop(is_looped):
    global looped

    
    looped = is_looped
    if looped:
        pygame.mixer.music.play(-1)
        looped = False
    else:
        pygame.mixer.music.play()
        looped = True

def remove():
    global i
    index = music_list[i]
    music_list.remove(index)
    music_box.delete(i)
    pygame.mixer.music.unload()
    print(i)
    print(len(music_list))
    os.remove("music\\" + index)
    

def shovethatshitincuh():
    for files in os.listdir("music"):
        music_list.append(files)
    fake_list = music_list[:]
    fake_list.reverse()
    print(fake_list)
    for i in range(len(music_list)):
        music_box.insert(0, fake_list[i])

def shovethatshitincuh2():
    for files in os.listdir("music"):
        music_list.append(files)
    random.shuffle(music_list)
    fake_list = music_list[:]
    fake_list.reverse()
    print(fake_list)
    for i in range(len(music_list)):
        music_box.insert(0, fake_list[i])

def converted():
    convert()
    fix3()

def converted2():
    convert2()
    fix3()
    

file_list = []

def search2():
    inp = input_playlist.get(1.0, "end-1c")
    print(inp)

def convert():
    inp = input_text.get(1.0, "end-1c")
    music_playlist = Playlist(inp)

    for video in music_playlist.videos:
        video.streams.filter(only_audio = True).first().download(output_path= "test", filename=f"{video.title}.mp3")

def convert2():
    inp = input_text.get(1.0, "end-1c")
    song = YouTube(inp)
    song.streams.filter(only_audio = True).first().download(output_path= "test", filename=f"{song.title}.mp3")

def fix3():
    for files in os.listdir("test"):
        file_list.append(files)
       
    for songs in file_list:
        mp4_file = songs
        mp3_file = songs
        test1 = "Canon in D (Pachelbel) Piano Cover by Ryan Jones.mp4"
        test2 = "Canon in D (Pachelbel) Piano Cover by Ryan Jones.mp3"
        print(mp4_file)
        print(mp3_file)
        #videoClip = VideoFileClip("test/" + mp4_file)
        audioClip = AudioFileClip("test/" + mp4_file)
        audioClip.write_audiofile("temp/" + mp3_file)
        audioClip.close()

        #videoClip.close()
        #question for shag why can't i have "," but i can do "+"

    for files in glob.glob('test\\*mp3'):
        os.remove(files)
    
    for files in os.listdir("temp"):
        current_song.append(files)
    for i in range(len(current_song)):
        input_playlist.insert(0, current_song[i])

def nvm():
    current_song.clear()
    input_playlist.delete(0,END)
    input_text.delete('1.0', END)
    file_list.clear()
    for files in glob.glob('temp\\*mp3'):
        os.remove(files)


nav_bar = Frame(base)
search_bar = Frame(base)
button_bar = Frame(base)
music_box = Listbox(base, bg="black", fg="yellow", selectbackground="green",width =80, height =20)
music_box.pack(pady=20)

def select_music(event):
    global i
    selection = event.widget.curselection()
    w = event.widget
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        value = w.get(index)
        real_index = music_list.index(value)
        i = real_index
        print(real_index)
        pygame.mixer.music.load(path + music_list[i])
        pygame.mixer.music.play()
        queue()
    else:
        print("no")
music_box.bind("<<ListboxSelect>>", select_music)


nav_bar.pack()
input_text = Text(search_bar, height = 5, width = 20)
input_playlist = Listbox(search_bar, height = 5, width = 20)

search_bar.pack()
button_bar.pack()


play_button = Button(nav_bar, image=play_img, borderwidth=0, command= lambda: pause(paused))
#stop_button = Button(nav_bar, image=pause_img,borderwidth=0, command= lambda: pause(paused))
skipF_button = Button(nav_bar, image=skip_img,borderwidth=0, command = skip)
go_back_button = Button(nav_bar, image=back_img,borderwidth=0,command = goBack)
shuffle_button = Button(nav_bar, image=loop_img,borderwidth=0, command = mixemupcuh)
move_button = Button(button_bar, text="Move", command = move)
nvm_button = Button(button_bar, text="Nvm", command = nvm)
input_button = Button(button_bar, text = "Search", command = print_input)
play_listbutton = Button(button_bar, text="ConvertPL", command = converted)
video_button = Button(button_bar, text="ConvertVD", command = converted2)
remove_button = Button(button_bar, text="Remove",command = remove)
loop_button = Button(nav_bar, image=shuffle_img, command = lambda: loop(looped))

#chiefkeef_button = Button(base, image=chiefkeef,borderwidth=0, command = skip)


play_button.grid(row=0, column=3)
#stop_button.grid(row=0, column=5)
skipF_button.grid(row=0, column=4)
go_back_button.grid(row=0, column=2)
shuffle_button.grid(row=0,column=0)


input_button.grid(row=0,column=2)
play_listbutton.grid(row=0,column=0)
video_button.grid(row=0,column=1)
move_button.grid(row=0,column=3)
nvm_button.grid(row=0,column=4)
remove_button.grid(row=0,column=5)
loop_button.grid(row=0,column=6)

input_text.grid(row=1,column=0)
input_playlist.grid(row=1, column=1)
#chiefkeef_button.place(x=50,y=200)

shovethatshitincuh()
base.mainloop()
print(music_list)
print(len(music_list))
