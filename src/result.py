from tkinter import *
def result(corr,incorr):
    def func1():
        win.destroy()
        from options import option
        option()
    from PIL import Image, ImageTk
    win=Tk()
    win.maxsize(width=600,height=600)
    win.minsize(width=600,height=600)
    win.title('Egal')
    bg = ImageTk.PhotoImage(file="Images/bg1.PNG")
    canvas = Canvas(win,width=600, height=600)
    canvas.pack(fill= "both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    label1=Label(win,text='RESULT!!',font=('Times New Roman',24,'bold','italic','underline'),bg='#95c5f5')
    label1.place(x=250,y=16)
    label2=Label(win,text=f'Total Questions : {incorr+corr}',font=('Times New Roman',18,'italic'),bg='#95c5f5')
    label2.place(x=200,y=120)
    label3=Label(win,text=f'Correct Responses : {corr}',font=('Times New Roman',18,'italic'),bg='#95c5f5')
    label3.place(x=200,y=180)
    label4=Label(win,text=f'Incorrect Responses : {incorr}',font=('Times New Roman',18,'italic'),bg='#95c5f5')
    label4.place(x=200,y=240)
    label5=Label(win,text=f"Overall : {round((corr*100)/(corr+incorr))} %",font=('Times New Roman',18,'italic'),bg='#95c5f5')
    label5.place(x=200,y=300)
    btn1=Button(win,text='END',bg='white',fg='black',font=('Times New Roman',20,'bold','italic'),command=func1)
    btn1.place(x=260,y=400)
    win.mainloop()
#result(4,2)
