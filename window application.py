import tkinter.messagebox
from tkinter import *
def add():
    num1 = number1.get()
    num2 = number2.get()
    num3 = number3.get()
    num4 = number4.get()
    num5 = number5.get()
    result = int(num1)+int(num2)+int(num3)+int(num4)+int(num5)
    tkinter.messagebox.showinfo('Result',result)

obj = Tk()
obj.geometry('500x400')
obj.title('register job application')
obj.configure(bg='red')

Label(obj,text='alex name:',font=('arial',15,'bold'),bg='red').grid(row=1,column=1)
Label(obj,text='enter value B:',font=('arial',15,'bold'),bg='red').grid(row=2,column=1)
Label(obj,text='enter value C:',font=('arial',15,'bold'),bg='red').grid(row=3,column=1)
Label(obj,text='enter value D:',font=('arial',15,'bold'),bg='red').grid(row=4,column=1)
Label(obj,text='enter value E:',font=('arial',15,'bold'),bg='red').grid(row=5,column=1)

number1 = StringVar()
number2 = StringVar()
number3 = StringVar()
number4 = StringVar()
number5 = StringVar()


Entry(obj,textvariable=number1,font=('arial',15)).grid(row=1,column=2)
Entry(obj,textvariable=number2,font=('arial',15)).grid(row=2,column=2)
Entry(obj,textvariable=number3,font=('arial',15)).grid(row=3,column=2)
Entry(obj,textvariable=number4,font=('arial',15)).grid(row=4,column=2)
Entry(obj,textvariable=number5,font=('arial',15)).grid(row=5,column=2)

Button(obj,text='ADD',width='15',height='2',bg='gray',fg='white',command=add).grid(row=4,column=3)

obj.mainloop()

