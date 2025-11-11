import pandas as pd
import os
from pathlib import Path
from time import sleep

# --- Configurações ---
PASTA_IMAGENS = Path('./imageUpload/') 
PASTA_DESTINO = './pasta-teste/'
ARQUIVO_CSV = 'cf_imagem.csv'

'''Definindo a planilha'''
df = pd.read_csv(ARQUIVO_CSV)

'''Indicar planilha'''
try:
    if not df.empty:
        print('Planilha importada.')
        sleep(10)
    else:
        print('Planilha importada, mas está vazia.')
        sleep(10)
except FileNotFoundError:
    print(f'ERRO: O arquivo {df} não foi encontrado.')
    sleep(10)
except Exception as e:
    print(f'Ocorreu um erro inesperado ao importar {e}.')
    sleep(10)
'''Busca pela coluna que eu quero'''
coluna_1 = df.iloc[:, 0]

'''Mudando para a pasta das imagens'''
os.chdir(PASTA_IMAGENS)

'''Função de apagar as imagens'''
def apagar_imagens():
    try: 
        for i in coluna_1:
            if not os.path.isfile(i):
                print('Arquivo não existe')
            else:
                os.remove(i)
                print(f'Arquivo {i} deletado com sucesso.')
    except Exception as e:
        print(f'Ocorreu um erro {e}')
apagar_imagens()