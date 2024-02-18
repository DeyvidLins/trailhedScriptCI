import xml.etree.ElementTree as ET

# Função para adicionar elementos do arquivo 01 ao arquivo 02
def update_xml_tags(arquivo_01, arquivo_02):
    print(arquivo_01)
    print(arquivo_02)
    tree_01 = ET.parse(arquivo_01)
    root_01 = tree_01.getroot()

    tree_02 = ET.parse(arquivo_02)
    root_02 = tree_02.getroot()

    # Verificar cada elemento do arquivo 01
    for elemento_01 in root_01:
        encontrado = False
        # Verificar se o elemento já existe no arquivo 02
        for elemento_02 in root_02:
            if elemento_01.tag == elemento_02.tag:
                # Se encontrado, marcar como encontrado e sair do loop
                encontrado = True
                break
        # Se não encontrado, adicionar ao arquivo 02
        if not encontrado:
            root_02.append(elemento_01)

    # Escrever as alterações de volta no arquivo 02
    tree_02.write(arquivo_02)


update_xml_tags(r'../manifestXML//objects/Account.object',r'C:\Users\deyvi\OneDrive\Área de Trabalho\Todos os arquivos\pasta01\TodosMeusProjetos\Python\sfdxNewProject\Retrieeve xml/source/objects/Account.object')