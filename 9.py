import random
from tkinter import*
def oval():  
    a=random.randint(20,40)
    x=random.randint(a,300-a)
    y=random.randint(a,300-a)
    canvas.create_oval(x-a,y-a,x+a,y+a,fill='red')

def tri():
    x1=random.randint(0,300)
    x2=random.randint(0,300)
    x3=random.randint(0,300)
    y1=random.randint(0,300)
    y2=random.randint(0,300)
    y3=random.randint(0,300)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill='red')

def sq():
    a=random.randint(20,40)
    x=random.randint(a,300-a)
    y=random.randint(a,300-a)  #'oval','triangle','square'
    canvas.create_rectangle(x-a,y-a,x+a,y+a,fill='red')

def New_geometry():
    f=random.choice(['oval','triangle','square'])
    canvas.create_rectangle(0,0,300,300,fill='black')
    if f=='oval':
         oval()
    elif f=='triangle':
        tri()
    else:sq()

root=Tk()
root.geometry('400x400')
canvas=Canvas(bg='black',height=300,width=300)
canvas.pack()
but=Button(height=2,width=20,bg='grey',command=New_geometry)
but.pack()
root.mainloop()