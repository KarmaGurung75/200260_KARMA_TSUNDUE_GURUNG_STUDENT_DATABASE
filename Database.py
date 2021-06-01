from tkinter import *
from tkinter import ttk

import sqlite3
from tkinter import messagebox
import time;
import datetime


def std_data():
    database = Tk()
    database.title("Student Database")
    database.geometry('1350x750+0+0')
    database.config(bg="light gray")

    # Create a databases
    conn = sqlite3.connect('project_database3.db')
    # Create cursor
    c = conn.cursor()

    ''''#create table
    c.execute(""" CREATE TABLE student_data2(
          StdID text,
          Firstname text,
          Surname text,
          Date_Of_Birth text,
          Age text,
          Address text,
          Gender text,
          Email text,
          Mobile_number text
    ) """)
    print("create table success")
    '''

    # user input data
    StdID = StringVar()
    Firstname = StringVar()
    Surname = StringVar()
    Date_Of_Birth = StringVar()
    Age = StringVar()
    Gender = StringVar()
    Address = StringVar()
    Email = StringVar()
    Mobile_number = StringVar()
    DateIssued = StringVar()

    # Frame
    MainFrame = Frame(database, bg="light blue")
    MainFrame.grid()
    # Frame For top side
    DataFrame1 = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="light blue")
    DataFrame1.pack(side=TOP)

    # Frame For right and left side
    DataFrameLeft = LabelFrame(DataFrame1, bd=1, width=1000, height=200, padx=20, pady=6, relief=RIDGE, bg="White",
                               font=("Times New Roman", 18, "bold",), text="Add Student Record\n")
    DataFrameLeft.pack(side=LEFT)
    DataFrameRight = LabelFrame(DataFrame1, bd=1, width=450, height=200, padx=31, pady=8, relief=RIDGE,
                                bg="powder blue", font=("Times New Roman", 18, "bold",), text="Student Information\n")
    DataFrameRight.pack(side=RIGHT)
    # student information
    std_info = Text(DataFrameRight, height=15, width=50, bd=1, font=("Times New Roman", 12, "bold",))
    std_info.grid()


    # Frame For button side
    DataFrame2 = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="powder blue")
    DataFrame2.pack(side=BOTTOM)

    # List Frame
    ButtonFrame = Frame(DataFrame2, bd=2, width=1350, height=40, padx=18, pady=10, relief=RIDGE, bg="powder blue")
    ButtonFrame.pack(side=BOTTOM)


    # user input label and Entry
    lblStdID = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="student ID",
                     bg="white")
    lblStdID.grid(row=0, column=0, sticky=W)
    EntryStdID = Entry(DataFrameLeft, textvariable=StdID, font=("Times New Roman", 14, "bold",), bg="white", width=28)
    EntryStdID.grid(row=0, column=1)

    lblFirst_name = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="First Name",
                          bg="white")
    lblFirst_name.grid(row=1, column=0, sticky=W)
    EntryFirst_name = Entry(DataFrameLeft, textvariable=Firstname, font=("Times New Roman", 14, "bold",), bg="white",
                            width=28)
    EntryFirst_name.grid(row=1, column=1)

    lblSur_name = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Surname",
                        bg="white")
    lblSur_name.grid(row=2, column=0, sticky=W)
    EntrySur_name = Entry(DataFrameLeft, textvariable=Surname, font=("Times New Roman", 14, "bold",), bg="white",
                          width=28)
    EntrySur_name.grid(row=2, column=1)

    lblDate_Of_Birth = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10,
                             text="Date Of Birth", bg="white")
    lblDate_Of_Birth.grid(row=3, column=0, sticky=W)
    EntryDate_Of_Birth = Entry(DataFrameLeft, textvariable=Date_Of_Birth, font=("Times New Roman", 14, "bold",),
                               bg="white", width=28)
    EntryDate_Of_Birth.grid(row=3, column=1)

    lblAge = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Age", bg="white")
    lblAge.grid(row=4, column=0, sticky=W)
    EntryAge = Entry(DataFrameLeft, textvariable=Age, font=("Times New Roman", 14, "bold",), bg="white", width=28)
    EntryAge.grid(row=4, column=1)

    lblAddress = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Address",
                       bg="white")
    lblAddress.grid(row=5, column=0, sticky=W)
    EntryAddress = Entry(DataFrameLeft, textvariable=Address, font=("Times New Roman", 14, "bold",), bg="white",
                         width=28)
    EntryAddress.grid(row=5, column=1)

    lblGender = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Gender", bg="white")
    lblGender.grid(row=6, column=0, sticky=W)
    # EntryGender=Entry(DataFrameLeft,textvariable=Gender,font=("Times New Roman",14,"bold",),bg="white",width=28)
    # EntryGender.grid(row=6,column=1)
    cboGender = ttk.Combobox(DataFrameLeft, textvariable=Gender, state="readonly",
                             font=("Times New Roman", 14, "bold",), width=26)
    cboGender['value'] = ('', 'Male', 'Female', 'Other')
    cboGender.current(0)
    cboGender.grid(row=6, column=1)

    lblEmail = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Email", bg="white")
    lblEmail.grid(row=7, column=0, sticky=W)
    EntryEmail = Entry(DataFrameLeft, textvariable=Email, font=("Times New Roman", 14, "bold",), bg="white", width=28)
    EntryEmail.grid(row=7, column=1)

    lblMobile = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Mobile No.",
                      bg="white")
    lblMobile.grid(row=8, column=0, sticky=W)
    EntryMobile = Entry(DataFrameLeft, textvariable=Mobile_number, font=("Times New Roman", 14, "bold",), bg="white",
                        width=28)
    EntryMobile.grid(row=8, column=1)

    # function of the data management button

    # exit function
    def Exit():
        Exit = messagebox.askyesno("Quit System", "Do you want to quite")
        if Exit > 0:
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
        std_info.delete("1.0", END)

        EntryStdID.delete(0, END)
        EntryFirst_name.delete(0, END)
        EntrySur_name.delete(0, END)
        EntryDate_Of_Birth.delete(0, END)
        EntryAge.delete(0, END)
        cboGender.delete(0, END)
        EntryAddress.delete(0, END)
        EntryEmail.delete(0, END)
        EntryMobile.delete(0, END)

    # Add Data Function
    def Add():
        # Create a databases or connect to one
        conn = sqlite3.connect('project_database3.db')
        # Create cursor
        c = conn.cursor()
        # Insert into table
        c.execute(
            "INSERT INTO student_data2 VALUES (:StdID, :Firstname, :Surname, :Date_Of_Birth, :Age, :Address,:Gender, :Email,:Mobile_number)",
            {
                'StdID': EntryStdID.get(),
                'Firstname': EntryFirst_name.get(),
                'Surname': EntrySur_name.get(),
                'Date_Of_Birth': EntryDate_Of_Birth.get(),
                'Age': EntryAge.get(),
                'Address': EntryAddress.get(),
                'Gender': cboGender.get(),
                'Email': EntryEmail.get(),
                'Mobile_number': EntryMobile.get()
            })

        messagebox.showinfo("student_data2", "Inserted Successfully")
        conn.commit()
        conn.close()
        # clear the text boxes
        '''EntryStdID.delete(0, END)
        EntryFirst_name.delete(0, END)
        EntrySur_name.delete(0, END)
        EntryDate_Of_Birth.delete(0, END)
        EntryAge.delete(0, END)
        cboGender.delete(0, END)
        EntryAddress.delete(0, END)
        EntryEmail.delete(0, END)
        EntryMobile.delete(0, END)'''

        DateIssued.set(time.strftime("%d/%m/%Y"))
        std_info.insert(END, '============Student Detail=====================' + "\n")
        std_info.insert(END, 'Student ID:\t\t' + EntryStdID.get() + '\t\t' + DateIssued.get() + "\n")
        std_info.insert(END, '============================================' + "\n")
        std_info.insert(END, 'First Name:\t\t'+ '\t\t' + EntryFirst_name.get() + "\n")
        std_info.insert(END, 'Surname:\t\t'+ '\t\t' +  EntrySur_name.get() + "\n")
        std_info.insert(END, 'Date_Of_Birth:\t\t'+ '\t\t' + EntryDate_Of_Birth.get() + "\n")
        std_info.insert(END, 'Age:\t\t'+ '\t\t' +  EntryAge.get() +  "\n")
        std_info.insert(END, 'Gender:\t\t'+ '\t\t' +  cboGender.get() + "\n")
        std_info.insert(END, 'Address:\t\t' + '\t\t'+ EntryAddress.get() + "\n")
        std_info.insert(END, 'Email:\t\t'+ '\t\t'  + EntryEmail.get()  + "\n")
        std_info.insert(END, 'Mobile:\t\t'+ '\t\t'  + EntryMobile.get() + "\n")
        std_info.insert(END, '==============================================' + "\n")

    # Displaying Data
    def Display():
        global display
        display = Tk()
        display.title('Display')
        display.geometry('500x500')

        # databases connect to one project-database3 for getting data
        conn = sqlite3.connect('project_database3.db')
        # Create cursor
        c = conn.cursor()
        # query of the database
        c.execute("SELECT *, StdID FROM student_data2")
        records = c.fetchall()

        # Loop through the results
        print_record = ''
        print_record += str("student ID") +' \t'+ str("First Name") +' \t'+ str("Surname") +' \t\t'+ str(
            "Gender""\t\t'\n")
        for record in records:

            print_record +=str(record[0]) + ' \t\t' + str(record[1])  + '\t\t' + \
                           str(record[2])+' \t\t'  + str(record[6]) +'\t\t' + "\n"
        query_label = Label(display, text=print_record,font=("Times New Roman", 10, "bold",))
        query_label.grid(row=1, column=0)

        conn.commit()
        conn.close()

    def Save():
        # Create a databases or connect to one
        conn = sqlite3.connect('project_database3.db')
        # Create cursor
        c = conn.cursor()
        record_id = StdID.get()
        c.execute(""" UPDATE student_data2 SET
                 StdID = :EntryStdID,
                 Firstname = :EntryFirstname,
                 Surname = :EntrySurname,
                 Date_Of_Birth = :EntryDate_Of_Birth,
                 Age = :EntryAge,
                 Address = :EntryAddress,
                 cboGender=:cboGender,
                 Email=:EntryEmail,
                 Mobile_number =: EntryMobile_number
                 WHERE oid = :oid""",
                  {'EntryStdID': EntryStdID.get(),
                   'EntryFirstname': EntryFirst_name.get(),
                   'EntrySurname': EntrySur_name.get(),
                   'EntryDate_Of_Birth': EntryDate_Of_Birth.get(),
                   'EntryAge':EntryAge.get(),
                   'EntryAddress':EntryAddress.get(),
                   'cboGender': cboGender.get(),
                   'EntryEmail': EntryEmail.get(),
                   'EntryMobile_number': EntryMobile.get(),
                   'oid': record_id
                        }
            )


        conn.commit()
        conn.close()


    def Update():
        from tkinter import ttk
        # Create a databases or connect to one
        conn = sqlite3.connect('project_database3.db')
        # Create cursor
        c = conn.cursor()
        record_id = EntryStdID.get()
        # query of the database
        c.execute("SELECT * FROM student_data2 WHERE StdID=" + record_id)
        records = c.fetchall()
        # print(records)

        # Create textbox labels
        global EntryStdID1
        global EntryFirstname1
        global EntrySur_name1
        global EntryDate_Of_Birth1
        global EntryAge1
        global EntryAddress1
        global cboGender1
        global EntryEmail1
        global EntryMobile1

        # label and entry for data to update
        lblStdID1 = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="student ID",
                         bg="white")
        lblStdID1.grid(row=0, column=0, sticky=W)
        EntryStdID1= Entry(DataFrameLeft, textvariable=StdID, font=("Times New Roman", 14, "bold",), bg="white",
                           width=28)
        EntryStdID1.grid(row=0, column=1)

        lblFirst_name1 = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="First Name",
                              bg="white")
        lblFirst_name1.grid(row=1, column=0, sticky=W)
        EntryFirst_name1 = Entry(DataFrameLeft, textvariable=Firstname, font=("Times New Roman", 14, "bold",),
                                bg="white",
                                width=28)
        EntryFirst_name1.grid(row=1, column=1)

        lblSur_name1 = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Surname",
                            bg="white")
        lblSur_name1.grid(row=2, column=0, sticky=W)
        EntrySur_name1 = Entry(DataFrameLeft, textvariable=Surname, font=("Times New Roman", 14, "bold",), bg="white",
                              width=28)
        EntrySur_name1.grid(row=2, column=1)

        lblDate_Of_Birth1 = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10,
                                 text="Date Of Birth", bg="white")
        lblDate_Of_Birth1.grid(row=3, column=0, sticky=W)
        EntryDate_Of_Birth1 = Entry(DataFrameLeft, textvariable=Date_Of_Birth, font=("Times New Roman", 14, "bold",),
                                   bg="white", width=28)
        EntryDate_Of_Birth1.grid(row=3, column=1)

        lblAge1 = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Age", bg="white")
        lblAge1.grid(row=4, column=0, sticky=W)
        EntryAge1 = Entry(DataFrameLeft, textvariable=Age, font=("Times New Roman", 14, "bold",), bg="white", width=28)
        EntryAge1.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Address",
                           bg="white")
        lblAddress1.grid(row=5, column=0, sticky=W)
        EntryAddress1 = Entry(DataFrameLeft, textvariable=Address, font=("Times New Roman", 14, "bold",), bg="white",
                             width=28)
        EntryAddress1.grid(row=5, column=1)

        lblGender1 = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Gender",
                          bg="white")
        lblGender1.grid(row=6, column=0, sticky=W)
        cboGender1 = ttk.Combobox(DataFrameLeft, textvariable=Gender, state="readonly",
                                 font=("Times New Roman", 14, "bold",), width=26)
        cboGender1['value'] = ('', 'Male', 'Female', 'Other')
        cboGender1.current(0)
        cboGender1.grid(row=6, column=1)

        lblEmail1 = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Email",
                         bg="white")
        lblEmail1.grid(row=7, column=0, sticky=W)
        EntryEmail1 = Entry(DataFrameLeft, textvariable=Email, font=("Times New Roman", 14, "bold",), bg="white",
                           width=28)
        EntryEmail1.grid(row=7, column=1)

        lblMobile1 = Label(DataFrameLeft, font=("Times New Roman", 14, "bold",), padx=10, pady=10, text="Mobile No.",
                          bg="white")
        lblMobile1.grid(row=8, column=0, sticky=W)
        EntryMobile1 = Entry(DataFrameLeft, textvariable=Mobile_number, font=("Times New Roman", 14, "bold",),
                            bg="white",
                            width=28)
        EntryMobile1.grid(row=8, column=1)

        EntryStdID.delete(0, END)
        EntryFirst_name.delete(0, END)
        EntrySur_name.delete(0, END)
        EntryDate_Of_Birth.delete(0, END)
        EntryAge.delete(0, END)
        EntryAddress.delete(0, END)
        cboGender.delete(0, END)
        EntryEmail.delete(0, END)
        EntryMobile.delete(0, END)

        # loop through the results
        for record in records:
            EntryStdID.insert(0, record[0])
            EntryFirst_name.insert(0, record[1])
            EntrySur_name.insert(0, record[2])
            EntryDate_Of_Birth.insert(0, record[3])
            EntryAge.insert(0, record[4])
            EntryAddress.insert(0, record[5])
            cboGender.insert(0, record[6])
            EntryEmail.insert(0, record[7])
            EntryMobile.insert(0, record[8])

        edit_btn = Button(ButtonFrame, text=" SAVE ",font=("Times New Roman", 12, "bold"), command=Save)
        edit_btn.grid(row=0, column=5)

    def Delete():
        # connect data base to project_database3
        conn = sqlite3.connect('project_database3.db')
        # create cursor
        c = conn.cursor()
        # delete a record
        c.execute("DELETE from student_data2 WHERE StdID = " + EntryStdID.get())
        print('Deleted Successfully')
        # query of the database
        c.execute("SELECT *, StdID FROM student_data2")


        conn.commit()
        conn.close()


    #data management button
    # Add data button
    dataAdd = Button(ButtonFrame, text="Add", font=("Times New Roman", 12, "bold"), height=1, width=16, bd=2, padx=8,
                     command=Add)
    dataAdd.grid(row=0, column=0)
    # Display button
    dataDisplay = Button(ButtonFrame, text="Display", font=("Times New Roman", 12, "bold"), height=1, width=16, bd=2,
                         padx=8,command=Display)
    dataDisplay.grid(row=0, column=1)
    # Clear Data button
    dataClear = Button(ButtonFrame, text="Clear", font=("Times New Roman", 12, "bold"), height=1, width=16, bd=2,
                       padx=8, command=Clear)
    dataClear.grid(row=0, column=2)
    # Delete Data button
    dataDelete = Button(ButtonFrame, text="Delete", font=("Times New Roman", 12, "bold"), height=1, width=16, bd=2,
                        padx=8,command=Delete)
    dataDelete.grid(row=0, column=3)
    # update data button

    dataUpdate = Button(ButtonFrame, text=" Update ",font=("Times New Roman", 12, "bold"), height=1, width=16, bd=2,
                       padx=8,command=Update)
    dataUpdate.grid(row=0,column=4)
    #dataSave = Button(ButtonFrame, text=" Save ", font=("Times New Roman", 12, "bold"), height=1, width=16, bd=2,
                    #  padx=8, command=Save)
    #dataSave.grid(row=0, column=5)
    # exit data button
    Exit = Button(ButtonFrame, text="Exit", font=("Times New Roman", 12, "bold"), height=1, width=16, bd=2, padx=8,
                  command=Exit)
    Exit.grid(row=0, column=6)

    # commit change
    conn.commit()
    # close connection
    conn.close()
    database.mainloop()