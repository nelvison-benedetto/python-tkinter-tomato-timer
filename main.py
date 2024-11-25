import tkinter
from tkinter import PhotoImage, Canvas
from tkinter import *

def checkbutton_used():
    print("dhcbsdjc")
def countdown(minutes,seconds):
    canvas.itemconfig(timer_text, text= f"{minutes:02}:{seconds:02}")
    if seconds > 0:
        window.after(1000, countdown, minutes,seconds - 1)
    elif minutes > 0:  #si attiva solo quando if seconds>0 non si attiva
        window.after(1000, countdown, minutes -1, 59)
    else:
        canvas.itemconfig(timer_text, text="00:00")
        title_label.config(text="Time's up!")

def button_start_clicked():
    min, sec = scale_minutes_seconds()
    countdown(min, sec)

def scale_minutes_seconds(value = None):
    #print(value, value2)
    minutes = scaleminutes.get()  #UPLOAD TEXT 00:00 IN REAL TIME!!
    seconds = scaleseconds.get()
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    return minutes, seconds

def scale_used_min(value):
    print(value)
    countdown()
def scale_used_sec(value):
    print(value)

FONT = "Times New Roman",15,"italic"
text = "00:00"

window = tkinter.Tk()
window.title = "Tkinter 2 Tomato Timer"
window.config(padx=100,pady=50, background="yellow",highlightthickness=0)

title_label = tkinter.Label(text="Timer",font=("Times New Roman",50,"italic"))
title_label.grid(column=1, row=0)

canvas = Canvas(width= 200,height =200 )
root = "D:\\Python_Projects\\pyCharm_Prjs\\3-Day28_Tkinter2"
image_path = f"{root}\\tomato.png"
image = PhotoImage(file=image_path)

canvas.create_image(100,112, image=image)
timer_text = canvas.create_text(103,112,text=text, font=("Times New Roman",35,"bold"))
canvas.grid(column=1,row=1)

start_button = tkinter.Button(text="Start",highlightthickness=0, command=button_start_clicked)
start_button.grid(column=0,row=2)
reset_button = tkinter.Button(text="Stop", highlightthickness=0)
reset_button.grid(column=2,row=2)

check_label = tkinter.Label(text="✔", fg="green")
check_label.grid(column=1, row=2)

scaleminutes = Scale(from_=0, to=59, command=scale_minutes_seconds)
scaleminutes.grid(column=0, row= 3)
scaleseconds = Scale(from_=0, to=59, command=scale_minutes_seconds)
scaleseconds.grid(column=2, row= 3)



window.mainloop()


