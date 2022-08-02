# Importar as bibliotecas
from  tkinter import *
from tkinter import messagebox
import tkinter
from turtle import left, right
from tkinter import ttk 

# Criar janela
janela = Tk()
janela.title("System_Elegance - Acess Panel") # Título da tela
janela.geometry("600x300") # Tamanho da tela
janela.configure(background="white") # cor da tela
janela.resizable(width= False, height=False) # Configurar para que não seja possivel deixar ela maximizada ou mudar de tamanho com ela


# carregando imagens
logo = PhotoImage(file="icons/logo.png")
# Widgets

# criar widget da esquerda
LeftFrame = Frame(janela, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise") # widget da esquerda
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela, width=399, height=300, bg="MIDNIGHTBLUE", relief="raise") # widget da direito
RightFrame.pack(side=RIGHT)



LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE") #posição do logo
LogoLabel.place(x=50, y=125)

 # Nome do usuario
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White") # Titulo
UserLabel.place(x=5, y=100) # Local to titulo

# Caixa para digitar o nome
UserEntry = ttk.Entry(RightFrame, width=30) # Caixa para colocar o nome
UserEntry.place(x=150, y=110) # local
 
# caixa para digitar a senha
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White") # Titulo
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30) # Caixa para colocar o nome
PassEntry.place(x=150, y=160) # local

# Botões

# Botão de logar

LoginButton = ttk.Button(RightFrame, text="Login", width=30) # Botão de logar
LoginButton.place(x=125, y=200) # local do botão

# Botão de cadastrar
RegisterButton = ttk.Button(RightFrame, text="Cadastrar", width=20) # Botão de logar
RegisterButton.place(x=150, y=233) # local do botão





janela.mainloop()
