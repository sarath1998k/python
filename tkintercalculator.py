from tkinter import *
import parser
root = Tk()
root.title("Calculator")
display = Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)
#geting the user input
i=0
def getnum(num):
    global i
    display.insert(i,num)
    i+=1
def clearall():
    display.delete(0,END)
def undo():
    str = display.get()
    if len(str):
        new_str=str[:-1]
        clearall()
        display.insert(0,new_str)
    else:
        clearall()
        display.insert(0,"error")
def get_operator(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def calculate():
    entire_str = display.get()
    try:
        a = parser.expr(entire_str).compile()
        result = eval(a)
        clearall()
        display.insert(0,result)
    except EXCEPTION:
        clearall()
        display.insert(0,"error")


#adding button in calculator
Button(root,text="1",command=lambda :getnum(1)).grid(row=2,column=1)
Button(root,text="2",command=lambda :getnum(2)).grid(row=2,column=2)
Button(root,text="3",command=lambda :getnum(3)).grid(row=2,column=3)
Button(root,text="4",command=lambda :getnum(4)).grid(row=3,column=1)
Button(root,text="5",command=lambda :getnum(5)).grid(row=3,column=2)
Button(root,text="6",command=lambda :getnum(6)).grid(row=3,column=3)
Button(root,text="7",command=lambda :getnum(7)).grid(row=4,column=1)
Button(root,text="8",command=lambda :getnum(8)).grid(row=4,column=2)
Button(root,text="9",command=lambda :getnum(9)).grid(row=4,column=3)
Button(root,text="0",command=lambda :getnum(0)).grid(row=5,column=1)
Button(root,text="AC",command=lambda :clearall()).grid(row=5,column=2)
Button(root,text="=",command=lambda :calculate()).grid(row=5,column=3)
Button(root,text="+",command=lambda :get_operator('+')).grid(row=2,column=4)
Button(root,text="-",command=lambda :get_operator('-')).grid(row=3,column=4)
Button(root,text="*",command=lambda :get_operator('*')).grid(row=4,column=4)
Button(root,text="/",command=lambda :get_operator('/')).grid(row=5,column=4)
Button(root,text=")",command=lambda :get_operator(')')).grid(row=6,column=1)
Button(root,text="(",command=lambda :get_operator('(')).grid(row=6,column=2)
Button(root,text="pi",command=lambda :get_operator('*3.14')).grid(row=6,column=3)
Button(root,text="%",command=lambda :get_operator('%')).grid(row=7,column=1)
Button(root,text="exp",command=lambda :get_operator('**')).grid(row=7,column=2)
Button(root,text="^2",command=lambda :get_operator('**2')).grid(row=7,column=3)
Button(root,text="<-",command=lambda :undo()).grid(row=6,column=4)




root.mainloop()