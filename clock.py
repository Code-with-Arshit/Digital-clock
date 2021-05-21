from tkinter import *
from tkinter.ttk import *
from time import strftime
clock = Tk()
clock.title("Digital Clock")
def time():
    string = strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)
label = Label(clock, font=("ds-digital" ,80), background="black", foreground="cyan")
label.pack(anchor="center")
time()
mainloop()