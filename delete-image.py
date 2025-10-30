import pandas as pd
import os
from pathlib import Path
import itertools
from time import sleep
import logging # Importar o módulo de log

# --- 1. CONFIGURAÇÃO DO LOG ---
# Define como e onde as mensagens de log serão salvas.
LOG_FILE = 'limpeza_arquivos.log'
logging.basicConfig(
    level=logging.INFO,                                   # Capturar mensagens INFO e acima
    format='%(asctime)s - %(levelname)s - %(message)s',    # Formato do log
    filename=LOG_FILE,                                    # Nome do arquivo de log
    filemode='a'                                          # 'a' para adicionar ao log existente
)
logger = logging.getLogger(__name__)
logger.info("--- SCRIPT INICIADO ---")
# -----------------------------


'''Caminho para buscar a planilha'''
path_planilha = Path('/usr/share/limpar_arquivos')
logger.info(f"Diretório de busca da planilha: {path_planilha}")

'''Filtro dos arquivos que eu quero'''
padrao_csv = '**/*.csv'
padrao_xlsx = '**/*.xlsx'

'''Busca recursiva dos arquivos de planilha'''
# O glob retorna um gerador (lazy), o que é bom.
arquivo_csv = path_planilha.glob(padrao_csv)
arquivo_xlsx = path_planilha.glob(padrao_xlsx)

'''Perguntar ao usuário o nome do cliente'''
cliente = str(input('Qual o nome do cliente?: '))
logger.info(f"Nome do cliente inserido: {cliente}")

cliente_midia = Path(f'/var/www/{cliente}/imageUpload/')
PASTA_DESTINO = cliente_midia.parent / 'pasta-teste' # Define a pasta de destino fora da pasta de upload

'''Verificar se a pasta do cliente existe'''
if cliente_midia.is_dir():
    print(f'Cliente {cliente} selecionado.')
    logger.info(f'Diretório de mídia do cliente encontrado: {cliente_midia}')
    sleep(1) 
    
    # Verifica e cria a pasta de destino
    if not PASTA_DESTINO.is_dir():
        PASTA_DESTINO.mkdir(exist_ok=True)
        logger.info(f"Pasta de destino criada: {PASTA_DESTINO}")
    
else:
    print(f'Cliente {cliente} não encontrado em: {cliente_midia}')
    logger.error(f'Cliente {cliente} NÃO ENCONTRADO. Encerrando o script.')
    # Não faz sentido continuar se o diretório principal não existe
    exit(1)


'''Match dos arquivos'''
planilha_filtrada_gen = itertools.chain(arquivo_csv, arquivo_xlsx)
# Tenta pegar o primeiro arquivo do iterador
try:
    planilha_caminho = next(planilha_filtrada_gen)
except StopIteration:
    planilha_caminho = None

'''Valida se a planilha foi encontrada'''
if planilha_caminho:
    print(f'Arquivo encontrado: {planilha_caminho.name}')
    logger.info(f'Planilha encontrada: {planilha_caminho}')
    sleep(1)
else:
    print(f'Planilha não encontrada em: {path_planilha}')
    logger.error(f'Nenhuma planilha CSV/XLSX encontrada em: {path_planilha}. Encerrando o script.')
    exit(1) # Sai se não encontrar a planilha

'''Importar a planilha pro programa'''
try:
    if planilha_caminho.suffix == '.csv':
        data = pd.read_csv(planilha_caminho)
    elif planilha_caminho.suffix in ['.xlsx', '.xls']:
        data = pd.read_excel(planilha_caminho)
    else:
        # Caso improvável, mas é bom tratar
        raise ValueError("Formato de arquivo não suportado após a busca.")
        
    logger.info(f"Planilha '{planilha_caminho.name}' importada com sucesso.")

except Exception as e:
    logger.critical(f"Erro ao importar a planilha: {planilha_caminho}. Detalhes: {e}", exc_info=True)
    exit(1)


'''Busca pela coluna que eu quero'''
COLUNA_IMAGENS = 'imagens_del'
if COLUNA_IMAGENS in data.columns:
    imagens = data[COLUNA_IMAGENS].dropna() # Remove valores NaN para evitar erros
    logger.info(f"Colunas de imagem ({COLUNA_IMAGENS}) carregadas: {len(imagens)} itens.")
else:
    logger.error(f"Coluna '{COLUNA_IMAGENS}' não encontrada na planilha. Encerrando o script.")
    exit(1)


'''Função de apagar as imagens'''
def apagar_imagens():
    logger.info("Iniciando a movimentação das imagens.")
    contador_movidos = 0
    contador_nao_encontrados = 0
    
    for nome_imagem in imagens:
        # Cria o caminho completo da imagem original usando Path
        caminho_original = cliente_midia / nome_imagem
        caminho_destino = PASTA_DESTINO / nome_imagem
        
        if caminho_original.is_file():
            try: 
                # Melhor usar Path.rename() ou shutil.move() do que os.system() para mover
                # No seu caso, Path.rename() move ou renomeia o arquivo.
                caminho_original.rename(caminho_destino)
                print(f'Item {nome_imagem} movido com sucesso.')
                logger.info(f'MOVENDO: {nome_imagem} -> {caminho_destino}')
                contador_movidos += 1
            except Exception as e:
                print(f'Erro ao mover o item {nome_imagem}.')
                logger.error(f'ERRO ao mover {nome_imagem}. Detalhes: {e}', exc_info=False)
        else:
            # Imagem não encontrada no disco
            print(f'AVISO: Imagem {nome_imagem} não encontrada no disco.')
            logger.warning(f'NÃO ENCONTRADO: Imagem {nome_imagem} não existe em {cliente_midia}.')
            contador_nao_encontrados += 1

    logger.info(f"--- FIM DA MOVIMENTAÇÃO ---")
    logger.info(f"Total de arquivos movidos: {contador_movidos}")
    logger.info(f"Total de arquivos não encontrados: {contador_nao_encontrados}")

# Execução da função
apagar_imagens()
logger.info("Script finalizado com sucesso.")