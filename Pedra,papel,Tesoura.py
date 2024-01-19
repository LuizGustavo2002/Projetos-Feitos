import random

minha_pontuacao = 0
pontuacao_computador = 0 

print("\n============================================\nBem Vindo ao jogo de Pedra, papel ou Tesoura\n============================================\n")

escolha = True

while escolha:
    print("\n\nPLACAR:\nVoce: {}\nComputador: {}\n".format(minha_pontuacao,pontuacao_computador))
    resposta_usuario = int(input("Escolha seu lance:\n0 - PAPEL | 1 - Pedra | 2 - Tesoura\n"))
    mapa_escolhas = {0:"PAPEL", 1:"PEDRA", 2:"TESOURA"}
    if resposta_usuario not in [0,1,2]:
        print("\nOpcao Invalida!")
        Deseja_Continuar = int(input("Deseja continuar jogando? 1 - SIM | 2 - NAO\n"))
        if Deseja_Continuar == 1:
            escolha = True
        else: 
            escolha = False
            print("\n\nFIM DE JOGO!\n\n\n")
            break
    else:
        print("==================================\n")
        print("Sua jogada: ",mapa_escolhas[resposta_usuario])

        resposta_computador = random.choice([0,1,2])
        print("Jogada do computador: ",mapa_escolhas[resposta_computador])

        if resposta_usuario == resposta_computador:
            print("\nEmpate!\n")
        elif (resposta_usuario == 0 and resposta_computador == 1) or (resposta_usuario == 1 and resposta_computador == 2) or (resposta_usuario == 2 and resposta_computador == 0):
            print("\nVoce ganhou!\n")
            minha_pontuacao = minha_pontuacao + 1 
        else:
            print("\nVoce perdeu. O computador ganhou!\n")
            pontuacao_computador = pontuacao_computador + 1

        Deseja_Continuar = int(input("\nDeseja continuar jogando? 1 - SIM | 2 - NAO\n"))
        if Deseja_Continuar == 1:
            escolha = True
        else: 
            escolha = False
            print("\n\nFIM DE JOGO!\n\n\n")
            break
    
    