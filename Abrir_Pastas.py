# Para quebrar pastas em os arquivos ".exepmlo". Basta colocar esse .py no diretorio que deseja e executar 

import os

diretorio = os.getcwd()

pastas = []

pastas = os.listdir()

arquivos = []

for pasta in pastas:

    if os.path.isdir(pasta): #confere se eh uma pasta

        pastas_endereco = os.path.join(diretorio,pasta)

        arquivos = os.listdir(pastas_endereco) 

        for arquivo in arquivos:

            pasta_atual = os.path.join(pastas_endereco,arquivo)

            pasta_nova = os.path.join(diretorio,arquivo)

            os.replace(pasta_atual, pasta_nova)

        os.rmdir(pastas_endereco)