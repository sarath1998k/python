from tkinter import *
root = Tk()
canvas = Canvas(root,height=100,width=200)
canvas.pack()
newline=canvas.create_line(10,30,200,100,fill="red")
newarc=canvas.create_oval(0,10,200,200,fill="green")
root.mainloop()