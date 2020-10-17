from tkinter import *
from tkinter import messagebox
"""
Creation of a TicTacToe Game
Initiate the window
"""
win=Tk()
win.title("Tic Tac Toe")

bclick = True

mainFrm = Frame(win)
mainFrm.pack()


# Defining buttons
def ttt(buttons):
    global bclick
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
    CheckWinner()

# Checking for winner
def CheckWinner():
    if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'or
    button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'or
    button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'or
    button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'or
    button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'or
    button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'or
    button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'or
    button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'or
    button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'or
    button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'):
        messagebox.showinfo("Player X",'Winner is X !')
        button1["text"] = " "
        button2["text"] = " "
        button3["text"] = " "
        button4["text"] = " "
        button5["text"] = " "
        button6["text"] = " "
        button7["text"] = " "
        button8["text"] = " "
        button9["text"] = " "
        bclick = True
    elif(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
    button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'or
    button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'or
    button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'or
    button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'or
    button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
    button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'or
    button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'or
    button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'or
    button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'):
        messagebox.showinfo("Player O",'Winner is O !')
        button1["text"] = " "
        button2["text"] = " "
        button3["text"] = " "
        button4["text"] = " "
        button5["text"] = " "
        button6["text"] = " "
        button7["text"] = " "
        button8["text"] = " "
        button9["text"] = " "
        bclick = True
    elif(button1['text'] != ' ' and button2['text'] != ' ' and button3['text'] != ' ' and
    button4['text'] != ' ' and button5['text'] != ' ' and button6['text'] != ' ' and
    button7['text'] != ' ' and button8['text'] != ' ' and button9['text'] != ' '):
        messagebox.showinfo("No winners","That's a tie!")
        button1["text"] = " "
        button2["text"] = " "
        button3["text"] = " "
        button4["text"] = " "
        button5["text"] = " "
        button6["text"] = " "
        button7["text"] = " "
        button8["text"] = " "
        button9["text"] = " "
        bclick = True


# Buttons and the colors to change
buttons=StringVar()

# Creation of buttons to represent the houses of TicTacToe
# Buttons from 1-9 starting on the top left
# Bottom right represent the last button
button1 = Button(mainFrm,text=" ",font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button1))
button1.grid(row=1,column=0,sticky = S+N+E+W)

button2 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button2))
button2.grid(row=1,column=1,sticky = S+N+E+W)

button3 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button3))
button3.grid(row=1,column=2,sticky = S+N+E+W)

button4 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button4))
button4.grid(row=2,column=0,sticky = S+N+E+W)

button5 = Button(mainFrm, text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button5))
button5.grid(row=2,column=1,sticky = S+N+E+W)

button6 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button6))
button6.grid(row=2,column=2,sticky = S+N+E+W)

button7 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button7))
button7.grid(row=3,column=0,sticky = S+N+E+W)

button8 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button8))
button8.grid(row=3,column=1,sticky = S+N+E+W)

button9 = Button(mainFrm,text=' ',font=('Times 24 bold'),bg='gray',fg='blue',height=4,width=8,command=lambda:ttt(button9))
button9.grid(row=3,column=2,sticky = S+N+E+W)
win.mainloop()


