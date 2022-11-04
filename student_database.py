import sqlite3

def create_db():
    db = sqlite3.connect(database="student_project.db")
    cr = db.cursor()
    cr.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY , name TEXT, duration TEXT, charges TEXT, description TEXT )")
    db.commit()
    # cr.execute("DROP TABLE course")
    # db.commit()

    cr.execute("CREATE TABLE IF NOT EXISTS student(Roll INTEGER PRIMARY KEY,Name text,Email text,Gender text,DOB text,Contact text,Admission text,Course text,State text,City text,Address text )")
    db.commit()
    # cr.execute("DROP TABLE student")
    # db.commit()

    cr.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY , roll TEXT, name TEXT, course TEXT, marks_ob TEXT, full_marks TEXT,per TEXT )")
    db.commit()
    # cr.execute("DROP TABLE result")
    # db.commit()



create_db()