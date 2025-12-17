import pandas as pd
import shutil, os
from pathlib import Path
from time import sleep

'''Caminho para buscar a planilha'''
planilha = "/home/jean.alencar/scripts-py-and-bash/naousadas-bengala.csv"
cliente_midia = Path('/var/www/bengala/imageUpload/')
imagens_movidas = Path('/home/jean.alencar/scripts-py-and-bash/imagens-movidas/')

'''Verificar se a pasta existe'''
if not cliente_midia.is_dir():
    print('Cliente não encontrado.')
    exit()
else:
    print('Pasta de backup selecionada.')
    if not imagens_movidas.is_dir():
        os.system(f'mkdir {imagens_movidas}')

print('Pasta de destino encontrada.')
'''Importar a planilha pro programa'''
data = pd.read_csv(planilha)
print('Planilha encontrada.')
imagens = data['imagens_del']
print('Dados carregados.')
'''Função de apagar as imagens'''
def apagar_imagens():
    try: 
        for i in imagens:
            arquivo_origem = f'{cliente_midia}/{i}'
            arquivo_path = Path(arquivo_origem)
            if not arquivo_path.is_file():
                print(f'Arquivo {i} não existe na pasta.')
                continue
            shutil.move(arquivo_origem, imagens_movidas)
            print(f'Movido de: {arquivo_origem} para: {imagens_movidas}.')
    except FileNotFoundError:
        print('Arquivo não encontrado.')
    except PermissionError:
        print('Erro de execução por falta de permissão. Você é root?')
'''    except:
        print('Erro genérico. Por favor, contate o desenvolvedor do script.')'''
apagar_imagens()
