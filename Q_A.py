from tkinter import *
import os
import mysql.connector as mysql
mycon=mysql.connect(host=os.environ.get("DB_SERVER"), user=os.environ.get("DB_USER"),
                      password=os.environ.get("DB_PASS"), database='Egal')
def Q_A(qid):
    def show_Q(label2):
        k=0
        #if(label2.winfo_exists()):
            #label2.destroy()
        for i in li:
            if(k==0):
                k+=1
                continue
            else:
                label2=Label(win,text=i,bg='pink',fg='black',font=('Times New Roman',16,'bold','italic'),height='4',width='48')
                label2.place(x=100,y=140)
    def submit():
        pass
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
    # show Question label
    label2=Label(win,text=li[0],bg='pink',fg='black',font=('Times New Roman',16,'bold','italic'),height='4',width='56')
    label2.place(x=180,y=140)
    var=StringVar()
    ent1=Entry(win,bg='white',fg='black',bd=2,font=('Times New Roman',22,'italic'),width='60',textvariable=var)
    ent1.place(x=60,y=300) # answer wala entry box
    btn1=Button(win,text="END TEST",bg='pink',font=('Times New Roman',18,'italic'),command=submit)
    btn1.place(x=130,y=380)
    btn2=Button(win,text="SUBMIT & NEXT",bg='#0ceb86',font=('Times New Roman',18,'italic'),command=show_Q(label2))
    btn2.place(x=700,y=380)
    win.mainloop()
Q_A('w23')
