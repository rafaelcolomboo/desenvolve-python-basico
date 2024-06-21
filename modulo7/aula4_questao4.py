import random

# Função para ler as palavras do arquivo gabarito_forca.txt
def ler_palavras(arquivo):
    with open(arquivo, "r") as f:
        palavras = f.read().splitlines()
    return palavras

# Função para ler os estágios do enforcado do arquivo gabarito_enforcado.txt
def ler_estagios_enforcado(arquivo):
    with open(arquivo, "r") as f:
        estagios = f.read().split("----\n")
    return estagios

# Função para imprimir o enforcado com base no número de erros
def imprime_enforcado(estagios, erros):
    print(estagios[erros])

# Função principal do jogo da forca
def jogo_da_forca():
    palavras = ler_palavras("gabarito_forca.txt")
    estagios = ler_estagios_enforcado("gabarito_enforcado.txt")

    # Escolhe uma palavra aleatória
    palavra = random.choice(palavras)
    palavra_escondida = ["_"] * len(palavra)
    tentativas = 6
    erros = 0
    letras_tentadas = []

    print("Bem-vindo ao jogo da forca!")
    print("A palavra tem", len(palavra), "letras.")
    print(" ".join(palavra_escondida))

    while erros < tentativas and "_" in palavra_escondida:
        letra = input("Digite uma letra: ").lower()
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        letras_tentadas.append(letra)

        if letra in palavra:
            for idx, char in enumerate(palavra):
                if char == letra:
                    palavra_escondida[idx] = letra
            print("Boa! A palavra agora é:")
            print(" ".join(palavra_escondida))
        else:
            erros += 1
            imprime_enforcado(estagios, erros)
            print(f"Você errou! Ainda tem {tentativas - erros} tentativas.")

        if "_" not in palavra_escondida:
            print("Parabéns! Você ganhou!")
            break

    if "_" in palavra_escondida:
        print(f"Você perdeu! A palavra era '{palavra}'.")

# Executa o jogo
jogo_da_forca()
