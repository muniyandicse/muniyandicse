import tkinter.messagebox
from tkinter import *

play = Tk()
play.geometry('700x500')
play.title('XO games')
play.configure(bg ='aqua')

playerA = StringVar()
playerB = StringVar()
p1 = StringVar()
p2 = StringVar()
buttons = StringVar()
bclick = True
turns = 0
def btnclick(buttons):
    global bclick, turns, playerB, playerA
    if buttons['text'] == ' ' and bclick == True:
        buttons['text'] ='X'
        bclick = False
        playerB = p2.get() + " Wins"
        playerA = p1.get() + " Wins"
        possibilities()
        turns += 1
    elif buttons['text'] == ' ' and bclick == False:
        buttons['text'] = 'O'
        bclick = True
        possibilities()
        turns += 1
    else:
        tkinter.messagebox.showinfo(' XO games','buttons already clicked')

def possibilities():
    if (button1['text'] == 'X'and button2['text'] == 'X' and button3['text'] == 'X'or
            button4['text'] == 'X'and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X'and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X'and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X'and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X'and button6['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X'and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X'and button5['text'] == 'X' and button7['text'] == 'X'):
         tkinter.messagebox.showinfo('XO games',playerA)
    elif (button1['text'] == 'O'and button2['text'] == 'O' and button3['text'] == 'O'or
            button4['text'] == 'O'and button5['text'] == 'O' and button6['text'] == 'O' or
            button7['text'] == 'O'and button8['text'] == 'O' and button9['text'] == 'O' or
            button1['text'] == 'O'and button4['text'] == 'O' and button7['text'] == 'O' or
            button2['text'] == 'O'and button5['text'] == 'O' and button8['text'] == 'O' or
            button3['text'] == 'O'and button6['text'] == 'O' and button9['text'] == 'O' or
            button1['text'] == 'O'and button5['text'] == 'O' and button9['text'] == 'O' or
            button3['text'] == 'O'and button5['text'] == 'O' and button7['text'] == 'O'):
         tkinter.messagebox.showinfo('XO games',playerB)
    elif turns == 8:
        tkinter.messagebox.showinfo('XO games','match Draw')



player1_name_label = Label(play,text='player 1 name',font=('batmfa',15,'bold'),bg='aqua')
player1_name_label.grid(row=1,column=1)
player1_name_entry = Entry(play,textvariable=p1,font=('batmfa',15,'bold'))
player1_name_entry.grid(row=1,column=2)
player2_name_label = Label(play,text='player 2 name',font=('batmfa',15,'bold'),bg='aqua')
player2_name_label.grid(row=2,column=1)
player2_name_entry = Entry(play,textvariable=p2,font=('batmfa',15,'bold'))
player2_name_entry.grid(row=2,column=2)

button1 = Button(play,text=' ',font=('arial',15,'bold'),bg='gray', fg='white', width='7', height='3',
                 command = lambda :btnclick(button1))
button1.grid(row=3,column=3)

button2 = Button(play,text=' ',font=('arial',15,'bold'),bg='gray', fg='white', width='7', height='3',
                command = lambda :btnclick(button2))
button2.grid(row=3,column=4)

button3 = Button(play,text=' ',font=('arial',15,'bold'),bg='gray', fg='white', width='7', height='3',
                command = lambda :btnclick(button3))
button3.grid(row=3,column=5)

button4 = Button(play,text=' ',font=('arial',15,'bold'),bg='gray', fg='white', width='7', height='3',
                command = lambda :btnclick(button4))
button4.grid(row=4,column=3)

button5 = Button(play,text=' ',font=('arial',15,'bold'),bg='gray', fg='white', width='7', height='3',
                command = lambda :btnclick(button5))
button5.grid(row=4,column=4)

button6 = Button(play,text=' ',font=('arial',15,'bold'),bg='gray', fg='white', width='7', height='3',
                command = lambda :btnclick(button6))
button6.grid(row=4,column=5)

button7 = Button(play,text=' ',font=('arial',15,'bold'),bg='gray', fg='white', width='7', height='3',
                command = lambda :btnclick(button7))
button7.grid(row=5,column=3)

button8 = Button(play,text=' ',font=('arial',15,'bold'),bg='gray', fg='white', width='7', height='3',
                command = lambda :btnclick(button8))
button8.grid(row=5,column=4)

button9 = Button(play,text=' ',font=('arial',15,'bold'),bg='gray', fg='white', width='7', height='3',
                command = lambda :btnclick(button9))
button9.grid(row=5,column=5)
play.mainloop()




