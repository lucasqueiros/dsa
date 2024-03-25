import random
from os import system, name

#funcao para limpar a tela a cada execucao
def limpa_tela():
    if name == 'nt':
        #windows
        _=system('cls')
    else:
        #mac ou linux
        _=system('clear')
        
def game():
    limpa_tela()
    
    print("Bem vindo ao jogo da forca")
    print("Advinhe a palavra abaixo:")
    
    banco_palavras = ['forno', 'amarelo', "abacaxi", "girafa", "computador", "cachorro", "telefone", "escola", "motocicleta", "futebol", "banana", "guitarra"]
    palavra_do_dia = random.choice(banco_palavras)
    vidas = 6
    letras_erradas = []
    letras_descobertas = ['-' for letra in palavra_do_dia]

    
    while(vidas > 0):
        print(" ".join(letras_descobertas))
        print("\nVidas Restantes:", vidas)
        print("Letras erradas:", " ".join(letras_erradas))
        print("----------------------------------------------")
        
        tentativa = str(input("Digite uma letra: ").lower())
        
        if tentativa in palavra_do_dia:
            index = 0
            for letra in palavra_do_dia:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            vidas -= 1
            letras_erradas.append(tentativa)
        if "-" not in letras_descobertas:
            print("\nVoce ganhou, a palavra era: ", palavra_do_dia)
            break
    if "-" in letras_descobertas:
            print("\nVoce perdeu, a palavra era: ", palavra_do_dia)
        
        

if __name__ == "__main__":
    game()
    