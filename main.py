import tkinter as Tk
from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Gerador De Senhas")
root.geometry("400x400")
root.maxsize(400 , 400)
root.minsize(400, 400)
root.configure(background="black")
root.iconbitmap("key.ico")

def senha():
    var1 = var.get()
    
    letra_maiuscula = chr(random.randint(65,90))

    letra_minuscula = chr(random.randint(97,122))

    car_especial =  chr(random.randint(35,38))

    numeros1 = chr(random.randint(48,52))
    
    numeros2 = chr(random.randint(48,52))
    
    numeros3= chr(random.randint(48,52))
    
    numeros4 = chr(random.randint(48,52))
    
    numeros5 = chr(random.randint(48,52))
    
    if var1 == '4':
        senha_criada.configure(text=(letra_maiuscula, numeros1, letra_minuscula, car_especial))

    elif var1 == '5':
        senha_criada.configure(text=(letra_maiuscula, letra_minuscula, numeros1, car_especial, numeros2))

    elif var1 == '6':
        senha_criada.configure(text=(letra_maiuscula, numeros1, car_especial, numeros3, numeros5, letra_minuscula))

    elif var1 == '7':
        senha_criada.configure(text=(letra_maiuscula, numeros1, numeros2, letra_minuscula, numeros3, numeros5, car_especial))

    elif var1 == '8':
        senha_criada.configure(text=(letra_maiuscula, numeros1, numeros2, letra_minuscula, numeros4, car_especial, numeros3, letra_minuscula))

def copiar(): 
    if senha_criada["text"] == "":
        messagebox.showinfo("Aviso:", "Nada copiado")
    else:
        root.clipboard_clear()
        root.clipboard_append(senha_criada["text"])
        root.update()           
        messagebox.showinfo("Aviso:", "Copiado")

opcoes = "4", "5", "6", "7", "8"

var = StringVar(root)
var.set(opcoes[0]) 

menu = OptionMenu(root, var, *opcoes)
menu.place(x=320, y=80)

ola = Label(text="Gerador de Senhas", bg="black", fg="white", font="Gabriola 20")
ola.place(x=120, y=10)

quantidade = Label(text="Escolha o tamnho da sua senha:", bg="black", fg="white", font="Gabriola 20")
quantidade.place(x=20, y=70)

criar = Button(text="Gerar", bg="black", fg="white", font="arial 13 ", command=senha, height=1)
criar.place(x= 179, y=150)

senha_criada = Label(bg="black", fg="white", font="arial 15")
senha_criada.place(relx=0.5, y=230, anchor="center")

copiar = Button(text="Copiar", bg="black", fg="white", font="arial 13 ", command=copiar, height=1)
copiar.place(x= 175, y=285)


root.mainloop()