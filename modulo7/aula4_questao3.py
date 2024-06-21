import requests

# URL do arquivo
url = "https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt"

# Baixa o arquivo e salva como estomago.txt
response = requests.get(url)
with open("estomago.txt", "wb") as file:
    file.write(response.content)

print("Arquivo baixado e salvo como estomago.txt")
# Função principal para processar o arquivo estomago.txt
def processa_arquivo():
    # Nome do arquivo
    nome_arquivo = "estomago.txt"

    # Lê todo o conteúdo do arquivo
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    # 1. Imprime as primeiras 25 linhas
    print("Primeiras 25 linhas do arquivo:")
    for linha in linhas[:25]:
        print(linha, end='')

    # 2. Número de linhas do arquivo
    num_linhas = len(linhas)
    print(f"\n\nNúmero de linhas do arquivo: {num_linhas}")

    # 3. Linha com maior número de caracteres
    linha_mais_longa = max(linhas, key=len)
    print(f"\nLinha com maior número de caracteres: {linha_mais_longa}")
    print(f"Número de caracteres: {len(linha_mais_longa)}")

    # 4. Número de menções aos personagens "Nonato" e "Íria"
    # Considera variações de maiúsculas e minúsculas e exclui substrings indesejadas
    count_nonato = sum(1 for linha in linhas if "Nonato" in linha or "nonato" in linha)
    count_iria = sum(1 for linha in linhas if re.search(r'\b[Ii]ría\b', linha))

    print(f"\nNúmero de menções a 'Nonato': {count_nonato}")
    print(f"Número de menções a 'Íria': {count_iria}")

# Importa o módulo regex
import re

# Chama a função principal
processa_arquivo()
