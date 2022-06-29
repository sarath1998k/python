from tkinter import *
root=Tk()
l1 = Label(root,text="username")
m1 = Label(root,text="mobile number")
email = Label(root,text="email")
age1=Label(root,text="age")
l2 = Label(root,text = "password")
l3 = Label(root,text="confirm password")
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)




l1.grid(row=0,column=0)
m1.grid(row=1,column=0)
email.grid(row=2,column=0)
age1.grid(row=3,column=0)
l2.grid(row=4,column=0)
l3.grid(row=5,column=0)


e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)

btn1 = Button(root,text ="Login",fg = "red",bg="blue")
btn2 = Button(root,text ="Cancel",fg = "red",bg="blue")
btn1.grid(row=6,column=0)
btn2.grid(row=6,column=1)


root.mainloop()