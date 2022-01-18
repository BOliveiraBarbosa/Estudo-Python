import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de Advinhação!")
    print("********************************")
    print("\n")

    numero_secreto = random.randrange(1,101) #[1, 100]
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil | (2) Médio | (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {} ".format(rodada, total_tentativas))

        chute = input("Digite um número entre 1 e 100: ")
        chute = int(chute)
        print("Você digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100\n")
            continue 

        if(chute == numero_secreto): #Acertou
            print("Você acertou")
            print("Sua pontuação é {}! \n".format(pontos))
            break
        else:
            if(chute > numero_secreto): #Maior
                print("Você errou! O seu chute foi MAIOR que o número secreto!")
            elif(chute < numero_secreto): #Menor
                print("Você errou! O seu chute foi MENOR que o número secreto!")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        print("\n")

    print("O número certo era: ", numero_secreto)
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
