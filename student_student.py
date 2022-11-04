from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox             #for tree view
import sqlite3
class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage courses")
        self.root.geometry("1140x700+80+80")
        self.root.config(bg="white")
        # self.root.focus_force()
        # ---------------title-----------------
        title = Label(self.root, text="Student Record Management",  font=("goudy ols style", 20, "bold"), bg="black",fg="white",height=50)
        title.place(x=0, y=0, height=70, relwidth=1)

        # --------------------------variables-----------------------
        self.var_sroll = StringVar()
        self.var_sname = StringVar()
        self.var_semail = StringVar()
        self.var_sgender = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        # self.var_pin = StringVar()

        # --------------Column1----------------------------------
        sroll = Label(self.root, text="Roll Number: ", font=("goudy ols style", 15, "bold"), fg="black")
        sroll.place(x=10, y=90, height=40)

        sname = Label(self.root, text="Name: ", font=("goudy ols style", 15, "bold"), fg="black")
        sname.place(x=10, y=140, height=40)

        semail = Label(self.root, text="Email ID:   ", font=("goudy ols style", 15, "bold"), fg="black")
        semail.place(x=10, y=190, height=40)

        sgender = Label(self.root, text="Gender: ", font=("goudy ols style", 15, "bold"), fg="black")
        sgender.place(x=10, y=240, height=40)

        state = Label(self.root, text="State: ", font=("goudy ols style", 15, "bold"), fg="black")
        state.place(x=10, y=300, height=40)

        add = Label(self.root, text="Address: ", font=("goudy ols style", 15, "bold"), fg="black")
        add.place(x=10, y=350, height=40)

        self.txt_sroll = Entry(self.root, textvariable=self.var_sroll, bg="lightyellow", font=("goudy ols style", 15, "bold"),fg="black")
        self.txt_sroll.place(x=140, y=90, height=40, width=150)

        self.txt_sname = Entry(self.root, textvariable=self.var_sname, bg="lightyellow", font=("goudy ols style", 15, "bold"),fg="black")
        self.txt_sname.place(x=140, y=140, height=40, width=150)

        self.txt_semail = Entry(self.root, textvariable=self.var_semail, bg="lightyellow", font=("goudy ols style", 15, "bold"),fg="black")
        self.txt_semail.place(x=140, y=190, height=40, width=150)

        # drop dowm for gender
        self.txt_sgender = ttk.Combobox(self.root, textvariable=self.var_sgender, values=("Select", "Male", "Female", "Other"),font=("goudy ols style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_sgender.place(x=140, y=240, height=40, width=150)
        self.txt_sgender.current(0)

        self.txt_state = Entry(self.root, textvariable=self.var_state, bg="lightyellow", font=("goudy ols style", 15, "bold"),fg="black")
        self.txt_state.place(x=140, y=300, height=40, width=150)

        self.txt_add = Text(self.root, font=("goudy ols style", 15, "bold"), bg="lightyellow", fg="black")
        self.txt_add.place(x=140, y=350, height=80, width=300)

        # ---------------------------COlumn2---------------------
        self.var_sdob = StringVar()
        self.var_scontact = StringVar()
        self.var_sadm = StringVar()
        self.var_scourse = StringVar()

        sdob = Label(self.root, text="DOB: ", font=("goudy ols style", 15, "bold"), fg="black")
        sdob.place(x=330, y=90, height=40)

        scontact = Label(self.root, text="Contact No.: ", font=("goudy ols style", 15, "bold"), fg="black")
        scontact.place(x=330, y=140, height=40)

        saddm = Label(self.root, text="Admission No.:   ", font=("goudy ols style", 15, "bold"), fg="black")
        saddm.place(x=330, y=190, height=40)

        scourse = Label(self.root, text="Courses: ", font=("goudy ols style", 15, "bold"), fg="black")
        scourse.place(x=330, y=240, height=40)

        self.course_list = []
        self.fetch_course()  # function call to update the list

        city = Label(self.root, text="City: ", font=("goudy ols style", 15, "bold"), fg="black")
        city.place(x=330, y=290, height=40)

        txt_sdob = Entry(self.root, textvariable=self.var_sdob, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
        txt_sdob.place(x=480, y=90, height=40, width=150)

        txt_scontact = Entry(self.root, textvariable=self.var_scontact, bg="lightyellow", font=("goudy ols style", 15, "bold"),fg="black")
        txt_scontact.place(x=480, y=140, height=40, width=150)

        txt_sadm = Entry(self.root, textvariable=self.var_sadm, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
        txt_sadm.place(x=480, y=190, height=40, width=150)

        # drop dowm for course
        self.txt_scourse = ttk.Combobox(self.root, textvariable=self.var_scourse, values=self.course_list,font=("goudy ols style", 15, "bold"), state="readonly", justify=CENTER)
        self.txt_scourse.place(x=480, y=240, height=40, width=150)
        self.txt_scourse.set("Select")

        self.txt_city = Entry(self.root, textvariable=self.var_city, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
        self.txt_city.place(x=480, y=290, height=40, width=150)

        # --------------------Buttons-----------------------------
        self.btn_add = Button(self.root, text="ADD", font=("goudy ols style", 10, "bold"), bg="blue", fg="white", cursor="hand2",command=self.add_course)
        self.btn_add.place(x=50, y=480, height=40, width=100)

        self.btn_update = Button(self.root, text="UPDATE", font=("goudy ols style", 10, "bold"), bg="orange", fg="white",cursor="hand2", command=self.update)
        self.btn_update.place(x=160, y=480, height=40, width=100)

        self.btn_delete = Button(self.root, text="DELETE", font=("goudy ols style", 10, "bold"), bg="maroon", fg="white",cursor="hand2", command=self.delete)
        self.btn_delete.place(x=280, y=480, height=40, width=100)

        self.btn_clear = Button(self.root, text="CLEAR", font=("goudy ols style", 10, "bold"), bg="brown", fg="white",cursor="hand2", command=self.clear)
        self.btn_clear.place(x=400, y=480, height=40, width=100)

        # ----------------Search Panel-------------------------
        self.f1 = Frame(self.root, bd=7, relief=RAISED)
        self.f1.place(x=650, y=90, height=500, width=470)

        scrolly = Scrollbar(self.f1, orient=VERTICAL)
        scrollx = Scrollbar(self.f1, orient=HORIZONTAL)

        self.course_detail = ttk.Treeview(self.f1, columns=(
        "Roll", "Name", "Email", "Gender", "DOB", "Contact", "Admission", "Course", "State", "City", "Address"),
        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.config(command=self.course_detail.xview)
        scrolly.config(command=self.course_detail.yview)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        self.course_detail.heading("Roll", text="Roll Number")
        self.course_detail.heading("Name", text="Name")
        self.course_detail.heading("Email", text="Email ID")
        self.course_detail.heading("Gender", text="Gender")
        self.course_detail.heading("DOB", text="D.O.B")
        self.course_detail.heading("Contact", text="Contact")
        self.course_detail.heading("Admission", text="Admission")
        self.course_detail.heading("Course", text="Course")
        self.course_detail.heading("State", text="State")
        self.course_detail.heading("City", text="City")
        # self.course_detail.heading("Pin", text="Pin Code")
        self.course_detail.heading("Address", text="Address")

        self.course_detail["show"] = "headings"

        self.course_detail.column("Roll", width=100)
        self.course_detail.column("Name", width=100)
        self.course_detail.column("Email", width=100)
        self.course_detail.column("Gender", width=100)
        self.course_detail.column("DOB", width=100)
        self.course_detail.column("Contact", width=100)
        self.course_detail.column("Admission", width=100)
        self.course_detail.column("Course", width=100)
        self.course_detail.column("State", width=100)
        self.course_detail.column("City", width=100)
        # self.course_detail.column("Pin", width=100)
        self.course_detail.column("Address", width=200)
        self.course_detail.pack(fill=BOTH, expand=1)

        self.course_detail.bind("<ButtonRelease-1>", self.get_record)
        self.show_course()

    # ------------------------------functions------------------------------------
    def show_course(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            cr.execute("select * from student")
            rows=cr.fetchall()
            self.course_detail.delete(*self.course_detail.get_children())
            for row in rows:
                self.course_detail.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=self.root)

    def fetch_course(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            cr.execute("select name from course")
            rows=cr.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=self.root)

    def get_record(self,e):
        self.txt_sroll.config(state="readonly")
        r = self.course_detail.focus()
        content = self.course_detail.item(r)
        row = content["values"]
        self.var_sroll.set(row[0]),
        self.var_sname.set(row[1]),
        self.var_semail.set(row[2]),
        self.var_sgender.set(row[3]),
        self.var_sdob.set(row[4]),
        self.var_scontact.set(row[5]),
        self.var_sadm.set(row[6]),
        self.var_scourse.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        # self.var_pin.set(row[10]),
        self.txt_add.delete("1.0", END)
        self.txt_add.insert(END, row[10])

    def search_course(self):
        try:
            cr.execute(f"select * from student where Roll=?",(self.var_search.get(),))
            row=cr.fetchone()
            if row!=None:
                self.course_detail.delete(*self.course_detail.get_children())
                self.course_detail.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=self.root)

    def add_course(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            if self.var_sroll.get() =="":
                messagebox.showinfo("Empty Name","Roll Number is required",parent=self.root)
            else:
                cr.execute("select * from student where Roll = ?",(self.var_sroll.get(),))
                row=cr.fetchone()
                if(row!=None):
                    messagebox.showinfo("Duplicate Entry :", " Entered Roll No. is Already Present ", parent=self.root)
                else:
                    cr.execute("insert into student(Roll,Name,Email,Gender,DOB,Contact,Admission,Course,State,City,Address) values(?,?,?,?,?,?,?,?,?,?,?)",
                               (self.var_sroll.get(),self.var_sname.get(),self.var_semail.get(),
                                self.var_sgender.get(),self.var_sdob.get(),self.var_scontact.get(),
                                self.var_sadm.get(),self.var_scourse.get(),self.var_state.get(),
                                self.var_city.get(),self.txt_add.get("1.0",END)))
                    db.commit()
                    messagebox.showinfo("Inserted","Record added successfully",parent=self.root)
                    self.show_course()
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=self.root)

    def update(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            if self.var_sroll.get() == "":
                messagebox.showinfo("Error", "Roll Number is required", parent=self.root)
            else:
                cr.execute("select * from student where Roll = ?", (self.var_sroll.get(),))
                row = cr.fetchone()
                if (row == None):
                    messagebox.showinfo("Error", " Please Select student From List", parent=self.root)
                else:
                    cr.execute("update student set Name=?,Email=?,Gender=?,DOB=?,Contact=?,Admission=?,Course=?,State=?,City=?,Address=? where Roll=?" ,(
                        self.var_sname.get(), self.var_semail.get(),
                        self.var_sgender.get(), self.var_sdob.get(), self.var_scontact.get(),
                        self.var_sadm.get(), self.var_scourse.get(), self.var_state.get(),
                        self.var_city.get(), self.txt_add.get("1.0", END),self.var_sroll.get()))

                    db.commit()
                    messagebox.showinfo("Success:"," Student updated successfully",parent=self.root)
                    self.show_course()
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=self.root)

    def delete(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            if self.var_sroll.get() == "":
                messagebox.showinfo("Error", "Roll Number is required", parent=self.root)
            else:
                cr.execute("select * from student where Roll = ?", (self.var_sroll.get(),))
                row = cr.fetchone()
                if (row == None):
                    messagebox.showinfo("Error", " Please Select student  From List ", parent=self.root)
                else:
                    cr.execute("delete from student where Roll =?",
                               (self.txt_sroll.get(),))
                    db.commit()
                    messagebox.showinfo("Delete"," Record Deleted Successfully",parent=self.root)
                    self.show_course()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=self.root)

    def clear(self):
        self.show_course()
        self.var_sroll.set(" "),
        self.var_sname.set(" "),
        self.var_semail.set(" "),
        self.var_sgender.set("Select"),
        self.var_sdob.set(" "),
        self.var_scontact.set(" "),
        self.var_sadm.set(" "),
        self.var_scourse.set("Select"),
        self.var_state.set(" "),
        self.var_city.set(" "),
        # self.var_pin.set(" "),
        self.txt_add.delete("1.0", END)
        self.txt_sroll.config(state=NORMAL)
        # self.var_search.set(" ")

if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()