import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas=tk.Tk()
canvas.title("Music Player | Developed by Kewal Suthar")
canvas.geometry("600x600+0+0")
canvas.config(bg='black')

rootpath="Your Path to your Music folder" # Make sure to edit this path and set this path.
pattern="*.mp3"

mixer.init()

prev_img=tk.PhotoImage(file='prev_img.png')
stop_img=tk.PhotoImage(file='stop_img.png')
pause_img=tk.PhotoImage(file='pause_img.png')
play_img=tk.PhotoImage(file='play_img.png')
next_img=tk.PhotoImage(file='next_img.png')

def select():
    label.config(text=listbox.get('anchor'))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear('active')

def play_next():
    next_song = listbox.curselection()
    next_song = next_song[0] + 1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def play_prev():
    next_song = listbox.curselection()
    next_song = next_song[0] - 1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def pause_song():
    if pauseButton["text"]=='Pause':
        mixer.music.pause()
        pauseButton["text"]='Play'
    else:
        mixer.music.unpause()
        pauseButton['text']="Pause"

listbox=tk.Listbox(canvas,fg='cyan',bg='black',width=100,font=("poppins",14))
listbox.pack(padx=15,pady=15)

label=tk.Label(canvas,text='',bg='black',fg='yellow',font=("poppins",14))
label.pack(pady=15)

top=tk.Frame(canvas,bd=3,bg='black')
top.pack(padx=10,pady=5,anchor='center')

prevButton=tk.Button(canvas,command=play_prev,text="Prev",image=prev_img,bg='black',borderwidth=0)
prevButton.pack(pady=15,in_=top,side='left')

stopButton=tk.Button(canvas,command=stop,text="Stop",image=stop_img,bg='black',borderwidth=0)
stopButton.pack(pady=15,in_=top,side='left')

playButton=tk.Button(canvas,command=select,text="Stop",image=play_img,bg='black',borderwidth=0)
playButton.pack(pady=15,in_=top,side='left')

pauseButton=tk.Button(canvas,command=pause_song,text="Stop",image=pause_img,bg='black',borderwidth=0)
pauseButton.pack(pady=15,in_=top,side='left')

nextButton=tk.Button(canvas,command=play_next,text="Stop",image=next_img,bg='black',borderwidth=0)
nextButton.pack(pady=15,in_=top,side='left')


for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert('end',filename)

canvas.mainloop()
