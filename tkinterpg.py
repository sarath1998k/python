from tkinter import *
from tkinter import messagebox
root=Tk()
label1 = Label(root,text="hello sarath")
label1.pack()
def fun():
    messagebox.showwarning("warning", "this is warning box")  # warning box

btn = Button(root,command = fun,text ="OK",fg = "red",bg="blue")
btn.pack()
messagebox.showinfo("title","this information box")  #info box
messagebox.showwarning("warning","this is warning box")#warning box
messagebox.askokcancel("ok cancel","are you ready")
messagebox.showerror("error","this is error box")#error box
messagebox.askretrycancel("retry cancel","are you ready")



root.mainloop()