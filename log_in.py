from tkinter import *

data=Tk()
data.title("Log in")
data.geometry("500x500")


def delete2():
    data2.destroy()


def login_success():
    global data2
    data2 = Toplevel()
    data2.title("success")
    data2.geometry("150x100")
    Label(data2, text="Log in success").pack()
    Button(data, text="Ok", command=delete2)


def password_not_recognize():
    print("working")


def user_not_found():
    print("working")

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
    username_entry.delete(0,END)
    password_entry.delete(0,END)

    list_of_files= os.listdir()
    if username in list_of_files:
        file1=open(username,"r")
        verify=file1.read().splitlines()
        if password in verify:
            login_success()
        else:
            password_not_recognize()


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
    address = StringVar()
    contact = StringVar()

    Label(data1,text="Enter the detail").pack()
    Label(data1,text="").pack()
    # username registration
    Label(data1,text="Username").pack()
    username_entry=Entry(data1,text=username)
    username_entry.pack()

    # password registration
    Label(data1, text="Password").pack()
    password_entry= Entry(data1, text=password)
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



Label(data,text="Enter your username and password",width=300,height=2,font="time 11").pack()
Label(data,text="").pack()

Button(data,text="Register", width=300, height=2,command=register).pack()
Button(data,text="Log in", width=300, height=2,command=login).pack()

data.mainloop()
