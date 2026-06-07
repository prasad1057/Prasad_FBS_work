from tkinter import *
from tkinter import messagebox


def changeBg():
    val = x.get()
    
    if (val == 1):
        window.config(bg='black')
    elif(val == 2):
        window.config(bg='red')
    elif (val == 3):
        window.config(bg='yellow')
    else:
        messagebox.showwarning(message='No color selected.')
        
    

window = Tk()
window.geometry('300x400')
window.title('Color Selection')


x = IntVar()

txt = Label(window, text='Please select color:')
txt.pack()

rdo1 = Radiobutton(window, text='black', variable=x, value=1)
rdo1.pack()

rdo2 = Radiobutton(window, text='red', variable=x, value=2)
rdo2.pack()

rdo3 = Radiobutton(window, text='yellow', variable=x, value=3)
rdo3.pack()


btn = Button(window, text='Apply', command=changeBg)
btn.pack()

window.mainloop()