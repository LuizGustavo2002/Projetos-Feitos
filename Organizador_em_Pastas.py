# Para organizar os arquivos ".exepmlo" em pastas basta colocar esse .py no diretorio que deseja e executar 

import os

diretorio = os.getcwd() # retorna o diretorio q esse .py se encontra

arquivos = os.listdir(diretorio) # cria uma lista com todos os elementos presentes no diretorio

extensoes = [] #lista vazia que colocaremos as extensoes

def criarpastas(caminho):
    if os.path.exists(caminho): # se ja existir a pasta, ignora
        print("Ja existe")
    else:
        os.mkdir(caminho) # se nao existir a pasta, cria ela

def renomeararquivos(caminho):

        if os.path.exists(caminho) and extensao!= '.py':

            arquivo_antigo = caminho

            arquivo_novo = diretorio + '\\' + extensao + '\\' + arquivo

            os.rename(arquivo_antigo, arquivo_novo)

for arquivo in arquivos:

    caminho = os.path.join(diretorio, arquivo) # junta o diretorio da pasta com o nome do arquivo para obter o endereco completo do arquivo

    if os.path.isfile(caminho):

        extensao = os.path.splitext(caminho)[-1] # separa o texto do endereco do '.', coloca numa lista e pegamos a extensao depois do ponto 

        if extensao not in extensoes and extensao!= '.py':

            extensoes.append(extensao) # adiciona essa nova extensao ao final da lista

            criarpastas(diretorio + '\\' + extensao + '\\')

        renomeararquivos(caminho)