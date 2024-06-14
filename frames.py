from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.iconbitmap("images/image.jpg")

frames = LabelFrame(root,text="My frame",padx=20,pady=20,relief=SUNKEN)
frames.pack()

b1 = Button(frames,text="Button_1",padx=5,pady=5)
b2 = Button(frames,text="Button_2",padx=5,pady=5)

b1.grid(row=0,column=0,pady=2)
b2.grid(row=1,column=0)


root.mainloop()
