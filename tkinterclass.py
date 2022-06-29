from tkinter import *
from tkinter import messagebox
class myfun:
    def __init__(self,root1):
        frame = Frame(root1)
        frame.pack()
        self.btn = Button(frame, text="okay",command=self.pmsg)
        self.btn.pack()
        self.cancelbtn = Button(frame, text="cancel", command=self.cancel)
        self.cancelbtn.pack()
        self.qbtn = Button(frame, text="exit",command=frame.quit)
        self.qbtn.pack(side = LEFT)
    def cancel(self):
        messagebox.showinfo("title", "canceled")

    def pmsg(self):
        print("clicked")
root=Tk()
obj = myfun(root)
root.mainloop()
