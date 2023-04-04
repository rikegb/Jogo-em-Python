import random
def jogar():
    print("******************************   Bem-Vindo no jogo de Advinhação ****************************** ")

    numero = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("--------------- \n Qual nível de dificuldade voce quer jogar? \n (1) Facil \n (2) Médio \n (3) Dificil \n --------------- ")
    nivel = int(input("Define o nível: "))
    if nivel == 1:
        tentativas = 20
    elif nivel == 2 :
        tentativas = 10
    else:
        tentativas = 5


    for rodada in range(1,tentativas + 1) :
        print("Tentativas {} de um total de {}".format(rodada,tentativas))
        chute = int(input("Digite o seu número entre 1 e 100: "))
        print("Você digitou", chute )

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero
        maior = chute > numero
        menor = chute < numero

        if acertou:
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if maior:
                print("Você errou!O seu chute foi maior que o número")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto")

            pontos_perdidos =  abs(numero - chute)
            pontos = pontos - pontos_perdidos

    print("****************************** Fim de Jogo ****************************** ")

if(__name__ == "__main__"):
    jogar()