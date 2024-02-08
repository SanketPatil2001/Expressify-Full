from tkinter import *
import tkinter as tk

from PIL import Image, ImageTk


def next_page():
    root.destroy()
    import video


def prev_page():
    root.destroy()
    import voice


root = Tk()
root.geometry("300x300")
root.title("EXPRESSIFY")
root.state('zoomed')


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # avoid garbage collection


image = Image.open('img.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)

l = Label(root, text="Welcome \n to two way ASL translator \n EXPRESSIFY", font='Helvetica 20 bold').place(relx=0.50,
                                                                                                           rely=0.10,
                                                                                                           anchor=N)
l1 = Label(root, text="To print Alphabets one-by-one  \n through video click this button",
           font='Helvetica 14 bold').place(relx=0.68, rely=0.56, anchor=W)
Display = Button(root, height=2,
                 width=20,
                 text="Start Video",
                 command=lambda: next_page()).place(relx=0.90, rely=0.56, anchor=W)

l2 = Label(root, text="For voice and text to ASL \n click this button",
           font='Helvetica 14 bold').place(relx=0.12, rely=0.56, anchor=W)
Display1 = Button(root, height=2,
                  width=20,
                  text="Start Voice",
                  command=lambda: prev_page()).place(relx=0.01, rely=0.56, anchor=W)

mainloop()
