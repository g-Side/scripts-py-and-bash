#!/bin/bash

###DECLARAÇÃO DAS VARIAVEIS
#LINK DO DISCORD 
WEBHOOK_URL="https://discord.com/api/webhooks/1407444877905494177/Qm3JIvdeZGLKjZbolLd1vP8wzRU6KX0kroeC5axqmZ9tVO0ExhPNAn9ExqL5H_JuyS-s"
#PASTA PARA REMOVER
CLIENTES_EXCLUIR=$(ls -la /var/www | grep "EXCLUIR*")
#FORMATANDO DATA
DATE=$(date +'%Y/%m/%d-%H:%M')
#DEFININDO ARQUIVO DE LOG E CRIANDO. CASO JÁ EXISTA NÃO FAZ NADA
ARQUIVO_LOG="/var/log/clientes_excluidos_pro.txt"
touch "$ARQUIVO_LOG" 2>/dev/null

### FUNÇÃO PARA ENVIAR A MENSAGEM AO DISCORD
NOTIFICA_DISCORD() {
  curl -H "Content-Type: application/json" \
       -X POST \
       -d "{\"content\": \"$MSG\"}" \
       $WEBHOOK_URL
       }
### FUNÇÃO PARA REGISTRAR EXCLUSÕES
LOG_APLICACAO() {
    echo "EM $DATE o $cliente foi removido." >> $ARQUIVO_LOG
    }

for cliente in CLIENTES_EXCLUIR ; do
    if [[ "$cliente" == "EXCLUIR"* ]]; then
        echo "Encontrado o cliente $cliente para excluir"
        #########COMENTADO PARA TESTE
        ##rm -Rf $cliente
        LOG_APLICACAO
        MSG=":rotating_light: $cliente foi removido do servidor PRO automaticamente em: $DATE"
        NOTIFICA_DISCORD
    fi
done
