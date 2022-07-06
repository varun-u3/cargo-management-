from tkinter import font, ttk
from tkinter import *
from tkinter import messagebox
from logging import error
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk, Image
import re

root = Tk()
root.geometry("2000x2000")
w1 = PanedWindow(bg='white')
w1.pack(fill=BOTH, expand=1)

w3 = PanedWindow(w1, orient=VERTICAL, bg="#191970")
w1.add(w3)
global ms_color
global bg_color 
global h_color
global fb_color
global bt_color
global b_font
global h_font
ms_color = "#a9a9a9"
b_font ="helevitica"
bg_color = "#191970"
h_color = "#F5F5F5"
fb_color = "black"
bt_color = "#00FFFF"
h_font = "TIMES NEW ROMAN"
def login():
    root1 = Toplevel(root)
    root1.minsize(520, 390)
    root1.maxsize(520, 390)
    global username
    global password
    global message
    username = StringVar()
    password = StringVar()
    message = StringVar()
    
    def onclick():
        connection = mysql.connector.connect( host="localhost",
                                            user ="root",
                                            password="1432",
                                            database ="cargoproject")  
        var = username.get()
        pas=password.get()
        cursor = connection.cursor()
        cursor.execute("select id from login where id=%s and password=%s",(var,pas))
        result = cursor.fetchone()
        if result==None:
            messagebox.showerror("CARGO","      ENTER VALID VALUES      ")
        else:
            messagebox.showinfo("CARGO","         WELCOME             ")   
            root1.withdraw()
            root.withdraw()
            def main():
                root2 = Toplevel(root1, bg="#F0FFF0")
                root2.geometry("2000x2000")
            
                def home():
                    root2.withdraw()

                #cutomer details

                def cust():
                    root3 = Toplevel(root2) 
                    root3.geometry("2000x2000")
                    root3.config(bg=bg_color)
                    root3.attributes('-fullscreen',True)
                    global cus_id
                    global cus_name
                    global cus_add
                    global cus_ph
                    global cus_mail
                    cus_id = StringVar()
                    cus_name = StringVar()
                    cus_add = StringVar()
                    cus_ph = StringVar()
                    cus_mail = StringVar()
                    
                    def c_des():
                        root3.withdraw()
                    button = Button(root3,text="BACK",command=c_des,width=10,font=(b_font, 18),fg=fb_color,bg=bt_color).place(x=1040, y=15)
                    
                    
                    label1 = Label(root3, text="CUSTOMER DETAILS", width=20, bg=bg_color,fg=h_color, relief=FLAT, font=(h_font, 35),height=2).place(x=412, y=80)
                    label2 = Label(root3, text="CUSTOMER ID :",width=25,font=(h_font,16),height=2,bg="#B0C4DE",relief=RAISED).place(x=330, y=240)
                    label3 = Label(root3, text="CUSTOMER NAME:",font=(h_font,16),width=25,height=2,bg="#B0C4DE",relief=RAISED).place(x=330, y=300)
                    label4 = Label(root3, text="CUSTOMER ADDRESS:",font=(h_font,16),width=25,height=2,bg="#B0C4DE",relief=RAISED).place(x=330, y=360)
                    label5 = Label(root3, text="CUSTOMER PHONE:",width=25,height=2,font=(h_font,16),bg="#B0C4DE",relief=RAISED).place(x=330, y=420)
                    label6 = Label(root3, text="CUSTOMER E-MAIL ID:",width=25,height=2,font=(h_font,16),bg="#B0C4DE",relief=RAISED).place(x=330, y=480)
                    e1 = Entry(root3, textvariable=cus_id, font=("calibri",18) ,width=30).place(x=660, y=250,height=30)
                    e2 = Entry(root3, textvariable=cus_name,font=("calibri",18) , width=30).place(x=660, y=310,height=30)
                    e3 = Entry(root3, textvariable=cus_add, font=("calibri",18) ,width=30).place(x=660, y=370,height=30)
                    e4 = Entry(root3, textvariable=cus_ph, font=("calibri",18) ,width=30).place(x=660, y=430,height=30)
                    e5 = Entry(root3, textvariable=cus_mail,font=("calibri",18) ,width=30).place(x=660, y=490,height=30)

                    def infoget():
                        def connect():
                            conn = None
                            try:
                                conn = mysql.connector.connect(host='localhost',
                                                                database="cargoproject",
                                                                user="root",
                                                                password="1432"
                                                                )
                                if conn.is_connected():
                                
                                    def insert_class(a, b, c, d, e):
                                        query = "INSERT INTO CUSTOMER(CUST_ID,C_NAME,ADDRESS,PHONE,EMAIL)"\
                                                "VALUES(%s,%s,%s,%s,%s)"
                                        args = (a, b, c, d, e)
                                        try:
                                            
                                            regex = re.compile(r'''(
                                                                    [a-z A-Z 0-9 ._%+-]+ #username
                                                                    @                   #@ symbol
                                                                    [a-z A-Z 0-9 .-]+ #domain name
                                                                    (\.[a-zA-Z]{2,4})
                                                                    )''',re.VERBOSE)
                                            regexnum = re.compile(r'^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$')
                                            
                                            resnum = regexnum.search(d)
                                            res =regex.search(e)
                                            if res is None:
                                                messagebox.showerror("error","enter the valid email address")
                                            elif resnum is None:
                                                messagebox.showerror("error","enter the valid phone number")
                                            else:
                                                cursor = conn.cursor()
                                                cursor.execute(query, args)
                                                conn.commit()
                                                messagebox.showinfo("inserted", "SUCCESSFULLY INSERTED")
                                                c_des()
                                                cursor.close()

                                        except Error as error:
                                                messagebox.showerror("error", error)
                                                c_des()
                                        finally:
                                            
                                            conn.close()
                
                                def main():
                                    v1 =cus_id.get()
                                    v2 = cus_name.get()
                                    v3 = cus_add.get()
                                    v4 = cus_ph.get()
                                    v5 = cus_mail.get()
                                    insert_class(v1, v2, v3, v4, v5)
                                main()
                            except Error as e:
                                messagebox.showerror("error", e)
                            finally:
                                if conn is not None and conn.is_connected():
                                    conn.close()
                                    c_des()
                        connect()
                        c_des()
                    button1 = Button(root3, text="SUBMIT", height=2, width=20, font=(b_font, 16), fg=fb_color, bg=bt_color,command=infoget).place(x=510, y= 630)
                #CARGO DETAILS
                def cargo():
                    root4 = Toplevel(root2)
                    root4.geometry("2000x2000")
                    root4.config(bg=bg_color)
                    root4.attributes('-fullscreen',True)
                    global cus_id
                    global cg_id
                    global cg_weight
                    global cg_date
                    global cg_name
                    cg_id = StringVar()
                    cg_weight = StringVar()
                    cg_date = StringVar()
                    cg_name = StringVar()
                    cus_id = StringVar()
                    
                    def c_des():
                        root4.withdraw()
                    button = Button(root4,text="BACK",command=c_des,width=20,height=3,font=("verdana", 10),fg=fb_color,bg=bt_color).place(x=500, y=600)
                    label1 = Label(root4, text="CARGO DETAILS", width=25, font=(h_font, 35), relief= FLAT, bg=bg_color,fg=h_color,height=2).place(x=250, y=70)
                    label2 = Label(root4, text="CARGO ID:",width=25,height=2,bg="#B0C4DE",font=(h_font,16),relief=RAISED).place(x=250, y=240)
                    label3 = Label(root4, text="CUSTOMER ID:",width=25,height=2,bg="#b0c4de",font=(h_font,16),relief=RAISED).place(x=250, y=300)
                    label4 = Label(root4, text="GROSS WEIGHT:(IN TONS)",width=25,height=2,bg="#b0c4de",font=(h_font,16),relief=RAISED).place(x=250, y=360)
                    label5 = Label(root4, text=" TO:",width=25,height=2,bg="#b0c4de",font=(h_font,16),relief=RAISED).place(x=250, y=420)
                    label6 = Label(root4, text="DATE OF SHIPPMENT:",width=25,height=2,bg="#b0c4de",font=(h_font,16),relief=RAISED).place(x=250, y=480)
                    def cargoinfo():
                        def con():
                            conn = None
                            try:
                                conn = mysql.connector.connect(host="localhost",
                                                                user="root",
                                                                database="cargoproject",
                                                                password="1432")
                                if conn.is_connected():
                                    print("connected to database")
                                    def insert_cargo(a,b,c,d,e):
                                        query = "INSERT INTO CARGO(CARGO_ID,CUST_ID,WEIGHT,D_PERSON,DATE_OF_SHIPPMENT)"\
                                                "VALUES(%s,%s,%s,%s,%s)"
                                        args= (a,b,c,d,e)
                                        try:
                                            cursor = conn.cursor()
                                            cursor.execute(query,args)
                                            conn.commit()
                                            messagebox.showinfo("successfull",'data inserted successfully')
                                            c_des()
                                        except Error as error:
                                            messagebox.showerror("error",error)
                                            c_des()
                                        finally:
                                            cursor.close()
                                            conn.close()
                                    def main():
                                        v1 = cg_id.get()
                                        v2 = cus_id.get()
                                        v3 = cg_weight.get()
                                        v4= cg_name.get()
                                        v5 = cg_date.get()
                                        insert_cargo(v1,v2,v3,v4,v5)
                                    main()
                            except Error as e:
                                messagebox.showerror("error", e)
                                c_des()
                            finally:
                                if conn is not None and conn.is_connected():
                                    conn.close()
                                    c_des()
                        con() 
                    connection = mysql.connector.connect(user ="root", host="localhost",database="cargoproject",password="1432")
                    cursor = connection.cursor()
                    cursor.execute("select cust_id from customer")
                    res = cursor.fetchall();             
                    button1 = Button(root4, text="SUBMIT", height=2, width=20, font=("verdana", 10), fg=fb_color,bg=bt_color,command=cargoinfo).place(x=498, y= 600)
                    e1 = Entry(root4, textvariable=cg_id, font=("calibri",18), width=30).place(x=662, y=250,height=30)
                    e2 = ttk.Combobox(root4,values=res, textvariable=cus_id, font=("calibri",18), width=30).place(x=662, y=310,height=30)
                    e3 = Entry(root4, textvariable=cg_weight, font=("calibri",18), width=30).place(x=662, y=370,height=30)
                    e4 = Entry(root4, textvariable=cg_name,  font=("calibri",18),width=30).place(x=662, y=430,height=30)
                    e5 = Entry(root4, textvariable=cg_date, font=("calibri",18), width=30).place(x=662, y=490,height=30)
                    root4.mainloop()
                # billing

                def billing():
                    root5 = Toplevel(root2)
                    root5.geometry("2000x2000")
                    
                    root5.config(bg=bg_color)
                    root5.attributes('-fullscreen',True)
                    global cg_id
                    global bl_to
                    global bl_fr
                    global bl_addr
                    global bl_amnt
                    global bl_date
                    cg_id = StringVar()
                    bl_to = StringVar()
                    bl_fr = StringVar()
                    bl_date = StringVar()
                    bl_addr = StringVar()
                    bl_amnt = StringVar()
                    
                    def c_des():
                        root5.withdraw()
                    button = Button(root5,text="BACK",command=c_des,width=20,height=3,font=("verdana", 10),fg=fb_color,bg=bt_color).place(x=1040, y=15)
                    label1 = Label(root5, text="BILLING DETAILS", width=30, font=(h_font, 35), relief=FLAT,fg=h_color, bg=bg_color,height=2).place(x=320 ,y=80)
                    label2 = Label(root5, text="CARGO ID:",font=(h_font,16),bg="#B0C4DE",relief=RAISED,width=25,height=2).place(x=350, y=240)
                    label3 = Label(root5, text="FROM:",font=(h_font,16),bg="#B0C4DE",relief=RAISED,width=25,height=2).place(x=350, y=300)
                    label4 = Label(root5, text="TO:",font=(h_font,16),bg="#B0C4DE",relief=RAISED,width=25,height=2).place(x=350, y=360)
                    label5 = Label(root5, text="ADDRESS:",font=(h_font,16),bg="#B0C4DE",relief=RAISED,width=25,height=2).place(x=350, y=420)
                    label6 = Label(root5, text="AMOUNT:",font=(h_font,16),bg="#B0C4DE",relief=RAISED,width=25,height=2).place(x=350, y=480)
                    label6 = Label(root5, text="DATE OF BILLING",font=(h_font,16),bg="#B0C4DE",relief=RAISED,width=25,height=2).place(x=350, y=540)
                    def billinfo():
                        def con():
                            conn = None
                            try:
                                conn = mysql.connector.connect(host="localhost",
                                                                user="root",
                                                                database="cargoproject",
                                                                password="1432")
                                if conn.is_connected():
                                    print("connected to database")
                                    def insert_cargo(a,b,c,d,e,f):
                                        query = "INSERT INTO BILLING(CARGO_ID,SENDER,RECIEPANT_NAME,ADDRESS,AMOUNT,BILLING_DATE)"\
                                                "VALUES(%s,%s,%s,%s,%s,%s)"
                                        args= (a,b,c,d,e,f)
                                        try:
                                            cursor = conn.cursor()
                                            cursor.execute(query,args)
                                            conn.commit()
                                            messagebox.showinfo("successfull",'data inserted successfully')
                                            c_des()
                                        except Error as error:
                                            messagebox.showerror("error",error)
                                            c_des()
                                        finally:
                                            cursor.close()
                                            conn.close()
                                    def main():
                                        v1 = cg_id.get()
                                        v2 = bl_fr.get()
                                        v3 = bl_to.get()
                                        v4= bl_addr.get()
                                        v5 = bl_amnt.get()
                                        v6 = bl_date.get()
                                        insert_cargo(v1,v2,v3,v4,v5,v6)
                                    main()
                            except Error as e:
                                messagebox.showerror("error", e)
                            finally:
                                if conn is not None and conn.is_connected():
                                    conn.close()
                                    c_des()
                        con()  
                    connection = mysql.connector.connect(user ="root", host="localhost",database="cargoproject",password="1432")
                    cursor = connection.cursor()
                    cursor.execute("select cargo_id from cargo")
                    res = cursor.fetchall()  
                   
                   
                    button1 = Button(root5, text="SUBMIT", height=2, width=20, font=(b_font, 16), fg=fb_color,bg=bt_color, command=billinfo).place(x=540, y= 640)
                    e1 = ttk.Combobox(root5,values=res, textvariable= cg_id,font=("calibri",18), width=30).place(x=672, y=250,height=30)
                    e2 = Entry(root5, textvariable=bl_fr,font=("calibri",18), width=30).place(x=672, y=310,height=30)
                    e3 = Entry(root5, textvariable=bl_to,font=("calibri",18), width=30).place(x=672, y=370,height=30)
                    e4 = Entry(root5, textvariable=bl_addr,font=("calibri",18), width=30).place(x=672, y= 430,height=30)
                    e5 = Entry(root5, textvariable=bl_amnt,font=("calibri",18), width=30).place(x=672, y =490,height=30)
                    e6 = Entry(root5, textvariable=bl_date,font=("calibri",18), width=30).place(x=672, y =550,height=30)
                    root5.mainloop()
                #transport

                def transport():
                    root6 = Toplevel(root2)
                    root6.geometry("2000x2000")
                    root6.config(bg=bg_color)
                    root6.attributes('-fullscreen',True)
                    global cg_id
                    global cust_id
                    global tr_vt  
                    global tr_date
                    global tr_recdate
                    cg_id = StringVar()
                    cust_id = StringVar()
                    tr_vt = StringVar()
                    tr_date = StringVar()
                    tr_recdate = StringVar()
                    
                    def c_des():
                        root6.withdraw()
                    button = Button(root6,text="BACK",command=c_des,width=20,height=3,font=("verdana", 10),fg=fb_color,bg=bt_color).place(x=1040, y=15)
                    label1 = Label(root6, text="TRANSPORT DETAILS", width=30, font=(h_font, 35),height=2, relief=FLAT, bg=bg_color,fg=h_color).place(x=250, y=80)
                    label2 = Label(root6, text="CARGO ID:",font=(h_font,16),bg="#B0C4DE",relief=RAISED,width=25,height=2).place(x=345, y=240)
                    label3 = Label(root6, text="CUSTOMER ID:",font=(h_font,16),bg="#B0C4DE",relief=RAISED,width=25,height=2).place(x=345, y=300)
                    label4 = Label(root6, text="VEHICLE TYPE:",font=(h_font,16),bg="#B0C4DE",relief=RAISED,width=25,height=2).place(x=345, y=360)
                    label5 = Label(root6, text=" DATE OF SHIPPMENT:",font=(h_font,16),bg="#B0C4DE",relief=RAISED,width=25,height=2).place(x=345, y=420)
                    label6 = Label(root6, text="DATE OF RECIEVE:",font=(h_font,16),bg="#B0C4DE",relief=RAISED,width=25,height=2).place(x=345, y=480)
                    def transportinfo():
                        def con():
                            conn = None
                            try:
                                conn = mysql.connector.connect(host="localhost",
                                                                user="root",
                                                                database="cargoproject",
                                                                password="1432")
                                if conn.is_connected():
                                    print("connected to database")
                                    def insert_cargo(a,b,c,d,e):
                                        query = "INSERT INTO TRANSPORT(CARGO_ID,CUST_ID,TYPE_OF_V,DATE_OF_SHIPPMENT,DATE_OF_RECEIVED)"\
                                                "VALUES(%s,%s,%s,%s,%s)"
                                        args= (a,b,c,d,e)
                                        try:
                                            cursor = conn.cursor()
                                            cursor.execute(query,args)
                                            conn.commit()
                                            messagebox.showinfo("successfull",'data inserted successfully')
                                            c_des()
                                        except Error as error:
                                            messagebox.showerror("error",error)
                                            c_des()
                                        finally:
                                            cursor.close()
                                            conn.close()
                                    def main():
                                        v1 = cg_id.get()
                                        v2 = cust_id.get()
                                        v3 = tr_vt.get()
                                        v4= tr_date.get()
                                        v5 = tr_recdate.get()
                                        insert_cargo(v1,v2,v3,v4,v5)
                                    main()
                            except Error as e:
                                messagebox.showerror("error", e)
                                c_des()
                            finally:
                                if conn is not None and conn.is_connected():
                                    conn.close()
                                    c_des()
                        con() 
                    connection = mysql.connector.connect(user ="root", host="localhost",database="cargoproject",password="1432")
                    cursor = connection.cursor()
                    cursor.execute("select cust_id from customer")
                    res = cursor.fetchall(); 
                    cursor.close()
                    connection = mysql.connector.connect(user ="root", host="localhost",database="cargoproject",password="1432")
                    cursor = connection.cursor()
                    cursor.execute("select cargo_id from cargo")
                    res1 = cursor.fetchall(); 
                    cursor.close()



                    button1 = Button(root6,text="SUBMIT", height=2, width=20, font=(b_font, 16), fg=fb_color,bg=bt_color,command=transportinfo).place(x=516, y=560)
                    e1 = ttk.Combobox(root6,values=res1, textvariable=cg_id,font=("calibri",18), width=30).place(x=672, y=240,height=30)
                    e2 = ttk.Combobox(root6,values=res ,textvariable=cust_id,font=("calibri",18), width=30).place(x=672, y=300,height=30)
                    e3 = ttk.Combobox(root6, textvariable=tr_vt,values=["truck","ship","aeroplane"],font=("calibri",18), width=30).place(x=672, y=360,height=30)
                    e4 = Entry(root6, textvariable=tr_date, font=("calibri",18),width=30).place(x=672, y=420,height=30)
                    e5 = Entry(root6, textvariable=tr_recdate,font=("calibri",18), width=30).place(x=672, y=480,height=30)
                    root6.mainloop()

               
                    root8 = Toplevel(root2)

                    root8.config(bg="#DAA520")
                    root8.attributes('-fullscreen',True)
                    def c_des():
                        root8.withdraw()
                    global e_name
                    global e_ssn
                    global e_dob
                    global e_mail
                    global e_phone
                    global e_gen
                    global e_bg
                    global e_passw
                    e_name = StringVar()
                    e_ssn = StringVar() 
                    e_dob = StringVar()
                    e_mail = StringVar()
                    e_phone =StringVar()
                    e_gen = StringVar()
                    e_bg = StringVar()
                    e_passw = StringVar()
                    button = Button(root8,text="BACK",command=c_des,width=20,height=3,font=("verdana", 10),fg="blue").place(x=1040, y=15)
                    label1 = Label(root8, text="------EMPLOYEE DETAILS-----", width=50, bg="#E6E6FA", relief=SUNKEN, font=("Times New Roman", 15),height=2).place(x=362 ,y=25)
                    label2 = Label(root8, text="SSN",width=25,height=2,bg="#B0C4DE",relief=RAISED).place(x=425, y=120)
                    label3 = Label(root8, text="NAME",width=25,height=2,bg="#B0C4DE",relief=RAISED).place(x=425, y=180)
                    label4 = Label(root8, text="DATEOFBIRTH",width=25,height=2,bg="#B0C4DE",relief=RAISED).place(x=425, y=240)
                    label5 = Label(root8, text="EMAIL_ID",width=25,height=2,bg="#B0C4DE",relief=RAISED).place(x=425, y=300)
                    label6 = Label(root8, text="PHONE NUMBER",width=25,height=2,bg="#B0C4DE",relief=RAISED).place(x=425, y=360)
                    label7 = Label(root8, text="GENDER",width=25,height=2,bg="#B0C4DE",relief=RAISED).place(x=425, y=420)
                    label8 = Label(root8, text="BLOODGROUP",width=25,height=2,bg="#B0C4DE",relief=RAISED).place(x=425, y=480)
                    label9 = Label(root8, text="PASSWORD",width=25,height=2,bg="#B0C4DE",relief=RAISED).place(x=425, y=540)
                    e1 = Entry(root8, textvariable=e_ssn, width=60).place(x=650, y=120,height=30)
                    e2 = Entry(root8, textvariable=e_name, width=60).place(x=650, y=180,height=30)
                    e3 = Entry(root8, textvariable=e_dob, width=60).place(x=650, y=240,height=30)
                    e4 = Entry(root8, textvariable=e_mail, width=60).place(x=650, y=300,height=30)
                    e5 = Entry(root8, textvariable=e_phone, width=60).place(x=650, y=360,height=30)
                    e5 = Entry(root8, textvariable=e_gen, width=60).place(x=650, y=420,height=30)
                    e6= Entry(root8, textvariable=e_bg, width=60).place(x=650, y=480,height=30)
                    e7 = Entry(root8, textvariable=e_passw, width=60).place(x=650, y=540,height=30) 
                    def emp_get():
                        def connect():
                            conn = None
                            try:
                                conn = mysql.connector.connect(host="localhost",
                                         database="cargoproject",
                                        user="root",
                                        password="1432"
                                        )
                                if conn.is_connected():
                                
                                    def insert_class(a, b, c, d, e,g,h):
                                        query = "INSERT INTO EMPLOYEE(SSN,NAME,DOB,EMAIL,PHONE,GENDER,BLOODGROUP)"\
                                        "VALUES(%s,%s,%s,%s,%s,%s,%s)"
                                        args = (a, b, c, d, e,g,h)
                                        try:
                                            cursor = conn.cursor()
                                            cursor.execute(query, args)
                                            conn.commit()
                                            messagebox.showinfo("inserted", cursor.lastrowid)
                                        except Error as error:
                                            messagebox.showerror("error", error)
                                        finally:
                                            cursor.close()
                                            conn.close()
                
                                        def main():
                                            v1 =e_ssn.get()
                                            v2 = e_name.get()
                                            v3 = e_dob.get()
                                            v4 = e_mail.get()
                                            v5 = e_phone.get()
                                            v6 = e_gen.get()
                                            v7 = e_bg.get()
                                            insert_class(v1, v2, v3, v4, v5,v6,v7)
                                        main()
                            except Error as e:
                                messagebox.showerror("error", e)
                            finally:
                                if conn is not None and conn.is_connected():
                                    conn.close()
                                root8.withdraw()
                        connect()
                        root8.withdraw()

                    button1 = Button(root8, text="SUBMIT", height=2, width=20, font=("verdana", 10), fg="blue",command=emp_get).place(x=510, y=630)
                    root8.mainloop()

                #employee
                def emp():
                
                    root8 = Tk()
                    h_font = "TIMES NEW ROMAN"
                    b_font ="helevitica"
                    bg_color = "#191970"
                    h_color = "#F5F5F5"
                    fb_color = "purple"
                    bt_color = "#00FFFF"
                    root8.config(bg=bg_color)
                    root8.attributes('-fullscreen',True)
                    def c_des():
                        root8.withdraw()
                    global e_name
                    global e_ssn
                    global e_dob
                    global e_mail
                    global e_phone
                    global e_gen
                    global e_bg
                    global e_passw
                    e_name = StringVar()
                    e_ssn = StringVar()
                    e_dob = StringVar()
                    e_mail = StringVar()
                    e_phone =StringVar()
                    e_gen = StringVar()
                    e_bg = StringVar()
                    e_passw = StringVar()
                    button = Button(root8,text="BACK",command=c_des,width=10,font=("verdana",18),fg=fb_color,bg=bt_color).place(x=1040, y=15)
                    label1 = Label(root8, text="EMPLOYEE DETAILS", width=25,font=(h_font,35), bg=bg_color,fg=h_color,height=2).place(x=250 ,y=5)
                    label2 = Label(root8, text="SSN",width=25,height=2,bg="#B0C4DE",relief=RAISED,font=(h_font,16)).place(x=320, y=120)
                    label3 = Label(root8, text="NAME",width=25,height=2,bg="#B0C4DE",relief=RAISED,font=(h_font,16)).place(x=320, y=180)
                    label5 = Label(root8, text="EMAIL_ID",width=25,height=2,font=(h_font,16),bg="#B0C4DE",relief=RAISED).place(x=320, y=240)
                    label6 = Label(root8, text="PHONE NUMBER",width=25,height=2,font=(h_font,16),bg="#B0C4DE",relief=RAISED).place(x=320, y=300)
                    label7 = Label(root8, text="GENDER",width=25,height=2,font=(h_font,16),bg="#B0C4DE",relief=RAISED).place(x=320, y=360)
                    label8 = Label(root8, text="BLOODGROUP",width=25,font=(h_font,16),height=2,bg="#B0C4DE",relief=RAISED).place(x=320, y=420)
                    l = Label(root8, text="PASSWORD",width=25,height=2,font=(h_font,16),bg="#B0C4DE",relief=RAISED).place(x=320, y=480)
                    #e1 = Entry(root8, font=("calibri",18),textvariable=e_ssn, width=30).place(x=650, y=130,height=30)
                    e2 = Entry(root8,font=("calibri",18), textvariable=e_name, width=30).place(x=650, y=190,height=30)
                    e4 = Entry(root8, textvariable=e_mail, width=30,font=("calibri",18),).place(x=650, y=250,height=30)
                    e5 = Entry(root8, textvariable=e_phone,font=("calibri",18), width=30).place(x=650, y=310,height=30)
                    e5 = Entry(root8, textvariable=e_gen,font=("calibri",18), width=30).place(x=650, y=370,height=30)
                    e6= Entry(root8, textvariable=e_bg, font=("calibri",18),width=30).place(x=650, y=430,height=30)
                    e7 = Entry(root8, textvariable=e_passw, font=("calibri",18),width=30).place(x=650, y=490,height=30) 
                    def emp_get():

                        try:
                           conn = mysql.connector.connect(host ="localhost",user="root",database="cargoproject",password="1432")
                           cursor = conn.cursor()
                           a= e_ssn.get()
                           b= e_name.get()
                           c = e_mail.get()
                           d = e_phone.get()
                           e = e_gen.get()
                           f = e_bg.get()
                           g = e_passw.get()

                           cursor.execute("INSERT INTO EMPLOYEE(SSN,NAME,EMAIL,PHONE,GENDER,BLOODGROUP) VALUES(%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f))
                           #cursor.execute("insert into login values (%s,%s)",(a,g))
                           conn.commit()
                           cursor.close()
                           messagebox.showinfo("cargo","data inserted successfully")
                        except Error as error:
                            messagebox.showerror("error",a)                        
                    

                    button1 = Button(root8, text="SUBMIT", height=2, width=20, font=(b_font, 16), fg=fb_color,bg=bt_color,command=emp_get).place(x=510, y=630)
                    root8.mainloop()
                #view
                def view_d():
                    root7 = Toplevel(root2)
                    global serach_item
                    serach_item = StringVar()
                    root7.geometry('2000x2000')
                    root7.config(bg=bg_color)
                    root7.attributes('-fullscreen',True)
                    def info():
                        def connect():
                            conn = NONE
                            try:
                                conn = mysql.connector.connect(host ="localhost",
                                                                database="cargoproject",
                                                                user="root",
                                                                password="1432")
                                if conn.is_connected():
                                    def transaction_display():
                                        root1 = Tk()
                                        root1.geometry('2000x2000')
                                        root1.config(bg=bg_color)
                                        root1.attributes('-fullscreen',True)
                                    
                                        def hi():
                                            root1.withdraw()
                    
                                        button = Button(root1,command=hi,text="BACK",width=20,height=3,font=("verdana", 12),fg=fb_color,bg=bt_color).pack(padx=25,pady=10,side=BOTTOM)
                                        label1 = Label( root1, text="TRANSACTION DETAILS",font=("Times New Roman", 35),width=25,bg=bg_color,fg=h_color).pack(padx=15, pady=15)
                                        
                                        tree = ttk.Treeview(root1, column=('CARGO_ID', 'CUSTOMER_ID', 'BILLING_DATE', 'AMOUNT'), show="headings", height=8)
                                        tree.column("#1", anchor=CENTER)
                                        tree.heading("#1", text="CARGO_ID")
                                        tree.column("#2", anchor=CENTER)
                                        tree.heading("#2", text="CUSTOMER_ID")
                                        tree.column("#3", anchor=CENTER)
                                        tree.heading("#3", text="BILLING_DATE")
                                        tree.column("#4", anchor=CENTER)
                                        tree.heading("#4", text="AMOUNT")
                                        try:
                                            mySql_dis_query = " SELECT C.CUST_ID, B.CARGO_ID,B.BILLING_DATE,B.AMOUNT FROM CARGO AS C , BILLING AS B WHERE B.CARGO_ID = C.CARGO_ID"
                                            cursor = conn.cursor()
                                            cursor.execute(mySql_dis_query)
                                            myresult= cursor.fetchall()
                                            for p in myresult:
                                                tree.insert('', 'end', values=p)
                                            tree.pack()
                                            root1.mainloop()
                                            cursor.close()
                                        except Error as e:
                                            messagebox.showerror('error',e)
                                    def main():
                                        transaction_display()
                                    main()
                            except Error as e:
                                messagebox.showerror('error',e)
                        connect()
                    def info_cargo():
                        def connect():
                            conn = NONE
                            try:
                                conn = mysql.connector.connect(host ="localhost",
                                                                database="cargoproject",
                                                                user="root",
                                                                password="1432")
                                if conn.is_connected():
                                    def transaction_display():
                                        root1 = Tk()
                                        root1.config(bg=bg_color)
                                        root1.geometry('2000x2000')
                                        root1.attributes('-fullscreen',True)
                                        def hi():
                                            root1.withdraw()
                                        
                                        button = Button(root1,command=hi,text="BACK",width=20,height=3,font=("verdana", 12),fg=fb_color,bg=bt_color).pack(padx=25,pady=10,side=BOTTOM)
                                        label1 = Label( root1, text="CARGO DETAILS",font=("Times New Roman", 35),width=20,bg=bg_color,fg=h_color).pack(padx=15, pady=15)
                                        
                                        tree = ttk.Treeview(root1, column=('CARGO_ID', 'CUSTOMER_ID', 'WEIGHT', 'D_PERSON','DATE_OF_SHIPPMENT'), show="headings", height=8)
                                        tree.column("#1", anchor=CENTER)
                                        tree.heading("#1", text="CARGO_ID")
                                        tree.column("#2", anchor=CENTER)
                                        tree.heading("#2", text="CUSTOMER_ID")
                                        tree.column("#3", anchor=CENTER)
                                        tree.heading("#3", text="WEIGHT")
                                        tree.column("#4", anchor=CENTER)
                                        tree.heading("#4", text="D_PERSON")
                                        tree.column("#5", anchor=CENTER)
                                        tree.heading("#5", text="DATE_OF_SHIPPMENT")
                                        try:
                                            mySql_dis_query = "select * from cargo"
                                            cursor = conn.cursor()
                                            cursor.execute(mySql_dis_query)
                                            myresult= cursor.fetchall()
                                            for p in myresult:
                                                tree.insert('', 'end', values=p)
                                            tree.pack()
                                            root1.mainloop()
                                            cursor.close()
                                        except Error as e:
                                            messagebox.showerror('error',e)
                                    def main():
                                        transaction_display()
                                    main()
                            except Error as e:
                                messagebox.showerror('error',e)
                        connect()
                    def info_transport():
                        def connect():
                            conn = NONE
                            try:
                                conn = mysql.connector.connect(host ="localhost",
                                                                database="cargoproject",
                                                                user="root",
                                                                password="1432")
                                if conn.is_connected():
                                    def transaction_display():
                                        root1 = Tk()
                                        root1.config(bg=bg_color)
                                        root1.geometry('2000x2000')
                                        root1.attributes('-fullscreen',True)
                                        
                                        def hi():
                                            root1.withdraw()
                            
                                        button = Button(root1,command=hi,text="BACK",width=20,height=3,font=("verdana", 12),fg=fb_color,bg=bt_color).pack(padx=25,pady=10,side=BOTTOM)
                                        label1 = Label( root1, text="TRANSPORT DETAILS",font=("Times New Roman", 35),width=30,bg=bg_color,fg=h_color).pack(padx=15, pady=15)
                                        
                                        tree = ttk.Treeview(root1, column=('CARGO_ID', 'CUSTOMER_ID', 'TYPE_OF_V', 'DATE_OF_SHIPPMENT','DATE_OF_DELIVERY'), show="headings", height=8)
                                        tree.column("#1", anchor=CENTER)
                                        tree.heading("#1", text="CARGO_ID")
                                        tree.column("#2", anchor=CENTER)
                                        tree.heading("#2", text="CUSTOMER_ID")
                                        tree.column("#3", anchor=CENTER)
                                        tree.heading("#3", text="TYPE_OF_V")
                                        tree.column("#4", anchor=CENTER)
                                        tree.heading("#4", text="DATE_OF_SHIPPMENT")
                                        tree.column("#5", anchor=CENTER)
                                        tree.heading("#5", text="DATE_OF_DELIVERY")
                                        try:
                                            mySql_dis_query = "select * from transport"
                                            cursor = conn.cursor()
                                            cursor.execute(mySql_dis_query)
                                            myresult= cursor.fetchall()
                                            for p in myresult:
                                                tree.insert('', 'end', values=p)
                                            tree.pack()
                                            root1.mainloop()
                                            cursor.close()
                                        except Error as e:
                                            messagebox.showerror('error',e)
                                    def main():
                                        transaction_display()
                                    main()
                            except Error as e:
                                messagebox.showerror('error',e)
                        connect()
                    def info_billing():
                        def connect():
                            conn = NONE
                            try:
                                conn = mysql.connector.connect(host ="localhost",
                                                                database="cargoproject",
                                                                user="root",
                                                                password="1432")
                                if conn.is_connected():
                                    def transaction_display():
                                        root1 = Tk()
                                        root1.config(bg=bg_color)
                                        root1.geometry('2000x2000')
                                        root1.attributes('-fullscreen',True)
                                        def hi():
                                            root1.withdraw()
                                        
                                        button = Button(root1,command=hi,text="BACK",width=20,height=3,font=("verdana", 12),fg=fb_color,bg=bt_color).pack(padx=25,pady=10,side=BOTTOM)
                                        label1 = Label( root1, text="BILLING DETAILS",font=("Times New Roman", 35),width=20,bg=bg_color,fg=h_color).pack(padx=15, pady=15)
                                        
                                        tree = ttk.Treeview(root1, column=('CARGO_ID', 'SENDER', 'RECIEPANT_NAME', 'ADDRESS','AMOUNT','BILLING_DATE'), show="headings", height=8)
                                        tree.column("#1", anchor=CENTER)
                                        tree.heading("#1", text="CARGO_ID")
                                        tree.column("#2", anchor=CENTER)
                                        tree.heading("#2", text="SENDER")
                                        tree.column("#3", anchor=CENTER)
                                        tree.heading("#3", text="RECIEPANT_NAME")
                                        tree.column("#4", anchor=CENTER)
                                        tree.heading("#4", text="ADDRESS")
                                        tree.column("#5", anchor=CENTER)
                                        tree.heading("#5", text="AMOUNT")
                                        tree.column("#6", anchor=CENTER)
                                        tree.heading("#6", text="BILLING_DATE")
                                        try:
                                            mySql_dis_query = "select * from billing"
                                            cursor = conn.cursor()
                                            cursor.execute(mySql_dis_query)
                                            myresult= cursor.fetchall()
                                            for p in myresult:
                                                tree.insert('', 'end', values=p)
                                            tree.pack()
                                            root1.mainloop()
                                            cursor.close()
                                        except Error as e:
                                            messagebox.showerror('error',e)
                                    def main():
                                        transaction_display()
                                    main()
                            except Error as e:
                                 messagebox.showerror('error',e)
                        connect()
                    def info_cus():
                        def connect():
                            conn = NONE
                            try:
                                conn = mysql.connector.connect(host ="localhost",
                                                                database="cargoproject",
                                                                user="root",
                                                                password="1432")
                                if conn.is_connected():
                                    def transaction_display():
                                        root1 = Tk()
                                        root1.config(bg=bg_color)
                                        root1.geometry('2000x2000')
                                        root1.attributes('-fullscreen',True)
                                        def hi():
                                            root1.withdraw()
                    
                                        button = Button(root1,command=hi,text="BACK",width=20,height=3,font=("verdana", 12),fg=fb_color,bg=bt_color).pack(padx=25,pady=10,side=BOTTOM)
                                        label1 = Label( root1, text="CUSTOMER DETAILS",font=("Times New Roman", 35),width=25,bg=bg_color,fg=h_color).pack(padx=15, pady=15)
                                            
                                        tree = ttk.Treeview(root1, column=('CUST_ID', 'C_NAME', 'ADDRESS','PHONE','EMAIL'),show="headings", height=8)
                                        tree.column("#1", anchor=CENTER)
                                        tree.heading("#1", text="CUST_ID")
                                        tree.column("#2", anchor=CENTER)
                                        tree.heading("#2", text="C_NAME")
                                        tree.column("#3", anchor=CENTER)
                                        tree.heading("#3", text="ADDRESS")
                                        tree.column("#4", anchor=CENTER)
                                        tree.heading("#4", text="PHONE")
                                        
                                        tree.column("#5", anchor=CENTER)
                                        tree.heading("#5", text="EMAIL")

                                        try:
                                            mySql_dis_query = "select * from customer"
                                            cursor = conn.cursor()
                                            cursor.execute(mySql_dis_query)
                                            myresult= cursor.fetchall()
                                            for p in myresult:
                                                tree.insert('', 'end', values=p)
                                            tree.pack()
                                            root1.mainloop()
                                            cursor.close()
                                        except Error as e:
                                            messagebox.showerror('error',e)
                                    def main():
                                        transaction_display()
                                    main()
                            except Error as e:
                                messagebox.showerror('error',e)
                        connect()
                    label1 = Label( root7, text="VIEW DETAILS",font=("Times New Roman", 35),width=20,bg=bg_color,fg=h_color).place(x=420, y=35)
                    label2 = Label(root7, text="CARGO DETAILS",font=("Times New Roman", 15),relief=GROOVE,height=2,width=25,bg="#B0C4DE").place(x=300, y=200)
                    button1 = Button(root7,text="CLICK HERE", height=2, width=20, font=("verdana", 10), fg="blue",bg="#dcdcdc",relief=RAISED,command=info_cargo).place(x=680,y=190)
                    label2 = Label(root7, text="TRANSPORT DETAILS",font=("Times New Roman", 15),relief=GROOVE,height=2,width=25,bg="#B0C4DE").place(x=300, y=280)
                    button1 = Button(root7,text="CLICK HERE", height=2, width=20, font=("verdana", 10), fg="blue",relief=RAISED,command=info_transport).place(x=680,y=270)
                    label2 = Label(root7, text="TRANSACTION DETAILS",font=("Times New Roman", 15),relief=GROOVE,height=2,width=25,bg="#B0C4DE").place(x=300, y=360)
                    button1 = Button(root7,text="CLICK HERE", height=2, width=20, font=("verdana", 10), fg="blue",relief=RAISED,command=info).place(x=680,y=350)
                    label2 = Label(root7, text="CUSTOMER DETAILS",font=("Times New Roman", 15),relief=GROOVE,height=2,width=25,bg="#B0C4DE").place(x=300, y=440)
                    button1 = Button(root7,text="CLICK HERE", height=2, width=20, font=("verdana", 10), fg="blue",relief=RAISED,command=info_cus).place(x=680,y=430)
                    label2 = Label(root7, text="BILLING DETAILS",font=("Times New Roman", 15),relief=GROOVE,height=2,width=25,bg="#B0C4DE").place(x=300, y=520)
                    button1 = Button(root7,text="CLICK HERE", height=2, width=20, font=("verdana", 10), fg="blue",relief=RAISED,command=info_billing).place(x=680,y=510)
                    def des():
                        root7.withdraw()
                    button = Button(root7,command=des,text="BACK",width=20,height=3,font=("verdana", 12),fg=fb_color,bg=bt_color).pack(padx=25,pady=10,side=BOTTOM)
                    root7.mainloop()
                #extra
                def dele():
                    root8 =Toplevel(root2)
                    label1 = Label(root8, width=13, text=" manager login", fg=bg_color, font=("Times New Roman", 35), bg="#a9a9a9").place(x=85, y= 15)
                    root8.title("login")
                    root8.config(bg="#a9a9a9")
                    global passwd 
                    passwd = StringVar()
                    root8.minsize(520, 390)
                    root8.maxsize(520, 390)
                    def mlogin():
                        pas= int(passwd.get())
                        val = 11
                        if pas  is not int(val):
                            root8.withdraw()
                            messagebox.showerror("CARGO","      ENTER VALID VALUES      ")
                        else:
                            messagebox.showinfo("CARGO","         WELCOME             ")   
                            root8.withdraw()
                            root9 = Tk()
                            root9.config(bg=bg_color)
                            global delc
                            delc = StringVar()
                            label1 = Label(root9, width=23, text="CUSTOMERID", fg=bg_color, font=("Times New Roman", 15), bg="#a9a9a9").place(x=40, y= 170)
                            e2 = Entry(root9,font=('verdana',12), width=22)
                            e2.place(x=260, y=170,height=35)
                            def delcargo():
                                
                                def connect():
                                    conn = None
                                    try:
                                        conn = mysql.connector.connect(host='localhost',
                                                                    database='cargoproject',
                                                                    user='root',
                                                    password="1432"
                                                    )
                                        if conn.is_connected():
                                            try:
                                                cursor = conn.cursor()
                                                cursor.execute("delete  from customer where cust_id=%s",(e2.get(),))
                                                conn.commit()
                                                messagebox.showinfo("error",'deleted')
                                            except Error as error:
                                                messagebox.showerror("error", error)
                                            finally:
                                                cursor.close()
                                                conn.close()

                                    
                                    except Error as e:
                                        messagebox.showerror("error", e)
                                    finally:
                                        if conn is not None and conn.is_connected():
                                            conn.close()
                                            root9.withdraw()
                                connect()
                            
                            button1 = Button(root9, text="delete", width=15, command=delcargo, font=(b_font,18),bg=bt_color,fg=fb_color).place(x=155, y=310)
                            root9.minsize(520, 390)
                            root9.maxsize(520, 390)
                            root9.mainloop()

                    label1 = Label(root8, width=13, text="password", fg=bg_color, font=("Times New Roman", 20), bg="#a9a9a9").place(x=40, y= 170)
                    e2 = Entry(root8,font=('verdana',12), textvariable=passwd, show='*', width=22).place(x=260, y=170,height=35)
                    button1 = Button(root8, text="login", width=15, command=mlogin, font=(b_font,18),bg=bt_color,fg=fb_color).place(x=155, y=310)
                    #root8.resizable(False, False)
                    root8.mainloop()

                #home
                root2.config(bg=bg_color)
                root2.attributes('-fullscreen',True)
                label = Label(root2, text= "CARGO MANAGEMENT",font=("verdana", 55),fg=h_color,bg=bg_color).place(x=280, y=50)
                button1 = Button(root2, text="logout", width=15, font=(b_font, 18), fg=fb_color,bg=bt_color, command=home).place(x=535, y=590)
                button2 = Button(root2, text="CUSTOMER DETAILS", height=3, width=20, font=("verdana", 11), fg="blue", command =cust).place(x=45, y=250)
               # button1 = Button(root2, text="DELETEOPTIONS", height=3, width=20, font=("verdana", 11), fg="blue",command=dele).place(x=300, y=450)
                button3 = Button(root2, text="CARGO DETAILS:", height=3, width=20, font=("verdana", 11), fg="blue", command =cargo).place(x=295, y=250)
                button4 = Button(root2, text="BILLING DETAILS:", height=3, width=20, font=("verdana", 11), fg="blue", command=billing).place(x=545, y=250)
                button5 = Button(root2, text="TRANSPORTATION", height=3, width=20, font=("verdana", 11), fg="blue", command=transport).place(x=795, y=250)
                button6 = Button(root2, text="VIEW", height=3, width=20, font=("verdana", 11), fg="blue",command=view_d).place(x=1045, y=250)
                root2.mainloop()
            main() 
    root1.title("login")
    root1.config(bg="#a9a9a9")
    label1 = Label(root1, width=13, text="login", fg=bg_color, font=("Times New Roman", 35), bg="#a9a9a9").place(x=85, y= 15)
    label2 = Label(root1, width =15,text="EMPLOYEE ID :", bg="#a9a9a9", fg=bg_color,relief=FLAT, font=("Times New Roman", 17),height=2).place(x=40, y=120)
    label3 = Label(root1, width = 15,text="PASSWORD :", font=("Times New Roman", 17), bg="#a9a9a9",fg=bg_color,relief=FLAT ,height=2).place(x=40, y=200)
    e1 = Entry(root1, font=('verdana',12),textvariable=username, width=22).place(x=260, y=130,height=35)
    e2 = Entry(root1,font=('verdana',12), textvariable=password, show='*', width=22).place(x=260, y=210,height=35)
    button1 = Button(root1, text="login", width=15, command=onclick, font=(b_font,18),bg=bt_color,fg=fb_color).place(x=155, y=310)
    root1.mainloop()


# start    
canvas = Canvas(w3, width=1500, height=600, bg="#191970")
canvas.place(x=0, y=120)
canvas2 = Canvas(w3, width=170, height=100,bg="#191970")
canvas2.place(x=1050, y=10)
def ex():
    root.destroy()
root.attributes('-fullscreen',True)
button2 = Button(w3, text = "exit", width=15, height=2, font=(b_font,13),bg=bt_color,fg=fb_color,command= ex).place(x=10,y=10)
label = Label(w3, text= "CARGO MANAGEMENT",font=("verdana", 45),fg=h_color,bg=bg_color).place(x=245, y=40)
button1 = Button(canvas2, text="login", width=15, height=2, font=(b_font,17),bg=bt_color,fg=fb_color, command=login).pack()
img = ImageTk.PhotoImage(Image.open("image.jpeg"))
canvas.create_image(20, 20, anchor=NW, image=img)
mainloop()