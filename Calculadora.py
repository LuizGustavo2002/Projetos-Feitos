import os

def limpar_tela():
    sistema_operacional = os.name

    if sistema_operacional == 'nt': 
         os.system('cls')
    else:  
        os.system('clear')

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero."

def exponenciacao(a, b):
    return a ** b

continuar = True

while continuar == True:

    limpar_tela()

    print("0 : soma")
    print("1 : subtracao")
    print("2 : multiplicacao")
    print("3 : divisao")
    print("4 : exponenciacao")
    print("\n")
    print("Escolha a opcao que deseja realizar:")

    escolha = int(input())


    num1 = float(input("Digite o primeiro numero:\n"))
    num2 = float(input("Digite o segundo numero:\n"))

    if escolha == 0:
        print("O resultado eh: {}\n\n".format(soma(num1,num2)))

    elif escolha == 1:
        print("O resultado eh: {}\n\n".format(subtracao(num1,num2)))

    elif escolha == 2:
        print("O resultado eh: {}\n\n".format(multiplicacao(num1,num2)))

    elif escolha == 3:
        print("O resultado eh: {}\n\n".format(divisao(num1,num2)))

    else:
        print("O resultado eh: {}\n\n".format(exponenciacao(num1,num2)))

    print("Deseja continuar? s ou n")
    resposta = input()
    
    if resposta == "s":
        continuar = True

    else:
        continuar = False
        break





