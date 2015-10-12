#! /usr/bin/python3

from tkinter import *

root = Tk()
root.title('gui password test')

# initialize some variables needed below
namevar = StringVar() 
passvar = StringVar()
displayvar = StringVar()

# create username/password labels and text boxes
label_name = Label(root, text='username:')
label_pass = Label(root, text='password:')
entry_name = Entry(root, textvariable=namevar)
entry_pass = Entry(root, textvariable=passvar)
label_name.grid(row=0)
label_pass.grid(row=1)
entry_name.grid(row=0, column=1)
entry_pass.grid(row=1, column=1)

# create a label to display entered values for testing
def display():
	label_display = Label(root, text=namevar, fg='blue', textvariable=namevar)
	label_display.grid(row=3, column=1)
	print (namevar)
	
# create a button to save
button_submit = Button(text='Submit', command=display)
button_submit.grid(row=3, column=0)

root.mainloop()
