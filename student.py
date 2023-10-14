

from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x790+0+0")
                self.root.title("Student Details")

#variabales
                self.var_dept=StringVar()
                self.var_year=StringVar()
                self.var_sem=StringVar()
                self.var_studentid=StringVar()
                self.var_studentname=StringVar()
                self.var_studentdiv=StringVar()
                self.var_studentrollno=StringVar()
                self.var_studentemail=StringVar()
                self.var_studentphone=StringVar()


        #image1
                img=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\studentstudying.png")
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
                img2=img2.resize((550,130),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                f_lbl=Label(self.root,image=self.photoimg2)
                f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
                img3=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\bg.webp")
                img3=img3.resize((1530,710),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=130,width=1530,height=710)

                title__lbl=Label(bg_img,text="Student Management System",font=("times new roaman",35,"bold"),bg="white",fg="black")
                title__lbl.place(x=0,y=0,width=1530,height=45)

                main_frame=Frame(bg_img,bd=2)
                main_frame.place(x=10,y=55,width=1500,height=600)

        #left Label Frame

                left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roaman",12,"bold"))
                left_frame.place(x=10,y=10,width=730,height=580)

                img_left=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\kirticollege.png")
                img_left=img_left.resize((530,130),Image.ANTIALIAS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                f_lbl=Label(left_frame,image=self.photoimg_left)
                f_lbl.place(x=5,y=0,width=720,height=130)
        #current course       
                current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roaman",12,"bold"))
                current_course_frame.place(x=5,y=135,width=720,height=150)

                dept_label=Label(current_course_frame,text="Department",font=("times new roaman",12,"bold"))
                dept_label.grid(row=0,column=0,padx=10)

                dept_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("times new roaman",12,"bold"), state="readonly",width=20)
                dept_combo["values"]=("Select Department","CS","IT")
                dept_combo.current(0)
                dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Year
                year_label=Label(current_course_frame,text="Year",font=("times new roaman",12,"bold"))
                year_label.grid(row=0,column=2,padx=10)

                year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roaman",12,"bold"), state="readonly",width=20)
                year_combo["values"]=("Select Year","FY","SY","TY")
                year_combo.current(0)
                year_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Semester       

                sem_label=Label(current_course_frame,text="Semester",font=("times new roaman",12,"bold"))
                sem_label.grid(row=1,column=0,padx=10)

                sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roaman",12,"bold"), state="readonly",width=20)
                sem_combo["values"]=("Select Semester","Sem I","Sem II","Sem III","Sem IV","Sem V","Sem VI")
                sem_combo.current(0)
                sem_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # student information       
                class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Student Information",font=("times new roaman",12,"bold"))
                class_student_frame.place(x=5,y=250,width=720,height=300)
                studentId_label=Label(class_student_frame,text="Student Id:",font=("times new roaman",12,"bold"))
                studentId_label.grid(row=0,column=0,padx=10,pady=5)

                studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentid,width=20,font=("times new roaman",12,"bold"))
                studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
                studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roaman",12,"bold"))
                studentname_label.grid(row=0,column=2,padx=10,pady=5)

                studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentname,width=20,font=("times new roaman",12,"bold"))
                studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #student division
                studentdiv_label=Label(class_student_frame,text="Student Division:",font=("times new roaman",12,"bold"))
                studentdiv_label.grid(row=1,column=0,padx=10,pady=5)

                studentdiv_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentdiv,width=20,font=("times new roaman",12,"bold"))
                studentdiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #student roll no.
                studentrollno_label=Label(class_student_frame,text="Student Rollno.:",font=("times new roaman",12,"bold"))
                studentrollno_label.grid(row=1,column=2,padx=10,pady=5)

                studentrollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentrollno,width=20,font=("times new roaman",12,"bold"))
                studentrollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #student Email
                studentmail_label=Label(class_student_frame,text="Student Email:",font=("times new roaman",12,"bold"))
                studentmail_label.grid(row=2,column=0,padx=10,pady=5)

                studentmail_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentemail,width=20,font=("times new roaman",12,"bold"))
                studentmail_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #student phoneno.
                studentphone_label=Label(class_student_frame,text="Student Phoneno.:",font=("times new roaman",12,"bold"))
                studentphone_label.grid(row=2,column=2,padx=10,pady=5)

                studentphone_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentphone,width=20,font=("times new roaman",12,"bold"))
                studentphone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Radio Button
                self.var_radio1=StringVar()
                radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
                radiobtn1.grid(row=6,column=0)

                radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
                radiobtn2.grid(row=6,column=1)

        #Button Frame
                btn_frame=LabelFrame(class_student_frame ,bd=2,relief=RIDGE,text="",font=("times new roaman",12,"bold"))
                btn_frame.place(x=0,y=150,width=715,height=100)

                save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roaman",12,"bold"))
                save_btn.grid(row=0,column=0)

                update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roaman",12,"bold"))
                update_btn.grid(row=0,column=1)

                delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roaman",12,"bold"))
                delete_btn.grid(row=0,column=2)

                restart_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roaman",12,"bold"))
                restart_btn.grid(row=0,column=3)

                takephoto_btn=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=18,font=("times new roaman",12,"bold"))
                takephoto_btn.grid(row=1,column=0)

                updatephoto_btn=Button(btn_frame,text="Update Photo Sample",width=18,font=("times new roaman",12,"bold"))
                updatephoto_btn.grid(row=1,column=1)


        #Right Label Frame

                right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roaman",12,"bold"))
                right_frame.place(x=750,y=10,width=720,height=580)

                img_right=Image.open (r"C:\Users\Sarthak\Desktop\Face_Recognition_System\studentimages\logokirti.jpeg")
                img_right=img_right.resize((720,130),Image.ANTIALIAS)
                self.photoimg_right=ImageTk.PhotoImage(img_right)

                f_lbl=Label(right_frame,image=self.photoimg_right)
                f_lbl.place(x=5,y=0,width=720,height=130)

        #Serach system
                search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search systems",font=("times new roaman",12,"bold"))
                search_frame.place(x=5,y=135,width=710,height=70)

                search_label=Label(search_frame,text="Search By:",font=("times new roaman",12,"bold"))
                search_label.grid(row=0,column=0,padx=10,pady=5)   

                search_combo=ttk.Combobox(search_frame,font=("times new roaman",12,"bold"), state="readonly",width=15)
                search_combo["values"]=("Select","Roll No.","Student Name")
                search_combo.current(0)
                search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

                search_entry=ttk.Entry(search_frame,width=15,font=("times new roaman",12,"bold"))
                search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


                search_btn=Button(search_frame,text="Search",width=12,font=("times new roaman",12,"bold"))
                search_btn.grid(row=0,column=3,padx=4)

                showall_btn=Button(search_frame,text="Show All",width=12,font=("times new roaman",12,"bold"))
                showall_btn.grid(row=0,column=4,padx=4)

        #Table 
                table_frame=Frame(right_frame,bd=2,relief=RIDGE)
                table_frame.place(x=5,y=210,width=710,height=350)

                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
                self.student_table=ttk.Treeview(table_frame,column=("dept","year","sem","id","name","div","rollno.","email","phoneno.","photo" ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)


                self.student_table.heading("dept",text="Department")
                self.student_table.heading("year",text="Year")
                self.student_table.heading("sem",text="Semester")
                self.student_table.heading("id",text="Student Id")
                self.student_table.heading("name",text="Student Name")
                self.student_table.heading("div",text="Student Division")
                self.student_table.heading("rollno.",text="Student Rollno.")
                self.student_table.heading("email",text="Student Email")
                self.student_table.heading("phoneno.",text="Student Phoneno.")
                self.student_table.heading("photo",text="Photo Sample Status")
                self.student_table["show"]="headings"

                self.student_table.column("dept",width=100)
                self.student_table.column("year",width=100)
                self.student_table.column("sem",width=100)
                self.student_table.column("id",width=100)
                self.student_table.column("name",width=100)
                self.student_table.column("div",width=100)
                self.student_table.column("rollno.",width=100)
                self.student_table.column("email",width=100)
                self.student_table.column("phoneno.",width=100)
                self.student_table.column("photo",width=150)

                self.student_table.pack(fill=BOTH,expand=1)

                
                self.student_table.bind("<ButtonRelease>",self.get_cursor)
                self.fetch_data()

###function
        def add_data(self):
                if self.var_dept.get()=="Select Department" or self.var_studentname.get()=="" or self.var_studentid.get()=="":
                        messagebox.showerror("Error","Ener the Data",parent=self.root)
                else :
                        try:
                                conn=mysql.connector.connect(host="localhost",username="root",password="sarthak@007",database="face_recogniser")
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dept.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_studentid.get(),
                                                                                                                self.var_studentname.get(),
                                                                                                                self.var_studentdiv.get(),
                                                                                                                self.var_studentrollno.get(),
                                                                                                                self.var_studentemail.get(),
                                                                                                                self.var_studentphone.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                
                                                                                                                ))
                                                                        
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","Student details has been inserted successfully",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

#fetch data
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="sarthak@007",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                data=my_cursor.fetchall()

                if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                                self.student_table.insert("",END,values=i)
                        conn.commit()
    
                conn.close
##get cursor
        def get_cursor(self,event=""):
                cursor_focus=self.student_table.focus
                content=self.student_table.item(cursor_focus)
                data=content['values']
                
                self.var_dept.set(data[0])
                self.var_year.set(data[1])
                self.var_sem.set(data[2])
                self.var_studentid.set(data[3])
                self.var_studentname.set(data[4])
                self.var_studentdiv.set(data[5])
                self.var_studentrollno.set(data[6])
                self.var_studentemail.set(data[7])
                self.var_studentphone.set(data[8])
                self.var_radio1.set(data[9])

#update function
        def update_data(self):
                if self.var_dept.get()=="Select Department" or self.var_studentname.get()=="" or self.var_studentid.get()=="":
                        messagebox.showerror("Error","Enter the Data",parent=self.root)

                else:
                        try:
                                Update=messagebox.askyesno("Update","Do you want to update this student details", parent=self.root)
                                if Update>0:
                                        conn=mysql.connector.connect(host="localhost",username="root",password="sarthak@007",database="face_recogniser")
                                        my_cursor=conn.cursor()
                                        my_cursor.execute("update student set dept=%s,year=%s,sem=%s,studentname=%s,studentdiv=%s,studentrollno=%s,studentemail=%s,studentphone=%s,photosample=%s where studentid=%s",(
                                                                                                                self.var_dept.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_studentname.get(),
                                                                                                                self.var_studentdiv.get(),
                                                                                                                self.var_studentrollno.get(),
                                                                                                                self.var_studentemail.get(),
                                                                                                                self.var_studentphone.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_studentid.get(),
                                                                                                         ))
                                else:
                                        if not Update:
                                                return
                                messagebox.showinfo("Success","Student details successfully Updated", parent=self.root)
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                
                        except Exception as es :
                                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)     

#delete function
        def delete_data(self):
                if self.var_studentid.get()=="":
                        messagebox.showerror("Error","Student id must be required",parent=self.root)             
                else:
                        try:
                                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student ",parent=self.root)
                                if delete>0:
                                        conn=mysql.connector.connect(host="localhost",username="root",password="sarthak@007",database="face_recogniser")
                                        my_cursor=conn.cursor()

                                        sql="delete from student where studentid=%s"
                                        val=(self.var_studentid.get(),)
                                        my_cursor.execute(sql,val)
                                else:
                                        if not delete:
                                                return
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Delete","Successfully deleted student details",parent = self.root)
                        except Exception as es :
                                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                                
#reset
        def reset_data(self):
                self.var_dept.set("Select Department")
                self.var_year.set("Select Year")
                self.var_sem.set("Select Sem")
                self.var_studentid.set("")
                self.var_studentname.set("")
                self.var_studentdiv.set("")
                self.var_studentrollno.set("")
                self.var_studentemail.set("")
                self.var_studentphone.set("")
                self.var_radio1.set("")

###Generate Data Set or Take Photo Sample

        def generate_dataset(self):
                if self.var_dept.get()=="Select Department" or self.var_studentname.get()=="" or self.var_studentid.get()=="":
                        messagebox.showerror("Error","Enter the Data",parent=self.root)

                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",username="root",password="sarthak@007",database="face_recogniser")
                                my_cursor=conn.cursor()
                                my_cursor.execute("select * from student")
                                myresult=my_cursor.fetchall()
                                id=0
                                for x in myresult:
                                        id+=1
                                my_cursor.execute("update student set dept=%s,year=%s,sem=%s,studentname=%s,studentdiv=%s,studentrollno=%s,studentemail=%s,studentphone=%s,photosample=%s where studentid=%s",(
                                                                                                                self.var_dept.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_studentname.get(),
                                                                                                                self.var_studentdiv.get(),
                                                                                                                self.var_studentrollno.get(),
                                                                                                                self.var_studentemail.get(),
                                                                                                                self.var_studentphone.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_studentid.get()==id+1
                                                                                                         ))
                                conn.commit()
                                self.fetch_data()
                                self.reset_data()
                                conn.close()


                                #######Load predefined data on face frontaal from open cv

                                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                                
                                def face_cropped(img):
                                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                        faces=face_classifier.detectMultiScale(gray,1.3,5)

                                        for (x,y,w,h) in faces:
                                                face_cropped=img[y:y+h,x:x+w]
                                                return face_cropped

                                cap=cv2.VideoCapture(0)
                                img_id=0
                                while True:
                                        ret,my_frame=cap.read()
                                        if face_cropped(my_frame) is not None:
                                                img_id+=1
                                                face=cv2.resize(face_cropped(my_frame),(450,450))
                                                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                                file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                                cv2.imwrite(file_name_path,face)
                                                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                                cv2.imshow("Croppped Face" ,face)

                                        if cv2.waitKey(1)==13 or int(img_id)==100:
                                                break
                                cap.release()
                                cv2.destroyAllWindows()
                                messagebox.showinfo("Result","Generating Data Sets completed!!")
                        except Exception as es :
                                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                                


                
        
                                






if __name__ =="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()