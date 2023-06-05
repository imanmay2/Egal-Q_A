from tkinter import *
import os
import mysql.connector as mysql
mycon=mysql.connect(host=os.environ.get("DB_SERVER"), user=os.environ.get("DB_USER"),
                      password=os.environ.get("DB_PASS"), database='Egal')
def Q_A(qid):
    tabl=qid
    win=Tk()
    win.title('Egal')
    win.maxsize(width='1000',height='500')
    win.minsize(width='1000',height='500')
    from PIL import Image, ImageTk
    canvas = Canvas(win,width=1000, height=600)
    canvas.pack(fill= "both", expand=True)
    img= (Image.open("Images/bg6.JPG"))
    resized_image= img.resize((1000,600), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    bg = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    label1=Label(win,text='SOLVE QUESTIONS!!',font=('Times New Roman',24,'bold','italic','underline'),bg='#03d3fc')
    label1.place(x=350,y=16)
    cursor=mycon.cursor()
    cursor.execute("select * from {}".format(tabl))
    data=cursor.fetchall()
    k=0
    li=list()
    for i in data:
        k=k+1
        if(k>2):
            li.append(i[0])
    #print(li)

        
    win.mainloop()
Q_A('w23')
