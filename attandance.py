from tkinter import *
from tkinter import messagebox,ttk
from  PIL import ImageTk as i
import mysql.connector
import datetime
def login():
    uname = e1.get()
    password = e2.get()

    if (uname == "" and password == ""):
        messagebox.showinfo("", "Blank Not allowed")


    elif (uname == "Admin" and password == "123"):
        f1.forget()
        f2.pack()

        messagebox.showinfo("", "Login Success")
        # root.destroy()


    else:
        messagebox.showinfo("", "Incorrent Username and Password")

def atd():
    f1.forget()
    f2.forget()
    f3.pack()
def save_atd():
    a=e3.get()
    b=cvar.get()
    c=datetime.datetime.now()
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="att_pro")
    cur=mydb.cursor()
    # cur.execute("CREATE TABLE employe_atd (id INT, atd_status VARCHAR(255)")
    # messagebox.showinfo(cur)
    sql = "insert into employe_atd(id, atd_status,time) values (%s, %s,%s)"
    val=(a,b,c)
    try:
        cur.execute(sql,val)
        mydb.commit()
    except:
        mydb.rollback()
    messagebox.showinfo('', "record inserted!")
    mydb.close()
def new_ep():

    f1.forget()
    f2.forget()
    f3.forget()
    f4.pack()
def emp_data():
    a = e4.get()
    b = e5.get()
    c = e6.get()
    d = e7.get()
    e = e8.get()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="att_pro")
    cur = mydb.cursor()
    #cur.execute("CREATE TABLE employe_details (id INT, name VARCHAR(255),age INT,department VARCHAR(255),Basic_pay VARCHAR(255))")
    # messagebox.showinfo(cur)
    sql = "insert into employe_details(id, name, age ,department,Basic_pay) values (%s, %s, %s, %s, %s)"
    val = (a,b,c,d,e)
    try:
        cur.execute(sql, val)
        mydb.commit()
    except:
        mydb.rollback()
    messagebox.showinfo('', "record inserted!")
    mydb.close()
def sal():
    f1.forget()
    f2.forget()
    f3.forget()
    f4.forget()
    f5.pack()
def sal_cal():
    f1.forget()
    f2.forget()
    f3.forget()
    f4.forget()
    f5.forget()
    f6.forget()
    f7.forget()
    f8.pack()
    a=e9.get()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="att_pro")
    cur=mydb.cursor()
    j = f"select name from employe_details where id={a}"
    cur.execute(j)
    res = cur.fetchall()
    j1 = f"select Basic_pay from employe_details where id={a}"
    cur.execute(j1)
    res1 = cur.fetchall()
    for x1 in res1:
        global z1
        z1 = x1[0]

    j2=f"select count(atd_status) from employe_atd where (atd_status='Present' and id={a})"
    cur.execute(j2)
    res2 = cur.fetchall()
    for x2 in res2:
        global z2
        z2=x2[0]
    j3 = f"select count(atd_status) from employe_atd where (atd_status='Late Time' and id={a})"
    cur.execute(j3)
    res3 = cur.fetchall()
    for x3 in res3:
        global z3
        z3 = x3[0]
    j4 = f"select count(atd_status) from employe_atd where (atd_status='Half Day' and id={a})"
    cur.execute(j4)
    res4 = cur.fetchall()
    for x4 in res4:
        global z4
        z4 = x4[0]
    j5 = f"select count(atd_status) from employe_atd where (atd_status='Absent' and id={a})"
    cur.execute(j5)
    res5 = cur.fetchall()
    for x5 in res5:
        global z5
        z5 = x5[0]
    j6 = f"select count(atd_status) from employe_atd where (atd_status='Over Time' and id={a})"
    cur.execute(j6)
    res6 = cur.fetchall()
    for x6 in res6:
        global z6
        z6 = x6[0]
    od_p=int(z1)/30
    hd_p=od_p/2
    lt_p=hd_p/2
    ot_p=hd_p/2
    cal=(od_p*int(z2))-(lt_p*int(z3))+(hd_p*int(z4))+(ot_p*int(z6))
    d = [[res, res2, res3, res4, res6, res5,cal]]
    # t.insert('','end',d)
    for i in d:
        t.insert('','end',values=i)
    # messagebox.showinfo("Net pay",cal)
def show():

    a=e3.get()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="att_pro")
    cur=mydb.cursor()
    j1 = f"select name from employe_details where id={a}"
    cur.execute(j1)
    res1 = cur.fetchall()
    for x1 in res1:
        global z1
        z1 = x1[0]

    j2=f"select count(atd_status) from employe_atd where (atd_status='Present' and id={a})"
    cur.execute(j2)
    res2 = cur.fetchall()
    for x2 in res2:
        global z2
        z2=x2[0]
    j3 = f"select count(atd_status) from employe_atd where (atd_status='Late Time' and id={a})"
    cur.execute(j3)
    res3 = cur.fetchall()
    for x3 in res3:
        global z3
        z3 = x3[0]
    j4 = f"select count(atd_status) from employe_atd where (atd_status='Half Day' and id={a})"
    cur.execute(j4)
    res4 = cur.fetchall()
    for x4 in res4:
        global z4
        z4 = x4[0]
    j5 = f"select count(atd_status) from employe_atd where (atd_status='Absent' and id={a})"
    cur.execute(j5)
    res5 = cur.fetchall()
    for x5 in res5:
        global z5
        z5 = x5[0]
    j6=f"select count(atd_status) from employe_atd where (atd_status='Over Time' and id={a})"
    cur.execute(j6)
    res6 = cur.fetchall()
    for x6 in res6:
        global z6
        z6 = x6[0]
    ttl=int(z2)+int(z3)+int(z4)+int(z5)+int(z6)

    d=(z1,"has ",z2,"present days ",z3," late Entry ",z4," half days ",z6," over time ",z5," absent out of",ttl," days")
    messagebox.showinfo("",d)
def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    # t.delete(0,END)
    # tv.delete(0,END)
def back():
    f3.forget()
    f4.forget()
    f5.forget()
    f6.forget()
    f7.forget()
    f8.forget()
    f2.pack()
def sal1():
    f1.forget()
    f2.forget()
    f3.forget()
    f4.forget()
    f5.forget()
    f6.pack()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="att_pro")
    cur = mydb.cursor()
    j1 = f"select * from employe_atd"
    cur.execute(j1)
    res = cur.fetchall()
    for i in res:
        tv.insert('', 'end', values=i)
def sal2():
    f7.forget()
    f8.forget()
    f1.forget()
    f2.forget()
    f3.forget()
    f4.forget()
    f5.forget()
    f6.forget()
    f7.pack()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="att_pro")
    cur = mydb.cursor()
    j1 = f"select * from employe_details"
    cur.execute(j1)
    res = cur.fetchall()
    for i in res:
        t1.insert('', 'end', values=i)
w=Tk()
w.title("Login")
w.geometry("1350x650+0+0")
w.resizable(0,0)
bg =i.PhotoImage(file ="b4.png")
bg1 =i.PhotoImage(file ="b5 .png")
bg2 =i.PhotoImage(file ="b7.png")
# can=Canvas(height=500,width=500)
# can.create_image(150,200,image=bg)
# frame 1 admin panel
f1=Frame(w,height=1600,width=1600)
my_lbl=Label(f1,image=bg)
my_lbl.place(x=0,y=0)
Label(f1, text="UserName",height=2,bg="#45ceff",padx=20).place(x=500, y=250)
Label(f1, text="Password",height=2,bg="#45ceff",padx=22).place(x=500, y=310)

e1 = Entry(f1,selectborderwidth=1,borderwidth=10,bg="#d9f5ff",fg="#000000",font="2")
e1.place(x=650, y=250)

e2 = Entry(f1,selectborderwidth=1,borderwidth=10,bg="#d9f5ff",fg="#000000",font="2")
e2.place(x=650, y=310)
e2.config(show="*")

Button(f1, text="Login",activeforeground = "red",activebackground = "pink",bg="#45ceff" ,command=login, height=3, width=13).place(x=620, y=400)
Button(f1, text="Clear", command=clear,activeforeground = "red",activebackground = "pink",bg="#45ceff", height=3, width=13).place(x=750, y=400)
f1.pack()

# frame 2 admin panel menu
f2=Frame(w,height=2000,width=2000)
my_lbl=Label(f2,image=bg1)
my_lbl.place(x=0,y=0)
Label(f2,text="Welcome",height=3,width=25,bg="#cba786",font=2).place(x=600,y=20)
Button(f2,text="New Employee",command=new_ep,height=3,width=25,font=2).place(x=600,y=120)
Button(f2,text="Employee Attandance",command=atd,height=3,width=25,font=2).place(x=600,y=220)
Button(f2,text="Salary Calculator",command=sal,height=3,width=25,font=2).place(x=600,y=320)
Button(f2,text="Check Attandance Database",command=sal1,height=3,width=25,font=2).place(x=600,y=420)
Button(f2,text="Check Employee Database",command=sal2,height=3,width=25,font=2).place(x=600,y=520)
# frame3
f3=Frame(w,height=2000,width=2000)
my_lbl=Label(f3,image=bg2)
my_lbl.place(x=0,y=0)
Label(f3,text="Attandance Time!!",height=3,width=25,font=2).place(x=550,y=20)
id=Label(f3,text="Employee Id",height=2,padx=20)
id.place(x=500,y=150)
cvar = StringVar()
cvar.set("Entery Status")
option = ("Present", "Late Time", "Half Day","Absent","Over Time")
o = OptionMenu(f3,cvar, *option)
o.config(font=("times",14))
o.place(x=500,y=250,width=300)
e3=Entry(f3,selectborderwidth=1,borderwidth=10,bg="#d9f5ff",fg="#000000",font=2)
e3.place(x=650,y=150)
Button(f3,text="Save",command=save_atd,height=3,width=13,font=2).place(x=600,y=400)
Button(f3, text="Clear", command=clear, height=3, width=13,font=2).place(x=800, y=400)
Button(f3, text="Previous", command=back, height=3, width=13,font=2).place(x=400, y=400)
# Button(f3, text="Show Attandance", command=show, height=3, width=13).place(x=50, y=250)
# frame 4 adding new employee
f4=Frame(w,height=2000,width=2000)
my_lbl=Label(f4,image=bg2)
my_lbl.place(x=0,y=0)
cr_ep=Label(f4,text="Employee ID",height=2,padx=20,width=20,font=2)
cr_ep.place(x=80,y=30)
nm=Label(f4,text="Employee Name",height=2,padx=20,width=20,font=2)
nm.place(x=80,y=90)
age=Label(f4,text="Employee Age",height=2,padx=20,width=20,font=2)
age.place(x=80,y=150)
cr_ep=Label(f4,text="Employee Department",height=2,padx=20,width=20,font=2)
cr_ep.place(x=80,y=210)
bs=Label(f4,text="Employee Basic Salary",height=2,padx=20,width=20,font=2)
bs.place(x=80,y=270)
e4=Entry(f4,selectborderwidth=1,borderwidth=10,bg="#d9f5ff",fg="#000000",font=2,width=30)
e4.place(x=380,y=30)
e5=Entry(f4,selectborderwidth=1,borderwidth=10,bg="#d9f5ff",fg="#000000",font=2,width=30)
e5.place(x=380,y=90)
e6=Entry(f4,selectborderwidth=1,borderwidth=10,bg="#d9f5ff",fg="#000000",font=2,width=30)
e6.place(x=380,y=150)
e7=Entry(f4,selectborderwidth=1,borderwidth=10,bg="#d9f5ff",fg="#000000",font=2,width=30)
e7.place(x=380,y=210)
e8=Entry(f4,selectborderwidth=1,borderwidth=10,bg="#d9f5ff",fg="#000000",font=2,width=30)
e8.place(x=380,y=270)
Button(f4,text="Save",command=emp_data,height=3,width=13,font=2).place(x=380,y=450)
Button(f4, text="Clear", command=clear, height=3, width=13,font=2).place(x=570, y=450)
Button(f4, text="Previous", command=back, height=3, width=13,font=2).place(x=190, y=450)
# frame5 salary calculator
f5=Frame(w,height=2000,width=2000)
my_lbl=Label(f5,image=bg2)
my_lbl.place(x=0,y=0)
i=Label(f5,text="Employe ID",height=2,padx=20,width=20,font=2).place(x=200,y=60)
e9=Entry(f5,selectborderwidth=1,borderwidth=10,bg="#d9f5ff",fg="#000000",font=2,width=30)
e9.place(x=500,y=60)
Button(f5,text="Calculate Salary",command=sal_cal,height=3,width=13,font=2).place(x=420,y=250)
Button(f5, text="Clear", command=clear, height=3, width=13,font=2).place(x=610, y=250)
Button(f5, text="Previous", command=back, height=3, width=13,font=2).place(x=230, y=250)
# frame 6 for showing data of employe attandance
f6=Frame(w,height=2000,width=2000)
tv=ttk.Treeview(f6,columns=(1,2,3),show="headings",height=10)
tv.pack()
tv.heading(1,text="employee id")
tv.heading(2,text="employee attandance")
tv.heading(3,text="entery time")
Button(f6,text="Previous",command=back,height=3,width=20).pack()
# frame 7 for showing employe data
f7=Frame(w,height=2000,width=2000)
t1=ttk.Treeview(f7,columns=(1,2,3,4,5),show="headings",height=10)
t1.pack()
t1.heading(1,text="Employee ID")
t1.heading(2,text="Employee Name")
t1.heading(3,text="Employee Age")
t1.heading(4,text="Employee Department")
t1.heading(5,text="Employee Salary")
Button(f7, text="Previous", command=back, height=3, width=13).pack()
#frame 8 for showing salary calculation
f8=Frame(w,height=2000,width=2000)
t = ttk.Treeview(f8, columns=(1, 2, 3, 4, 5,6,7), show="headings", height=10)
t.pack()
t.heading(1, text="Name")
t.heading(2, text="Present")
t.heading(3, text="Late Time")
t.heading(4, text="Half Day")
t.heading(5, text="Over Time")
t.heading(6, text="Absent")
t.heading(7, text="Net Pay")
Button(f8, text="Previous", command=back, height=3, width=13).pack()
w.mainloop()