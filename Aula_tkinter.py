from tkinter import *
from tkinter import messagebox



def impDados():
   # print("Imprime no terminal Nome: %s" % vnome.get())
    messagebox.showinfo(title="Exemplo",message=vnome.get())


app=Tk()

app.title("Curso")
app.geometry("500x300")
app.configure(background="#008")

txt1=Label(app,text="Curso Python",background="#008",foreground="#fff")
txt1.place(x=10,y=10,width=100,height=20)

vnome=Entry(app)
vnome.place(x=10,y=80,width=200,height=20)

btn=Button(app,text="Imprimir",command=impDados).place(x=10,y=200,width=100,height=20)




app.mainloop()