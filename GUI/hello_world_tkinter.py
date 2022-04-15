from tkinter import *

root = Tk()

# title of window
root.title("First Window")

# size of window
root.geometry('350x200')


# menu
# menu = Menu(root)
# item = Menu(menu)
# item.add_command(label='New')
# item.add_command(label='About')
# item.add_cascade(label='File', menu=item)
# root.config(menu=menu)

menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
item.add_command(label='About')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)


# lable
lbl = Label(root, text="Enter Name")
lbl.grid(column=3, row=0)  # For setting the position of element

# inout
name = Entry(root, width=25)
name.grid(column=3, row=2)

# event


def clicked():
    display_msg = Label(root, text="welcome, "+name.get())
    display_msg.grid(column=3, row=6)


# button
btn1 = Button(root, text="Button", fg="red", command=clicked)
btn1.grid(column=6, row=2)

# canvas
canvas =Canvas(root,bg='red')

# display window
root.mainloop()
