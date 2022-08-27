from tkinter import*
from tkinter import ttk

def func(selected):
    dropmenu2.set_menu(*option2.get(selected))

forms = Tk()
forms.geometry('400x500')
forms.configure(bg='light blue')
Label1 = Label(forms,text = 'select the state',font=('arial',12,'bold'))
Label1.place(x=20,y=100)
option1 = ['andhra pradesh','goa','karnataka','karala','tamilnadeu']
drop1 = StringVar()
dropmenu1 = ttk.optionmenu(forms,drop1,'.....select.....',command = func)
dropmenu1.place (x=200,y=100)
Label2 = Label(forms,text='select the district',font=('arial',12,'bold'))
Label2.place (x=20,y=200)
option2 ={'andhra pradesh':['chittor','gantur','nellore'],
    'goa':['north goa','south goa'],
    'karnataka':['mysore','kolar'],
    'karla':['ernakulam','kollam','alappizha'],
    'tamilnadu':['chennai','salem','trichy']
 }
drop2 = StringVar()
dropmenu2 = ttk.optionmenu(forms,drop2,'...select...')
dropmenu2.place(x=200,y=200)
forms.mainloop()