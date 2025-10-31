import pandas as pd
import os
from pathlib import Path
import itertools
from time import sleep

'''Caminho para buscar a planilha'''
path_planilha = Path('/usr/share/limpar_arquivos')

'''Filtro dos arquivos que eu quero'''
padrao_csv = '**/*.csv'
padrao_xlsx = '**/*.xlsx'

'''Busca recursiva dos arquivos de planilha'''
arquivo_csv = path_planilha.glob(padrao_csv)
arquivo_xlsx = path_planilha.glob(padrao_xlsx)

'''
---TAREFAS PARA O SCRIPT---
4. Adicionar log também para validação posterior e reter histórico.
'''

'''Perguntar ao usuário o nome do cliente'''
cliente = str(input('Qual o nome do cliente?: '))

cliente_midia = Path(f'/var/www/{cliente}/imageUpload/')

'''Verificar se a pasta existe'''
if cliente_midia.is_dir():
    print(f'Cliente {cliente} selecionado.')
    sleep(3) 
    os.system(f'cd {cliente_midia}')
else:
    print(f'Cliente {cliente} não encontrado.')

'''Match dos arquivos
melhorar a forma de encontrar a planilha, ver de passar o caminho da planilha 
ou alguma outra forma
'''
planilha_filtrada = itertools.chain(arquivo_csv, arquivo_xlsx)

'''Valida se a planilha foi encontrada'''
if planilha_filtrada:
    print(f'Arquivo encontrado.')
    sleep(3)
else:
    print(f'Planilha não encontrada em: {path_planilha}')

'''Importar a planilha pro programa'''
data = pd.read_csv(planilha_filtrada)

'''Busca pela coluna que eu quero'''
imagens = data['imagens_del']

'''Função de apagar as imagens'''
def apagar_imagens():
    try: 
        for i in imagens:
            os.system(f'mv {cliente_midia}{i} pasta-teste/')
            print(f'o item {i} movido')
    except:
        print('Erro ao executar script.')
apagar_imagens()