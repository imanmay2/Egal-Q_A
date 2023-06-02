from tkinter import *
def login():
    from PIL import Image, ImageTk
    win=Tk()
    win.maxsize(width=1000,height=600)
    win.minsize(width=1000,height=600)
    bg = ImageTk.PhotoImage(file="bg1.PNG")
    canvas = Canvas(win,width=1000, height=600)
    canvas.pack(fill= "both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    win.mainloop()

login()
