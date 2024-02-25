def ler_blocos(nome_arquivo):
    blocos = {}
    with open(nome_arquivo, 'r') as arquivo:
        bloco_temporario = []
        name = None
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                bloco_temporario.append(linha)
                if linha.startswith('<name>') and linha.endswith('</name>'):
                    name = linha.replace('<name>', '').replace('</name>', '')
            elif bloco_temporario and name:
                blocos[name] = '\n'.join(bloco_temporario)
                bloco_temporario = []
                name = None
        if bloco_temporario and name:
            blocos[name] = '\n'.join(bloco_temporario)
    return blocos

# Exemplo de uso:
nome_arquivo = 'saida.txt'
blocos = ler_blocos(nome_arquivo)

# Exibir blocos
for name, conteudo in blocos.items():
    print(f'{name}:')
    print(conteudo)
    print()


