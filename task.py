from tkinter import *
from turtle import bgcolor

fenetre = Tk();
fenetre.title("Attention DANGER!");
fenetre.configure(width=500, height=160, bg="#663333")

i = 0

def boom():
    global i
    if i % 2 == 0:
        Texte1.configure(text="BOOM !!", fg='black', font=('times', 72, 'bold'))
        Texte1.place(x=40, y=20)

        Bouton.configure(text="Désamorcer", fg='green', bg='lightgreen', font=('times', 12, 'bold'), command=boom)
        Bouton.place(x=400, y=120)

    else:
        Texte1.configure(bg="#663333",  text="Ne surtout pas appuyer sur le button ...", fg='red', font=('times', 22, 'bold'))
        Texte1.place(x=0, y=0)
        
        Bouton.configure(text='Bouton',  fg='black', bg='#EE2222', font=('times', 16, 'bold'), command=boom)
        Bouton.place(x=200, y=40)
    
    i = (i+1) % 2

Texte1 = Label(fenetre, bg="#663333", text="Ne surtout pas appuyer sur le button ...", fg='red', font=('times', 22, 'bold'))
Texte1.place(x=0, y=0)

Bouton = Button(fenetre, text='Bouton', fg='black', bg='#EE2222', font=('times', 16, 'bold'), command=boom)
Bouton.place(x=200, y=40)

fenetre.mainloop();