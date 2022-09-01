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
    Button(authenticate, text='login',command=adminlogin, width='12', height='1', font=('calibri', 10, 'bold'), bg='gray', fg='white')

def adminlogin():
    username = adimusername.get()
    password = adminpassword.get()
    if username == 'admin' and password == 'admin@123':
        thinter.messagebox.showinfo('Authenticaton','wlcome Admin')
    else:
        tkinter.Messagebox.showinfo('authenticate','Invalid')

def adminhome():
    global adminpage
    adminpage = toplevel(authenticate)
    adminpage.geometry('1200x700')
    adminpage.title('Admin home')
    adminpage.configure(bg='auqa')
    addcategory = Button(authenticate, text='Add Question Category', command=categoryform, width='15', height='1', font=('calibri', 13, 'bold'),bg='gray', fg='white')
    addcategory.place(x=20,y=50)
    addcategory = Button(authenticate, text='Add Question', command=questionfrom, width='15', height='1', font=('calibri', 13, 'bold'),bg='gray', fg='white')
    addcategory.palce(x=650,y=50)

def categoryform():
    global categoryframe
    global category
    category = StringVar()
    categoryframe = Frame(adminpage, height=180,width=500,bg = 'white').place(x=30,y=100)
    Label(adminpage, text='Enter category',font=('calibri',15,'bold')).place(x=80,y=130)
    Entry(adminpage, textvariable=category,font=('calibri',15,'bold'),bg='aqua').place(x=300,y=130)
    Button(adminpage, text='ADD', font=('calibri', 15, 'bold'),width='10',height='1',bg='gray',fg='white').place(x=400,y=180)
def store_category():
    cate = category.get()
    cursor.execute('insert into categorydata(name) values(%s)',[cate])
    db.commit()
    tkinter.messagebox.showinfo('Assessment','Added')
def categories():
    cursor.execute('select name from categorygata')
    new = []
    a = cursor,fetchall()
    for i in a:
        new.append(i[0])
    return new

def questionform():
    global questionframe
    global question
    global option1
    global option2
    global option3
    global option4
    global answer
    global selected
    question = StringVar()
    option1 = StringVar()
    option2 = StringVar()
    option3 = StringVar()
    option4 = StringVar()
    answer = StringVar()
    selected = StringVar()
    selected.set('------------select category-----------')
    questionframe = Frame(adminpage, height=180, width=500, bg='white').place(x=600, y=100)
    a = categories()
    Label(adminpage, text='Selected category', font=('calibri', 15, 'bold')).place(x=620, y=130)
    OptionMenu(adminpage, selected, *a).place(x=700, y=130)
    Label(adminpage, text='question', font=('calibri', 15, 'bold')).place(x=620, y=180)
    Entry(adminpage, textvariable=question, font=('calibri', 15, 'bold'), bg='aqua').place(x=780, y=180)
    Label(adminpage, text='optionA', font=('calibri', 15, 'bold')).place(x=620, y=230)
    Entry(adminpage, textvariable=optionA, font=('calibri', 15, 'bold'), bg='aqua').place(x=780, y=230)
    Label(adminpage, text='optionB', font=('calibri', 15, 'bold')).place(x=620, y=280)
    Entry(adminpage, textvariable=optionB, font=('calibri', 15, 'bold'), bg='aqua').place(x=700, y=130)
    Label(adminpage, text='optionC', font=('calibri', 15, 'bold')).place(x=620, y=330)
    Entry(adminpage, textvariable=optionC, font=('calibri', 15, 'bold'), bg='aqua').place(x=780, y=380)
    Label(adminpage, text='optionD', font=('calibri', 15, 'bold')).place(x=620, y=3380)
    Entry(adminpage, textvariable=optionD, font=('calibri', 15, 'bold'), bg='aqua').place(x=700, y=130)
    Label(adminpage, text='Answer', font=('calibri', 15, 'bold')).place(x=620, y=430)
    Entry(adminpage, textvariable=answer, font=('calibri', 15, 'bold'), bg='aqua').place(x=700, y=130)
    Button(adminpage, text='ADD',command=store_question, font=('calibri', 15, 'bold'), width='10', height='1', bg='gray',fg='white').place(x=850, y=180)

def store_question():
    quest = question.get()
    op1 = option1.get()
    op2 = option2.get()
    op3 = option3.get()
    op4 = option4.get()
    clicked = selected.get()
    cursor.execute('insert into questiondata(qstn,opA,opB,opC,opD,ans,category) values()%s,%s,%s,%s,%s,%s,%s',[quest,op1,op2,op3,op4,ans,clicked])
    db.commit()
    tkinter.messagebox,showinfo('assessment','Added')

def userlogin():
    username = userusername.get()
    password = userpassword.get()
    cursor.execute('select * from details were username=%s and password=%s',[username,passwword])
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
    button1 = Button(authenticate,text='admin',command=admin,width='15',height='1',font=('calibri',13,'bold'),bg='gray',fg='white')
    button1.pack()
    button2 = Button(authenticate, text='User',command=user, width='15', height='1', font=('calibri', 13, 'bold'), bg='gray', fg='white')
    button2.pack()
    authenticate.mainloop()

main()


