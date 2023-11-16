from tkinter import *
from tkinter import ttk
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
base.geometry("500x620")
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
create1_playlist = []
create2_playlist = []
create3_playlist = []
create4_playlist = []
create5_playlist = []

options = []
play_list = []
global f_path
f_path = "playlist\\music\\"
current_path = "playlist\\music"
global k
i = 0
x = 0
k = 0

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

def play():
        global i
        pygame.mixer.music.load(f_path + play_list[k][i])
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
    index = play_list[k].index(input)
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
    pygame.mixer.music.load(f_path + play_list[k][i])
    pygame.mixer.music.play()
    queue()
    
def skip():
    global i
    if play_list[k][i] != play_list[k][-1]:
        add()
        next_one = music_box.curselection()
        next_one = next_one[0] + 1
        music_box.selection_clear(0, END)
        music_box.activate(next_one)
        music_box.selection_set(next_one, last=None)
        pygame.mixer.music.load(f_path + play_list[k][i])
        pygame.mixer.music.play()
    else:
        print("fortnite")
        
def goBack():
    global i
    if play_list[k][i] != play_list[k][0]:
        subtract()
        next_one = music_box.curselection()
        next_one = next_one[0] - 1
        music_box.selection_clear(0, END)
        music_box.activate(next_one)
        music_box.selection_set(next_one, last=None)
        pygame.mixer.music.load(f_path + play_list[k][i])
        pygame.mixer.music.play()
    else:
        print("fortnite")

def queue():
    global i, play_list
    pos = pygame.mixer.music.get_pos()
    if int(pos) == -1:
        i += 1
        next_one = music_box.curselection()
        next_one = next_one[0] + 1
        music_box.selection_clear(0, END)
        music_box.activate(next_one)
        music_box.selection_set(next_one, last=None)
        pygame.mixer.music.load(f_path + play_list[k][i])
        pygame.mixer.music.play(0)
    base.after(1, queue)
    
def add():
    global i
    i += 1
    play()
    
def subtract():
    global i
    i -= 1
    play()

def stop():
    pygame.mixer.music.stop()
    
def mixemupcuh():
    global i
    play_list[k].clear()
    music_box.delete(0,END)
    i = 0
    print(play_list[k])
    shovethatshitincuh2()
    music_box.select_clear(0, END)
    music_box.activate(i)
    music_box.selection_set(i, last=None)
    pygame.mixer.music.load(f_path + play_list[k][i])
    pygame.mixer.music.play()
    queue()
    return

def move():
    for files in os.listdir("temp"):
        shutil.move("temp\\" + files, f_path + files)
    for files in os.listdir(current_path):
        play_list[k].append(files)
    play_list[k].clear()
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
    index = play_list[k][i]
    play_list[k].remove(index)
    music_box.delete(i)
    pygame.mixer.music.unload()
    print(i)
    print(len(play_list[k]))
    os.remove(f_path + index)
    
def shovethatshitincuh():
    combobox_length = len(play_list_button["values"])
    for i in range(combobox_length):
        play_list.append([])

    for files in os.listdir(current_path):
        play_list[k].append(files)
    fake_list = play_list[k][:]
    fake_list.reverse()
    print(fake_list)
    for i in range(len(play_list[k])):
        music_box.insert(0, fake_list[i])

def shovethatshitincuh2():
    for files in os.listdir(current_path):
        play_list[k].append(files)
    random.shuffle(play_list[k])
    fake_list = play_list[k][:]
    fake_list.reverse()
    print(fake_list)
    for i in range(len(play_list[k])):
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

def select():
    global k
    global f_path
    global current_path
    current_val = play_list_button.current()

    k = current_val

    f_path = "playlist\\" + options[k] + "\\"
    current_path = "playlist\\" + options[k] + "\\"
    print(f_path)
    try:
        play_list[k].clear()
    except:
        pass
    music_box.delete(0,END)
    music_box.selection_clear(0, END)
    pygame.mixer.music.unload()
    pygame.mixer.music.stop()
    shovethatshitincuh()
    print(play_list[k])

def create():
    folder_name = input_text.get(1.0, "end-1c")
    try:
        if not os.path.exists(folder_name):
            os.makedirs("playlist/" + folder_name)
    except OSError:
        print("Error creating:", folder_name)
    
    options.append(folder_name)
    play_list_button['values'] = options
    input_text.delete('1.0', END)

def remove_playlist():
    playlist_to_remove = play_list_button.current()
    playlist_name = options[playlist_to_remove]
    shutil.rmtree("playlist\\" + playlist_name + "\\")
    input_text.delete('1.0', END)
    play_list_button['values'] = options
    return print(playlist_name)

def the_creation():
    for files in os.listdir("playlist"):
        options.append(files)
    print(options)
    
the_creation()
selected = StringVar()
selected.trace('w', select)

nav_bar = Frame(base)
search_bar = Frame(base)
button_bar = Frame(base)
play_list_bar =Frame(base, pady=10)
music_box = Listbox(base, bg="black", fg="yellow", selectbackground="green",width =80, height =20)
music_box.pack(pady=20)

def select_music(event):
    global i
    global f_path
    #sourceFileDir = os.path.dirname(os.path.abspath(__file__))
    #filePath = os.path.join(sourceFileDir, play_list[k][i])

    selection = event.widget.curselection()
    w = event.widget
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        value = w.get(index)
        real_index = play_list[k].index(value)
        i = real_index
        print(real_index)
        pygame.mixer.music.load(f_path + play_list[k][i])
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
play_list_bar.pack()


play_button = Button(nav_bar, image=play_img, borderwidth=0, command= play)
stop_button = Button(nav_bar, image=pause_img,borderwidth=0, command= lambda: pause(paused))
skipF_button = Button(nav_bar, image=skip_img,borderwidth=0, command = skip)
go_back_button = Button(nav_bar, image=back_img,borderwidth=0,command = goBack)
shuffle_button = Button(nav_bar, image=loop_img,borderwidth=0, command = mixemupcuh)
loop_button = Button(nav_bar, image=shuffle_img,borderwidth=0, command = lambda: loop(looped))

move_button = Button(button_bar, text="Move", command = move)
nvm_button = Button(button_bar, text="Nvm", command = nvm)
input_button = Button(button_bar, text = "Search", command = print_input)
play_listbutton = Button(button_bar, text="ConvertPL", command = converted)
video_button = Button(button_bar, text="ConvertVD", command = converted2)
remove_button = Button(button_bar, text="Remove",command = remove)


play_list_button = ttk.Combobox(play_list_bar, values= options, state="readonly")
create_button = Button(play_list_bar,text="Create", command=create)
select_button = Button(play_list_bar,text="Select", command= select)
removePL_button = Button(play_list_bar,text="Remove", command=remove_playlist)

#chiefkeef_button = Button(base, image=chiefkeef,borderwidth=0, command = skip)


play_button.grid(row=0, column=3)
#stop_button.grid(row=0, column=5)
skipF_button.grid(row=0, column=5)
go_back_button.grid(row=0, column=2)
shuffle_button.grid(row=0,column=0)
stop_button.grid(row=0,column=4)


input_button.grid(row=0,column=2)
play_listbutton.grid(row=0,column=0)
video_button.grid(row=0,column=1)
move_button.grid(row=0,column=3)
nvm_button.grid(row=0,column=4)
remove_button.grid(row=0,column=5)
loop_button.grid(row=0,column=6)

play_list_button.grid(row=0,column=0)
select_button.grid(row=0,column=1)
create_button.grid(row=0,column=2)
removePL_button.grid(row=0,column=3)

input_text.grid(row=1,column=0)
input_playlist.grid(row=1, column=1)
#chiefkeef_button.place(x=50,y=200)

shovethatshitincuh()
base.mainloop()
print(play_list[k])
print(len(play_list[k]))
