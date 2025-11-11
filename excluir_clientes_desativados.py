import os
from time import sleep as sp

"""
1.DEFINIR PASTA ONDE ELE VAI TRABALHAR - OK

2.FAZER A BUSCA E FILTRO DAS PASTAS QUE CONTENHAM "EXCLUIR_" NO NOME
3.ADICIONAR NUMA LISTA ESSES NOMES DE PASTAS
4.REMOVER OS ITENS
5.ADICIONAR NUM ARQUIVO DE LOG PARA ARMAZENAR OS NOMES DOS ITENS EXCLUIDOS
6.REMOVER DO SITES-ENABLE E DAR UM REFRESH NO APACHE2
"""
"""DECLARAÇÃO DAS VARIAVEIS"""
pasta_clientes = '/var/www/'
filtrados_excluir = []

def limpar_clientes_antigos():
    try:
        itens = os.listdir(pasta_clientes)
    except FileNotFoundError:
        print(f'Erro: o diretório não foi encontrado')
    print('-' * 30)
    print(f'BUscando itens na pasta {pasta_clientes}...')
    print('-' * 30)
    sp(15)

    for cliente in itens:
        if cliente.startswith('EXCLUIR_'):
            filtrados_excluir.append(cliente)
            print(f'- {filtrados_excluir}')
limpar_clientes_antigos()

