from tkinter import *
from tkinter import messagebox


# for clearnig the screen (remove all the things from window)
def clearScreen():
    for widget in window.winfo_children():
        widget.destroy()
        


def empManage():
   # messagebox.showinfo(message='Logged in successful.')
    clearScreen()
    
    def addEmp():
        id = id_entry.get()
        nm = nm_entry.get()
        sal = sal_entry.get()
    
    def selectEmp():
        pass
    
    def updateEmp():
        pass
    
    def deleteEmp():
        pass
    
    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)
    
    # these all are in frame1
    id_label = Label(frame1, text='ID:')
    id_entry = Entry(frame1)
    nm_label = Label(frame1, text='NAME:')
    nm_entry = Entry(frame1)
    sal_label = Label(frame1, text='SALARY:')
    sal_entry = Entry(frame1)
    
    id_label.grid(row=0, column=0)
    id_entry.grid(row=0, column=1)
    nm_label.grid(row=1, column=0)
    nm_entry.grid(row=1, column=1)
    sal_label.grid(row=2, column=0)
    sal_entry.grid(row=2, column=1)
    
    frame1.pack()
    
    # all buttons are in frame2
    add_btn = Button(frame2, text='ADD', command=addEmp)
    sel_btn = Button(frame2, text='SELECT', command=selectEmp)
    upd_btn = Button(frame2, text='UPDATE', command=updateEmp)
    dele_btn = Button(frame2, text='DELETE', command=deleteEmp)
    
    add_btn.pack(side=LEFT)
    sel_btn.pack(side=LEFT)
    upd_btn.pack(side=LEFT)
    dele_btn.pack(side=LEFT)
    
    frame2.pack()
    
    
    #list box in frame3
    #scrollbar
    scrollbar = Scrollbar(frame3)
    scrollbar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(frame3, yscrollcommand=scrollbar.set, height=15, width=40)
    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    
    frame3.pack()
    

def login():
    uid = uid_entry.get()
    passw = passw_entry.get()
    
    uname = 'admin'
    password = '12345'
    
    if (uid == uname and passw == password):
        empManage()
    else:
        messagebox.showwarning(message='Invalid Credentials!')
        
def main():
    uid_label = Label(window, text='User ID:')
    
    global uid_entry
    uid_entry = Entry(window)
    
    passw_label = Label(window, text='Password:')
    
    global passw_entry
    passw_entry = Entry(window)
    
    btn = Button(window, text='LOGIN', command=login)
    
    uid_label.pack()
    uid_entry.pack()
    passw_label.pack()
    passw_entry.pack()
    btn.pack()



if (__name__ == '__main__'):
    
    window = Tk()
    window.geometry('300x400')
    
    #main()         #bypass the main method with empManage() method
    empManage()
    
    
    window.mainloop() 













####### from chatgpt for beautification





'''


from tkinter import *
from tkinter import messagebox


# for clearnig the screen (remove all the things from window)
def clearScreen():
    for widget in window.winfo_children():
        widget.destroy()
        


def empManage():

    clearScreen()

    window.config(bg="#1e1e2f")
    window.title("Employee Management System")

    def addEmp():
        pass

    def selectEmp():
        pass

    def updateEmp():
        pass

    def deleteEmp():
        pass

    # ---------------- Title ----------------
    title = Label(
        window,
        text="EMPLOYEE MANAGEMENT SYSTEM",
        font=("Arial", 16, "bold"),
        bg="#1e1e2f",
        fg="cyan",
        pady=10
    )
    title.pack()

    # ---------------- Frames ----------------
    frame1 = Frame(window, bg="#1e1e2f")
    frame2 = Frame(window, bg="#1e1e2f")
    frame3 = Frame(window, bg="#1e1e2f")

    # ---------------- Labels ----------------
    id_label = Label(
        frame1,
        text="ID:",
        font=("Arial", 11, "bold"),
        bg="#1e1e2f",
        fg="white"
    )

    nm_label = Label(
        frame1,
        text="NAME:",
        font=("Arial", 11, "bold"),
        bg="#1e1e2f",
        fg="white"
    )

    sal_label = Label(
        frame1,
        text="SALARY:",
        font=("Arial", 11, "bold"),
        bg="#1e1e2f",
        fg="white"
    )

    # ---------------- Entries ----------------
    id_entry = Entry(
        frame1,
        font=("Arial", 11),
        width=20,
        bg="#2e2e3f",
        fg="white",
        insertbackground="white"
    )

    nm_entry = Entry(
        frame1,
        font=("Arial", 11),
        width=20,
        bg="#2e2e3f",
        fg="white",
        insertbackground="white"
    )

    sal_entry = Entry(
        frame1,
        font=("Arial", 11),
        width=20,
        bg="#2e2e3f",
        fg="white",
        insertbackground="white"
    )

    id_label.grid(row=0, column=0, padx=10, pady=8, sticky=W)
    id_entry.grid(row=0, column=1, padx=10, pady=8)

    nm_label.grid(row=1, column=0, padx=10, pady=8, sticky=W)
    nm_entry.grid(row=1, column=1, padx=10, pady=8)

    sal_label.grid(row=2, column=0, padx=10, pady=8, sticky=W)
    sal_entry.grid(row=2, column=1, padx=10, pady=8)

    frame1.pack(pady=10)

    # ---------------- Buttons ----------------
    add_btn = Button(
        frame2,
        text="ADD",
        command=addEmp,
        bg="#28a745",
        fg="white",
        font=("Arial", 10, "bold"),
        width=10
    )

    sel_btn = Button(
        frame2,
        text="SELECT",
        command=selectEmp,
        bg="#007bff",
        fg="white",
        font=("Arial", 10, "bold"),
        width=10
    )

    upd_btn = Button(
        frame2,
        text="UPDATE",
        command=updateEmp,
        bg="#ffc107",
        font=("Arial", 10, "bold"),
        width=10
    )

    dele_btn = Button(
        frame2,
        text="DELETE",
        command=deleteEmp,
        bg="#dc3545",
        fg="white",
        font=("Arial", 10, "bold"),
        width=10
    )

    add_btn.pack(side=LEFT, padx=5)
    sel_btn.pack(side=LEFT, padx=5)
    upd_btn.pack(side=LEFT, padx=5)
    dele_btn.pack(side=LEFT, padx=5)

    frame2.pack(pady=10)

    # ---------------- Listbox ----------------
    scrollbar = Scrollbar(frame3)
    scrollbar.pack(side=RIGHT, fill=Y)

    mylist = Listbox(
        frame3,
        yscrollcommand=scrollbar.set,
        height=12,
        width=45,
        bg="#2e2e3f",
        fg="white",
        font=("Consolas", 10),
        selectbackground="cyan",
        selectforeground="black"
    )

    mylist.pack(side=LEFT, fill=BOTH)

    scrollbar.config(command=mylist.yview)

    frame3.pack(pady=15)

def login():
    uid = uid_entry.get()
    passw = passw_entry.get()
    
    uname = 'admin'
    password = '12345'
    
    if (uid == uname and passw == password):
        empManage()
    else:
        messagebox.showwarning(message='Invalid Credentials!')
        
def main():
    uid_label = Label(window, text='User ID:')
    
    global uid_entry
    uid_entry = Entry(window)
    
    passw_label = Label(window, text='Password:')
    
    global passw_entry
    passw_entry = Entry(window)
    
    btn = Button(window, text='LOGIN', command=login)
    
    uid_label.pack()
    uid_entry.pack()
    passw_label.pack()
    passw_entry.pack()
    btn.pack()



if (__name__ == '__main__'):
    
    window = Tk()
    window.geometry('500x550')
    window.config(bg='#1e1e2f')
    
    #main()         #bypass the main method with empManage() method
    empManage()
    
    
    window.mainloop()
    
    
'''