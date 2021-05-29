from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import os
data=Tk()
data.title("Welcome")
data.iconbitmap("")
data.geometry("500x600")

canvas = Canvas(data, width =350, height =340)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("photo.jpg"))
canvas.create_image(20, 20, anchor=NW, image=img)

welcomeLabel=Label(data,text="Welcome to Samjhana Pvt.lmt",font="Times 30",pady=10,padx=10)
welcomeLabel.pack()

def open():
    global data0
    data0=Toplevel()
    data0.title("")
    data0.geometry("500x500")
    Label(data0, text="Log in or Register", width=300, height=2, font="time 11").pack()
    Label(data0, text="").pack()
    Button(data0, text="Log in", width=300, height=2, command=login).pack()
    Button(data0, text="Register", width=300, height=2, command=register).pack()

def delete2():
    data2.destroy()


def login_success():
    global data2
    data2 = Toplevel()
    data2.title("success")
    data2.geometry("150x100")
    Label(data2, text="Log in success").pack()
    Button(data2, text="Ok", command=delete2).pack()


def password_not_recognize():
    print("Password is incorrect")


def user_not_found():
    print("username is incorrect")



def register_success():
    username_info=username.get()
    password_info=password.get()

    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    address_entry.delete(0, END)
    contact_entry.delete(0, END)

    Label(data1,text="Registration successful", fg="green",font="time,11").pack()

def login_verify():
    username=username_verify1.get()
    password=password_verify1.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files= os.listdir()
    if username in list_of_files:
        file1=open(username,"r")
        verify=file1.read().splitlines()
        if password in verify:
            login_success()
        else:
            password_not_recognize()
    else:
        user_not_found()


def register():
    global data1
    data1=Toplevel(data)
    data1.title("registration")
    data1.geometry("500x500")

    global username
    global password
    global address
    global contact
    global username_entry
    global password_entry
    global address_entry
    global contact_entry
    username= StringVar()
    password= StringVar()
    address= StringVar()
    contact= StringVar()

    Label(data1,text="Enter the detail").pack()
    Label(data1,text="").pack()
    # username registration
    Label(data1,text="Username").pack()
    username_entry=Entry(data1,text=username)
    username_entry.pack()
    # password registration
    Label(data1, text="Password").pack()
    password_entry = Entry(data1, text=password)
    password_entry.pack()

    Label(data1, text="Address").pack()
    address_entry = Entry(data1, text=address)
    address_entry.pack()

    Label(data1, text="Contact").pack()
    contact_entry = Entry(data1, text=contact)
    contact_entry.pack()

    Label(data1, text="").pack()
    Button(data1, text="Register", width=10, height=1,command=register_success).pack()

def login():
    global username_verify1
    global password_verify1
    global username_entry1
    global password_entry1
    global login
    login=Toplevel()
    login.title("Login")
    login.geometry("300x250")
    Label(login, text="Please Enter your username and password")
    Label(login, text="").pack()

    username_verify1=StringVar()
    password_verify1=StringVar()

    # username registration
    Label(login, text="Username").pack()
    username_entry1 = Entry(login, textvariable=username_verify1)
    username_entry1.pack()

    # password registration
    Label(login, text="Password").pack()
    password_entry1 = Entry(login, textvariable=password_verify1)
    password_entry1.pack()

    Button(login, text="Log in", width=300, height=2, command=login_verify).pack()



btn=Button(data,text="Click Here To Enter",font="Times 20",width=25,padx=10,pady=10,command=open).pack()

data.mainloop()
