from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
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
    Label(data0, text="Log in", width=300, height=2).pack()
    Label(data0, text="").pack()
    Button(data0, text="Register", width=300, height=2, command=register).pack()


def register_success():
    username_info=username.get()
    password_info=password.get()

    file=open(username_info +".txt","w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    address_entry.delete(0, END)
    contact_entry.delete(0, END)

    Label(data1,text="Registration successful", fg="green",font="time,11").pack()


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


btn=Button(data,text="Click Here To Enter",font="Times 20",width=25,padx=10,pady=10,command=open).pack()

data.mainloop()
