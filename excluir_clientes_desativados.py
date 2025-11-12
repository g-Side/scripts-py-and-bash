import os
import datetime as dt
from time import sleep as sp 

"""
6.REMOVER DO SITES-ENABLE E DAR UM REFRESH NO APACHE2
"""

"""DECLARAÇÃO DAS VARIAVEIS
---PASTA DE TRABALHO DO SCRIPT:
"""
pasta_clientes = '/var/www/'

"""LISTA DOS ITENS PARA EXCLUIR"""
filtrados_excluir = []

"""CONFIGURANDO A DATA"""
data_atual = dt.datetime.now()
data = data_atual.strftime("%Y-%m-%d")

"""ARQUIVO DE LOG:
arquivo_log = '/var/log/clientes_excluidos.txt'
with open(arquivo_log , 'a') as log:
    log.write(f'Data: {data}')
"""

def limpar_clientes_antigos():
    try:
        itens = os.listdir(pasta_clientes)
        print('-' * 30)
        print('Buscando itens na pasta de clientes...')
        print('-' * 30)
        sp(5)
        for i in itens:
            if i.startswith('EXCLUIR_'):
                filtrados_excluir.append(i)
                #ultimo_item = filtrados_excluir[-1]
                print(f'{data} - {filtrados_excluir[-1]} foi excluido.')
                #print(f'{data} - {ultimo_item} foi excluido.')"""
                #log.write(f'{data} - {ultimo_item} foi excluido.')"""
    except FileNotFoundError:
        print(f'Erro: o diretório não foi encontrado')
limpar_clientes_antigos()