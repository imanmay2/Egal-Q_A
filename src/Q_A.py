from tkinter import *
import os
import mysql.connector as mysql
mycon=mysql.connect(host='localhost', user='root',
                      password='Manmay@1234', database='Egal')

qno=0
ans_li={}
def Q_A(qid):
    cursor=mycon.cursor()
    global qno,ans_li
    def show_Q():
        global qno,ans_li
        if(qno==len(li)-1):
            btn2.config(text='SUBMIT',command=end)
            ans=ent1.get()
            ans_li[li[qno]]=ans
            print(ans_li)
            cursor.execute("UPDATE {} set Answer='{}' where Question='{}'".format(tabl,ans,li[qno]))
            mycon.commit()
        else:
            qno+=1
            label2.config(text=li[qno])
            ans=ent1.get()
            ans_li[li[qno-1]]=ans
            print(ans_li)
            ent1.delete(0,END)
            ent1.insert(0,ans_li[li[qno]] if(len(list(ans_li.keys()))>qno) else '')
            cursor.execute("UPDATE {} set Answer='{}' where Question='{}'".format(tabl,ans,li[qno-1]))
            mycon.commit()
        #ent1.delete(0,END)
    def prev_Q():
        global qno,ans_li
        qno-=1
        ent1.delete(0,END)
        ent1.insert(0,ans_li[li[qno]])
        label2.config(text=li[qno])
    def end():
        from options import option
        win.destroy()
        option()
    tabl=qid
    win=Tk()
    win.title('Egal')
    win.maxsize(width='1000',height='500')
    win.minsize(width='1000',height='500')
    from PIL import Image, ImageTk
    canvas = Canvas(win,width=1000, height=600)
    canvas.pack(fill= "both", expand=True)
    img= (Image.open("Images/bg6.JPG"))
    resized_image= img.resize((1000,600), Image.LANCZOS)
    new_image= ImageTk.PhotoImage(resized_image)
    bg = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    label1=Label(win,text='SOLVE QUESTIONS!!',font=('Times New Roman',24,'bold','italic','underline'),bg='#03d3fc')
    label1.place(x=350,y=16)
    
    cursor.execute("select * from {}".format(tabl))
    data=cursor.fetchall()
    k=0
    li=list()
    for i in data:
        k=k+1
        if(k>2):
            li.append(i[0])
    print(li)
    # show Question label
    label2=Label(win,text=li[qno],bg='pink',fg='black',font=('Times New Roman',16,'bold','italic'),height='4',width='56')
    label2.place(x=180,y=140)
    var=StringVar()
    ent1=Entry(win,bg='white',fg='black',bd=2,font=('Times New Roman',22,'italic'),width='60',textvariable=var)
    ent1.place(x=60,y=300) # answer wala entry box
    btn1=Button(win,text="PREVIOUS",bg='pink',font=('Times New Roman',18,'italic'),command=prev_Q)
    btn1.place(x=130,y=380)
    btn2=Button(win,text="SAVE & NEXT",bg='#0ceb86',font=('Times New Roman',18,'italic'),command=lambda: show_Q())
    btn2.place(x=700,y=380)
    win.mainloop()
#Q_A('test123')
