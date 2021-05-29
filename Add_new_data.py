import email
from datetime import date
from tkinter import *
import time
from tkinter import ttk
import tkinter.messagebox
import sqlite3

database=Tk()
database.title("Student Database")
database.geometry('1350x750+0+0')
database.config(bg="light green")

# user input data
StdID=StringVar()
Firstname=StringVar()
Surname=StringVar()
Date_Of_Birth=StringVar()
Age=StringVar()
Gender=StringVar()
Address=StringVar()
Email=StringVar()
Mobile_number=StringVar()



# Frame
MainFrame=Frame(database, bg="light blue")
MainFrame.grid()
# Frame For top side
DataFrame1=Frame(MainFrame, bd=1,width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="light blue")
DataFrame1.pack(side=TOP)

# Frame For right and left side
DataFrameLeft=LabelFrame(DataFrame1, bd=1,width=900, height=200, padx=20,pady=6, relief=RIDGE, bg="White", font=("Times New Roman",18,"bold",),text="Add Student Record\n")
DataFrameLeft.pack(side=LEFT)
DataFrameRight=LabelFrame(DataFrame1, bd=1,width=450, height=200, padx=31, pady=8, relief=RIDGE, bg="powder blue",font=("Times New Roman",18,"bold",),text="Student Information\n")
DataFrameRight.pack(side=RIGHT)
# student information
std_info=Text(DataFrameRight,height=13, width=43, bd=1, font=("Times New Roman",12,"bold",))
std_info.grid(row=0,column=0)


# Frame For buttom side
DataFrame2=Frame(MainFrame, bd=1,width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="powder blue")
DataFrame2.pack(side=BOTTOM)

# List Frame
ListFrame=Frame(DataFrame2, bd=2,width=1350, height=150, padx=18, pady=10, relief=RIDGE, bg="blue")
ListFrame.pack(side=TOP)
ButtonFrame=Frame(DataFrame2, bd=2,width=1350, height=40, padx=18, pady=10, relief=RIDGE, bg="powder blue")
ButtonFrame.pack(side=BOTTOM)

#scroll bar for student data display
scrollbar=Scrollbar(ListFrame)
scrollbar.grid(row=0,column=1, sticky='ns')

studentlist=Listbox(ListFrame, width=141, height=7,font=("Times New Roman",12,"bold"),yscrollcommand=scrollbar.set)
studentlist.grid(row=0,column=0,padx=8)
scrollbar.config(command=studentlist.yview)



# user input label and Entry
lblStdID=Label(DataFrameLeft,font=("Times New Roman",14,"bold",),padx=10,pady=10,text="student ID",bg="white")
lblStdID.grid(row=0,column=0,sticky=W)
EntryStdID=Entry(DataFrameLeft,textvariable=StdID,font=("Times New Roman",14,"bold",),bg="white",width=28)
EntryStdID.grid(row=0,column=1)

lblFirst_name=Label(DataFrameLeft,font=("Times New Roman",14,"bold",),padx=10,pady=10,text="First Name",bg="white")
lblFirst_name.grid(row=1,column=0,sticky=W)
EntryFirst_name=Entry(DataFrameLeft,textvariable=Firstname,font=("Times New Roman",14,"bold",),bg="white",width=28)
EntryFirst_name.grid(row=1,column=1)

lblSur_name=Label(DataFrameLeft,font=("Times New Roman",14,"bold",),padx=10,pady=10,text="Surname",bg="white")
lblSur_name.grid(row=2,column=0,sticky=W)
EntrySur_name=Entry(DataFrameLeft,textvariable=Surname,font=("Times New Roman",14,"bold",),bg="white",width=28)
EntrySur_name.grid(row=2,column=1)

lblDate_Of_Birth=Label(DataFrameLeft,font=("Times New Roman",14,"bold",),padx=10,pady=10,text="Date Of Birth",bg="white")
lblDate_Of_Birth.grid(row=3,column=0,sticky=W)
EntryDate_Of_Birth=Entry(DataFrameLeft,textvariable=date,font=("Times New Roman",14,"bold",),bg="white",width=28)
EntryDate_Of_Birth.grid(row=3,column=1)

lblAge=Label(DataFrameLeft,font=("Times New Roman",14,"bold",),padx=10,pady=10,text="Age",bg="white")
lblAge.grid(row=4,column=0,sticky=W)
EntryAge=Entry(DataFrameLeft,textvariable=Age,font=("Times New Roman",14,"bold",),bg="white",width=28)
EntryAge.grid(row=4,column=1)

lblAddress=Label(DataFrameLeft,font=("Times New Roman",14,"bold",),padx=10,pady=10,text="Address",bg="white")
lblAddress.grid(row=5,column=0,sticky=W)
EntryAddress=Entry(DataFrameLeft,textvariable=Address,font=("Times New Roman",14,"bold",),bg="white",width=28)
EntryAddress.grid(row=5,column=1)

lblGender=Label(DataFrameLeft,font=("Times New Roman",14,"bold",),padx=10,pady=10,text="Gender",bg="white")
lblGender.grid(row=6,column=0,sticky=W)
#EntryGender=Entry(DataFrameLeft,textvariable=Gender,font=("Times New Roman",14,"bold",),bg="white",width=28)
#EntryGender.grid(row=6,column=1)
cboGender=ttk.Combobox(DataFrameLeft,textvariable=Gender,state="readonly", font=("Times New Roman",14,"bold",),width=26)
cboGender['value']=('','Male','Female','Other')
cboGender.current(0)
cboGender.grid(row=6,column=1)

lblEmail=Label(DataFrameLeft,font=("Times New Roman",14,"bold",),padx=10,pady=10,text="Email",bg="white")
lblEmail.grid(row=7,column=0,sticky=W)
EntryEmail=Entry(DataFrameLeft,textvariable=email,font=("Times New Roman",14,"bold",),bg="white",width=28)
EntryEmail.grid(row=7,column=1)

lblMobile=Label(DataFrameLeft,font=("Times New Roman",14,"bold",),padx=10,pady=10,text="Mobile No.",bg="white")
lblMobile.grid(row=8,column=0,sticky=W)
EntryMobile=Entry(DataFrameLeft,textvariable=lblMobile,font=("Times New Roman",14,"bold",),bg="white",width=28)
EntryMobile.grid(row=8,column=1)

# function of the data management button

# exit function
def Exit():
    Exit=tkinter.messagebox.askyesno("Quit System", "Do you want to quite")
    if Exit>0:
        database.destroy()
        return

# clear data function
def Clear():
    StdID.set("")
    Firstname.set("")
    Surname.set("")
    Date_Of_Birth.set("")
    Age.set("")
    Gender.set("")
    Address.set("")
    Email.set("")
    Mobile_number.set("")
    std_info.delete("1.0",END)

# Add Data Function
def Add():
    # Create a databases or connect to one
    conn = sqlite3.connect('Student_Database.db')
    # Create cursor
    c = conn.cursor()
    # Insert into table
    c.execute("INSERT INTO Student_Database VALUES (:Firstname, :Surname, :Date_Of_Birth, :Age, :Gender, :Address, :Email,:Mobile_number)", {
        'firstname':Firstname.get(),
        'surname': Surname.get(),
        'Date_of_Birth':Date_Of_Birth.get(),
        'Age':Age.get(),
        'Gender':Gender.get(),
        'Address': Address.get(),
        'Email': Email.get(),
        'Mobile_number': Mobile_number.get()
    })
    # showinfo messagebox
   # messagebox.showinfo("Adresses", "Inserted Successfully")
    conn.commit()
    conn.close()
    # clear the text boxes
    Firstname.delete(0, END)
    Surname.delete(0, END)
    Date_Of_Birth.delete(0, END)
    Age.delete(0, END)
    Gender.delete(0, END)
    Address.delete(0, END)
    Email.delete(0, END)
    Mobile_number.delete(0, END)



# data management button
# Add data button
dataAdd=Button(ButtonFrame, text="Add",font=("Times New Roman",12,"bold"), height=1, width=16, bd=2, padx=8,command=Add)
dataAdd.grid(row=0,column=0)
#Display button
dataDisplay=Button(ButtonFrame, text="Display",font=("Times New Roman",12,"bold"), height=1, width=16, bd=2, padx=8)
dataDisplay.grid(row=0,column=1)
#Clear Data button
dataClear =Button(ButtonFrame, text="Clear",font=("Times New Roman",12,"bold"), height=1, width=16, bd=2, padx=8,command=Clear)
dataClear .grid(row=0,column=2)
#Delete Data button
dataDelete=Button(ButtonFrame, text="Delete",font=("Times New Roman",12,"bold"), height=1, width=16, bd=2, padx=8)
dataDelete.grid(row=0,column=3)
#search data button
dataSearch=Button(ButtonFrame, text="Search",font=("Times New Roman",12,"bold"), height=1, width=16, bd=2, padx=8)
dataSearch.grid(row=0,column=4)
#update data button
dataUpdate=Button(ButtonFrame, text="Update",font=("Times New Roman",12,"bold"), height=1, width=16, bd=2, padx=8)
dataUpdate.grid(row=0,column=5)
#exit data button
Exit=Button(ButtonFrame, text="Exit",font=("Times New Roman",12,"bold"), height=1, width=16, bd=2, padx=8,command=Exit)
Exit.grid(row=0,column=6)

# Database
def query():
    # Create a databases or connect to one
    conn = sqlite3.connect('Student_Database.db')
    # Create cursor
    c = conn.cursor()
    # query of the database
    c.execute("SELECT *, oid FROM Student_Database")
    records = c.fetchall()
   # print(records)
    # Loop through the results
    print_record=''
    for record in records:
        #str(record[6]) added for displaying the id
        print_record += str(record[0]) + ' ' + str(record[1]) + ' '+ '\t' + str(record[6]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()


database.mainloop()