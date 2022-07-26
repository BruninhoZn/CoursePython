from copy import copy
import pyautogui
import pyperclip
import pandas as pd 
import time


pyautogui.PAUSE = 3

# Passo 1 entrar no sistema
pyautogui.hotkey("ctrl", "t")
time.sleep(0.5)
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing\n')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")

# Site ta carregando
time.sleep(2)

# Passo 2: Navegar no sistema e encontrar a base de dados
pyautogui.click(x=373, y=307, clicks=2)
time.sleep(2)

# Passo 3: Download da base de dados
pyautogui.click(x=442,  y=370, clicks = 1) # clicou no arquivo
pyautogui.click(x=1717, y=181, clicks = 1)# clicou nos 3 pontos
pyautogui.click(x=1434, y=590, clicks = 1)# fez o donwload
time.sleep(2)

# Passo 4: Calcular os indicadores

tabela = pd.read_excel(r"C:\Users\Regina\Desktop\Downloads\Vendas - Dez.xlsx")
print(tabela)
quantidade = tabela["Quantidade"].sum()
fatoramento = tabela["Valor Final"].sum()





# Passo 5 entrar no email
pyautogui.hotkey("ctrl", "t") # Abrir uma nova aba
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox") # copiar esse link
pyautogui.hotkey("ctrl", "v") # colar na aba
pyautogui.press("enter") # pressionar enter
print(2)

# manda um email para diretoria

# clicar no botão +
pyautogui.click(x=87, y=195, clicks=1)
print(0.5)
pyautogui.click(x=1289, y=498, clicks=1)

# escrever email do destinatario

pyautogui.write("bruno.japones123@gmail.com") # escrever o email do destinatario
pyautogui.press("tab") # selecionar a pessoal   
pyautogui.press("tab") # passar para o campo de assunto

# escrever o assunto

pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab") # passar para o corpo do email

# escrever o corpo do email
texto = f"""Olá, Bom dia
O faturamento de ontem foi de: R$ {fatoramento}
A quantidade de produtos foi de: R${quantidade}
            
            Abraços Bruninho"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# Enviar o email
pyautogui.hotkey("ctrl", "enter")

