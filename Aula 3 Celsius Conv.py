from tkinter import *

def Temp():
     if Box_.get().isnumeric():
           F['text'] = (float(Box_.get())*1.8) + 32
     else:
           F['text'] = 'Valor Invalido'

SENAC = Tk()

SENAC.columnconfigure(0, weight=1)
SENAC.columnconfigure(1, weight=1)
SENAC.rowconfigure(1, weight=1)
SENAC.rowconfigure(2, weight=1)
SENAC.rowconfigure(3, weight=1)


SENAC.bind('<Return>',lambda event:Temp())
FN = 'Verdana 20 bold'
C= Label(SENAC, text='C°:', font=FN) 
Label_= Label(SENAC, text='Convert °F:', font=FN) 
F= Label(SENAC, text=0, font=FN) 
Box_= Entry(SENAC, font=FN)
But_= Button(SENAC, font=FN, text='Converter', command=Temp)

C.grid(row=1, column=0, sticky=NSEW)
Label_.grid(row=2, column=0, sticky=NSEW)
F.grid(row=2, column=1, sticky=NSEW)
Box_.grid(row=1, column=1, sticky=NSEW)
But_.grid(row=3, column=0, sticky=NSEW)
SENAC.mainloop()







