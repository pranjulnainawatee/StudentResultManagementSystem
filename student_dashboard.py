from tkinter import *
from PIL import Image, ImageTk          #pillow library
from student_course import CourseClass
from student_student import StudentClass
from student_result import ResultClass
from student_view_result import ViewResultClass
import sqlite3
class RMS:
    def __init__(self,root):            #default  constructor
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1140x700+0+0")  #1350x700
        self.root.config(bg="white")

        # -------------------icons------------------
        self.logo = Image.open("images/img.png")
        self.logo = self.logo.resize((50, 50), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(self.logo)
        #Compound and padx used for image
        #--------------title-------------------
        title = Label(self.root, text="Student Result Management System", padx=20, font=("goudy old  style", 20, "bold"),bg="gray5", fg="white", image=self.logo, compound=LEFT, height=50)
        title.place(x=0, y=0, height=70, relwidth=1)

        #---------------menu-------------------
        my_frame = LabelFrame(root, text="Menu Card", font=("goudy ols style", 15, "bold"), bg="white", fg="black",height=50)
        my_frame.place(x=30, y=80, height=100, relwidth=0.95)

        #---------------buttons----------------
        b1 = Button(my_frame, text="Course", font=("goudy ols style", 15, "bold"), bg="turquoise", fg="white",cursor="hand2",command=self.a_course)
        b1.place(x=30, y=5, height=50, width=250)

        b2 = Button(my_frame, text="Student", font=("goudy ols style", 15, "bold"), bg="turquoise", fg="white",cursor="hand2",command=self.a_student)
        b2.place(x=290, y=5, height=50, width=250)

        b3 = Button(my_frame, text="Result", font=("goudy ols style", 15, "bold"), bg="turquoise", fg="white",cursor="hand2", command=self.a_result)
        b3.place(x=550, y=5, height=50, width=250)

        b4 = Button(my_frame, text="View Result", font=("goudy ols style", 15, "bold"), bg="turquoise", fg="white",cursor="hand2",command=self.a_view_result)
        b4.place(x=810, y=5, height=50, width=250)

        #----------------background image----------------
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_student = Label(self.root, image=self.bg_img)
        self.lbl_student.place(x=200, y=200, width=620, height=350)

        #-------------------for update details function--------------------
        self.course = Label(self.root,  font=("goudy ols style", 15, "bold"), bg="orange", fg="white",bd=5, relief=RIDGE)
        self.course.place(x=200, y=570, height=70, width=190)

        self.student = Label(self.root, font=("goudy ols style", 15, "bold"), bg="red", fg="white",bd=5, relief=SUNKEN)
        self.student.place(x=410, y=570, height=70, width=190)

        self.result = Label(self.root,  font=("goudy ols style", 15, "bold"), bg="maroon", fg="white",bd=5, relief=RAISED)
        self.result.place(x=620, y=570, height=70, width=190)

        #----------------footer----------
        footer = Label(self.root, text="SRMS - Student Result Management System \n contact us 9876543210",font=("goudy ols style", 10, "bold"), bg="gray5", fg="white")
        footer.pack(side=BOTTOM, fill=X)

        self.update_details()

    def a_course(self):                     #add course details function
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def a_student(self):                    #add student details function
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)

    def a_result(self):                     #add result function
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)

    def a_view_result(self):                     #add view result function
        self.new_win=Toplevel(self.root)
        self.new_obj=ViewResultClass(self.new_win)

    def update_details(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            cr.execute("select * from course")
            num = cr.fetchall()
            self.course.config(text=f"Total Courses\n[{str(len(num))}]")

            cr.execute("select * from student")
            num = cr.fetchall()
            self.student.config(text=f"Total Students\n[{str(len(num))}]")

            cr.execute("select * from result")
            num = cr.fetchall()
            self.result.config(text=f"Total Results\n[{str(len(num))}]")

            #.after to automatically update changes on dashboard labels present at the bottom
            self.course.after(200,self.update_details)

        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()