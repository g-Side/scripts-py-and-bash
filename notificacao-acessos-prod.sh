#!/bin/bash

###DECLARACAO DAS VARIAVEIS
#LINK DO DISCORD 
WEBHOOK_URL="https://discordapp.com/api/webhooks/1442874750811766804/7CY6soEMp_fTX0JMIa1UWpMcP0aOilb3LeMSBZI28NGKKLicB5xmeXujvZzu8ozmlgKm"

### FUNCAO PARA PEGAR O RESULTADO DAS CONTAGENS DE ACESSOS
REQ=$(netstat -tulnp | grep "80" | wc -l)
MSG=$(echo "Quantidade de requisicoes agora: $REQ")

### FUNCAO PARA ENVIAR A MENSAGEM AO DISCORD
NOTIFICA_DISCORD() {
  curl -H "Content-Type: application/json" \
       -X POST \
       -d "{\"content\": \"$MSG\"}" \
       $WEBHOOK_URL
       }

NOTIFICA_DISCORD