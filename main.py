from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from numpy import imag
from student import student
from train import train
from face_recognition import Face_Recognition
import os
from help import help
from attendance import attendance

class Face_Recognition_System:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("Face Recognition system")

#image1
                img=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\start image.png")
                img=img.resize((500,130),Image.ANTIALIAS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=500,height=130)

#image2
                img1=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\logokirti.jpeg")
                img1=img1.resize((500,130),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=500,y=0,width=500,height=130)
#image3
                img2=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\kirticollege.png")
                img2=img2.resize((650,130),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                f_lbl=Label(self.root,image=self.photoimg2)
                f_lbl.place(x=1000,y=0,width=550,height=130)

#bg image
                img3=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\bg.webp")
                img3=img3.resize((1530,710),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=130,width=1530,height=710)

                title__lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM BY SARTHAK",font=("times new roaman",35,"bold"),bg="blue",fg="lightblue")
                title__lbl.place(x=0,y=0,width=1530,height=45)

#studentbutton
                img4=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\details.webp")
                img4=img4.resize((220,220),Image.ANTIALIAS)
                self.photoimg4=ImageTk.PhotoImage(img4)
                b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
                b1.place(x=200,y=100,width=220,height=220)
                b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roaman",15,"bold"),bg="blue",fg="lightblue")
                b1_1.place(x=200,y=300,width=220,height=40)


#attendance button
                img6=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\attend.jpg")
                img6=img6.resize((220,220),Image.ANTIALIAS)
                self.photoimg6=ImageTk.PhotoImage(img6)
                b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
                b1.place(x=500,y=100,width=220,height=220)
                b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roaman",15,"bold"),bg="blue",fg="lightblue")
                b1_1.place(x=500,y=300,width=220,height=40)

#helpdesk button
                img7=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\helpcontact.jpg")
                img7=img7.resize((220,220),Image.ANTIALIAS)
                self.photoimg7=ImageTk.PhotoImage(img7)
                b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.helpdesk)
                b1.place(x=800,y=100,width=220,height=220)
                b1_1=Button(bg_img,text="Helpdesk",cursor="hand2",font=("times new roaman",15,"bold"),bg="blue",fg="lightblue",command=self.helpdesk)
                b1_1.place(x=800,y=300,width=220,height=40)

#Train button
                img8=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\train_button.webp")
                img8=img8.resize((220,220),Image.ANTIALIAS)
                self.photoimg8=ImageTk.PhotoImage(img8)
                b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
                b1.place(x=200,y=380,width=220,height=220)
                b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roaman",15,"bold"),bg="blue",fg="lightblue")
                b1_1.place(x=200,y=580,width=220,height=40)

#Photos button
                img9=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\image_button.jpg")
                img9=img9.resize((220,220),Image.ANTIALIAS)
                self.photoimg9=ImageTk.PhotoImage(img9)
                b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
                b1.place(x=500,y=380,width=220,height=220)
                b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roaman",15,"bold"),bg="blue",fg="lightblue")
                b1_1.place(x=500,y=580,width=220,height=40)

#Exit button
                img10=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\exit_button.jpeg")
                img10=img10.resize((220,220),Image.ANTIALIAS)
                self.photoimg10=ImageTk.PhotoImage(img10)
                b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.iExit)
                b1.place(x=800,y=380,width=220,height=220)
                b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roaman",15,"bold"),bg="blue",fg="lightblue")
                b1_1.place(x=800,y=580,width=220,height=40)

        def open_img(self):
                os.startfile("data")

        def iExit(self):
                msg_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',icon='warning')
                if msg_box == 'yes':
                        root.destroy()
                else:
                       messagebox.showinfo('Return', 'You will now return to the application screen')




        def student_details(self):
                self.new_window=Toplevel(self.root)
                self.app=student(self.new_window)


        def train_data(self):
                self.new_window=Toplevel(self.root)
                self.app=train(self.new_window)

        def Face_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition(self.new_window)
        
        def attendance_data(self):
                self.new_window=Toplevel(self.root)
                self.app=attendance(self.new_window)

        def helpdesk(self):
                self.new_window=Toplevel(self.root)
                self.app=help(self.new_window)







if __name__ =="__main__":
        root=Tk()
        obj=Face_Recognition_System(root)
        root.mainloop()

