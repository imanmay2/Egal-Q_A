from tkinter import *
import mysql.connector as mysql
import os
mycon=mysql.connect(host=os.environ.get("DB_SERVER"), user=os.environ.get("DB_USER"),
                      password=os.environ.get("DB_PASS"), database='Egal')
qno=0
corr=0
incorr=0
def review_A(q_id):
    global qno,corr,incorr
    cursor=mycon.cursor()
    tabl=q_id
    def Exit():
        global corr,incorr
        win.destroy()
        from result import result
        result(corr,incorr)
    def correct():
        global qno,corr,incorr
        corr+=1
        qno+=1
        if(qno==len(d)):
            btn2.destroy()
            btn4=Button(win,text="EXIT",bg='#0ceb86',font=('Times New Roman',18,'italic'),command=Exit)
            btn4.place(x=700,y=380)
        else:
            label2.config(text=list(d.keys())[qno])
            label3.config(text=list(d.values())[qno])
        print(corr)
    def incorrect():
        global qno,corr,incorr
        incorr+=1
        qno+=1
        if(qno==len(d)):
            btn1.destroy()
            btn3=Button(win,text="EXIT",bg='pink',font=('Times New Roman',18,'italic'),command=Exit)
            btn3.place(x=130,y=380)
        else:
            label2.config(text=list(d.keys())[qno])
            label3.config(text=list(d.values())[qno])
    #print(corr,incorr)
    # db fetching for Q/A
    d=dict()
    k=-1
    cursor.execute("select * from {}".format(tabl))
    data=cursor.fetchall()
    for i in data:
        k+=1
        if(k>1):
            d[i[0]]=i[1] 
    #print(d)
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
    label1=Label(win,text='REVIEW ANSWERS!!',font=('Times New Roman',24,'bold','italic','underline'),bg='#03d3fc')
    label1.place(x=380,y=16)
    label2=Label(win,text=list(d.keys())[qno],bg='pink',fg='black',font=('Times New Roman',16,'bold','italic'),height='2',width='60')
    label2.place(x=140,y=140)
    label3=Label(win,text=list(d.values())[qno],bg='white',fg='black',font=('Times New Roman',16,'bold','italic'),height='2',width='72')
    label3.place(x=70,y=240)
    btn1=Button(win,text="INCORRECT",bg='pink',font=('Times New Roman',18,'italic'),command=incorrect)
    btn1.place(x=130,y=380)
    btn2=Button(win,text="CORRECT",bg='#0ceb86',font=('Times New Roman',18,'italic'),command=correct)
    btn2.place(x=700,y=380)
    win.mainloop()
#review_A('lesson_1')
