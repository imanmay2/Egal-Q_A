from tkinter import *
import mysql.connector as mysql
from add_Q import add_Q
import os
def signup():
    mycon=mysql.connect(host=os.environ.get("DB_SERVER"), user=os.environ.get("DB_USER"),
                      password=os.environ.get("DB_PASS"), database='Egal')
    def func1():
        uid=ent7.get()
        cursor=mycon.cursor()
        #with open('T_name','w') as f1:
            #f1.write(ent7.get())
        cursor.execute('create table {}(name TEXT);'.format(uid))
        cursor.execute("insert into {}(name) values('{}');".format(uid,str(ent1.get())))
        mycon.commit()
        cursor.execute("insert into {}(name) values('{}');".format(uid,str(ent2.get())))
        mycon.commit()
        win.destroy()
        add_Q(uid)
    from PIL import Image, ImageTk
    win=Tk()
    win.maxsize(width=600,height=600)
    win.minsize(width=600,height=600)
    win.title('Egal')
    bg = ImageTk.PhotoImage(file="Images/bg1.PNG")
    canvas = Canvas(win,width=600, height=600)
    canvas.pack(fill= "both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    label1=Label(win,text='SIGNUP!!',font=('Times New Roman',24,'bold','italic','underline'),bg='#95c5f5')
    label1.place(x=260,y=16)
    label2=Label(win,text='ENTER YOUR NAME : ',font=('Times New Roman',16,'bold','italic'),bg='#b011fa')
    label2.place(x=60,y=100)
    ent1=Entry(win,bg='white',fg='black',bd=2,font=('Times New Roman',16,'bold','italic'))
    ent1.place(x=280,y=100)
    label3=Label(win,text='HOW MANY QUESTIONS DO YOU WANT TO INSERT : ',font=('Times New Roman',10,'bold','italic'),bg='#b011fa')
    label3.place(x=60,y=200)
    ent2=Entry(win,bg='white',fg='black',bd=2,font=('Times New Roman',10,'bold','italic'))
    ent2.place(x=380,y=200)
    label7=Label(win,text='ENTER A UNIQUE Q_ADDRESS : ',font=('Times New Roman',12,'bold','italic'),bg='#b011fa')
    label7.place(x=60,y=300)
    ent7=Entry(win,bg='white',fg='black',bd=2,font=('Times New Roman',12,'bold','italic'))
    ent7.place(x=310,y=300)
    btn1=Button(win,text='START',bg='white',fg='black',font=('Times New Roman',20,'bold','italic'),command=func1)
    btn1.place(x=240,y=420)
    label5=Label(win,text='**After hitting the start button ,user will start adding Question ,afterwards he/she will answer.',font=('Times New Roman',8,'bold'),bg='#b011fa')
    label5.place(x=40,y=570)
    win.mainloop()
signup()
