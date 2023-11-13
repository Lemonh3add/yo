from pytube import Playlist
from pytube import YouTube
from gtts import gTTS
from io import BytesIO
import os
from os import path 
from pydub import AudioSegment
import subprocess
from moviepy.editor import *
import glob

file_list = []

music_playlist = Playlist('https://www.youtube.com/playlist?list=PLyN-YGKnqFXwjlLADg5R6_CdP6os1Q4TB')
def convert():
    for video in music_playlist.videos:
        video.streams.filter(only_audio = True).first().download(output_path= "test", filename=f"{video.title}.mp3")

def convert2():
    inp = "https://www.youtube.com/watch?v=NA5kbUQD8JI&ab_channel=LILUZIVERT"
    song = YouTube(inp)
    song.streams.filter(only_audio = True).first().download(output_path= "test", filename=f"{song.title}.mp3")
def convert3():
    for video in music_playlist.videos:
        video.streams.first().download(output_path= "test", filename=f"{video.title}.mp4")

def fix3():
    for files in os.listdir("test"):
        file_list.append(files)
       
    for i in file_list:
        mp4_file = i
        mp3_file = i
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



def fix():
    for files in os.listdir("test"):
        input_file = files
        output_file = "result.wav"
  
# convert mp3 file to wav file 
        sound = AudioSegment.from_file("test") 
        sound.export(output_file, format="wav") 

def fix2():
    subprocess.call(['ffmpeg', ''])


def main():
    convert2()
    fix3()

main()