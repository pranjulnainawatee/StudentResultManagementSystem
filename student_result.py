from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox             #for tree view
import sqlite3
class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage courses")
        self.root.geometry("1140x700+80+80")
        self.root.config(bg="white")
        # self.root.focus_force()

        title = Label(self.root, text="Add Student Result", font=("goudy ols style", 20, "bold"), bg="black", fg="white",height=50)
        title.place(x=0, y=0, height=70, relwidth=1)

        lbl_select = Label(self.root, text="Select Student: ", font=("goudy ols style", 15, "bold"), bg="white")
        lbl_select.place(x=50, y=100)

        lbl_name = Label(self.root, text="Name:", font=("goudy ols style", 15, "bold"), bg="white")
        lbl_name.place(x=50, y=160)

        lbl_course = Label(self.root, text="Course:", font=("goudy ols style", 15, "bold"), bg="white")
        lbl_course.place(x=50, y=220)

        lbl_marks = Label(self.root, text="Marks Obtained:", font=("goudy ols style", 15, "bold"), bg="white")
        lbl_marks.place(x=50, y=280)

        lbl_fullmarks = Label(self.root, text="Full Marks:", font=("goudy ols style", 15, "bold"), bg="white")
        lbl_fullmarks.place(x=50, y=340)

        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks_ob = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []                     #for combo box

        self.fetch_roll()

        txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, font=("goudy ols style", 15, "bold"),state="readonly", justify=CENTER)
        txt_student.place(x=280, y=100, width=200)
        txt_student.set("Select")

        btn_search = Button(self.root, text="SEARCH", font=("goudy ols style", 10, "bold"), bg="blue", fg="white",cursor="hand2", command=self.search_course)
        btn_search.place(x=500, y=100, height=30, width=100)

        txt_name = Entry(self.root, textvariable=self.var_name, bg="lightyellow", font=("goudy ols style", 20, "bold"),state="readonly")
        txt_name.place(x=280, y=160, width=320)

        txt_course = Entry(self.root, textvariable=self.var_course, bg="lightyellow", font=("goudy ols style", 20, "bold"),state="readonly")
        txt_course.place(x=280, y=220, width=320)

        txt_marks = Entry(self.root, textvariable=self.var_marks_ob, bg="lightyellow", font=("goudy ols style", 20, "bold"))
        txt_marks.place(x=280, y=280, width=320)

        txt_fullmarks = Entry(self.root, textvariable=self.var_full_marks, bg="lightyellow", font=("goudy ols style", 20, "bold"))
        txt_fullmarks.place(x=280, y=340, width=320)

        btn_submit = Button(self.root, text="Submit", font=("goudy ols style", 15), bg="lightgreen",activebackground="lightgreen", cursor="hand2", command=self.add_result)
        btn_submit.place(x=300, y=420, height=35, width=120)

        btn_clear = Button(self.root, text="Clear", font=("goudy ols style", 15), bg="lightgrey",activebackground="lightgrey", cursor="hand2", command=self.clear)
        btn_clear.place(x=430, y=420, height=35, width=120)

        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((450, 350), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_student = Label(self.root, image=self.bg_img)
        self.lbl_student.place(x=650, y=100)

    # ------------------------FUNCTIONS----------------------------
    def fetch_roll(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            cr.execute("select Roll from student")
            rows = cr.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex}",parent=self.root)

    def search_course(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            cr.execute(f"select Name,Course from student where Roll=?", (self.var_roll.get(),))
            row = cr.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=self.root)

    def add_result(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            if self.var_name.get() == " ":
                messagebox.showinfo("Error", "Please first search student record", parent=self.root)
            else:
                cr.execute("select * from result where roll = ? and course=?", (self.var_roll.get(), self.var_course.get()))
                row = cr.fetchone()
                if (row != None):
                    messagebox.showinfo("Error", "Result already present ", parent=self.root)
                else:
                    per = (int(self.var_marks_ob.get()) * 100) / int(self.var_full_marks.get())  # error if submit empty result
                    cr.execute("insert into result(roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)", (
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_marks_ob.get(),
                    self.var_full_marks.get(),
                    str(per)))
                    db.commit()
                    messagebox.showinfo("Success", "Result added successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=self.root)

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set(" ")
        self.var_course.set(" ")
        self.var_marks_ob.set(" ")
        self.var_full_marks.set(" ")

if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()