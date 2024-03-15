#!/usr/bin/env python3
import random
import time
import os

def escolher_palavra():
    return random.choice(["lasanha", "futebol", "programacao", "brasil"])

def adivinhar_letra(palavra, letras_adivinhadas, listaDeChutes):
    while True:
        palpite = input("Escolha uma letra: ").lower()
        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas uma letra.")
        elif palpite in listaDeChutes:
            print("Você já escolheu esta letra. Tente novamente.")
        else:
            listaDeChutes.append(palpite)
            break

    if palpite not in palavra:
        print("Letra incorreta! Você perdeu uma chance.")
        return False

    for index, letra in enumerate(palavra):
        if letra == palpite:
            letras_adivinhadas[index] = palpite

    return True

def main():
    print("Olá! Seja bem-vind@ ao nosso JOGO DA FORCA.")
    print("Esperamos que se divirta, vamos começar !?")
    time.sleep(3)
    os.system("cls")
    palavraEscolhida = escolher_palavra()

    letras_adivinhadas = ["_"] * len(palavraEscolhida)
    listaDeChutes = []
    chances = 5

    while chances >= 0:
        print(f"Você tem {chances} chances para acertar!")
        print(" ".join(letras_adivinhadas))
        print()

        if not adivinhar_letra(palavraEscolhida, letras_adivinhadas, listaDeChutes):
            chances -= 1

        print("=-" * 30)

        if "_" not in letras_adivinhadas:
            print("Parabéns! Você adivinhou a palavra.")
            break

    if "_" in letras_adivinhadas:
        print("Ahh, não foi dessa vez, mas não desista, tente novamente até acertar!")
        print("Você consegue!!!")
        print(f"A palavra era: {palavraEscolhida}")

if __name__ == "__main__":
    main()