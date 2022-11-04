from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox             #for tree view
import sqlite3
class ViewResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage courses")
        self.root.geometry("1140x700+80+80")
        self.root.config(bg="white")
        # self.root.focus_force()

        title = Label(self.root, text="View Student Result", font=("goudy ols style", 20, "bold"), bg="black", fg="white",height=50)
        title.place(x=0, y=0, height=70, relwidth=1)

        #--------------search--------------------
        self.var_search = StringVar()
        self.var_id = ""
        lbl_search = Label(self.root, text="Search by roll number: ", font=("goudy ols style", 15, "bold"), bg="white")
        lbl_search.place(x=280, y=100)

        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy ols style", 15), bg="lightyellow")
        txt_search.place(x=520, y=100, width=150)

        btn_search = Button(self.root, text="SEARCH", font=("goudy ols style", 10, "bold"), bg="blue", fg="white",cursor="hand2", command=self.search)
        btn_search.place(x=680, y=100, height=35, width=100)

        btn_clear = Button(self.root, text="CLEAR", font=("goudy ols style", 10, "bold"), bg="grey", fg="white",cursor="hand2", command=self.clear)
        btn_clear.place(x=800, y=100, height=35, width=100)

        #------------------headings-------------------
        lbl_roll = Label(self.root, text="Roll No.", font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_roll.place(x=150, y=230, height=50, width=150)
        #bd is border for each cell
        lbl_name = Label(self.root, text="Name", font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_name.place(x=300, y=230, height=50, width=150)

        lbl_course = Label(self.root, text="Course", font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_course.place(x=450, y=230, height=50, width=150)

        lbl_marks = Label(self.root, text="Marks Obtained", font=("goudy ols style", 15, "bold"), bg="white", bd=2,relief=GROOVE)
        lbl_marks.place(x=600, y=230, height=50, width=150)

        lbl_fullmarks = Label(self.root, text="Total Marks", font=("goudy ols style", 15, "bold"), bg="white", bd=2,relief=GROOVE)
        lbl_fullmarks.place(x=750, y=230, height=50, width=150)

        lbl_per = Label(self.root, text="Percentage", font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        lbl_per.place(x=900, y=230, height=50, width=150)

        #---------------actual value cells----------------
        self.roll = Label(self.root, font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, height=50, width=150)

        self.name = Label(self.root, font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, height=50, width=150)

        self.course = Label(self.root, font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, height=50, width=150)

        self.marks = Label(self.root, font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.marks.place(x=600, y=280, height=50, width=150)

        self.fullmarks = Label(self.root, font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.fullmarks.place(x=750, y=280, height=50, width=150)

        self.per = Label(self.root, font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.per.place(x=900, y=280, height=50, width=150)

        btn_delete = Button(self.root, text="Delete", font=("goudy ols style", 10, "bold"), bg="red", fg="white",cursor="hand2", command=self.delete)
        btn_delete.place(x=500, y=350, height=35, width=150)

    #---------------FUNCTIONS----------------
    def search(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll number required",parent=self.root)
            else:
                cr.execute(f"select * from result where Roll=?",(self.var_search.get(),))
                row=cr.fetchone()
                if row!=None:
                    #config is used to fetch value in each cell
                    self.var_id =row[0]           #dynamic
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.fullmarks.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=self.root)

    def clear(self):
        self.roll.config(text=" ")
        self.name.config(text=" ")
        self.course.config(text=" ")
        self.marks.config(text=" ")
        self.fullmarks.config(text=" ")
        self.per.config(text=" ")
        self.var_search.set("")
        self.var_id=""

    def delete(self):
        db = sqlite3.connect(database="student_project.db")
        cr = db.cursor()
        try:
            if self.var_id== "":
                messagebox.showinfo("Error", "Search student result first", parent=self.root)
            else:
                cr.execute("select * from result where rid = ?", (self.var_id,))
                row = cr.fetchone()
                if (row == None):
                    messagebox.showinfo("Error", "Invalid student result", parent=self.root)
                else:
                    cr.execute("delete from result where rid =?", (self.var_id,))
                    db.commit()
                    messagebox.showinfo("Success","Result deleted successfully",parent=self.root)

                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=ViewResultClass(root)
    root.mainloop()