from tkinter import *

window = Tk()                                   # make a Tkinter window

window.geometry('300x400')                     # size of window

window.title('First Program')                   # give a title 

window.config(bg='#1e1e2f')               # to give the background color

txt = Label(
    window,
    text='Hello World!',                # if u want to add text in window
    font =('Arial', 18, 'bold'),
    bg = '#1e1e2f',
    fg = 'cyan',
    pady= 20
    )        

txt.pack()              # put take text into the middle

window.mainloop()               # to hold the the output screen (window)