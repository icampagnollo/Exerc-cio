import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Seja bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 100...")
    print("Pensei!")
    print("Digite 'sair' a qualquer momento para encerrar o jogo, ok?")

    while True:
        entrada = input("Qual é o seu palpite? ")
        
        if entrada.lower() == 'sair':
            print(f"O número secreto era {numero_secreto}. Obrigada por jogar! :)")
            break
        
        try:
            tentativa = int(entrada)
        except ValueError:
            print("Por favor, digite um número válido ou 'sair'.")
            continue

        tentativas += 1
        
        if tentativa < numero_secreto:
            print("Muito baixo! Tente novamente zé mané")
        elif tentativa > numero_secreto:
            print("Muito alto! Tente novamente ><")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
            break

if __name__ == "__main__":
    jogo_adivinhacao()