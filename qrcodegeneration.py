from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root = Tk()
def generate():
    link_name=name_entry.get()
    link=link_entry.get()
    file_name=link_name+".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,400,window=image_label)

canvas=Canvas(root,height=600,width=400)
canvas.pack()
label1=Label(root,text="qrcode generator",fg="blue",font=("Ariel",30))
canvas.create_window(200,50,window=label1)
name_label=Label(root,text="link name",font=20)
link_label=Label(root,text="link",font=20)
canvas.create_window(150,100,window=name_label)
canvas.create_window(150,130,window=link_label)
name_entry=Entry(root)
link_entry=Entry(root)
canvas.create_window(300,100,window=name_entry)
canvas.create_window(300,130,window=link_entry)
button=Button(root,text="generate QR code",command=generate)
canvas.create_window(200,180,window=button)

root.mainloop()
