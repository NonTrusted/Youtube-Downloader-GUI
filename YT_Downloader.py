import pytube
from pytube import YouTube
from pydub import AudioSegment
import os
from tkinter import *

root = Tk()
root.geometry("400x90")
root.title("MP3 Or MP4")

def mp4_downloader(url):
    video = pytube.YouTube(url)

    stream = video.streams.get_highest_resolution()
    stream.download()


def mp3_downloader(url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()

    file_name = stream.default_filename
    mp4_audio = AudioSegment.from_file(file_name, format="mp4")
    mp4_audio.export(file_name.replace("mp4", "mp3"), format="mp3")

    os.remove(file_name)

def mp3():
    root = Tk()
    root.geometry("500x100")
    root.title("MP3")

    label = Label(root, text="MP3 Downloader")
    label.pack()

    mp3_link = Entry(root, width = 40)
    mp3_link.focus_set()
    mp3_link.pack()

    def say():
        mp3_downloader(mp3_link.get())

    login = Button(root, text=' Enter ',command=say)
    login.pack()

def mp4():
    root = Tk()
    root.geometry("500x100")
    root.title("MP4")

    label = Label(root, text="MP4 Downloader")
    label.pack()

    mp4_link = Entry(root, width = 40)
    mp4_link.focus_set()
    mp4_link.pack()

    def say():
        mp4_downloader(mp4_link.get())

    login = Button(root, text=' Enter ',command=say)
    login.pack()

mp3 = Button(root, text="MP3", command=mp3)
empty1 = Label(root, text="‎")
empty2 = Label(root, text="‎")
mp4 = Button(root, text="MP4", command=mp4)

mp3.pack()
empty1.pack()
mp4.pack()
empty2.pack()

root.mainloop()
