from tkinter import *

SENAC = Tk()
def Impressao():
    Nome['text'] = Botao.get()
#--------------------------------------------------------------------
#Front-End
Nome = Label(SENAC, text='Flamengo!',font='Calibri 20 ')
Caxinha = Entry(SENAC, font='Calibri 20')
Botao = Button(SENAC, text='Sim', font='Arial 20', bg='Green',command=Impressao)
Botao2 = Button(SENAC, text='Não', font='Arial 20', bg='Red',command=quit)
SENAC.geometry('300x190')
#SENAC.config(bg='Black')
#SENAC.maxsize(width=400, height=200)
#SENAC.minsize(width=1920, height=1080)
#--------------------------------------------------------------------
Nome.pack()
Caxinha.pack(),
Botao.pack()
Botao2.pack()
SENAC.mainloop()
