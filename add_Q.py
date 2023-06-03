from tkinter import *
def add_Q():
    win=Tk()
    win.maxsize(width=1000,height=500)
    win.minsize(width=1000,height=500)
    from PIL import Image, ImageTk
    canvas = Canvas(win,width=1000, height=600)
    canvas.pack(fill= "both", expand=True)
    img= (Image.open("Images/bg5.JPG"))
    resized_image= img.resize((1000,600), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    bg = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    win.mainloop()

