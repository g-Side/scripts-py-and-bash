import os
import datetime as dt
import shutil

# DECLARAÇÃO DAS VARIAVEIS
# --- PASTA DE TRABALHO DO SCRIPT:
pasta_clientes = '/var/www/'

# ARQUIVO DE LOG (Comentado):
arquivo_log = '/var/log/clientes_excluidos.txt'

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
                with open('arquivo_log' , 'a') as log:
                    log.write("data teste log.")
                # shutil.rmtree(ultimo_item)
                # print(f'{ultimo_item} foi removido')

    except FileNotFoundError:
        print('Erro: o diretório não foi encontrado')
        
limpar_clientes_antigos()