from tkinter import *

def tot():
    student_overall.set(product_price.get() * student_prcantage.get())

access = Tk()
access.geometry('700x600')
access.title('access control matrix')
access.configure(bg='lightblue')


Label(access,text='Student attendance Entry',font=('arial',17,'bold'),bg='lightblue',fg='blue').grid(row=1,column=1)

student_id_label = Label(access,text='student id', font=('arial',15,'bold'),bg='lightblue')
student_id_label.grid(row=2,column=1)
student_id = StringVar()
student_id_entry = Entry(access,textvariable=student_id, font=('arial',15,'bold'))
student_id_entry.grid(row=2,column=2)

student_name_label = Label(access,text='student name', font=('arial',15,'bold'),bg='lightblue')
student_name_label.grid(row=3,column=1)
student_name = StringVar()
student_name_entry = Entry(access,textvariable=student_name, font=('arial',15,'bold'))
student_name_entry.grid(row=3,column=2)


student_monthly_label = Label(access,text='student monthly', font=('arial',15,'bold'),bg='lightblue')
student_monthly_label.grid(row=4,column=1)
student_monthly = IntVar()
student_monthly_entry = Entry(access,textvariable=student_monthly, font=('arial',15,'bold'))
student_monthly_entry.grid(row=4,column=2)


student_prcantage_label = Label(access,text='student prcantage', font=('arial',15,'bold'),bg='lightblue')
student_prcantage_label.grid(row=5,column=1)
student_prcantage = IntVar()
student_prcantage_entry = Entry(access,textvariable=student_prcantage, font=('arial',15,'bold'))
student_prcantage_entry.grid(row=5,column=2)

student_overall_label = Label(access,text='student overall', font=('arial',15,'bold'),bg='lightblue')
student_overall_label.grid(row=6,column=1)
student_overall = IntVar()
student_overall_entry = Entry(access,textvariable=student_overall, font=('arial',15,'bold'))
student_overall_entry.grid(row=6,column=2)

but_cal = Button(access,text='CALCULATE',command=tot,font=('arial',15,'bold'),bg='gray',fg='white',width='10',height='1')
but_cal.grid(row=8,column=3)


but_add = Button(access,text='ADD', font=('arial',15,'bold'),bg='gray',fg='white',width='7',height='1')
but_add.grid(row=7,column=1)

but_view = Button(access,text='VIEW', font=('arial',15,'bold'),bg='gray',fg='white',width='7',height='1')
but_view.grid(row=7,column=2)

but_upd = Button(access,text='UPDATE', font=('arial',15,'bold'),bg='gray',fg='white',width='7',height='1')
but_upd.grid(row=8,column=1)

but_del = Button(access,text='DELETE', font=('arial',15,'bold'),bg='gray',fg='white',width='7',height='1')
but_del.grid(row=8,column=2)

but_over = Button(access,text='OVERALL', font=('arial',15,'bold'),bg='gray',fg='white',width='7',height='1')
but_over.grid(row=9,column=1)

but_clr = Button(access,text='CLEAR', font=('arial',15,'bold'),bg='gray',fg='white',width='7',height='1')
but_clr.grid(row=9,column=2)
access.mainloop()