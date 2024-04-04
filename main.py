import customtkinter
from tkinter import messagebox
from customtkinter import *
import random


root = customtkinter.CTk()
root.title("Gerador de Senhas")
root.geometry("400x400")
root.maxsize(400, 400)
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
        senha_criada.configure(text=(letra_maiuscula+numeros1+letra_minuscula+car_especial))

    elif var1 == '5':
        senha_criada.configure(text=(letra_maiuscula+letra_minuscula+numeros1+car_especial+numeros2))

    elif var1 == '6':
        senha_criada.configure(text=(letra_maiuscula+numeros1+car_especial+numeros3+numeros5+letra_minuscula))

    elif var1 == '7':
        senha_criada.configure(text=(letra_maiuscula+numeros1+numeros2+letra_minuscula+numeros3+numeros5+car_especial))

    elif var1 == '8':
        senha_criada.configure(text=(letra_maiuscula+numeros1+numeros2+letra_minuscula+numeros4+car_especial+numeros3+letra_minuscula))
    
    return aviso.configure(text=(''))

def copiar(): 
    if senha_criada.cget("text") == "":
       return aviso.configure(text=('Nada Copiado'))
    else:
        root.clipboard_clear()
        root.clipboard_append(senha_criada.cget("text"))
        root.update()           
        return aviso.configure(text=('Copiado'))
        
opcoes = ["4", "5", "6", "7", "8"]

var = customtkinter.StringVar(root)
var.set(opcoes[0]) 

menu = customtkinter.CTkOptionMenu(root, variable=var, values=opcoes)
menu.place(x=240, y=70)


ola = customtkinter.CTkLabel(root, text="Gerador de Senhas")
ola.place(relx=0.5, y=30, anchor="center")

quantidade = customtkinter.CTkLabel(root, text="Escolha o tamanho da sua senha:")
quantidade.place(x=20, y=70)

criar = customtkinter.CTkButton(root, text="Gerar", command=senha)
criar.place(relx=0.5, y=150, anchor="center")

senha_criada = customtkinter.CTkLabel(root, text="")
senha_criada.place(relx=0.5, y=215, anchor="center")

copiar = customtkinter.CTkButton(root, text="Copiar", command=copiar)
copiar.place(relx=0.5, y=285, anchor="center")

aviso = customtkinter.CTkLabel(root, text="")
aviso.place(relx=0.5, y=350, anchor="center")

root.mainloop()