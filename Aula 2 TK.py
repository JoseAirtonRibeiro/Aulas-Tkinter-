from tkinter import *
#________________________________________________________________
#Back-end

#________________________________________________________________
Jan = Tk()
Jan.grid_rowconfigure(1, weight=1)
Jan.grid_rowconfigure(2, weight=1)
Jan.grid_rowconfigure(3, weight=1)
Jan.grid_rowconfigure(4, weight=1)
Jan.grid_columnconfigure(0, weight=1)

Jan.grid_columnconfigure(1, weight=1)

Jan.grid_columnconfigure(2, weight=1)


SENAC = 'Calibri 50'

SenP = Button(Jan, text='+', font=SENAC, foreground='green', background='black')
SenL = Button(Jan, text='_', font=SENAC, foreground='green', background='black')
SenE = Button(Jan, text='=', font=SENAC, foreground='green', background='black')
Sen1 = Button(Jan, text='1', font=SENAC, foreground='green', background='black')
Sen2 = Button(Jan, text='2', font=SENAC, foreground='green', background='black')
Sen3 = Button(Jan, text='3', font=SENAC, foreground='green', background='black')
Sen4 = Button(Jan, text='4', font=SENAC, foreground='green', background='black')
Sen5 = Button(Jan, text='5', font=SENAC, foreground='green', background='black')
Sen6 = Button(Jan, text='6', font=SENAC, foreground='green', background='black')
Sen7 = Button(Jan, text='7', font=SENAC, foreground='green', background='black')
Sen8 = Button(Jan, text='8', font=SENAC, foreground='green', background='black')
Sen9 = Button(Jan, text='9', font=SENAC, foreground='green', background='black')
Jan.config(bg='Black')



SenE.grid(row=1,column=0, sticky= NSEW)
SenP.grid(row=1,column=1, sticky= NSEW)
SenL.grid(row=1,column=2, sticky= NSEW)
Sen1.grid(row=2,column=0, sticky= NSEW)
Sen2.grid(row=2,column=1, sticky= NSEW)
Sen3.grid(row=2,column=2, sticky= NSEW)
Sen4.grid(row=3,column=0, sticky= NSEW)
Sen5.grid(row=3,column=1, sticky= NSEW)
Sen6.grid(row=3,column=2, sticky= NSEW)
Sen7.grid(row=4,column=0, sticky= NSEW)
Sen8.grid(row=4,column=1, sticky= NSEW)
Sen9.grid(row=4,column=2, sticky= NSEW)

Jan.mainloop()
