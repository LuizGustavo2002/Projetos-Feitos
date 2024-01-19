#Exemplo de como uma minoria pode afetar a organizacao de todo um todo. Bagunca de halteres numa academia
import random
import seaborn as sns

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 100) if i % 2 == 0] # halteres que existem nessa academia
        self.porta_halteres = {} # Dicionario para associar o lugar correto demarcado para cada peso e o peso que esta nessa posicao
        self.reiniciar_o_dia()# um instrutor reorganiza todos os halteres

    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0] #retorna os halteres possiveis de serem utilizados, marcados com 0 significa que o halter esta sendo utilizado

    def listar_espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def pegar_haltere(self, peso):
        haltere_posicao = list(self.porta_halteres.values()).index(peso) #achar a posicao atual do peso
        key_haltere = list(self.porta_halteres.keys())[haltere_posicao]
        self.porta_halteres[key_haltere] = 0
        return peso

    def devolver_haltere(self, pos, peso):
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres)

class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos) #o usuario escolhe um peso aleatoriamente
        self.academia.pegar_haltere(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()

        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_haltere(self.peso, self.peso)#ele devolve o peso para o valor igaul ao do halter que esta segurando
            else:
                pos = random.choice(espacos) #coloca aleatoriamente se a correta estiver ocupada
                self.academia.devolver_haltere(pos, self.peso)

        if self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.devolver_haltere(pos, self.peso)
        self.peso = 0

academia = Academia()

usuarios = [Usuario(1, academia) for i in range(10)] #10 usuarios "corretos" para 1 bagunceiro
usuarios += [Usuario(2, academia) for i in range(1)]
random.shuffle(usuarios)

lista_caos = []
#calcular o "indide de caos" por 1000 vezes e plotar
for k in range(1000):
    academia.reiniciar_o_dia()
    for i in range(10):#10 treinos 
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    lista_caos.append(academia.calcular_caos())

sns.displot(lista_caos)
