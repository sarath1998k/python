from gtts import gTTS
import os
from tkinter import *
root=Tk()
canvas=Canvas(root,height=400,width=400)
canvas.pack()
def texttospeech():
    text=entry.get()
    output = gTTS(text=text, lang="en", slow=False)
    output.save('output.mp3')
    os.system("start output.mp3")


entry=Entry(root)
canvas.create_window(200,160,window=entry)
button=Button(text="start",command=texttospeech)
canvas.create_window(200,230,window=button)


root.mainloop()