import os
import re

# Define o nome dos arquivos
nome_arquivo_origem = "frase.txt"
nome_arquivo_destino = "palavras.txt"

# Lê o conteúdo do arquivo original
with open(nome_arquivo_origem, "r") as arquivo_origem:
    conteudo = arquivo_origem.read()

# Remove caracteres não alfabéticos e separa as palavras
palavras = re.findall(r'\b\w+\b', conteudo)

# Salva as palavras no novo arquivo, uma por linha
with open(nome_arquivo_destino, "w") as arquivo_destino:
    for palavra in palavras:
        arquivo_destino.write(palavra + "\n")

# Lê e imprime o conteúdo do novo arquivo
with open(nome_arquivo_destino, "r") as arquivo_destino:
    conteudo_destino = arquivo_destino.read()

print(conteudo_destino)
