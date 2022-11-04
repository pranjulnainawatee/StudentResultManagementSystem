import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk           #pillow library
root=Tk()
db=sqlite3.connect(database="student_project.db")
cr=db.cursor()

root.geometry("1350x700")
root.config(bg="white")
cr.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY , name TEXT, duration TEXT, charges TEXT, description TEXT )")
db.commit()

cr.execute("CREATE TABLE IF NOT EXISTS student(Roll INTEGER PRIMARY KEY,Name text,Email text,Gender text,DOB text,Contact text,Admission text,Course text,State text,City text,Pin text,Address text )")
db.commit()

cr.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY , roll TEXT, name TEXT, course TEXT, marks TEXT, fullmarks TEXT, per TEXT )")
db.commit()
# db.close()
def menu_course():
    top=Toplevel(root)
    top.geometry("1300x650+10+20")
    top.focus_force()
#
    def show_course():
        try:
            cr.execute("select * from course")
            rows = cr.fetchall()
            course_detail.delete(*course_detail.get_children())
            for row in rows:
                course_detail.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=top)
    def search_course():
        try:
            cr.execute(f"select * from course where Name LIKE  '%{search.get()}%'")
            rows=cr.fetchall()
            course_detail.delete(*course_detail.get_children())
            for row in rows:
                course_detail.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=top)
    def add_course():
        try:
            if var_name.get() =="":
                messagebox.showinfo("Empty Name",f"Course Name is required",parent=top)
            else:
                cr.execute("select * from course where Name = ?",(var_name.get(),))
                row=cr.fetchone()
                if(row!=None):
                    messagebox.showinfo("Duplicate Entry :", " Entered Course IS Already Present ", parent=top)
                else:
                    cr.execute("insert into course (Name, Duration, Charges , Description) values(?,?,?,?)",(var_name.get(),var_duration.get(),var_charges.get(),txt_dis.get("1.0",END)))
                    db.commit()
                    messagebox.showinfo("Inserted Successfully :",
                                        f" Record Inserted {var_name.get()} {var_duration.get()} {var_charges.get()} {txt_dis.get('1.0', END)}",
                                        parent=top)
                    show_course()
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=top)
    def update():
        try:
            if var_name.get() == "":
                messagebox.showinfo("Empty Name", f"Course Name is required", parent=top)
            else:
                cr.execute("select * from course where Name = ?", (var_name.get(),))
                row = cr.fetchone()
                if (row == None):
                    messagebox.showinfo("Select Record :", " Please Select a Record  From List :", parent=top)
                else:
                    cr.execute("update course  set Duration=?, Charges=? , Description=? where Name =?" ,
                               (var_duration.get(), var_charges.get(), txt_dis.get("1.0",END), txt_cname.get()))
                    db.commit()
                    messagebox.showinfo("Updated Successfully :",
                                        f" Record Updated {var_name.get()} {var_duration.get()} {var_charges.get()} {txt_dis.get('1.0', END)}",
                                        parent=top)
                    show_course()
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=top)
    def delete():
        try:
            if var_name.get() == "":
                messagebox.showinfo("Empty Name", f"Course Name is required", parent=top)
            else:
                cr.execute("select * from course where Name = ?", (var_name.get(),))
                row = cr.fetchone()
                if (row == None):
                    messagebox.showinfo("Select Record :", " Please Select a Record  From List :", parent=top)
                else:
                    cr.execute("delete from course where Name =?",
                               (txt_cname.get(),))
                    db.commit()
                    messagebox.showinfo("Deleted Successfully :",
                                        f" Record Deleted {var_name.get()} {var_duration.get()} {var_charges.get()} {txt_dis.get('1.0', END)}",
                                        parent=top)
                    show_course()
                    clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=top)
    def clear():
        show_course()
        var_name.set("")
        var_duration.set("")
        var_charges.set("")
        txt_dis.delete('1.0', END)
        txt_cname.config(state=NORMAL)
        search.set("")
#
    title = Label(top, text="Course Management", padx=20, font=("goudy ols style", 20, "bold"),bg="black", fg="white", image=logo, compound=LEFT, height=50)
    title.place(x=0, y=0, height=70, relwidth=1)

    var_name=StringVar()
    var_duration=StringVar()
    var_charges=StringVar()

    cname = Label(top, text="Course Name : ",font=("goudy ols style", 15, "bold"),fg="black")
    cname.place(x=10, y=90, height=40)

    duration = Label(top, text="Duration : ", font=("goudy ols style", 15, "bold"), fg="black")
    duration.place(x=10, y=140, height=40)

    charges = Label(top, text="Charges : ", font=("goudy ols style", 15, "bold"), fg="black")
    charges.place(x=10, y=190, height=40)

    dis = Label(top, text="Description : ", font=("goudy ols style", 15, "bold"), fg="black")
    dis.place(x=10, y=240, height=40)

    txt_cname = Entry(top, textvariable=var_name,bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_cname.place(x=180, y=90, height=40,width=300)

    txt_duration = Entry(top,textvariable=var_duration,bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_duration.place(x=180, y=140, height=40,width=300)

    txt_charges = Entry(top,textvariable=var_charges,bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_charges.place(x=180, y=190, height=40,width=300)

    txt_dis = Text(top, font=("goudy ols style", 15, "bold"),bg="lightyellow", fg="black")
    txt_dis.place(x=180, y=240, height=80, width=300)
    #----------------------Buttons-----------------------------
    btn_add = Button(top, text="ADD", font=("goudy ols style", 10, "bold"), bg="blue", fg="white",cursor="hand2",command= add_course)
    btn_add.place(x=10, y=340, height=40, width=100)

    btn_update = Button(top, text="UPDATE", font=("goudy ols style", 10, "bold"), bg="orange", fg="white",cursor="hand2", command=update)
    btn_update.place(x=120, y=340, height=40, width=100)

    btn_delete = Button(top, text="DELETE", font=("goudy ols style", 10, "bold"), bg="maroon", fg="white",cursor="hand2",command=delete)
    btn_delete.place(x=240, y=340, height=40, width=100)

    btn_clear = Button(top, text="CLEAR", font=("goudy ols style", 10, "bold"), bg="brown", fg="white",cursor="hand2", command=clear)
    btn_clear.place(x=360, y=340, height=40, width=100)
#
#
#
    def get_record(e):
        txt_cname.config(state="readonly")
        r=course_detail.focus()          # is maintain index number
        content=course_detail.item(r)   # it access record
        row=content["values"]      # 1 python 45 15000 best
        var_name.set(row[1])
        var_duration.set(row[2])
        var_charges.set(row[3])
        txt_dis.delete('1.0',END)
        txt_dis.insert(END,row[4])
#
#
    #-----------------Search Panel-----------------------------------
    search=StringVar()
    lbl_search = Label(top, text="Course Name  : ", font=("goudy ols style", 15, "bold"), fg="black")
    lbl_search.place(x=650, y=90)
    # lbl_search.bind("<KeyPress-Down>", search_course())
    txt_search = Entry(top, textvariable=search, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_search.place(x=820, y=90)

    btn_search = Button(top, text="SEARCH", font=("goudy ols style", 10, "bold"), bg="brown", fg="white", cursor="hand2",command=search_course)
    btn_search.place(x=1050, y=90)
    #-------------------Content----------------------------------------
    f1=Frame(top,bd=7, relief=RAISED)
    f1.place(x=650,y=150,height=550,width=680)

    scrolly=Scrollbar(f1,orient=VERTICAL)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)

    course_detail=ttk.Treeview(f1,columns=("Cid","Name","Duration","Charges","Description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    scrollx.config(command=course_detail.xview)
    scrolly.config(command=course_detail.yview)

    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y )

    course_detail.heading("Cid",text="Course ID")
    course_detail.heading("Name",text="Name")
    course_detail.heading("Duration",text="Duration")
    course_detail.heading("Charges",text="Charges")
    course_detail.heading("Description",text="Description")
    course_detail["show"]="headings"
    course_detail.column("Cid",width=100)
    course_detail.column("Name",width=150)
    course_detail.column("Duration",width=100)
    course_detail.column("Charges",width=100)
    course_detail.column("Description",width=250)

    course_detail.pack(fill=BOTH, expand=1)
    course_detail.bind("<ButtonRelease-1>", get_record)
    show_course()

#
    top.mainloop()

def menu_student():
    top = Toplevel(root)
    top.geometry("1300x650+10+20")
    top.focus_force()
#
    def show_course():
        try:
            cr.execute("select * from student")
            rows=cr.fetchall()
            course_detail.delete(*course_detail.get_children())
            for row in rows:
                course_detail.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=top)
    def fetch_course():
        try:
            cr.execute("select name from course")
            rows=cr.fetchall()
            if len(rows)>0:
                for row in rows:
                    course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=top)
    def search_course():
        try:
            cr.execute(f"select * from student where Roll=?",(var_search.get(),))
            row=cr.fetchone()
            if row!=None:
                course_detail.delete(*course_detail.get_children())
                course_detail.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=top)
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=top)
    def add_course():
        try:
            if var_sroll.get() =="":
                messagebox.showinfo("Empty Name","Roll Number is required",parent=top)
            else:
                cr.execute("select * from student where Roll = ?",(var_sroll.get(),))
                row=cr.fetchone()
                if(row!=None):
                    messagebox.showinfo("Duplicate Entry :", " Entered Roll No. is Already Present ", parent=top)
                else:
                    cr.execute("insert into student (Roll,Name,Email,Gender,DOB,Contact,Admission,Course,State,City,Pin,Address) values(?,?,?,?,?,?,?,?,?,?,?,?)",
                               (var_sroll.get(),var_sname.get(),var_semail.get(),
                                var_sgender.get(),var_sdob.get(),var_scontact.get(),
                                var_sadm.get(),var_scourse.get(),var_state.get(),
                                var_city.get(),var_pin.get(),txt_add.get("1.0",END)))
                    db.commit()
                    messagebox.showinfo("Inserted","Record added successfully",parent=top)
                    show_course()
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=top)
    def update():
        try:
            if var_sroll.get() == "":
                messagebox.showinfo("Error", "Roll Number is required", parent=top)
            else:
                cr.execute("select * from student where Roll = ?", (var_sroll.get(),))
                row = cr.fetchone()
                if (row == None):
                    messagebox.showinfo("Error", " Please Select student From List", parent=top)
                else:
                    cr.execute("update student set Name=?,Email=?,Gender=?,DOB=?,Contact=?,Admission=?,Course=?,State=?,City=?,Pin=?,Address=? where Roll=?" ,(
                        var_sname.get(), var_semail.get(),
                        var_sgender.get(), var_sdob.get(), var_scontact.get(),
                        var_sadm.get(), var_scourse.get(), var_state.get(),
                        var_city.get(), var_pin.get(), txt_add.get("1.0", END),var_sroll.get()))

                    db.commit()
                    messagebox.showinfo("Success:"," Student updated successfully",parent=top)
                    show_course()
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=top)
    def delete():
        try:
            if var_sroll.get() == "":
                messagebox.showinfo("Error", "Roll Number is required", parent=top)
            else:
                cr.execute("select * from student where Roll = ?", (var_sroll.get(),))
                row = cr.fetchone()
                if (row == None):
                    messagebox.showinfo("Error", " Please Select student  From List ", parent=top)
                else:
                    cr.execute("delete from student where Roll =?",
                               (txt_sroll.get(),))
                    db.commit()
                    messagebox.showinfo("Delete"," Record Deleted Successfully",parent=top)
                    show_course()
                    clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=top)
    def clear():
        show_course()
        var_sroll.set(" "),
        var_sname.set(" "),
        var_semail.set(" "),
        var_sgender.set("Select"),
        var_sdob.set(" "),
        var_scontact.set(" "),
        var_sadm.set(" "),
        var_scourse.set("Select"),
        var_state.set(" "),
        var_city.set(" "),
        var_pin.set(" "),
        txt_add.delete("1.0", END)
        txt_sroll.config(state=NORMAL)
        var_search.set(" ")

    title = Label(top, text="Student Record Management", padx=20, font=("goudy ols style", 20, "bold"),bg="black", fg="white", image=logo, compound=LEFT, height=50)
    title.place(x=0, y=0, height=70, relwidth=1)


    var_sroll=StringVar()
    var_sname=StringVar()
    var_semail=StringVar()
    var_sgender = StringVar()
    var_state = StringVar()
    var_city = StringVar()
    var_pin = StringVar()
    #--------------Column1----------------------------------
    sroll = Label(top, text="Roll Number: ",font=("goudy ols style", 15, "bold"),fg="black")
    sroll.place(x=10, y=90, height=40)

    sname = Label(top, text="Name: ", font=("goudy ols style", 15, "bold"), fg="black")
    sname.place(x=10, y=140, height=40)

    semail = Label(top, text="Email ID:   ", font=("goudy ols style", 15, "bold"), fg="black")
    semail.place(x=10, y=190, height=40)

    sgender = Label(top, text="Gender: ", font=("goudy ols style", 15, "bold"), fg="black")
    sgender.place(x=10, y=240, height=40)

    state = Label(top, text="State: ", font=("goudy ols style", 15, "bold"), fg="black")
    state.place(x=10, y=300, height=40)

    city = Label(top, text="City: ", font=("goudy ols style", 15, "bold"), fg="black")
    city.place(x=270, y=300, height=40)

    pin = Label(top, text="Pin Code: ", font=("goudy ols style", 15, "bold"), fg="black")
    pin.place(x=430, y=300, height=40)

    add = Label(top, text="Address: ", font=("goudy ols style", 15, "bold"), fg="black")
    add.place(x=10, y=350, height=40)

    txt_sroll = Entry(top, textvariable=var_sroll,bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_sroll.place(x=140, y=90, height=40,width=150)

    txt_sname = Entry(top,textvariable=var_sname,bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_sname.place(x=140, y=140, height=40,width=150)

    txt_semail = Entry(top,textvariable=var_semail, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_semail.place(x=140, y=190, height=40,width=150)

    txt_sgender = ttk.Combobox(top, textvariable=var_sgender,values=("Select","Male","Female","Other"),font=("goudy ols style", 15, "bold"), state="readonly",justify=CENTER)
    txt_sgender.place(x=140, y=240, height=40, width=150)
    txt_sgender.current(0)

    txt_state = Entry(top, textvariable=var_state, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_state.place(x=140, y=300, height=40, width=100)

    txt_city = Entry(top, textvariable=var_city, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_city.place(x=320, y=300, height=40, width=100)

    txt_pin = Entry(top, textvariable=var_pin, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_pin.place(x=530, y=300, height=40, width=100)

    txt_add = Text(top, font=("goudy ols style", 15, "bold"), bg="lightyellow", fg="black")
    txt_add.place(x=140, y=350, height=80, width=300)
    #---------------------------COlumn2---------------------
    var_sdob = StringVar()
    var_scontact = StringVar()
    var_sadm = StringVar()
    var_scourse = StringVar()
    sdob = Label(top, text="DOB: ", font=("goudy ols style", 15, "bold"), fg="black")
    sdob.place(x=330, y=90, height=40)

    scontact = Label(top, text="Contact No.: ", font=("goudy ols style", 15, "bold"), fg="black")
    scontact.place(x=330, y=140, height=40)

    saddm = Label(top, text="Admission No.:   ", font=("goudy ols style", 15, "bold"), fg="black")
    saddm.place(x=330, y=190, height=40)

    scourse = Label(top, text="Courses: ", font=("goudy ols style", 15, "bold"), fg="black")
    scourse.place(x=330, y=240, height=40)

    course_list=[]
    fetch_course()      #function call to update the list
    txt_sdob = Entry(top, textvariable=var_sdob, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_sdob.place(x=480, y=90, height=40, width=150)

    txt_scontact = Entry(top, textvariable=var_scontact, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_scontact.place(x=480, y=140, height=40, width=150)

    txt_sadm = Entry(top, textvariable=var_sadm, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_sadm.place(x=480, y=190, height=40, width=150)

    txt_scourse = ttk.Combobox(top, textvariable=var_scourse, values=course_list,font=("goudy ols style", 15, "bold"), state="readonly", justify=CENTER)
    txt_scourse.place(x=480, y=240, height=40, width=150)
    txt_scourse.set("Select")
    #--------------------Buttons-----------------------------
    btn_add = Button(top, text="ADD", font=("goudy ols style", 10, "bold"), bg="blue", fg="white",cursor="hand2",command= add_course)
    btn_add.place(x=50, y=480, height=40, width=100)

    btn_update = Button(top, text="UPDATE", font=("goudy ols style", 10, "bold"), bg="orange", fg="white",cursor="hand2", command=update)
    btn_update.place(x=160, y=480, height=40, width=100)

    btn_delete = Button(top, text="DELETE", font=("goudy ols style", 10, "bold"), bg="maroon", fg="white",cursor="hand2",command=delete)
    btn_delete.place(x=280, y=480, height=40, width=100)

    btn_clear = Button(top, text="CLEAR", font=("goudy ols style", 10, "bold"), bg="brown", fg="white",cursor="hand2", command=clear)
    btn_clear.place(x=400, y=480, height=40, width=100)

    def get_record(e):
        txt_sroll.config(state="readonly")
        r=course_detail.focus()
        content=course_detail.item(r)
        row=content["values"]
        var_sroll.set(row[0]),
        var_sname.set(row[1]),
        var_semail.set(row[2]),
        var_sgender.set(row[3]),
        var_sdob.set(row[4]),
        var_scontact.set(row[5]),
        var_sadm.set(row[6]),
        var_scourse.set(row[7]),
        var_state.set(row[8]),
        var_city.set(row[9]),
        var_pin.set(row[10]),
        txt_add.delete("1.0", END)
        txt_add.insert(END,row[11])
    #----------------Search Panel-------------------------
    var_search=StringVar()
    lbl_search = Label(top, text="Roll Number: ", font=("goudy ols style", 15, "bold"), fg="black")
    lbl_search.place(x=650, y=90)
    # lbl_search.bind("<KeyPress-Down>", search_course())
    txt_search = Entry(top, textvariable=var_search, bg="lightyellow", font=("goudy ols style", 15, "bold"), fg="black")
    txt_search.place(x=930, y=90)

    btn_search = Button(top, text="SEARCH", font=("goudy ols style", 10, "bold"), bg="brown", fg="white", cursor="hand2",command=search_course)
    btn_search.place(x=1170, y=90)

    f1=Frame(top,bd=7, relief=RAISED)
    f1.place(x=650,y=150,height=500,width=630)

    scrolly=Scrollbar(f1,orient=VERTICAL)
    scrollx=Scrollbar(f1,orient=HORIZONTAL)

    course_detail=ttk.Treeview(f1,columns=("Roll","Name","Email","Gender","DOB","Contact","Admission","Course","State","City","Pin","Address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    scrollx.config(command=course_detail.xview)
    scrolly.config(command=course_detail.yview)

    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y )
    course_detail.heading("Roll",text="Roll Number")
    course_detail.heading("Name",text="Name")
    course_detail.heading("Email",text="Email ID")
    course_detail.heading("Gender",text="Gender")
    course_detail.heading("DOB", text="D.O.B")
    course_detail.heading("Contact", text="Contact")
    course_detail.heading("Admission", text="Admission")
    course_detail.heading("Course", text="Course")
    course_detail.heading("State", text="State")
    course_detail.heading("City", text="City")
    course_detail.heading("Pin", text="Pin Code")
    course_detail.heading("Address", text="Address")

    course_detail["show"]="headings"


    course_detail.column("Roll", width=100)
    course_detail.column("Name", width=100)
    course_detail.column("Email", width=100)
    course_detail.column("Gender", width=100)
    course_detail.column("DOB", width=100)
    course_detail.column("Contact", width=100)
    course_detail.column("Admission", width=100)
    course_detail.column("Course", width=100)
    course_detail.column("State", width=100)
    course_detail.column("City", width=100)
    course_detail.column("Pin", width=100)
    course_detail.column("Address", width=200)
    course_detail.pack(fill=BOTH, expand=1)

    course_detail.bind("<ButtonRelease-1>", get_record)
    show_course()

    top.mainloop()

def menu_result():
    top = Toplevel(root)
    top.geometry("1300x650+10+20")
    top.focus_force()

    # ------------------------FUNCTIONS----------------------------
    def fetch_roll():
        try:
            cr.execute("select Roll from student")
            rows = cr.fetchall()
            if len(rows) > 0:
                for row in rows:
                    roll_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=top)

    def search_course():
        try:
            cr.execute(f"select Name,Course from student where Roll=?",(var_roll.get(),))
            row=cr.fetchone()
            if row!=None:
                var_name.set(row[0])
                var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent=top)
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=top)

    def add_course():
        try:
            if var_name.get() ==" ":
                messagebox.showinfo("Error","Please first search student record",parent=top)
            else:
                cr.execute("select * from result where roll = ? and course=?",(var_roll.get(),var_course.get()))
                row=cr.fetchone()
                if(row!=None):
                    messagebox.showinfo("Error", "Result already present ", parent=top)
                else:
                    per=(int(var_marks.get())*100)/int(var_fullmarks.get())     #error if submit empty result
                    cr.execute("insert into result (roll,name,course,marks,fullmarks,per) values(?,?,?,?,?,?)",(var_roll.get(),var_name.get(),var_course.get(),var_marks.get(),var_fullmarks.get(),str(per)))
                    db.commit()
                    messagebox.showinfo("Success","Result added successfully", parent=top)

        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=top)

    def clear():
        var_roll.set("Select")
        var_name.set(" ")
        var_course.set(" ")
        var_marks.set(" ")
        var_fullmarks.set(" ")

    title = Label(top,text="Add Student Result",font=("goudy ols style",20,"bold"),bg="black",fg="white",height=50)
    title.place(x=0,y=0,height=70,relwidth=1)
    lbl_select = Label(top, text="Select Student: ", font=("goudy ols style", 15, "bold"), bg="white")
    lbl_select.place(x=50, y=100)
    lbl_name=Label(top,text="Name:",font=("goudy ols style",15,"bold"),bg="white")
    lbl_name.place(x=50,y=160)
    lbl_course=Label(top,text="Course:", font=("goudy ols style",15,"bold"),bg="white")
    lbl_course.place(x=50,y=220)
    lbl_marks=Label(top,text="Marks Obtained:",font=("goudy ols style",15,"bold"),bg="white")
    lbl_marks.place(x=50,y=280)
    lbl_fullmarks=Label(top,text="Full MArks:",font=("goudy ols style",15,"bold"),bg="white")
    lbl_fullmarks.place(x=50,y=340)

    var_roll = StringVar()
    var_name = StringVar()
    var_course = StringVar()
    var_marks = StringVar()
    var_fullmarks = StringVar()
    roll_list=[]
    fetch_roll()
    txt_student = ttk.Combobox(top, textvariable=var_roll, values=roll_list,font=("goudy ols style", 15, "bold"), state="readonly", justify=CENTER)
    txt_student.place(x=280, y=100, width=200)
    txt_student.set("Select")
    btn_search = Button(top, text="SEARCH", font=("goudy ols style", 10, "bold"), bg="blue", fg="white",cursor="hand2", command=search_course)
    btn_search.place(x=500, y=100,height=30, width=100)

    txt_name = Entry(top, textvariable=var_name, bg="lightyellow", font=("goudy ols style", 20, "bold"),state="readonly")
    txt_name.place(x=280, y=160,  width=320)
    txt_course = Entry(top, textvariable=var_course, bg="lightyellow", font=("goudy ols style", 20, "bold"),state="readonly")
    txt_course.place(x=280, y=220,  width=320)
    txt_marks = Entry(top, textvariable=var_marks, bg="lightyellow", font=("goudy ols style", 20, "bold"))
    txt_marks.place(x=280, y=280, width=320)
    txt_fullmarks = Entry(top, textvariable=var_fullmarks, bg="lightyellow", font=("goudy ols style", 20, "bold"))
    txt_fullmarks.place(x=280, y=340, width=320)

    btn_submit = Button(top, text="Submit", font=("goudy ols style", 15), bg="lightgreen",activebackground="lightgreen" , cursor="hand2",command=add_course)
    btn_submit.place(x=300, y=420, height=35, width=120)
    btn_clear = Button(top, text="Clear", font=("goudy ols style", 15), bg="lightgrey",activebackground="lightgrey", cursor="hand2",command=clear)
    btn_clear.place(x=430, y=420, height=35, width=120)

    bg_img = Image.open("images/bg.png")
    bg_img = bg_img.resize((500, 300), Image.ANTIALIAS)
    bg_img = ImageTk.PhotoImage(bg_img)
    lbl_bg = Label(top, image=bg_img)
    lbl_bg.place(x=650, y=100)


    top.mainloop()

def menu_report():
    top = Toplevel(root)
    top.geometry("1300x650+10+20")
    top.focus_force()

    def search():
        try:
            if var_search.get()=="":
                messagebox.showerror("Error","Roll number reqiured",parent=top)
            else:
                cr.execute(f"select * from result where Roll=?",(var_search.get(),))
                row=cr.fetchone()
                if row!=None:
                    var_id =row[0]           #dynamic
                    roll.config(text=row[1])
                    name.config(text=row[2])
                    course.config(text=row[3])
                    marks.config(text=row[4])
                    fullmarks.config(text=row[5])
                    per.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record found",parent=top)
        except Exception as ex:
            messagebox.showerror("Error",f"Error found Due to {ex} ",parent=top)

    def clear():
        roll.config(text=" ")
        name.config(text=" ")
        course.config(text=" ")
        marks.config(text=" ")
        fullmarks.config(text=" ")
        per.config(text=" ")
        var_search.set("")
        # var_id=""

    def delete():
        try:
            if var_id== "":
                messagebox.showinfo("Error", "Search student result first", parent=top)
            else:
                cr.execute("select * from result where rid = ?", (var_id,))
                row = cr.fetchone()
                if (row == None):
                    messagebox.showinfo("Error", "Invalid student result", parent=top)
                else:
                    cr.execute("delete from result where rid =?",
                               (var_id,))
                    db.commit()
                    messagebox.showinfo("Delete","Result deleted successfully",parent=top)

                    clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error found Due to {ex} ", parent=top)


    title = Label(top, text="View Student Result", font=("goudy ols style", 20, "bold"), bg="black", fg="white",height=50)
    title.place(x=0, y=0, height=70, relwidth=1)

    var_id = " "
    var_search=StringVar()
    lbl_search = Label(top, text="Search by roll number: ", font=("goudy ols style", 15, "bold"), bg="white")
    lbl_search.place(x=280, y=100)
    txt_search = Entry(top, textvariable=var_search, font=("goudy ols style", 15), bg="lightyellow")
    txt_search.place(x=520, y=100,width=150)

    btn_search = Button(top, text="SEARCH", font=("goudy ols style", 10, "bold"), bg="blue", fg="white", cursor="hand2",command=search)
    btn_search.place(x=680, y=100, height=35, width=100)
    btn_clear = Button(top, text="CLEAR", font=("goudy ols style", 10, "bold"), bg="grey", fg="white", cursor="hand2",command=clear)
    btn_clear.place(x=800, y=100, height=35, width=100)

    lbl_roll = Label(top, text="Roll No.", font=("goudy ols style", 15, "bold"), bg="white",bd=2,relief=GROOVE)
    lbl_roll.place(x=150, y=230,height=50,width=150)
    lbl_name = Label(top, text="Name", font=("goudy ols style", 15, "bold"), bg="white",bd=2,relief=GROOVE)
    lbl_name.place(x=300, y=230,height=50,width=150)
    lbl_course = Label(top, text="Course", font=("goudy ols style", 15, "bold"), bg="white",bd=2,relief=GROOVE)
    lbl_course.place(x=450, y=230,height=50,width=150)
    lbl_marks = Label(top, text="Marks Obtained", font=("goudy ols style", 15, "bold"), bg="white",bd=2,relief=GROOVE)
    lbl_marks.place(x=600, y=230,height=50,width=150)
    lbl_fullmarks = Label(top, text="Total MArks", font=("goudy ols style", 15, "bold"), bg="white",bd=2,relief=GROOVE)
    lbl_fullmarks.place(x=750, y=230,height=50,width=150)
    lbl_per = Label(top, text="Percentage", font=("goudy ols style", 15, "bold"), bg="white",bd=2,relief=GROOVE)
    lbl_per.place(x=900, y=230,height=50,width=150)

    roll = Label(top, font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
    roll.place(x=150, y=280, height=50, width=150)
    name = Label(top, font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
    name.place(x=300, y=280, height=50, width=150)
    course = Label(top, font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
    course.place(x=450, y=280, height=50, width=150)
    marks = Label(top, font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
    marks.place(x=600, y=280, height=50, width=150)
    fullmarks = Label(top, font=("goudy ols style", 15, "bold"), bg="white", bd=2,relief=GROOVE)
    fullmarks.place(x=750, y=280, height=50, width=150)
    per = Label(top, font=("goudy ols style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
    per.place(x=900, y=280, height=50, width=150)

    btn_delete = Button(top, text="Delete", font=("goudy ols style", 10, "bold"), bg="red", fg="white", cursor="hand2",command=delete)
    btn_delete.place(x=500, y=350, height=35, width=150)

    top.mainloop()
#---------------------CREATING DASHBOARD------------------------
#-------------------icons------------------
logo=Image.open("images/img.jpg")
logo=logo.resize((50,50),Image.ANTIALIAS)
logo=ImageTk.PhotoImage(logo)
#-------------------menu-------------------
title=Label(root,text="Student Result Management System", padx=20, font=("goudy ols style",20,"bold"),bg="black",fg="white",image=logo,compound=LEFT,height=50)
title.place(x=0,y=0,height=70,width=1350)
#
my_frame=LabelFrame(root,text="Menu Card",font=("goudy ols style",15,"bold"),bg="white",fg="blue",height=50)
my_frame.place(x=10,y=100,height=120,width=1320)

b1=Button(my_frame,text="Course", font=("goudy ols style",15,"bold"),bg="blue",fg="white",cursor="hand2",command=menu_course)
b1.place(x=12,y=5,height=70,width=204)

b2=Button(my_frame,text="Student", font=("goudy ols style",15,"bold"),bg="blue",fg="white",cursor="hand2",command=menu_student)
b2.place(x=228,y=5,height=70,width=204)

b3=Button(my_frame,text="Result", font=("goudy ols style",15,"bold"),bg="blue",fg="white",cursor="hand2",command=menu_result)
b3.place(x=444,y=5,height=70,width=204)

b4=Button(my_frame,text="View Result", font=("goudy ols style",15,"bold"),bg="blue",fg="white",cursor="hand2",command=menu_report)
b4.place(x=660,y=5,height=70,width=204)

b5=Button(my_frame,text="Log Out", font=("goudy ols style",15,"bold"),bg="blue",fg="white",cursor="hand2")
b5.place(x=876,y=5,height=70,width=204)

b6=Button(my_frame,text="Exit", font=("goudy ols style",15,"bold"),bg="blue",fg="white",cursor="hand2")
b6.place(x=1092,y=5,height=70,width=204)

# my_frame2=LabelFrame(root,text="Menu Card",font=("goudy ols style",15,"bold"),bg="white",fg="blue",height=50)
# my_frame2.place(x=10,y=250,height=120,width=1320)
#
# b1=Button(my_frame2,text="Course", font=("goudy ols style",15,"bold"),bg="blue",fg="white")
# b1.place(x=2,y=5,height=70,width=170)
#
# b2=Button(my_frame2,text="Course", font=("goudy ols style",15,"bold"),bg="blue",fg="white")
# b2.place(x=190,y=5,height=70,width=170)
#
# b3=Button(my_frame2,text="Course", font=("goudy ols style",15,"bold"),bg="blue",fg="white")
# b3.place(x=378,y=5,height=70,width=170)
#
# b4=Button(my_frame2,text="Course", font=("goudy ols style",15,"bold"),bg="blue",fg="white")
# b4.place(x=566,y=5,height=70,width=170)

# b5=Button(my_frame2,text="Course", font=("goudy ols style",15,"bold"),bg="blue",fg="white")
# b5.place(x=754,y=5,height=70,width=170)

# b6=Button(my_frame2,text="Course", font=("goudy ols style",15,"bold"),bg="blue",fg="white")
# b6.place(x=942,y=5,height=70,width=170)

# b7=Button(my_frame2,text="Course", font=("goudy ols style",15,"bold"),bg="blue",fg="white")
# b7.place(x=1130,y=5,height=70,width=170)

# logo=Image.open("img.png")
# logo=logo.resize((30,30),Image.ANTIALIAS)
# logo=ImageTk.PhotoImage(logo)

#----------------------content window------------------------------

bg_img=Image.open("images/bg.png")
bg_img=bg_img.resize((920,350),Image.ANTIALIAS)
bg_img=ImageTk.PhotoImage(bg_img)

lbl_student=Label(root,image=bg_img)
lbl_student.place(x=700, y=250,width=620, height=300)

course=Label(root,text="Total Courses \n[0]",font=("goudy ols style",15,"bold"),bg="orange",fg="white",bd=5, relief=RIDGE)
course.place(x=700,y=570,height=70,width=190)

student=Label(root,text="Total Students \n[0]",font=("goudy ols style",15,"bold"),bg="red",fg="white",bd=5, relief=SUNKEN)
student.place(x=900,y=570,height=70,width=190)

result=Label(root,text="Total Results \n[0]",font=("goudy ols style",15,"bold"),bg="maroon",fg="white",bd=5, relief=RAISED)
result.place(x=1100,y=570,height=70,width=190)
#------------------------------footer-----------------------
footer=Label(root,text="SRMS - Student Result Management System \n contact us 9251420811", font=("goudy ols style",10,"bold"),bg="black",fg="white")
footer.pack(side=BOTTOM, fill=X)

# footer2=Label(root,text="SMRS - Student Management", padx=15,font=("goudy ols style",10,"bold"),bg="white",fg="black",image=logo,compound=LEFT,height=50)
# footer2.place(x=950,y=650)

# footer2=Label(root,text="SMRS - Student Management", padx=15,font=("goudy ols style",10,"bold"),bg="white",fg="black",image=logo,compound=LEFT,height=50)
# footer2.place(x=70,y=650)

root.mainloop()