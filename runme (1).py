#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter
from PIL import ImageTk,Image
top=tkinter.Tk()
top.geometry("360x360")
def ok():
    top.destroy()
    import chess1
def ok1():
    top.destroy()
    import gui
    
filename = ImageTk.PhotoImage(Image.open('image.jpg' ))

background_label = tkinter.Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
b=tkinter.Button(background_label,command=ok,bd=2,width=15,text="TWO PLAYER")
b.place(x=120,y=330)
b1=tkinter.Button(background_label,bd=2,width=15,text="PLAY WITH AI",command=ok1)
b1.place(x=120,y=300)
top.mainloop()





