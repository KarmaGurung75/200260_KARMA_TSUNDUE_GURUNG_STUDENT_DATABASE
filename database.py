from tkinter import *
import sqlite3
database= Tk()
database.title("Database Address Book")

# Database

# create a database or connect to one
conn=sqlite3.connect("student_management.db")

# create cursor
# cursor  class is an instance using which you can invoke methods that
# execute SQLite statement, fetch data from the result sets of the quries
c= conn.cursor()

# create table
c.execute("""CREATE TABLE student(
         StdID text,
         Firstname text,
         Surname text,
         Date_Of_Birth  text,
         Age text,
         Gender text,
         Address text,
         Email text,
         Mobile_number integer,
)
""")
print("Table Create successfully")




# commit change
conn.commit()

# close connection
conn.close()

mainloop()