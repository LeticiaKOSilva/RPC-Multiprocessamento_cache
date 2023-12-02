#!/bin/bash

# Verifique se o nome do arquivo é fornecido como argumento
if [ "$#" -ne 1 ]; then
    echo "Uso: $0 <arquivo_de_log>"
    exit 1
fi

# Extrai IPs únicos do arquivo de log
ips=$(awk '{print $4}' "$1" | sort -u)

# Exibe os IPs únicos sem vírgula no final e sem parênteses no início
echo "IPs únicos que fizeram requisições:"
echo "$ips" | sed 's/,$//' | sed 's/^[()]//'
