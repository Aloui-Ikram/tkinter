from tkinter import *
fentre=Tk()
def ditBonjour():
    Text.place(x=20,y=20)
fentre.title("ikram")
fentre.config(width=300,height=200 , bg="yellow")
Text = Label(fentre,text="hello !")
Text.place(x=10,y=10)
Text.config(font=('times',20,'bold '))
Text.config(text="bas")
Button1=Button(fentre,text="clique", command=ditBonjour)
Button1.place(x=0,y=0)
Button1.configure(text="khtk")
fentre.mainloop()