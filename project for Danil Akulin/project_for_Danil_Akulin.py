from tkinter import *
from math import *



aken=Tk()
aken.geometry("600x200")
aken.title('kvadratnoe uravnenie')
lbl=Label(aken,text='resenie kvadratnovo urovnenija', font='Calibri 26', fg='green', bg='lightblue')
lbl.pack()
a=Entry(aken,font='Calibri 26', fg='green', bg='lightblue', width=3)
a.pack(side=LEFT)

g=Label(aken,text='resenie', font='Calibri 26', fg='yellow', bg='lightblue')
g.pack(side=BOTTOM)

x2=Label(aken,text='x**2+', font='Calibry 26', fg='green')
x2.pack(side=LEFT)

b=Entry(aken,font='Calibri 26', fg='green', bg='lightblue', width=3)
b.pack(side=LEFT)

x3=Label(aken,text='x+', font='Calibry 26', fg='green')
x3.pack(side=LEFT)

c=Entry(aken,font='Calibri 26', fg='green', bg='lightblue', width=3)
c.pack(side=LEFT)

x4=Label(aken,text='=0', font='Calibry 26', fg='green')
x4.pack(side=LEFT)

btn=Button(aken,text='resit', font='Calibri 26', bg='green', command=lahenda)
btn.pack(side=LEFT)
vastus=lahenda



def lahenda():
    if (a.get()!=''and b.get()!='' and c.get()!=''):
        a_int(a.get())
        b_int(a.get())
        c_int(a.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_sqrt(D))/(2*a_),2)
            x2_=round((-1*b_sqrt(D))/(2*a_),2)
            t=f'X1={x1_}, \nX2={x2_}'
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
        t=f'X1={x1_}'
    else:
        t=('Корней нет')
    vastus.configure(text=f'D={D}\n{t}')
    a.configure(bg='lightblue')
    b.configure(bg='lightblue')
    c.configure(bg='lightblue')
    

aken.mainloop()