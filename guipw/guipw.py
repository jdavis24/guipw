#! /usr/bin/python

from Tkinter import *

root = Tk()

label_name = Label(root, text='username:')
label_pass = Label(root, text='password:')
entry_name = Entry(root)
entry_pass = Entry(root)

label_name.grid(row=0)
label_pass.grid(row=1)
entry_name.grid(row=0, column=1)
entry_name.grid(row=1, column=1)

root.mainloop()
