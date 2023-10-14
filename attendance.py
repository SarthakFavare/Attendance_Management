from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class attendance:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("Attendance Details")

                #variables
                self.var_attend_id=StringVar()
                self.var_attend_rollno=StringVar()
                self.var_attend_date=StringVar()
                self.var_attend_name=StringVar()
                self.var_attend_subject=StringVar()
                self.var_attend_time=StringVar()
                self.var_attend_attendance=StringVar()


                #image1
                img=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\attendancetop1.jpg")
                img=img.resize((800,200),Image.ANTIALIAS)
                self.photoimg=ImageTk.PhotoImage(img)

                f_lbl=Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=800,height=200)

        #image2
                img1=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\attendancetop2.webp")
                img1=img1.resize((800,200),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=800,y=0,width=800,height=200)
                #bg image
                img3=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\bg.webp")
                img3=img3.resize((1530,710),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=130,width=1530,height=710)

                title__lbl=Label(bg_img,text="Attendance Management System",font=("times new roaman",35,"bold"),bg="white",fg="black")
                title__lbl.place(x=0,y=0,width=1530,height=45)

                main_frame=Frame(bg_img,bd=2)
                main_frame.place(x=10,y=55,width=1500,height=600)

                #left Label Frame

                left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roaman",12,"bold"))
                left_frame.place(x=10,y=10,width=730,height=580)

                img_left=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\kirticollege.png")
                img_left=img_left.resize((730,130),Image.ANTIALIAS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                f_lbl=Label(left_frame,image=self.photoimg_left)
                f_lbl.place(x=5,y=0,width=720,height=130)

                left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
                left_inside_frame.place(x=0,y=135,width=720,height=370)

                #label and entry
                #attendance id
                attendanceId_label=Label(left_inside_frame,text="Attendance Id:",font=("times new roaman",12,"bold"))
                attendanceId_label.grid(row=0,column=0,padx=10,pady=5)

                attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_id,font=("times new roaman",12,"bold"))
                attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

                #Rollno
                rollno_label=Label(left_inside_frame,text="Roll No.:",font=("times new roaman",12,"bold"))
                rollno_label.grid(row=0,column=2,padx=4,pady=8)

                rollno_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_rollno,font=("times new roaman",12,"bold"))
                rollno_entry.grid(row=0,column=3,pady=8)

                #Date
                Date_label=Label(left_inside_frame,text="Date:",font=("times new roaman",12,"bold"))
                Date_label.grid(row=1,column=0)

                Date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_date,font=("times new roaman",12,"bold"))
                Date_entry.grid(row=1,column=1,pady=8)

                #Name
                Name_label=Label(left_inside_frame,text="Name",font=("times new roaman",12,"bold"))
                Name_label.grid(row=1,column=2)

                Name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_name,font=("times new roaman",12,"bold"))
                Name_entry.grid(row=1,column=3,pady=8)

                #Department
                Subject_label=Label(left_inside_frame,text="Subject:",font=("times new roaman",12,"bold"))
                Subject_label.grid(row=2,column=0)

                Subject_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_subject,font=("times new roaman",12,"bold"))
                Subject_entry.grid(row=2,column=1,pady=8)

                #Time
                Time_label=Label(left_inside_frame,text="Time:",font=("times new roaman",12,"bold"))
                Time_label.grid(row=2,column=2)

                Time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_time,font=("times new roaman",12,"bold"))
                Time_entry.grid(row=2,column=3,pady=8)

                #attendance
                attendance_label=Label(left_inside_frame,text="Attendance:",font=("times new roaman",12,"bold"))
                attendance_label.grid(row=3,column=0)

                self.attend_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_attend_attendance,font="comicsansns 11 bold", state="readonly")
                self.attend_status["values"]=("Status","Present","Absent")
                self.attend_status.grid(row=3,column=1,pady=8)
                self.attend_status.current(0)

                #Buttons
                btn_frame=LabelFrame(left_inside_frame ,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=300,width=715,height=100)

                save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roaman",12,"bold"))
                save_btn.grid(row=0,column=0)

                update_btn=Button(btn_frame,text="Export csv",width=17,command=self.exportCsv,font=("times new roaman",12,"bold"))
                update_btn.grid(row=0,column=1)

                delete_btn=Button(btn_frame,text="Update",command=self.write_data,width=17,font=("times new roaman",12,"bold"))
                delete_btn.grid(row=0,column=2)

                restart_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roaman",12,"bold"))
                restart_btn.grid(row=0,column=3)







                #Right Label Frame

                right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roaman",12,"bold"))
                right_frame.place(x=750,y=10,width=720,height=580)
                
                table_frame=LabelFrame(right_frame ,bd=2,relief=RIDGE,text="",font=("times new roaman",12,"bold"))
                table_frame.place(x=5,y=5,width=700,height=455)

                #Scroll bar
                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.attendancereporttable=ttk.Treeview(table_frame,column=("id","rollno.","date","name","subject","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.attendancereporttable.xview)
                scroll_y.config(command=self.attendancereporttable.yview)

                self.attendancereporttable.heading("id",text="Attendance ID")
                self.attendancereporttable.heading("rollno.",text="Roll No.")
                self.attendancereporttable.heading("date",text="Date")
                self.attendancereporttable.heading("name",text="Name")
                self.attendancereporttable.heading("subject",text="Subject")
                self.attendancereporttable.heading("time",text="Time")
                self.attendancereporttable.heading("attendance",text="Attendance")

                self.attendancereporttable["show"]="headings"
                self.attendancereporttable.column("id",width=100)
                self.attendancereporttable.column("rollno.",width=100)
                self.attendancereporttable.column("date",width=100)
                self.attendancereporttable.column("name",width=100)
                self.attendancereporttable.column("subject",width=100)
                self.attendancereporttable.column("time",width=100)
                self.attendancereporttable.column("attendance",width=100)


                self.attendancereporttable.pack(fill=BOTH,expand=1)
                self.attendancereporttable.bind("<ButtonRelease>",self.get_cursor)
        ####fetch data
        def  fetchData(self,rows):
                self.attendancereporttable.delete(*self.attendancereporttable.get_children())
                for i in rows:
                        self.attendancereporttable.insert("",END,values=i)
        #import csv
        def importCsv(self):
                global mydata
                mydata.clear()
                fln=filedialog.askopenfilename(initialdir=os.getcwd,title="Open csv",filetypes=(("CSV File","*.csv"),("All Files",".")),parent=self.root)
                with open(fln) as myfile:
                        csvread=csv.reader(myfile,delimiter=",")
                        for i in csvread:
                                mydata.append(i)
                        self.fetchData(mydata)
        #Export csv
        def exportCsv(self):
                try:
                        if len(mydata)<1:
                                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                                return False
                        fln=filedialog.asksaveasfilename(initialdir=os.getcwd,title="Open csv",filetypes=(("CSV File","*.csv"),("All Files",".")),parent=self.root)
                        with open(fln,mode="w",newline="") as myfile:
                                exp_write=csv.writer(myfile,delimiter=",")
                                for i in mydata:
                                        exp_write.writerow(i)
                                messagebox.showinfo("Data Export", " Your data is Exported to"+os.path.basename(fln)+"successfully")
                except Exception as es:
                        messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

        def get_cursor(self,event=""):
                cursor_row=self.attendancereporttable.focus()
                content=self.attendancereporttable.item(cursor_row)
                rows=content['values']
                self.var_attend_id.set(rows[0])
                self.var_attend_rollno.set(rows[1])
                self.var_attend_date.set(rows[2])
                self.var_attend_name.set(rows[3])
                self.var_attend_subject.set(rows[4])
                self.var_attend_time.set(rows[5])
                self.var_attend_attendance.set(rows[6])
        
        def write_data(self):
                with open("sarthak.csv","a",newline="") as fobj:
                        wt=csv.writer(fobj,delimiter=',')
                        id=self.var_attend_id.get()
                        rollno=self.var_attend_rollno.get()
                        date=self.var_attend_date.get()
                        name=self.var_attend_name.get()
                        subject=self.var_attend_subject.get()
                        time=self.var_attend_time.get()
                        attend=self.var_attend_attendance.get()
                        wt.writerow([id,rollno,date,name,subject,time,attend])
                        messagebox.showinfo("Success","Student details successfully Updated", parent=self.root)
                fobj.close()
        
        def reset_data(self):
                self.var_attend_id.set("")
                self.var_attend_rollno.set("")
                self.var_attend_date.set("")
                self.var_attend_name.set("")
                self.var_attend_subject.set("")
                self.var_attend_time.set("")
                self.var_attend_attendance.set("")










                


if __name__ =="__main__":
    root=Tk()
    obj=attendance(root)
    root.mainloop()
