from tkinter import *

def IMC():
    try:
        Lab_['text'] = float(En1.get()) / (float(En2.get()) * float(En2.get()))
    except:
        Lab_['text'] = 'Valor Invalido'
FN = 'Verdana 20 bold'

def Temp():
     if Ent.get().isnumeric():
           Resul['text'] = (float(Ent.get())*1.8) + 32
     else:
           Resul['text'] = 'Valor Invalido'






#__________________________________________________________________________________________________
SENAC = Tk()
Fra_ = Frame(SENAC)
Fra2 = Frame(SENAC)

Fra_.bind('<Return>',lambda event:IMC())
Lab_= Label(Fra_, text=0.0, font=FN) 
Lab2= Label(Fra_, text='Altura:', font=FN) 
Lab3= Label(Fra_, text='Peso:', font=FN) 
En1= Entry(Fra_, font=FN)
En2= Entry(Fra_, font=FN)
Bt_= Button(Fra_, font=FN, text='IMC', command=IMC)

Lab_.grid(row=0, column=1, sticky=NSEW)
Lab2.grid(row=2, column=0, sticky=NSEW)
Lab3.grid(row=1, column=0, sticky=NSEW)
En1.grid  (row=1, column=1, sticky=NSEW)
En2.grid  (row=2, column=1, sticky=NSEW)
Bt_.grid  (row=3,column=1, sticky=NSEW)





Fra_.columnconfigure(0, weight=1)
Fra_.columnconfigure(1, weight=1)
Fra_.rowconfigure(1, weight=1)
Fra_.rowconfigure(2, weight=1)
Fra_.rowconfigure(3, weight=1)

#___________________________________________________________________________________________
Fra2.bind('<Return>',lambda event:Temp())
LabF= Label(Fra2, text='C°:', font=FN) 
LabF2= Label(Fra2, text='Convert °F:', font=FN) 
Resul= Label(Fra2, text=0, font=FN) 
Ent= Entry(Fra2, font=FN)
But= Button(Fra2, font=FN, text='Converter', command=Temp)

LabF.grid(row=2, column=0, sticky=NSEW)
LabF2.grid(row=3, column=0, sticky=NSEW)
Resul.grid(row=3, column=1, sticky=NSEW)
Ent.grid(row=2, column=1, sticky=NSEW)
But.grid(row=4, column=0, sticky=NSEW)
Fra2.columnconfigure(0, weight=1)
Fra2.columnconfigure(1, weight=1)
Fra2.rowconfigure(1, weight=1)
Fra2.rowconfigure(2, weight=1)
Fra2.rowconfigure(3, weight=1)


Fra_.pack(side=LEFT)
Fra2.pack(side=LEFT)
SENAC.mainloop()