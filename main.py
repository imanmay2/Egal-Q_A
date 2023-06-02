from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from login import login
win=Tk()
def func1():
    if(checkbtn1.get()==1):
        win.destroy()
        login()
    elif(checkbtn1.get()!=1):
        messagebox.showwarning('Warning','To proceed furthur, please hit the checkbox!!')
win.maxsize(width=1000,height=600)
win.minsize(width=1000,height=600)
bg = ImageTk.PhotoImage(file="bg1.PNG")
canvas = Canvas(win,width=1000, height=600)
canvas.pack(fill= "both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")
#win.configure(bg='#03dbfc')
label3=Label(win,text='GUIDELINES FOR USING THE SOFTWARE :',font=('Serif',11,'bold','italic'),bg='#03dbfc')
label3.place(x=50,y=80)
label4=Label(win,text='1. First of all , enter the number of Questions you want to answer.',font=('Serif',11,'bold','italic'),bg='#03dbfc')
label4.place(x=50,y=110)
label5=Label(win,text='2. Secondly, enter the Questions .',font=('Serif',11,'bold','italic'),bg='#03dbfc')
label5.place(x=50,y=130)
label6=Label(win,text='3. After entering all the Questions , You have to enter a Unique name for saving this Questions.',font=('Serif',11,'bold','italic'),bg='#03dbfc')
label6.place(x=50,y=150)
label7=Label(win,text='4. Enter the day and time after which you will be eligible to answer all the Questions.',font=('Serif',11,'bold','italic'),bg='#03dbfc')
label7.place(x=50,y=170)
label8=Label(win,text='5. When all Answer are entered successfully , you can mark your answers to be correct or wrong.',font=('Serif',11,'bold','italic'),bg='#03dbfc')
label8.place(x=50,y=190)
label9=Label(win,text='6. At the end , you will be shown how many are correct and how many are wrong.',font=('Serif',11,'bold','italic'),bg='#03dbfc')
label9.place(x=50,y=210)
label1=Label(win,text='WELCOME TO THE QUESTION ANSWER APPLICATION!!',font=('Times New Roman',24,'bold','italic','underline'),bg='#4520ab')
label1.place(x=100,y=16)
label3=Label(win,text='GUIDELINES FOR USING THE SOFTWARE :',font=('Serif',11,'bold','italic'),bg='#03dbfc')
label3.place(x=50,y=80)
checkbtn1=IntVar()
select=Checkbutton(win,text='I have understood all the Guidelines stated above and I will follow them accordingly',variable=checkbtn1)
select.place(x=250,y=300)
#label2=Label(win,text='How many Questions do you want to practise with??',font=('Normal',16,'italic'),bg='yellow')
#label2.place(x=200,y=120)
#ent1=Entry(win,bg='#d18306',fg='#010f24',bd=2,font=('Normal',16),width=8)
#ent1.place(x=800,y=120)
btn1=Button(win,text='CONTINUE',command=func1,font=40,bg='#f04167')
btn1.place(x=420,y=400)
win.mainloop()
