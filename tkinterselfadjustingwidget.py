from tkinter import *
root = Tk()
label1 = Label(root,text="hello sarath",bg ="red",fg="blue")
label1.pack(fill=X)
label2 = Label(root,text="hello sarath",bg ="red",fg="blue")
label2.pack(side = LEFT ,fill=X)
def fun():
    print("click here")

btn = Button(root,command= fun ,text ="OK",fg = "red",bg="blue")
btn.pack(side = RIGHT,fill = Y)

root.mainloop()