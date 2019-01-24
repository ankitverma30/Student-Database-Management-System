import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import ttk
import tkinter.messagebox

xWindow = tk.Tk()
xWindow.title("Welcome!")

label1 = Label(xWindow, text="What you are : ", fg="#0000A0", width="100")
label1.grid(row=0, column=2, padx=(30, 30), pady=(30, 0))

connection = sqlite3.connect('Student.db')
print('Database Created Successfully')

cursor = connection.cursor()

TABLE_NAME5 = 'marks_table'
STUDENT_ID = 'student_id'
STUDENT_NAME2 = 'student_name'
MATHS_MARKS = 'maths_marks'
CHEM_MARKS = 'chem_marks'
PHYSICS_MARKS = 'physics_marks'
ENGLISH_MARKS = 'english_marks'
SAP_ID = 'sap_id'
PASS = "password"

TABLE_NAME = 'student_table'
STUDENT_NAME = 'student_name'
FATHERS_NAME = 'father_name'
MOTHERS_NAME = "mother_name"
STUDENT_COURSE = 'student_course'
LOGIN_ID = 'logi_id'
PASSWORD = 'pass'
SAP_ID2 = 'sap_id'

TABLE_NAME2="admin_table"
ADMIN_LOGIN="login"
PASSWORD2="pwd"


TABLE_NAME8='teacher_table'
TEACHER_ID='teacher_id'
PASSWORD3='password'

conn = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME8 + " ( " + TEACHER_ID + " TEXT , " + PASSWORD3 + " TEXT );"
if (connection.execute(conn)):
    print("Teacher Table Created Succesfully")
conn = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME2 + " ( " + ADMIN_LOGIN + " TEXT , " + PASSWORD2 + " TEXT );"
if (connection.execute(conn)):
    print("Admin Table Created Succesfully")
if(connection.execute("INSERT INTO " + TABLE_NAME2 + "( " + ADMIN_LOGIN + " , " + PASSWORD2  + " ) VALUES ( 'admin','pwd')")):
        print ("Record Updated")
        connection.commit()
conn = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME5 + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + SAP_ID + " NUMBER , " + PASS + " TEXT , " + STUDENT_NAME2 + " TEXT , " + MATHS_MARKS + " INTEGER, " + CHEM_MARKS + " INTEGER, " + PHYSICS_MARKS + " INTEGER, " + LOGIN_ID + " TEXT, "+ENGLISH_MARKS+" INTEGER );"
if (connection.execute(conn)):
        print("Table Created Succesfully")
conn = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + STUDENT_NAME + " TEXT NOT NULL, " + FATHERS_NAME + " TEXT, " + MOTHERS_NAME + " TEXT, " + LOGIN_ID + " TEXT, " + SAP_ID2 + " NUMBER, " + PASSWORD + " TEXT, " + STUDENT_COURSE + " TEXT);"
if (connection.execute(conn)):
        print("Table 2 Created Succesfully")


def student():
    xWindow.destroy()
    mainWindow = tk.Tk()

    mainWindow.title("Student Login")
    label1 = Label(mainWindow, text="Student Login", fg="#0000A0", width="100")
    label1.grid(row=0,columnspan=2, padx=(30, 30), pady=(30,30))

    loginLabel = Label(mainWindow, text="Enter Your Login ID", width="40", fg="#FF0000")
    loginLabel.grid(row=1, column=0, padx=(30, 30), pady=(30,30))

    loginvar = Entry(mainWindow)
    loginvar.grid(row=1, column=1)

    pwdLabel = Label(mainWindow, text="Enter Your Password", width="40", fg="#FF0000")
    pwdLabel.grid(row=2, column=0, padx=(30, 30), pady=(30,30))

    pwdvar = Entry(mainWindow)
    pwdvar.grid(row=2, column=1)

    def submit():

        login = loginvar.get()
        loginvar.delete(0, END)

        passw = pwdvar.get()
        pwdvar.delete(0, END)

        cursor2=connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE " + LOGIN_ID + " = '" + login + "' AND " +PASSWORD+" = '"+passw+"';")
        print(cursor2)
        a = ""
        b = ""

        for row in cursor2:
            a=row[4]
            b=row[6]

        if(login==a and passw==b):
            cursor2 = connection.execute("SELECT * FROM " + TABLE_NAME5 + " WHERE " + LOGIN_ID + " = '" + login + "' ;")
            i=0

            for row in cursor2:
             markse=row[8]
             nam=row[3]
             print(markse)

             if(markse==None):
                 seventhwindow=tk.Tk()
                 seventhwindow.title("Result Declaration")
                 label888=tk.Label(seventhwindow,text="Sorry "+nam+"  ! You Have not been graded yet!!",width=40, fg="#FF0000")
                 label888.config(font=("Sylfaen", 30))
                 label888.pack()
                 def destri():
                     seventhwindow.destroy()
                 distButton = tk.Button(seventhwindow, text="Ok", command=lambda: destri)
                 distButton.pack()

                 seventhwindow.mainloop()
             else:
                mainWindow.destroy()
                fifthWindow = tk.Tk()
                fifthWindow.title("Result Declaration")

                label5 = tk.Label(fifthWindow, text="Result", width=40, fg="#FF0000")
                label5.config(font=("Sylfaen", 30))
                label5.pack()

                tree = ttk.Treeview(fifthWindow)

                tree["columns"] = ("one", "two", "three", "four", "five", "six")
                tree.column("one", width=200)
                tree.column("two", width=200)
                tree.column("three", width=200)
                tree.column("four", width=200)
                tree.column("five", width=200)
                tree.column("six", width=200)
                tree.heading("one", text="Student Name")
                tree.heading("two", text="English Marks")
                tree.heading("three", text="Maths Marks")
                tree.heading("four", text="Physics Marks")
                tree.heading("five", text="Chemistry Marks")
                tree.heading("six", text=" Login")

                cursor2 = connection.execute("SELECT * FROM " + TABLE_NAME5 + " WHERE "+LOGIN_ID+" = '"+login+"' ;")
                i = 0
                for row in cursor2:
                    tree.insert('', i, text=str(row[0]),
                                values=(row[3], row[8], row[4], row[6], row[5], row[7]))
                    i = i + 1
                    var=0
                    var=(int(row[8])+int(row[4])+int(row[6])+int(row[5]))/4
                    if int(var)>35:
                        label88 = tk.Label(fifthWindow, text="Congratulation "+str(row[3])+" ! You have secured "+str(var)+"%age", width=100, fg="#FF0000")
                        label88.config(font=("Sylfaen", 20))
                        label88.pack()
                    else:
                        label99= tk.Label(fifthWindow,text="Sorry  " +str(row[3]) + "! You have secured "+ str(var)+ "%age"+". ", width=80,
                                           fg="#FF0000")
                        label99.config(font=("Sylfaen", 20))
                        label99.pack()

                tree.pack()

                fifthWindow.mainloop()

        else:
            tkinter.messagebox.showinfo('Sorry', "Your login ID or password does not exist")
    def signup():
            mainWindow.destroy()

            secondWindow = tk.Tk()
            secondWindow.title("Welcome!")

            fatherLabel = Label(secondWindow, text="Enter Your fathers's Name", width="40", fg="#FF0000")
            fatherLabel.grid(row=1, column=0,padx=(30, 30), pady=(30,30))

            fathervar = Entry(secondWindow)
            fathervar.grid(row=1, column=1, padx=(30, 30), pady=(30,30))

            motherLabel = Label(secondWindow, text="Enter Your Mother's Name", width="40", fg="#FF0000")
            motherLabel.grid(row=2, column=0, padx=(30, 30), pady=(30,30))

            mothervar = Entry(secondWindow)
            mothervar.grid(row=2, column=1, padx=(30, 30), pady=(30,30))

            courseLabel = Label(secondWindow, text="Enter Your Selected Course", width="40", fg="#FF0000")
            courseLabel.grid(row=3, column=0, padx=(30, 30), pady=(30,30))

            coursevar = Entry(secondWindow)
            coursevar.grid(row=3, column=1, padx=(30, 30), pady=(30,30))

            sapLabel = Label(secondWindow, text="Enter Your Enrollment No.", width="40", fg="#FF0000")
            sapLabel.grid(row=4, column=0,padx=(30, 30), pady=(30,30))

            sapvar2 = Entry(secondWindow)
            sapvar2.grid(row=4, column=1, padx=(30, 30), pady=(30,30))

            loginLabel = Label(secondWindow, text="Create Login ID", width="40", fg="#FF0000")
            loginLabel.grid(row=5, column=0, padx=(30, 30), pady=(30,30))

            loginvar2 = Entry(secondWindow)
            loginvar2.grid(row=5, column=1, padx=(30, 30), pady=(30,30))

            pwadLabel = Label(secondWindow, text="Create password ", width="40", fg="#FF0000")
            pwadLabel.grid(row=6, column=0, padx=(30, 30), pady=(30,30))

            pwdvar2 = Entry(secondWindow)
            pwdvar2.grid(row=6, column=1, padx=(30, 30), pady=(30,30))


            def submit2():

                father = fathervar.get()
                fathervar.delete(0, END)

                mother = mothervar.get()
                mothervar.delete(0, END)

                course = coursevar.get()
                coursevar.delete(0, END)

                sapp=sapvar2.get()
                sapvar2.delete(0,END)

                logi= loginvar2.get()
                loginvar2.delete(0, END)

                pwwd=pwdvar2.get()
                pwdvar2.delete(0,END)

                cursor3 = connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE " + SAP_ID + " = " +sapp+" ;")
                b=0
                for row in cursor3:
                    b= row[5]
                    print(b)

                if(int(sapp)==b):
                    connection.execute("UPDATE " + TABLE_NAME + " SET  " + FATHERS_NAME + "= '" + father + "' ,"+STUDENT_COURSE + "= '" + course + "' ," + MOTHERS_NAME + "= '" + mother + "' ," + LOGIN_ID + "= '" + logi + "' , " + PASSWORD + "= '" + pwwd + "' WHERE " + SAP_ID + "= " + sapp + " ;")
                    print("Record Updated ")
                    connection.commit()
                    connection.execute("UPDATE " + TABLE_NAME5 + " SET " + LOGIN_ID  + " = '" + logi + "' WHERE " + SAP_ID + " = " + sapp + " ;")
                    print("Record Updated ")
                    tkinter.messagebox.showinfo('Ok', str(sapp) + " record has updated!")
                    connection.commit()
                else:
                    tkinter.messagebox.showinfo('Sorry', "Your Enrollement ID does not exist.Reenter your Enrollement ID or contact admin Depratment")

            def destroy2():
                secondWindow.destroy()
                sixthWindow = tk.Tk()
                sixthWindow.title("Student Database Management System")
                label5 = tk.Label(sixthWindow, text="Student Management System", width=40, fg="#FF0000")
                label5.config(font=("Sylfaen", 30))
                label5.pack()

                tree = ttk.Treeview(sixthWindow)

                tree["columns"] = ("one", "two", "three", "four", "five")
                tree.column("one", width=200)
                tree.column("two", width=200)
                tree.column("three", width=200)
                tree.column("four", width=200)
                tree.column("five", width=200)
                tree.heading("one", text="Student Name")
                tree.heading("two", text="Father Name")
                tree.heading("three", text="Mother Name")
                tree.heading("four", text="Student Course")
                tree.heading("five", text="SAP ID")

                cursor2 = connection.execute("SELECT * FROM " + TABLE_NAME + ";")
                i = 0
                for row in cursor2:
                    tree.insert('', i, text=str(row[0]),
                                values=(row[1], row[2], row[7], row[3],
                                        row[5]))
                    i = i + 1
                tree.pack()
                sixthWindow.mainloop()

            button1 = tk.Button(secondWindow, text="Submit", command=lambda: submit2())
            button1.grid(row=7, column=0, padx=(30, 30), pady=(30,30))

            displayButton = tk.Button(secondWindow, text="Display", command=lambda: destroy2())
            displayButton.grid(row=7, column=2, padx=(30, 30), pady=(30,30))

            secondWindow.mainloop()

    button2 = tk.Button(mainWindow, text="Submit", command=lambda: submit())
    button2.grid(row=3, column=1,padx=(30, 30), pady=(30,30))
    signupButton = tk.Button(mainWindow, text="Signup", command=lambda: signup())
    signupButton.grid(row=3, column=0,padx=(30, 30), pady=(30,30))
    mainWindow.mainloop()

def teacher():
    xWindow.destroy()
    cWindow = tk.Tk()
    cWindow.title("Teacher")

    loginLabel55 = Label(cWindow, text="Enter Your login ID", width="40", fg="#FF0000")
    loginLabel55.grid(row=1, column=0, padx=(30,30), pady=(30,30))

    loginvar55 = Entry(cWindow)
    loginvar55.grid(row=1, column=1, padx=(30,30), pady=(30,30))

    pwdLabel22 = Label(cWindow, text="Enter Your Password", width="40", fg="#FF0000")
    pwdLabel22.grid(row=2, column=0, padx=(30,30), pady=(30,30))

    pwdvar22 = Entry(cWindow)
    pwdvar22.grid(row=2, column=1, padx=(30,30), pady=(30,30))

    def submittea():
        login8 = loginvar55.get()
        loginvar55.delete(0, END)

        pas = pwdvar22.get()
        pwdvar22.delete(0, END)

        cursor2 = connection.execute(
            "SELECT * FROM " + TABLE_NAME8 + " WHERE " + TEACHER_ID + " = '" + login8 + "' AND " + PASSWORD3 + " = '" + pas + "';")
        a = ""
        b = ""

        for row in cursor2:
            a = row[0]
            b = row[1]

        if (login8 == a and pas == b):
            cWindow.destroy()
            thirdWindow = tk.Tk()
            thirdWindow.title("Teacher")

            label33 = Label(thirdWindow, text="Prepare Report ", fg="#0000A0", width="100")
            label33.grid(row=0, columnspan=2, padx=(30, 30), pady=(30, 0))

            sapLabel = Label(thirdWindow, text="Enter Enrollment No. of Student", width="40", fg="#FF0000")
            sapLabel.grid(row=2, column=0, padx=(30, 0))

            sapvar2 = Entry(thirdWindow)
            sapvar2.grid(row=2, column=1)

            mathLabel = Label(thirdWindow, text="Enter Maths Marks of Student", width="40", fg="#FF0000")
            mathLabel.grid(row=4, column=0, padx=(30, 0))

            mathvar = Entry(thirdWindow)
            mathvar.grid(row=4, column=1)

            physicsLabel = Label(thirdWindow, text="Enter Physics Marks of Student", width="40", fg="#FF0000")
            physicsLabel.grid(row=5, column=0, padx=(30, 0))

            physicsvar = Entry(thirdWindow)
            physicsvar.grid(row=5, column=1)

            chemLabel = Label(thirdWindow, text="Enter Chemistry Marks of Student", width="40", fg="#FF0000")
            chemLabel.grid(row=6, column=0, padx=(30, 0))

            chemvar = Entry(thirdWindow)
            chemvar.grid(row=6, column=1)

            englishLabel = Label(thirdWindow, text="Enter English Marks of student", width="40", fg="#FF0000")
            englishLabel.grid(row=7, column=0, padx=(30, 0))

            englishvar = Entry(thirdWindow)
            englishvar.grid(row=7, column=1)

            def submite():

                math = mathvar.get()
                mathvar.delete(0, END)

                physics = physicsvar.get()
                physicsvar.delete(0, END)

                chemistry = chemvar.get()
                chemvar.delete(0, END)

                english = englishvar.get()
                englishvar.delete(0, END)

                sap= sapvar2.get()
                sapvar2.delete(0, END)

                cursor3 = connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE " + SAP_ID + " = " + sap + " ;")
                b = 0
                for row in cursor3:
                    b = row[5]
                    print(b)

                if (int(sap) == b):
                    connection.execute("UPDATE " + TABLE_NAME5 + " SET  "+ MATHS_MARKS +"= '"+math+"' ,"+ ENGLISH_MARKS +"= '"+english+"' ,"+PHYSICS_MARKS +"= '"+physics+"' , "+ CHEM_MARKS +"= '"+chemistry+"' WHERE "+SAP_ID+"= "+sap+" ;")
                    print("Record Updated ")
                    tkinter.messagebox.showinfo('Ok',str(sap)+" record has updated!")
                    connection.commit()
                else:
                    tkinter.messagebox.showinfo('Error', "Student Enrollment "+str(sap) + " does not exit! Contact Admin.")

            def destroyee():
                eightWindow=tk.Tk()
                eightWindow.title("Student Database ")

                label5=tk.Label(eightWindow,text="Student Management System",width=40,fg="#FF0000")
                label5.config(font=("Sylfaen",30))
                label5.pack()

                tree=ttk.Treeview(eightWindow)

                tree["columns"]=("one","two","three","four","five","six")
                tree.column("one",width=200)
                tree.column("two",width=200)
                tree.column("three",width=200)
                tree.column("four",width=200)
                tree.column("five",width=200)
                tree.column("six", width=200)
                tree.heading("one",text="SAP ID ")
                tree.heading("two",text="Student Name")
                tree.heading("three",text="Maths Marks")
                tree.heading("four",text="Physics Marks")
                tree.heading("five",text="Chemistry Marks")
                tree.heading("six", text="English Marks")

                cursor2=connection.execute("SELECT * FROM "+TABLE_NAME5+";")
                i=0
                for row in cursor2:
                    tree.insert('', i,text=str(row[0]),
                                    values=(row[1],row[3],row[4],row[5],row[6],row[8]))
                    i=i+1
                tree.pack()

                eightWindow.mainloop()

            button3 = tk.Button(thirdWindow, text="Submit", command=lambda: submite())
            button3.grid(row=8, column=0,padx=(20,10),pady=(20,20))
            button4 = tk.Button(thirdWindow, text="Display", command=lambda: destroyee())
            button4.grid(row=8, column=1,padx=(20,10),pady=(20,20))
            thirdWindow.mainloop()
        else:
            tkinter.messagebox.showinfo('Error', "Sorry! Incorrect ID or PASSWORD")
    buttonmm = tk.Button(cWindow, text="Submit", command=lambda: submittea())
    buttonmm.grid(row=3, column=1)

    cWindow.mainloop()


def admin():
    xWindow.destroy()

    yWindow = tk.Tk()
    yWindow.title("Welcome!")

    loginLabel2 = Label(yWindow, text="Enter Your ADMIN ID", width="40", fg="#FF0000")
    loginLabel2.grid(row=1, column=0, padx=(30,30),pady=(30,30))

    loginvar2 = Entry(yWindow)
    loginvar2.grid(row=1, column=1,padx=(30,30),pady=(30,30))

    pwdLabel2 = Label(yWindow, text="Enter Your Password", width="40", fg="#FF0000")
    pwdLabel2.grid(row=2, column=0, padx=(30,30),pady=(30,30))

    pwdvar2 = Entry(yWindow)
    pwdvar2.grid(row=2, column=1,padx=(30,30),pady=(30,30))


    def submitadm():

        login22 = loginvar2.get()
        loginvar2.delete(0, END)

        passww = pwdvar2.get()
        pwdvar2.delete(0, END)

        cursor2 = connection.execute("SELECT * FROM " + TABLE_NAME2+ " WHERE " + ADMIN_LOGIN + " = '" + login22+ "' AND " + PASSWORD2 + " = '" + passww + "';")
        print(cursor2)
        a = ""
        b = ""

        for row in cursor2:
            a = row[0]
            b = row[1]

        if (login22 == a and passww == b):
            yWindow.destroy()
            hWindow=tk.Tk()
            hWindow.title("Update Record")

            label1 = Label(hWindow, text="Add New Student Or Teacher: ", fg="#0000A0", width="100")
            label1.grid(row=0, column=2, padx=(30, 30), pady=(30, 0))


            def submitww():
                zWindow = tk.Tk()
                zWindow.title('Update Student Record')

                sapLabel2 = Label(zWindow, text="Enter Enrollment No. for Student", width="40", fg="#FF0000")
                sapLabel2.grid(row=1, column=0, padx=(30, 30), pady=(30, 30))

                sapvar2 = Entry(zWindow)
                sapvar2.grid(row=1, column=1, padx=(30, 30), pady=(30, 30))

                nameLabel2 = Label(zWindow, text="Enter Name of Student ", width="40", fg="#FF0000")
                nameLabel2.grid(row=2, column=0, padx=(30, 30), pady=(30, 30))

                nmvar2 = Entry(zWindow)
                nmvar2.grid(row=2, column=1, padx=(30, 30), pady=(30, 30))

                def update():
                    sp = sapvar2.get()
                    sapvar2.delete(0, END)

                    nm = nmvar2.get()
                    nmvar2.delete(0, END)

                    if connection.execute(
                            "INSERT INTO " + TABLE_NAME + " ( " + SAP_ID + ", " + STUDENT_NAME2 + " ) VALUES ( " + sp + ", '" + nm + "' ); "):
                        print("Record Updated ")
                        connection.commit()

                    if connection.execute(
                            "INSERT INTO " + TABLE_NAME5 + " ( " + SAP_ID + ", " + STUDENT_NAME2 + " ) VALUES ( " + sp + ", '" + nm + "' ); "):
                        print("Record Updated ")
                        tkinter.messagebox.showinfo('Ok', str(sp) + " record has updated!")
                        connection.commit()

                button4 = tk.Button(zWindow, text="Update", command=lambda: update(), bg="#FFC0CB", fg="#0000A0",
                                    bd=8)
                button4.grid(row=3, column=1, padx=(30, 30), pady=(30, 30))
                zWindow.mainloop()
            def teacherw():
                zWindow = tk.Tk()
                zWindow.title('Update Teacher Record')

                logLabel2 = Label(zWindow, text="Enter Login ID for Teacher", width="40", fg="#FF0000")
                logLabel2.grid(row=1, column=0, padx=(30, 30), pady=(30, 30))

                logvar2 = Entry(zWindow)
                logvar2.grid(row=1, column=1, padx=(30, 30), pady=(30, 30))

                pwdLabe = Label(zWindow, text="Enter Password for Teacher", width="40", fg="#FF0000")
                pwdLabe.grid(row=2, column=0, padx=(30, 30), pady=(30, 30))

                pwddvar2 = Entry(zWindow)
                pwddvar2.grid(row=2, column=1, padx=(30, 30), pady=(30, 30))

                def update():
                    spp = logvar2.get()
                    logvar2.delete(0, END)

                    nmaa = pwddvar2.get()
                    pwddvar2.delete(0, END)

                    if connection.execute(
                            "INSERT INTO " + TABLE_NAME8 + " ( " + TEACHER_ID + ", " + PASSWORD3 + " ) VALUES ( '" + spp + "' , '" + nmaa + "' ); "):
                        print("Record Updated ")
                        tkinter.messagebox.showinfo('Ok', str(spp) + " record has updated!")
                        connection.commit()

                button4 = tk.Button(zWindow, text="Update", command=lambda: update(), bg="#FFC0CB", fg="#0000A0",
                                    bd=8)
                button4.grid(row=3, column=1, padx=(30, 30), pady=(30, 30))
                zWindow.mainloop()

            buttonu = tk.Button(hWindow, text="Student", command=lambda: submitww(), height=10, width=50, bg="#FFC0CB",
                                fg="#0000A0", bd=8)
            buttonu.grid(row=1, column=2, padx=(30, 30), pady=(30, 30))

            buttonhh = tk.Button(hWindow, text="Teacher", command=lambda: teacherw(), height=10, width=50, bg="#FFC0CB",
                                fg="#0000A0", bd=8)
            buttonhh.grid(row=2, column=2, padx=(30, 30), pady=(30, 30))

            hWindow.mainloop()

        else:
            tkinter.messagebox.showinfo('Error', "Sorry! Incorrect ID or PASSWORD")

    button4 = tk.Button(yWindow, text="Submit", command=lambda: submitadm(), bg="#FFC0CB",fg="#0000A0", bd=8)
    button4.grid(row=3, column=1, padx=(30, 30), pady=(30,30))
    yWindow.mainloop()

button2 = tk.Button(xWindow, text="Student", command=lambda: student(),height=10,width=50,bg="#FFC0CB",fg="#0000A0",bd=8)
button2.grid(row=1, column=2,padx=(30, 30), pady=(30,30))

buttont=tk.Button(xWindow,text="Teacher",command=lambda : teacher(),height=10,width=50,bg="#FFC0CB",fg="#0000A0",bd=8)
buttont.grid(row=2,column=2,padx=(30, 30), pady=(30,30))

buttont=tk.Button(xWindow,text="Admin",command=lambda : admin(),height=10,width=50,bg="#FFC0CB",fg="#0000A0",bd=8)
buttont.grid(row=3,column=2,padx=(30, 30), pady=(30,30))

xWindow.mainloop()