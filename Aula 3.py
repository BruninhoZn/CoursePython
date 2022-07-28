from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Passo 1: Pegar cotação do dólar
#   abrir o navegador
navegador = webdriver.Chrome()

#   entrar no google
navegador.get('http://www.google.com.br')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# pegar cotação

dolar = navegador.find_element('xpath','/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(dolar)




# Passo 2: Pegar cotação do euro

#   entrar no google

navegador.get('http://www.google.com.br')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# pegar cotação

euro = navegador.find_element('xpath','/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(euro)


# Passo 3: Pegar cotação do ouro

navegador.get('https://www.melhorcambio.com/ouro-hoje')
ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
ouro = ouro.replace(",", ".")
print(ouro)

navegador.quit()

# Passo 4: Atualizar a base de dados

tabela = pd.read_excel(r'C:\Python Scripts\Python\Curso do Lira de automoção etc\Aula 3\Produtos.xlsx')

# Passo 5: Recalcular os preços

# Atualizar as cotações

tabela["Moeda"]=="Dólar"

tabela.loc[tabela["Moeda"]=="Dólar", "Cotação"] = float(dolar)

tabela.loc[tabela["Moeda"]=="Euro", "Cotação"] = float(euro)

tabela.loc[tabela["Moeda"]=="Ouro", "Cotação"] = float(ouro)
# Preço de compra = Preço original * Cotação

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

# Preço de venda = Preço de compra * Margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

print(tabela)

# Passo 6: Exportar a base de dados
tabela.to_excel("Produtos Novo.xlsx", index="false")
