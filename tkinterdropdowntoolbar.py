from tkinter import *
root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)
filemenu = Menu(mymenu)
mymenu.add_cascade(label="File",menu=filemenu)
def myfun():
    print("new project")
filemenu.add_command(label="new project",command=myfun)
def myfun():
    print("new")
filemenu.add_command(label="new ",command=myfun)
filemenu.add_separator()
def myfun():
    print("new scratchfile")
filemenu.add_command(label="new scratchfile",command=myfun)
def myfun():
    print("exit")
filemenu.add_command(label="exit",command=root.quit)



editmenu = Menu(mymenu)
mymenu.add_cascade(label="edit",menu=editmenu)
def myfun():
    print("undo typing")
editmenu.add_command(label="undo typing",command=myfun)
def myfun():
    print("redo ")
editmenu.add_command(label="redo ",command=myfun)
def myfun():
    print("cut")
editmenu.add_separator()
editmenu.add_command(label="cut",command=myfun)
def myfun():
    print("copy")
editmenu.add_command(label="copy",command=myfun)


viewmenu = Menu(mymenu)
mymenu.add_cascade(label="view",menu=viewmenu)
def myfun():
    print("tool window")
viewmenu.add_command(label="tool window",command=myfun)
def myfun():
    print("appearance")
viewmenu.add_command(label="appearance",command=myfun)
viewmenu.add_separator()
def myfun():
    print("quick definition")
viewmenu.add_command(label="quick definition",command=myfun)
def myfun():
    print("quick type definition")
viewmenu.add_command(label="quick type definition",command=myfun)



navigatemenu = Menu(mymenu)
mymenu.add_cascade(label="navigate",menu=navigatemenu)
def myfun():
    print("back")
navigatemenu.add_command(label="back",command=myfun)
def myfun():
    print("forward")
navigatemenu.add_command(label="forward",command=myfun)
navigatemenu.add_separator()
def myfun():
    print("class")
navigatemenu.add_command(label="class",command=myfun)
def myfun():
    print("file")
navigatemenu.add_command(label="file",command=myfun)

codemenu = Menu(mymenu)
mymenu.add_cascade(label="code",menu=codemenu)
def myfun():
    print("over ride")
codemenu.add_command(label="over ride",command=myfun)
def myfun():
    print("implement")
codemenu.add_command(label="implement",command=myfun)
codemenu.add_separator()
def myfun():
    print("code completion")
codemenu.add_command(label="code completion",command=myfun)
def myfun():
    print("surround width")
codemenu.add_command(label="surround width",command=myfun)

#toolbar
toolbar = Frame(root,bg="red")
btn1 = Button(toolbar,text="btn")
btn1.pack(side=LEFT,padx=20,pady=20)
btn2 = Button(toolbar,text="btn")
btn2.pack(side=LEFT,padx=20,pady=20)
btn2 = Button(toolbar,text="btn")
btn2.pack(side=LEFT,padx=20,pady=20)
toolbar.pack(side=TOP,fill=X)
statusbar = Label(root,text="this is status bar",bg="pink",bd=10,relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()