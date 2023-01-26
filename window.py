import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("The Big Phonebook")
window.geometry("600x400")
window.resizable(0, 0)

import sqlite3
from operator import contains
import array

conn = sqlite3.connect('phonedata.db')
conn.execute('CREATE TABLE IF NOT EXISTS data(number TEXT, realname TEXT, grade TEXT, nickname TEXT, address TEXT, description TEXT)')
c = conn.cursor()

tabController = ttk.Notebook(window)
  
tab1 = ttk.Frame(tabController)
tab2 = ttk.Frame(tabController)
tab3 = ttk.Frame(tabController)
tab4 = ttk.Frame(tabController)
tab5 = ttk.Frame(tabController)
  
tabController.add(tab1, text =' Search Number ')
tabController.add(tab2, text =' Search Nickname ')
tabController.add(tab3, text =' Search Realname ')
tabController.add(tab4, text =' Input Data ')
tabController.add(tab5, text =' Delete Data ')
tabController.pack(expand=1, fill="both")
#===============================================================#
ttk.Label(tab1, text="Phone Number : ").grid(row=0, column=0, padx=50, pady=30)
var8 = StringVar()
entry1 = ttk.Entry(tab1, width=50, textvariable=var8).grid(row=0, column=1, pady=5, padx=2)
def search_number():
    if var8.get() == "":
        messagebox.showwarning("The Big Phonebook", "Please input number!")
    else:
        c.execute("SELECT * FROM data WHERE number=?", (var8.get(),))
        Label(tab1, text="Result : ").grid(row=2, column=1, pady=20)
        for row in c.fetchall():
            tempdata = row
            for list in tempdata:
                            ttk.Label(tab1, text=list).grid( column=1)
ttk.Button(tab1, text="Search", width="30", command=search_number).grid(row=1, column=1, padx=30)
#===============================================================#
ttk.Label(tab4, text="Phone Number : ").grid(row=0, column=0, padx=50, pady=10)
var1 = StringVar()
entry1 = ttk.Entry(tab4, width=50, textvariable=var1).grid(row=0, column=1, pady=5, padx=2)
ttk.Label(tab4, text="Nick Name : ").grid(row=1, column=0, padx=50, pady=10)
var2 = StringVar()
entry1 = ttk.Entry(tab4, width=50, textvariable=var2).grid(row=1, column=1, pady=5, padx=2)
ttk.Label(tab4, text="Real Name : ").grid(row=2, column=0, padx=50, pady=10)
var3 = StringVar()
entry1 = ttk.Entry(tab4, width=50, textvariable=var3).grid(row=2, column=1, pady=5, padx=2)
ttk.Label(tab4, text="Address : ").grid(row=3, column=0, padx=50, pady=10)
var4 = StringVar()
entry1 = ttk.Entry(tab4, width=50, textvariable=var4).grid(row=3, column=1, pady=5, padx=2)
ttk.Label(tab4, text="Grade : ").grid(row=4, column=0, padx=50, pady=10)
var5 = StringVar()
entry1 = ttk.Entry(tab4, width=50, textvariable=var5).grid(row=4, column=1, pady=5, padx=2)
ttk.Label(tab4, text="Description : ").grid(row=5, column=0, padx=50, pady=10)
var6 = StringVar()
entry1 = ttk.Entry(tab4, width=50, textvariable=var6).grid(row=5, column=1, pady=5, padx=2)
def input_number():
    if var1.get() == "":
        messagebox.showwarning("The Big Phonebook", "Please input number!")
    elif var2.get() == "":
        messagebox.showwarning("The Big Phonebook", "Please input nickname!")
    elif var3.get() == "":
        messagebox.showwarning("The Big Phonebook", "Please input realname!")
    elif var4.get() == "":
        messagebox.showwarning("The Big Phonebook", "Please input address!")
    elif var5.get() == "":
        messagebox.showwarning("The Big Phonebook", "Please input grade!")
    elif var6.get() == "":
        messagebox.showwarning("The Big Phonebook", "Please input description!")
    else:
        try:
            c.execute("INSERT INTO data(number, realname, grade, nickname, address, description) VALUES(?, ?, ?, ?, ?, ?)", [var1.get(), var3.get(), var5.get(), var2.get(), var4.get(), var6.get()])
            conn.commit()
            messagebox.showinfo("The Big Phonebook", "Successfullly save data")
        except:
            messagebox.showerror("The Big Phonebook", "Error! Cannot save data")
ttk.Button(tab4, text="Input Data", width="30", command=input_number).grid(row=6, column=1, padx=30, pady=30)
#===============================================================#
ttk.Label(tab2, text="Nick Name : ").grid(row=0, column=0, padx=50, pady=30)
var9 = StringVar()
entry1 = ttk.Entry(tab2, width=50, textvariable=var9).grid(row=0, column=1, pady=5, padx=2)
def search_nickname():
    if var9.get() == "":
        messagebox.showwarning("The Big Phonebook", "Please input nickname!")
    else:
        c.execute("SELECT * FROM data WHERE nickname=?", (var9.get(),))
        Label(tab2, text="Result : ").grid(row=2, column=1, pady=20)
        for row in c.fetchall():
            tempdata = row
            for list in tempdata:
                            ttk.Label(tab2, text=list).grid( column=1)
ttk.Button(tab2, text="Search", width="30", command=search_nickname).grid(row=1, column=1, padx=30)
#===============================================================#
ttk.Label(tab3, text="Real Name : ").grid(row=0, column=0, padx=50, pady=30)
var10 = StringVar()
entry1 = ttk.Entry(tab3, width=50, textvariable=var10).grid(row=0, column=1, pady=5, padx=2)
def search_realname():
    if var10.get() == "":
        messagebox.showwarning("The Big Phonebook", "Please input realname!")
    else:
        c.execute("SELECT * FROM data WHERE realname=?", (var10.get(),))
        Label(tab3, text="Result : ").grid(row=2, column=1, pady=20)
        for row in c.fetchall():
            tempdata = row
            for list in tempdata:
                            ttk.Label(tab3, text=list).grid( column=1)
ttk.Button(tab3, text="Search", width="30", command=search_realname).grid(row=1, column=1, padx=30)
#===============================================================#
ttk.Label(tab5, text="Phone Number : ").grid(row=0, column=0, padx=50, pady=30)
var11 = StringVar()
entry1 = ttk.Entry(tab5, width=50, textvariable=var11).grid(row=0, column=1, pady=5, padx=2)
def delete_number():
    if var11.get() == "":
        messagebox.showwarning("The Big Phonebook", "Please input number!")
    else:
        try:
            c.execute("DELETE FROM data WHERE number = ?", (var11.get(),))
            messagebox.showinfo("The Big Phonebook", "Successfully delete data")
        except:
            messagebox.showerror("The Big Phonebook", "Error! cannot delete data")
ttk.Button(tab5, text="Delete", width="30", command=delete_number).grid(row=1, column=1, padx=30)

window.mainloop()
conn.commit()
c.close()
conn.close()