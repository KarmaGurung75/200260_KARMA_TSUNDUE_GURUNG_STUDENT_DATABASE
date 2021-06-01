from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
from tkinter import messagebox
import os
import sqlite3
import Database



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
conn=sqlite3.connect("login_register.db")

c=conn.cursor()
'''
c.execute("""CREATE TABLE login(
      Firstname text,
      Surname text,
      Email text,
      address text,
      contact text,
      password text
)
""")
print("Insert table success")'''

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

def register_success():
    if Firstname.get() == "" or Surname.get() == "" or Email.get() == "" or address.get() == "" or contact.get() == " " or password.get() == " ":
        messagebox.showinfo("Incomplete registration", "Please fill the form completely")
    else:
        conn = sqlite3.connect('login_register.db')
        # Create cursor
        c = conn.cursor()
        # Insert into table
        c.execute("INSERT INTO login VALUES (:Firstname,:Surname,:Email,:address,:contact,:password)", {
                    'Firstname': Firstname.get(),
                    'Surname': Surname.get(),
                    'Email': Email.get(),
                    'address':address.get(),
                    'contact':contact.get(),
                    'password': password.get(),

                })
        # showinfo
        # messagebox
        conn.commit()
        conn.close()
        messagebox.showinfo("Register", "You have successfully registered")


    Firstname_entry.delete(0, END)
    Surname_entry.delete(0, END)
    Email_entry.delete(0, END)
    address_entry.delete(0, END)
    contact_entry.delete(0, END)
    password_entry.delete(0, END)
    #Label(data1,text="Registration successful", fg="green",font="time,11").pack()

def login_verify():
    # Create a databases or connect to one
    conn = sqlite3.connect('login_register.db')
    # Create cursor
    c = conn.cursor()
    # query of the database
    c.execute("SELECT *, oid FROM login")
    records = c.fetchall()
    # Loop through the results
    for record in records:
        if str(record[2]) == Email_entry1.get() and str(record[5]) == password_entry1.get():
            # str(record[6]) added for displaying the id
            try:
                messagebox.showinfo("login", "login successful", parent=login1)
                login1.withdraw()
                data0.withdraw()
                data.withdraw()
                return Database.std_data()


            except:
                pass
        elif Email_entry1.get() == "" or password_entry1.get() == "":
            try:
                return messagebox.showinfo("login", "Please fill completely.", parent=login1)
            except:
                pass
    messagebox.showinfo("login", "Your Email and password do not match.", parent=login1)

    conn.commit()
    conn.close()


def register():
    global data1
    data1=Toplevel(data)
    data1.title("registration")
    data1.geometry("500x500")


    global Firstname
    global Surname
    global Email
    global password
    global address
    global contact
    global Firstname_entry
    global Surname_entry
    global Email_entry
    global password_entry
    global address_entry
    global contact_entry
    Firstname= StringVar()
    Surname=StringVar()
    Email=StringVar()
    address= StringVar()
    contact= StringVar()
    password = StringVar()

    Label(data1,text="Enter the detail").pack()
    Label(data1,text="").pack()
    # username registration
    Label(data1,text="First Name").pack()
    Firstname_entry=Entry(data1,text=Firstname)
    Firstname_entry.pack()
    Label(data1, text="Surname").pack()
    Surname_entry = Entry(data1, text=Surname)
    Surname_entry.pack()
    # password registration
    Label(data1, text="Email").pack()
    Email_entry = Entry(data1, text=Email)
    Email_entry.pack()

    Label(data1, text="Address").pack()
    address_entry = Entry(data1, text=address)
    address_entry.pack()

    Label(data1, text="Contact").pack()
    contact_entry = Entry(data1, text=contact)
    contact_entry.pack()

    Label(data1, text="Password").pack()
    password_entry = Entry(data1, text=password)
    password_entry.pack()

    Label(data1, text="").pack()
    Button(data1, text="Register", width=10, height=1,command=register_success).pack()

def login():
    global Email_1
    global password_1
    global Email_entry1
    global password_entry1
    global login1
    login1=Toplevel()
    login1.title("Login")
    login1.geometry("300x250")
    Label(login1, text="Please Enter your username and password")
    Label(login1, text="").pack()

    Email_1=StringVar()
    password_1=StringVar()

    # username registration
    Label(login1, text="Email").pack()
    Email_entry1= Entry(login1, textvariable=Email_1)
    Email_entry1.pack()

    # password registration
    Label(login1, text="Password").pack()
    password_entry1 = Entry(login1, textvariable=password_1)
    password_entry1.pack()

    Button(login1, text="Log in", width=300, height=2, command=login_verify).pack()



btn=Button(data,text="Click Here To Enter",font="Times 20",width=25,padx=10,pady=10,command=open).pack()
conn.commit()
conn.close()
data.mainloop()
