import tkinter
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='',db='authenticate')
cursor = db.cursor()


def admin():
    global adminframe
    global adminusername
    global adminpassword
    adminframe = Frame(authenticate)
    adminframe.pack()
    adminusername = StringVar()
    adminpassword = StringVar()
    Label(adminframe, text='username',font=('Arial',12,'bold')).pack()
    Entry(adminframe,textvariable=adminusername,font=('Arial',12,'bold')).pack()
    Label(adminframe, text='password', font=('Arial', 12, 'bold')).pack()
    Entry(adminframe, textvariable=adminpassword, font=('Arial', 12, 'bold')).pack()
    Button(adminframe, text='Login',command=adminlogin, width='12', height='1', font=('calibri', 10, 'bold'), bg='gray', fg='white').pack()

def adminlogin():
    username = adimusername.get()
    password = adminpassword.get()
    if username == 'admin' and password == 'admin@123':
        thinter.messagebox.showinfo('Authenticaton','wlecome Admin')
    else:
        tkinter.Messagebox.showinfo('authenticate','Invalid')

def userlogin():
    username = userusername.get()
    password = userpassword.get()
    cursor.execute('select * from details were username=%s and password=%s',[username,password])
    a = cursor.etchone()
    if a==None:
        thinter.messagebox.showinfo('Authenticaton', 'wlecome user')
    else:
        tkinter.Messagebox.showinfo('authenticate', 'Invalid')
def user():
    global userframe
    global userusername
    global userpassword
    userframe = Frame(authenticate)
    userframe.pack()
    userusername = StringVar()
    userpassword = StringVar()
    Label(userframe, text='username', font=('Arial', 12, 'bold')).pack()
    Entry(userframe, textvariable=userusername, font=('Arial', 12, 'bold')).pack()
    Label(userframe, text='password', font=('Arial', 12, 'bold')).pack()
    Entry(userframe, textvariable=userpassword, font=('Arial', 12, 'bold')).pack()
    Button(authenticate, text='login',command=userlogin, width='12', height='1', font=('calibri', 10, 'bold'), bg='gray',fg='white').pack()
    Button(authenticate, text='signup',command=register, width='12', height='1', font=('calibri', 10, 'bold'), bg='gray',fg='white').pack()


def register():
    global registerframe
    global registerrname
    global registermail
    global registeraddress
    global registergender
    global registerusername
    global registerpassword
    userframe.destroy()
    registerframe = Frame(authenticate)
    registerframe.pack()
    registername = StringVar()
    registermail = StringVar()
    registeraddress = StringVar()
    registergender = StringVar()
    registerusername = StringVar()
    registerpassword = StringVar()
    Label(registerframe, text='Name', font=('Arial', 12, 'bold')).pack()
    Entry(registerframe, textvariable=registername, font=('Arial', 12, 'bold')).pack()
    Label(registerframe, text='mail', font=('Arial', 12, 'bold')).pack()
    Entry(registerframe, textvariable=registermail, font=('Arial', 12, 'bold')).pack()
    Label(registerframe, text='gender', font=('Arial', 12, 'bold')).pack()
    Radiobutton(registerframe, text='Male',variable=registergender,value='male', font=('Arial', 12, 'bold')).pack()
    Radiobutton(registerframe, text='Female', variable=registergender, value='female', font=('Arial', 12, 'bold')).pack()
    Label(registerframe, text='address', font=('Arial', 12, 'bold')).pack()
    Entry(registerframe, textvariable=registeraddress, font=('Arial', 12, 'bold')).pack()
    Label(registerframe, text='username', font=('Arial', 12, 'bold')).pack()
    Entry(registerframe, textvariable=registerusername, font=('Arial', 12, 'bold')).pack()
    Label(registerframe, text='password', font=('Arial', 12, 'bold')).pack()
    Entry(registerframe, textvariable=registerpassword, font=('Arial', 12, 'bold')).pack()
    Button(authenticate, text='submit',command=store_data, width='12', height='1', font=('calibri', 10, 'bold'), bg='gray',fg='white').pack()

def store_data():
    name = registername.get()
    mail = registermail.get()
    address = registeraddress.get()
    gender = registergender.get()
    username = registerusername.get()
    password = registerpassword.get()
    cursor.execute('insert into details(name,mail,gender,address,username,password)values(%s,%s,%s,%s,%s,%s)',[name,mail,gender,address,username,password])
    db.commit()
    thinter.massagebox.showinfo('authentication','register successfully')

def main():
    global authenticate
    global data
    authenticate = Tk()
    authenticate.geometry('1080x650')
    authenticate.title('Authenticate & Authorization')
    authenticate.configure(bg='lightblue')
    button1 = Button(authenticate,text='Admin',command=admin,width='15',height='1',font=('calibri',13,'bold'),bg='gray',fg='white')
    button1.pack()
    button2 = Button(authenticate, text='User',command=user, width='15', height='1', font=('calibri', 13, 'bold'), bg='gray', fg='white')
    button2.pack()
    authenticate.mainloop()

main()


