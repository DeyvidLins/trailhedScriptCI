import os

def procurar_imagens(caminho):
    imagens = []
    # Percorre recursivamente as pastas e subpastas
    for pasta_raiz, _, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            # Verifica se o arquivo tem extensão .jpeg ou .jpg
            if arquivo.lower().endswith(('.jpeg', '.jpg')):
                imagens.append(os.path.join(pasta_raiz, arquivo))
    return imagens

# Diretório raiz para procurar as imagens
diretorio_raiz = 'C:\\'

# Procura as imagens dentro do diretório raiz e suas subpastas
imagens_encontradas = procurar_imagens(diretorio_raiz)

# Imprime o caminho de cada imagem encontrada
for imagem in imagens_encontradas:
    print(imagem)
