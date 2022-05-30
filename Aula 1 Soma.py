from tkinter import *



#Back-end   
def Soma():
    if en1.get().isnumeric() and en2.get().isnumeric():
        Janela['text'] = float(en1.get()) + float(en2.get())
    else:
        Janela['text'] = 'Valor Invalido'


Caixa = Tk()
Font = 'Arial 12 bold'
#--------------------------------------------------------------------
#Front-End
Janela   = Label(Caixa, text=(),font=Font)
en1  = Entry(Caixa, font=Font)
en2 = Entry(Caixa, font=Font)
Soma = Button(Caixa, text='Soma', font=Font, bg='Green',command=Soma)
Caixa.geometry('300x150')
Caixa.config (bg='Black')
#--------------------------------------------------------------------



#--------------------------------------------------------------------
Janela.pack()
en1.pack()
en2.pack()
Soma.pack()
Caixa.mainloop()