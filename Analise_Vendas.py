#Bibliotecas usadas: pandas, openpyxl, twilio

# Verificar se algum valor na coluna Vendas é maior que $55,000, meta da empresa
# Se for maior que $55.00 enviar um sms com o nome, mês en vendas do vendedor

##Envio de mensagens pelo Twilio, é preciso criar uma conta antes
#account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#auth_token  = "your_auth_token"
#client = Client(account_sid, auth_token)
#message = client.messages.create(
    #to="+15558675309",
    #from_="+15017250604",
    #body="Hello from Python!")
#print(message.sid)


import pandas as pd
import openpyxl
from twilio.rest import Client

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']


for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel (f'{mes}.xlsx')
    print (tabela_vendas)
    if (tabela_vendas ["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas ['Vendas'] > 55000, "Vendas"].values[0]
        print(f'No mês {mes} a meta foi batida. Vendedor: {vendedor}, Vendas:{vendas}')
        message = client.messages.create(
            to="+15558675309",
            from_="+15017250604",
            body=f'Non mês{mes} a meta foi batida. Vendedor: {vendedor}, Vendas:{Vendas}')
        print(message.id)




