from tkinter import*

def click():
    name=En.get()
    l1.configure(text=f'Приветствую тебя,{name}, очень рад знакомству!')
    
root=Tk()
root.geometry('400x400')
root.title('Задание 10')
En=Entry(bg='white',font='colsolas',width=10)
l1=Label(bg='White',width=60)
button=Button(text='Приветствие',bg='grey',command=click)
l1.place(relx=0,rely=0)
En.place(relx=0.4,rely=0.2)
button.place(relx=0.4,rely=0.5)
root.mainloop()
