import os
import datetime as dt
from time import sleep as sp 
import shutil


# 6. REMOVER DO SITES-ENABLE E DAR UM REFRESH NO APACHE2

# DECLARAÇÃO DAS VARIAVEIS
# --- PASTA DE TRABALHO DO SCRIPT:
pasta_clientes = '/var/www/'

# LISTA DOS ITENS PARA EXCLUIR
filtrados_excluir = []

# CONFIGURANDO A DATA
data_atual = dt.datetime.now()
data = data_atual.strftime("%Y-%m-%d")

def limpar_clientes_antigos():
    try:
        itens = os.listdir(pasta_clientes)
        print('-' * 50)
        print('Buscando itens na pasta de clientes...')
        print('-' * 50)
        for i in itens:
            if i.startswith('EXCLUIR_'):
                filtrados_excluir.append(i)
                ultimo_item = filtrados_excluir[-1]
                print(ultimo_item)
                # ARQUIVO DE LOG (Comentado):
                arquivo_log = "/var/log/clientes_excluidos.txt"
                with open(arquivo_log , 'a') as log:
                    log.write(f'{data} teste log.\n')
                # shutil.rmtree(ultimo_item)
                # print(f'{ultimo_item} foi removido')

    except FileNotFoundError:
        print('Erro: o diretório não foi encontrado')
        
limpar_clientes_antigos()