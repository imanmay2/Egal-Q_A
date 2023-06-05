from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from login import login
from signup import signup
def option():
    def Exit():
        win.destroy()
    def Next():
        if var.get()==0:
            win.destroy()
            signup()
        elif(var.get()==1):
            win.destroy()
            login()
    win=Tk()
    win.maxsize(width=800,height=600)
    win.minsize(width=800,height=600)
    win.title('Egal')
    canvas = Canvas(win,width=1000, height=600)
    canvas.pack(fill= "both", expand=True)
    img= (Image.open("Images/bg5.JPG"))
    resized_image= img.resize((1000,600), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    bg = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    var=IntVar()
    radio1=Radiobutton(win,text='ADD QUESTIONS',value=0,variable=var,font=20,bg='black',fg='white')
    radio1.place(x=250,y=140)
    radio2=Radiobutton(win,text='SOLVE QUESTIONS',value=1,variable=var,font=20,bg='black',fg='white')
    radio2.place(x=250,y=210)
    btn1=Button(win,text='EXIT',command=Exit,bg='black',fg='white',font=25)
    btn1.place(x=200,y=300)
    btn2=Button(win,text='NEXT',command=Next,bg='black',fg='white',font=24)
    btn2.place(x=450,y=295)
    win.mainloop()

