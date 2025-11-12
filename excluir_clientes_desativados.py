import os
import datetime as dt
from time import sleep as sp 

"""
1.DEFINIR PASTA ONDE ELE VAI TRABALHAR - OK
2.FAZER A BUSCA E FILTRO DAS PASTAS QUE CONTENHAM "EXCLUIR_" NO NOME
3.ADICIONAR NUMA LISTA ESSES NOMES DE PASTAS
5.ADICIONAR NUM ARQUIVO DE LOG PARA ARMAZENAR OS NOMES DOS ITENS EXCLUIDOS

4.REMOVER OS ITENS
6.REMOVER DO SITES-ENABLE E DAR UM REFRESH NO APACHE2
"""

"""DECLARAÇÃO DAS VARIAVEIS
---PASTA DE TRABALHO DO SCRIPT:
"""
pasta_clientes = '/var/www/'

"""LISTA DOS ITENS PARA EXCLUIR"""
filtrados_excluir = []

"""ARQUIVO DE LOG:"""
arquivo_log = '/var/log/clientes_excluidos.txt'
with open(arquivo_log, 'a') as log:
    log.write('Data:')

"""CONFIGURANDO A DATA"""
data_atual = dt.datetime.now()
date = data_atual.strftime("%Y-%m-%d")
    
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
                """ultimo_item = filtrados_excluir[-1]"""
                print(f'{date} - {filtrados_excluir[-1]} foi excluido.')
                """print(f'{date} - {ultimo_item} foi excluido.')"""
                """log.write(f'{date} - {ultimo_item} foi excluido.')"""
    except FileNotFoundError:
        print(f'Erro: o diretório não foi encontrado')
limpar_clientes_antigos()