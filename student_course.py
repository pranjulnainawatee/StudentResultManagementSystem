from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox             #for tree view
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage courses")
        self.root.geometry("1140x700+80+80")
        self.root.config(bg="white")
        # self.root.focus_force()

        title = Label(self.root, text="Course Management", font=("goudy ols style", 20, "bold"), bg="black",fg="white",height=50)
        title.place(x=0, y=0, height=70, relwidth=1)

        self.var_name = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        cname = Label(self.root, text="Course Name : ", font=("goudy ols style", 15, "bold"), fg="black")
        cname.place(x=10, y=90, height=40)

        duration = Label(self.root, text="Duration : ", font=("goudy ols style", 15, "bold"), fg="black")
        duration.place(x=10, y=140, height=40)

        charges = Label(self.root, text="Charges : ", font=("goudy ols style", 15, "bold"), fg="black")
        charges.place(x=10, y=190, height=40)

        dis = Label(self.root, text="Description : ", font=("goudy ols style", 15, "bold"), fg="black")
        dis.place(x=10, y=240, height=40)

        self.txt_cname = Entry(self.root, textvariable=self.var_name, bg="lightyellow", font=("goudy ols style", 15, "bold"),fg="black")
        self.txt_cname.place(x=180, y=90, height=40, width=300)

        self.txt_duration = Entry(self.root, textvariable=self.var_duration, bg="lightyellow", font=("goudy ols style", 15, "bold"),fg="black")
        self.txt_duration.place(x=180, y=140, height=40, width=300)

        self.txt_charges = Entry(self.root, textvariable=self.var_charges, bg="lightyellow", font=("goudy ols style", 15, "bold"),fg="black")
        self.txt_charges.place(x=180, y=190, height=40, width=300)

        self.txt_dis = Text(self.root, font=("goudy ols style", 15, "bold"), bg="lightyellow", fg="black")
        self.txt_dis.place(x=180, y=240, height=80, width=300)
        # ----------------------Buttons-----------------------------
        self.btn_add = Button(self.root, text="ADD", font=("goudy ols style", 10, "bold"), bg="blue", fg="white", cursor="hand2",command=self.add_course)
        self.btn_add.place(x=10, y=340, height=40, width=100)

        self.btn_update = Button(self.root, text="UPDATE", font=("goudy ols style", 10, "bold"), bg="orange", fg="white",cursor="hand2", command=self.update)
        self.btn_update.place(x=120, y=340, height=40, width=100)

        self.btn_delete = Button(self.root, text="DELETE", font=("goudy ols style", 10, "bold"), bg="maroon", fg="white",cursor="hand2", command=self.delete)
        self.btn_delete.place(x=240, y=340, height=40, width=100)

        self.btn_clear = Button(self.root, text="CLEAR", font=("goudy ols style", 10, "bold"), bg="brown", fg="white",cursor="hand2", command=self.clear)
        self.btn_clear.place(x=360, y=340, height=40, width=100)

        # -----------------Search Panel-----------------------------------
        self.f1 = Frame(self.root, bd=7, relief=RAISED)
        self.f1.place(x=520, y=90, height=450, width=580)

        scrolly = Scrollbar(self.f1, orient=VERTICAL)
        scrollx = Scrollbar(self.f1, orient=HORIZONTAL)

        self.course_detail = ttk.Treeview(self.f1, columns=("Cid", "Name", "Duration", "Charges", "Description"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.config(command=self.course_detail.xview)
        scrolly.config(command=self.course_detail.yview)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.course_detail.heading("Cid", text="Course ID")
        self.course_detail.heading("Name", text="Name")
        self.course_detail.heading("Duration", text="Duration")
        self.course_detail.heading("Charges", text="Charges")
        self.course_detail.heading("Description", text="Description")
        self.course_detail["show"] = "headings"
        self.course_detail.column("Cid", width=100)
        self.course_detail.column("Name", width=150)
        self.course_detail.column("Duration", width=100)
        self.course_detail.column("Charges", width=100)
        self.course_detail.column("Description", width=250)

        self.course_detail.pack(fill=BOTH, expand=1)
        #if click on any course, all details appear in resp. text boxes so that they can be updated
        self.course_detail.bind("<ButtonRelease-1>", self.get_record)
        self.show_course()

    # ----------------functions---------
    def add_course(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            if self.var_name.get() =="":
                messagebox.showinfo("Empty Name",f"Course Name is required",parent=self.root)
            else:
                cr.execute("select * from course where Name = ?",(self.var_name.get(),))
                row=cr.fetchone()
                if(row!=None):
                    messagebox.showinfo("Duplicate Entry :", " Entered Course IS Already Present ", parent=self.root)
                else:
                    cr.execute("insert into course (Name, Duration, Charges , Description) values(?,?,?,?)",(
                        self.var_name.get(),self.var_duration.get(),self.var_charges.get(),self.txt_dis.get("1.0",END)))
                    db.commit()
                    messagebox.showinfo("Success","Record Inserted Successfully",parent=self.root)
                    self.show_course()
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=self.root)

    def show_course(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            cr.execute("select * from course")
            rows = cr.fetchall()
            self.course_detail.delete(*self.course_detail.get_children())
            for row in rows:
                self.course_detail.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=self.root)

    def get_record(self,e):
        self.txt_cname.config(state="readonly")     #to make course name unique, cannot change/update course name
        r=self.course_detail.focus()          # variable, maintain index number
        content=self.course_detail.item(r)   #variable,it access record
        row=content["values"]      # values fetch in row variable
        # print(row)
        self.var_name.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_dis.delete('1.0',END)
        self.txt_dis.insert(END,row[4])

    def update(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showinfo("Empty Name", f"Course Name is required", parent=self.root)
            else:
                cr.execute("select * from course where Name = ?", (self.var_name.get(),))
                row = cr.fetchone()
                if (row == None):
                    messagebox.showinfo("Select Record :", " Please Select a Record  From List :", parent=self.root)
                else:
                    cr.execute("update course set Duration=?, Charges=? , Description=? where Name =?" ,
                               (self.var_duration.get(), self.var_charges.get(), self.txt_dis.get("1.0",END), self.txt_cname.get()))
                    db.commit()
                    messagebox.showinfo("Success","Record Updated Successfully",parent=self.root)
                    self.show_course()
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=self.root)

    def clear(self):
        self.show_course()
        self.var_name.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.txt_dis.delete('1.0', END)
        self.txt_cname.config(state=NORMAL)
        # self.var_search.set("")

    def delete(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showinfo("Empty Name", f"Course Name is required", parent=self.root)
            else:
                cr.execute("select * from course where Name = ?", (self.var_name.get(),))
                row = cr.fetchone()
                if (row == None):
                    messagebox.showinfo("Select Record :", " Please Select a Record  From List :", parent=self.root)
                else:
                    cr.execute("delete from course where Name =?",(self.txt_cname.get(),))
                    db.commit()
                    messagebox.showinfo("Success","Record Deleted Successfully",parent=self.root)
                    # self.show_course()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()