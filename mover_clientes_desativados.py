import os
import datetime as dt
import shutil

# DECLARAÇÃO DAS VARIAVEIS
# --- PASTA DE TRABALHO DO SCRIPT:
pasta_clientes = '/var/www'
pasta_excluir = '/var/www/excluir/'

# CRIAR PASTA SE NÃO EXISTIR
os.makedirs(pasta_excluir, exist_ok=True)

# CONFIGURANDO A DATA
data_atual = dt.datetime.now()
data = data_atual.strftime("%Y-%m-%d")

# ARQUIVO DE LOG (Comentado):
arquivo_log = '/var/www/excluir/clientes_movidos.txt'

# LISTA DOS ITENS PARA EXCLUIRk
filtrados_excluir = []

def limpar_clientes_antigos():
    try:
        itens = os.listdir(pasta_clientes)
        print('-' * 50)
        print('Buscando itens na pasta de clientes...')
        print('-' * 50)
        for i in itens:
            if i.startswith('EXCLUIR_'):
                filtrados_excluir.append(i)
                ultimo_item = filtrados_excluir[-1]+'/'
                print(ultimo_item)
                path_completo = pasta_clientes+ultimo_item
                print(path_completo)
                shutil.move(path_completo, pasta_excluir)
                print(ultimo_item + ' foi movido para: '+pasta_excluir)
                #GERENCIAMENTO DO LOG
                logar = data + ultimo_item + 'foi movido.'
                with open(arquivo_log , 'a') as log:
                    log.write(logar)
    except FileNotFoundError:
        print('Erro: o diretório não foi encontrado')
limpar_clientes_antigos()