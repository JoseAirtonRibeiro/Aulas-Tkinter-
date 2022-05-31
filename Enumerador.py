from itertools import count
from tkinter import *
#_______________________________________________________________________________________________
nume=1
def Less():
    Janelinha['text'] = int(Janelinha['text']) - nume

def Plus():
    Janelinha['text'] = int(Janelinha['text']) + nume
#_______________________________________________________________________________________________
Regulador = Tk()
Regulador.geometry('500x200')
Regulador.grid_columnconfigure(0, weight=10)
Regulador.grid_rowconfigure(0, weight=10)

Regulador.grid_columnconfigure(1, weight=10)

Regulador.grid_columnconfigure(2, weight=10)




Regulador.config(bg='black')

FONT ='Calibri 40 bold'

Janelinha= Label(Regulador, text='0', font=FONT, foreground='#5AF90A', background='#000000')
Nu_= Button(Regulador, text='+', font=FONT, foreground='#5AF90A', background='#000000', command=Plus)
Nu2= Button(Regulador, text='_', font=FONT, foreground='#5AF90A', background='#000000', command=Less)



Janelinha.grid(row=0, column=1, sticky= NSEW)
Nu2.grid(row=0, column=0, sticky= NSEW)
Nu_.grid(row=0, column=2, sticky= NSEW)
Regulador.mainloop()