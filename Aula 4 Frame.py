from tkinter import *
root = Tk()

fr1 = Frame(root)
fr2 = Frame(root)

lb1 = Label(fr1, text='Label Frame 1')
lb2 = Label(fr2, text='Label Frame 2')
bt1 = Button(fr1, text='Bt Frame 1')
bt2 = Button(fr2, text='Bt Frame 2')




fr1.pack()
fr2.pack()
lb1.grid(row=0, column=0)
bt1.grid(row=1, column=1)
lb2.grid(row=0, column=0)
bt2.grid(row=1, column=1)

root.mainloop()