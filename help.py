from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2

class help:
    def __init__(self,root):
            self.root=root
            self.root.geometry("1530x790+0+0")
            self.root.title("Help")



            title__lbl=Label(self.root,text="Help Desk",font=("times new roaman",35,"bold"),bg="white",fg="red")
            title__lbl.place(x=0,y=0,width=1530,height=45)

            img_top=Image.open (r"studentimages\helpdesk.jpg")
            img_top=img_top.resize((1530,720),Image.ANTIALIAS)
            self.photoimg_top=ImageTk.PhotoImage(img_top)

            f_lbl=Label(self.root,image=self.photoimg_top)
            f_lbl.place(x=0,y=55,width=1530,height=720)

            help_label=Label(f_lbl,text="Email id : sarthakfavare@gmail.com",font=("times new roman",20,"bold"),fg="blue")
            help_label.place(x=600,y=100)


if __name__ =="__main__":
    root=Tk()
    obj=help(root)
    root.mainloop()