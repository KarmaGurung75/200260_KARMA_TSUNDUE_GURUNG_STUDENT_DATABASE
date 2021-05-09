from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
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

welcome.mainloop()
