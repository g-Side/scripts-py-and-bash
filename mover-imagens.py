import pandas as pd
import os
from pathlib import Path
from time import sleep

'''Caminho para buscar a planilha'''
planilha = "/var/www/negreiros/imageUpload-bkp/scripts-py-and-bash/mover-imagens.py"
cliente_midia = Path('/var/www/negreiros/imageUpload-bkp/')

'''Verificar se a pasta existe'''
if not cliente_midia.is_dir():
    print('Cliente não encontrado.')
    exit
else:
    print('Cliente selecionado.')
    os.system('mkdir imagens-movidas')

'''Importar a planilha pro programa'''
data = pd.read_csv(planilha)
if not data.empty:
    print('Importando dados para a remoção.')
'''Busca pela coluna que eu quero'''
imagens = data['imagens_del']
print('Dados selecionados.')
'''Função de apagar as imagens'''
def apagar_imagens():
    try: 
        for i in imagens:
            os.system('mv {} imagens-movidas/'.format(i))
            print('o item {} movido'.format(i))
    except:
        print('Erro ao executar script.')
apagar_imagens()
