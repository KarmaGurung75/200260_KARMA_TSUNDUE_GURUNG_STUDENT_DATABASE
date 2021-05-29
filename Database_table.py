from tkinter import *
import sqlite3

database=Tk()

conn=sqlite3.connect("student_database.db")

c=conn.cursor()

c.execute("""CREATE TABLE student(
      StdID text,
      Firstname text,
      Surname text,
      Date_Of_Birth text,
      Age text,
      Gender text,
      Address text,
      Email text,
      Mobile_number text,
)
""")
print("Table create successfull")


database.mainloop()