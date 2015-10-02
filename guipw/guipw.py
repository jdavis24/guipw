#! /usr/bin/python

from Tkinter import *

root = Tk()
root.title('gui password test')

label_name = Label(root, text='username:')
label_pass = Label(root, text='password:')
entry_name = Entry(root)#, textvariable=namevar)
entry_pass = Entry(root)#, textvariable=passvar)

label_name.grid(row=0)
label_pass.grid(row=1)
entry_name.grid(row=0, column=1)
entry_pass.grid(row=1, column=1)

# label_displayname = Label(root, textvariable=namevar)
# label_display.grid(row=2)

root.mainloop()
