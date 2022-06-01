from tkinter import *

def Temp(event):
     if Box_.get().isnumeric():
           F['text'] = (float(Box_.get())*1.8) + 32
     else:
           F['text'] = 'Valor Invalido'

SENAC = Tk()
SENAC.bind('<Return>', Temp)
FN = 'Verdana 20 bold'
C= Label(SENAC, text='C°:', font=FN) 
Label_= Label(SENAC, text='Convert °F:', font=FN) 
F= Label(SENAC, text=0, font=FN) 
Box_= Entry(SENAC, font=FN)
But_= Button(SENAC, font=FN, text='Converter', command=Temp)





C.grid(row=2, column=0)
Label_.grid(row=3, column=0)
F.grid(row=3, column=1)
Box_.grid(row=2, column=1)
But_.grid(row=4, column=0)
SENAC.mainloop()





