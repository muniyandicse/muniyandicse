from tkinter import *

def red():
    Canvas1.create_oval(120,120,50,50, fill='red', outline='lightgray', width=3)
    Canvas2.create_oval(120,120,50,50, fill='white', outline='lightgray', width=3)
    Canvas3.create_oval(120,120,50,50, fill='white', outline='lightgray', width=3)

def yellow():
    Canvas1.create_oval(120,120,50,50, fill='white', outline='lightgray', width=3)
    Canvas2.create_oval(120,120,50,50, fill='yellow', outline='lightgray', width=3)
    Canvas3.create_oval(120,120,50,50, fill='white', outline='lightgray', width=3)

def green():
    Canvas1.create_oval(120, 120, 50, 50, fill='white', outline='lightgray', width=3)
    Canvas2.create_oval(120, 120, 50, 50, fill='white', outline='lightgray', width=3)
    Canvas3.create_oval(120, 120, 50, 50, fill='green', outline='lightgray', width=3)

obj = Tk()
obj.geometry('260x400')
obj.title('Traffic Lights - manual')

button1 = Button(obj, text='RED', font=('calibri',15),bg= 'gray',fg='white', width='11',height='1',command=red)
button1.grid(row=1,column=1)
Canvas1 = Canvas(obj, height=130, bg='black')
Canvas1.grid(row=1,column=2)

button2 = Button(obj, text='YELLOW', font=('calibri',15),bg= 'gray',fg='white', width='11',height='1',command=yellow)
button2.grid(row=2,column=1)
Canvas2 = Canvas(obj, height=130, bg='black')
Canvas2.grid(row=2,column=2)

button3 = Button(obj, text='GREEN', font=('calibri', 15), bg='gray', fg='white', width='11', height='1',command=green)
button3.grid(row=3, column=1)
Canvas3 = Canvas(obj, height=130, bg='black')
Canvas3.grid(row=3, column=2)

obj.mainloop()

