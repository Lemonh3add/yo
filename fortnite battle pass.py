from tkinter import *
import time
import pygame
import os
import mutagen
import random
from PIL import Image, ImageTk

base = Tk()
base.title('pluh')
base.geometry("500x600")
player = pygame.image.load('images\\player.png')
play_img = PhotoImage(file="images\play.png")
skip_img = PhotoImage(file="images\skipF.png")
back_img = PhotoImage(file="images\\skipB.png")
pause_img = PhotoImage(file="images\\pause.png")
shuffle_img = PhotoImage(file="images\\shuffle.png")
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


pygame.mixer.init()
pygame.mixer.music.set_endevent(69)

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
    add()
    next_one = music_box.curselection()
    next_one = next_one[0] + 1
    music_box.selection_clear(0, END)
    music_box.activate(next_one)
    music_box.selection_set(next_one, last=None)
    pygame.mixer.music.load(path + music_list[i])
    pygame.mixer.music.play()

def goBack():
    global i
    subtract()
    next_one = music_box.curselection()
    next_one = next_one[0] - 1
    music_box.selection_clear(0, END)
    music_box.activate(next_one)
    music_box.selection_set(next_one, last=None)
    pygame.mixer.music.load(path + music_list[i])
    pygame.mixer.music.play()

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
    
nav_bar = Frame(base)
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
input_text = Text(base, height = 5, width = 20)
input_text.pack()


play_button = Button(nav_bar, image=play_img, borderwidth=0, command= lambda: play)
stop_button = Button(nav_bar, image=pause_img,borderwidth=0, command= lambda: pause(paused))
skipF_button = Button(nav_bar, image=skip_img,borderwidth=0, command = skip)
go_back_button = Button(nav_bar, image=back_img,borderwidth=0,command = goBack)
shuffle_button = Button(nav_bar, image=shuffle_img,borderwidth=0, command = mixemupcuh)
input_button = Button(base, text = "Search", command = print_input)
input_button.pack()
#chiefkeef_button = Button(base, image=chiefkeef,borderwidth=0, command = skip)


play_button.grid(row=0, column=3)
stop_button.grid(row=0, column=5)
skipF_button.grid(row=0, column=4)
go_back_button.grid(row=0, column=2)
shuffle_button.grid(row=0,column=0)

#chiefkeef_button.place(x=50,y=200)

shovethatshitincuh()
base.mainloop()
print(music_list)
print(len(music_list))
