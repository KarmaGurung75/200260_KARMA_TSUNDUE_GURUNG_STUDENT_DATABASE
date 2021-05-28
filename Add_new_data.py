from tkinter import *
import sqlite3
welcome=Tk()
welcome.geometry("500x500")

conn=sqlite3.connect("student_data.db")

c=conn.cursor()






conn.commit()
conn.close()
welcome.mainloop()