from tkinter import *
#___________________________________________________________________________________
#Back-end
def Num(Vl):
    Scr['text']+= Vl
    pass

def NumOp():
  Res= eval(Scr['text'])
  Scr['text'] = str(Res)


def Clean():
    Scr['text']= ''
  
def Del():
    
    Scr['text'] -= ''
    pass
#___________________________________________________________________________________
fn= 'verdana 30 bold'
SENAC = Tk()
Scr= Label(SENAC, text='',font='verdana 40 bold', fg='black')

Lpa = Button(SENAC, text='(', font=fn, bg='#302930',fg='white',command=lambda: Num('('))
Rpa = Button(SENAC, text=')', font=fn, bg='#302930',fg='white',command=lambda: Num(')'))
Sum = Button(SENAC, text='+', font=fn, bg='#302930',fg='white',command=lambda: Num('+'))
Div = Button(SENAC, text='/', font=fn, bg='#302930',fg='white',command=lambda: Num('/'))
Mul = Button(SENAC, text='*', font=fn, bg='#302930',fg='white',command=lambda: Num('*'))
Les = Button(SENAC, text='_', font=fn, bg='#302930',fg='white',command=lambda: Num('-'))
Dot = Button(SENAC, text='.', font=fn, bg='#302930',fg='white',command=lambda: Num('.'))
One = Button(SENAC, text='1', font=fn, bg='#302930',fg='white',command=lambda: Num('1'))
Two = Button(SENAC, text='2', font=fn, bg='#302930',fg='white',command=lambda: Num('2'))
Thr = Button(SENAC, text='3', font=fn, bg='#302930',fg='white',command=lambda: Num('3'))
Fou = Button(SENAC, text='4', font=fn, bg='#302930',fg='white',command=lambda: Num('4'))
Fiv = Button(SENAC, text='5', font=fn, bg='#302930',fg='white',command=lambda: Num('5'))
Six = Button(SENAC, text='6', font=fn, bg='#302930',fg='white',command=lambda: Num('6'))
Sev = Button(SENAC, text='7', font=fn, bg='#302930',fg='white',command=lambda: Num('7'))
Eig = Button(SENAC, text='8', font=fn, bg='#302930',fg='white',command=lambda: Num('8'))
Nin = Button(SENAC, text='9', font=fn, bg='#302930',fg='white',command=lambda: Num('9'))
Zer = Button(SENAC, text='0', font=fn, bg='#302930',fg='white',command=lambda: Num('0'))
Equ = Button(SENAC, text='=', font=fn, bg='#302930',fg='white',command=NumOp)
C = Button(SENAC, text='C', font=fn, bg='#302930',fg='white', command=Clean)
Del = Button(SENAC, text='Del', font=fn,bg='#302930',fg='white', command=Del)

SENAC.geometry('500x700')
SENAC.grid_columnconfigure(0, weight=1)
SENAC.grid_columnconfigure(1, weight=1)
SENAC.grid_columnconfigure(2, weight=1)
SENAC.grid_columnconfigure(3, weight=1)
SENAC.grid_columnconfigure(4, weight=1)
SENAC.grid_rowconfigure(0, weight=1)
SENAC.grid_rowconfigure(1, weight=1)
SENAC.grid_rowconfigure(2, weight=1)
SENAC.grid_rowconfigure(3, weight=1)
SENAC.grid_rowconfigure(4, weight=1)



#___________________________________________________________________________________
Scr.grid(row=0, column=1, sticky=NSEW, columnspan=4)
Sum.grid(row=4, column=0, sticky=NSEW)
Div.grid(row=4, column=1, sticky=NSEW)
Mul.grid(row=4, column=2, sticky=NSEW)
Les.grid(row=4, column=3, sticky=NSEW)
Equ.grid(row=4, column=4, sticky=NSEW)
One.grid(row=3, column=1, sticky=NSEW)
Two.grid(row=3, column=2, sticky=NSEW)
Thr.grid(row=3, column=3, sticky=NSEW)
Fou.grid(row=2, column=1, sticky=NSEW)
Fiv.grid(row=2, column=2, sticky=NSEW)
Six.grid(row=2, column=3, sticky=NSEW)
Sev.grid(row=1, column=1, sticky=NSEW)
Eig.grid(row=1, column=2, sticky=NSEW)
Nin.grid(row=1, column=3, sticky=NSEW)
Zer.grid(row=3, column=0, sticky=NSEW)
Rpa.grid(row=2, column=0, sticky=NSEW)
Lpa.grid(row=1, column=0, sticky=NSEW)
Dot.grid(row=1, column=4, sticky=NSEW)
Del.grid(row=3, column=4, sticky=NSEW)
C.grid  (row=2, column=4, sticky=NSEW)
SENAC.bind('1',lambda event:Num('1'))
SENAC.bind('2',lambda event:Num('2'))
SENAC.bind('3',lambda event:Num('3'))
SENAC.bind('4',lambda event:Num('4'))
SENAC.bind('5',lambda event:Num('5'))
SENAC.bind('6',lambda event:Num('6'))
SENAC.bind('7',lambda event:Num('7'))
SENAC.bind('8',lambda event:Num('8'))
SENAC.bind('9',lambda event:Num('9'))
SENAC.bind('/',lambda event:Num('/'))
SENAC.bind('*',lambda event:Num('*'))
SENAC.bind('+',lambda event:Num('+'))
SENAC.bind('-',lambda event:Num('-'))
SENAC.bind('.',lambda event:Num('.'))
SENAC.bind('<Return>',lambda event:NumOp())
SENAC.bind('<Backspace>',lambda event:Del())

SENAC.mainloop()
#___________________________________________________________________________________