import mysql.connector as mysql
import os
from tkinter import *
from Q_A import Q_A
mycon=mysql.connect(host='localhost', user='root',
                      password='Manmay@1234', database='Egal')

def login():
    def func1():
        qid=ent2.get()
        win.destroy()
        Q_A(qid)
    from PIL import Image, ImageTk
    win=Tk()
    win.maxsize(width=600,height=600)
    win.minsize(width=600,height=600)
    win.title('Egal')
    bg = ImageTk.PhotoImage(file="Images/bg1.PNG")
    canvas = Canvas(win,width=600, height=600)
    canvas.pack(fill= "both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    label1=Label(win,text='LOGIN!!',font=('Times New Roman',24,'bold','italic','underline'),bg='#95c5f5')
    label1.place(x=260,y=16)
    label2=Label(win,text='ENTER YOUR NAME : ',font=('Times New Roman',16,'bold','italic'),bg='#b011fa')
    label2.place(x=60,y=100)
    ent1=Entry(win,bg='white',fg='black',bd=2,font=('Times New Roman',16,'bold','italic'))
    ent1.place(x=280,y=100)
    label3=Label(win,text='ENTER THE Q_ADDRESS : ',font=('Times New Roman',14,'bold','italic'),bg='#b011fa')
    label3.place(x=60,y=200)
    ent2=Entry(win,bg='white',fg='black',bd=2,font=('Times New Roman',16,'bold','italic'))
    ent2.place(x=300,y=200)
    btn1=Button(win,text='START',bg='white',fg='black',font=('Times New Roman',20,'bold','italic'),command=func1)
    btn1.place(x=240,y=360)
    label5=Label(win,text='**After hitting the start button ,Questions will appear on the screen , which he/she have to answer.',font=('Times New Roman',8,'bold'),bg='#b011fa')
    label5.place(x=40,y=570)
    win.mainloop()

