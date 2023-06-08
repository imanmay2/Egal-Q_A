from tkinter import *
import os
import mysql.connector as mysql
from tkinter import messagebox

mycon=mysql.connect(host=os.environ.get("DB_SERVER"), user=os.environ.get("DB_USER"),
                      password=os.environ.get("DB_PASS"), database='Egal')

count_Q=0
def add_Q(uid,no_of_ques):
    global count_Q
    def comp():
        win.destroy()
        from options import option
        option()
    def add():
        global count_Q
        count_Q+=1
        cursor=mycon.cursor(buffered=True)
        #with open('T_name') as f1:
            #tabl=f1.read()
        tabl=uid
        if(ent2.get()!=''):
            cursor.execute("insert into {} (Question) values('{}')".format(tabl,str(ent2.get())))
            mycon.commit()
        else:
            messagebox.showwarning("Warning","Question can't be blank!!!!")
        #cursor.execute("select * from {}".format(tabl))
        #f=cursor.rowcount
        #if(f==int(count)+int(ct[0])):
        if(count_Q==int(no_of_ques)):
            messagebox.showwarning("Warning",f"You have already added {count_Q} Questions")
        ent2.delete(0,END)
    win=Tk()
    win.maxsize(width=1000,height=500)
    win.minsize(width=1000,height=500)
    win.title('Egal')
    from PIL import Image, ImageTk
    canvas = Canvas(win,width=1000, height=600)
    canvas.pack(fill= "both", expand=True)
    img= (Image.open("Images/bg6.JPG"))
    resized_image= img.resize((1000,600), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    bg = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    label1=Label(win,text='ADD QUESTIONS!!',font=('Times New Roman',24,'bold','italic','underline'),bg='#03d3fc')
    label1.place(x=380,y=16)
    label2=Label(win,text='Please enter the Questions , you want to add!!',font=('Times New Roman',18,'italic'),bg='#03fc8c')
    label2.place(x=280,y=160)
    var=StringVar()
    ent2=Entry(win,bg='pink',fg='black',bd=2,font=('Times New Roman',20,'italic'),width='60',textvariable=var)
    ent2.place(x=85,y=240)
    btn1=Button(win,text="COMPLETE",bg='pink',font=('Times New Roman',18,'italic'),command=comp)
    btn1.place(x=130,y=380)
    btn2=Button(win,text="ADD",bg='#0ceb86',font=('Times New Roman',18,'italic'),command=add)
    btn2.place(x=800,y=380)
    label5=Label(win,text="**NOTE You can't edit or retrieve the Questions after clicking in the ADD button!!",font=('Times New Roman',9,'bold','italic'),bg='pink')
    label5.place(x=300,y=470)
    win.mainloop()


