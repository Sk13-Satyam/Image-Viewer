from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.iconbitmap("images/image.jpg")

img1 = ImageTk.PhotoImage(Image.open("images/0.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
img6 = ImageTk.PhotoImage(Image.open("images/5.jpg"))
img7 = ImageTk.PhotoImage(Image.open("images/6.jpg"))
img8 = ImageTk.PhotoImage(Image.open("images/7.jpg"))

img_list = [img1, img2, img3, img4, img5, img6, img7, img8]

staus = Label(
    root, text="Image 1 of " + str(len(img_list)), bd=2, relief=SUNKEN, anchor=E
)

label_img = Label(image=img1)
label_img.grid(row=0, column=0, columnspan=3)


def next(number):
    global label_img
    global button_back
    global button_next

    label_img.grid_forget()
    label_img = Label(image=img_list[number - 1])
    button_next = Button(root, text=">>", command=lambda: next(number + 1))
    button_back = Button(root, text="<<", command=lambda: back(number - 1))

    if number == 8:
        button_next = Button(root, text=">>", state=DISABLED)

    label_img.grid(row=0, column=0, columnspan=3)
    button_back.grid(
        row=1,
        column=0,
    )
    button_next.grid(row=1, column=2)

    staus = Label(
        root,
        text="Image " + str(number) + " of " + str(len(img_list)),
        bd=2,
        relief=SUNKEN,
        anchor=E,
    )
    staus.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(number):
    global label_img
    global back
    global next

    label_img.grid_forget()
    label_img = Label(image=img_list[number - 1])
    button_next = Button(root, text=">>", command=lambda: next(number + 1))
    button_back = Button(root, text="<<", command=lambda: back(number - 1))

    if number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    label_img.grid(row=0, column=0, columnspan=3)
    button_back.grid(
        row=1,
        column=0,
    )
    button_next.grid(row=1, column=2)
    staus = Label(
        root,
        text="Image " + str(number) + " of " + str(len(img_list)),
        bd=2,
        relief=SUNKEN,
        anchor=E,
    )
    staus.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", command=back, state=DISABLED, pady=11)
button_exit = Button(root, text="Exit", command=root.quit, pady=10)
button_next = Button(root, text=">>", command=lambda: next(2), pady=10)

button_exit.grid(row=1, column=1)
button_back.grid(
    row=1,
    column=0,
)
button_next.grid(row=1, column=2, pady=10)
staus.grid(row=2, column=0, columnspan=3, sticky=W + E)


root.mainloop()
