from tkinter import *
from tkinter import messagebox
def option():
    def Exit():
        win.destroy()
    def Next():
        if (var.get()==0):
            win.destroy()
            from signup import signup
            signup()
        elif(var.get()==1):
            win.destroy()
            from login import login
            login()
        elif(var.get()==2):
            win.destroy()
            from review_in import review_in
            review_in()
    win=Tk()
    win.maxsize(width=720,height=600)
    win.minsize(width=720,height=600)
    win.title('Egal')
    from PIL import Image, ImageTk
    canvas = Canvas(win,width=1000, height=600)
    canvas.pack(fill= "both", expand=True)
    img= (Image.open("Images/bg5.JPG"))
    resized_image= img.resize((1000,600), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    bg = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    var=IntVar()
    label1=Label(win,text='CHOOSE!!',font=('Times New Roman',24,'bold','italic','underline'),bg='black',fg='white')
    label1.place(x=300,y=16)
    radio1=Radiobutton(win,text='ADD QUESTIONS',value=0,variable=var,font=20,bg='black',fg='white')
    radio1.place(x=250,y=140)
    radio2=Radiobutton(win,text='SOLVE QUESTIONS',value=1,variable=var,font=20,bg='black',fg='white')
    radio2.place(x=250,y=210)
    radio2=Radiobutton(win,text='REVIEW ANSWERS',value=2,variable=var,font=20,bg='black',fg='white')
    radio2.place(x=250,y=280)
    btn1=Button(win,text='EXIT',command=Exit,bg='black',fg='white',font=25)
    btn1.place(x=200,y=370)
    btn2=Button(win,text='NEXT',command=Next,bg='black',fg='white',font=24)
    btn2.place(x=450,y=370)
    win.mainloop()

#option()
