from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import sqlite3
welcome=Tk()
welcome.title("Welcome")
welcome.iconbitmap("")
welcome.geometry("500x600")

canvas = Canvas(welcome, width =350, height =340)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("photo.jpg"))
canvas.create_image(20, 20, anchor=NW, image=img)

welcomeLabel=Label(welcome,text="Welcome to Samjhana Pvt.lmt",font="Times 30",pady=10,padx=10)
welcomeLabel.pack()

def open():
    global my_img
    top=Toplevel()
    top.title("")
    top.geometry("500x500")
    myButton=Button(top, text="Show Data",width=10, height=10)
    myButton.grid()
    myButton1= Button(top, text="Add Data ",width = 10, height = 10)
    myButton1.grid()

btn=Button(welcome,text="Click Here To Enter",font="Times 20",width=25,padx=10,pady=10,command=open).pack()

welcome.mainloop()
