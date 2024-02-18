import xml.etree.ElementTree as ET

def update_xml_tags(file1, file2):
    # Parsear os arquivos XML
    tree1 = ET.parse(file1)
    tree2 = ET.parse(file2)

    # Obter a raiz dos elementos
    root1 = tree1.getroot()
    root2 = tree2.getroot()

    # Dicionário para armazenar as tags do primeiro arquivo
    tags_file1 = {}

    # Iterar sobre as tags do primeiro arquivo e armazenar em tags_file1
    for elem in root1.iter():
        if elem.tag not in tags_file1:
            tags_file1[elem.tag] = []
        tags_file1[elem.tag].append(elem)

    # Iterar sobre as tags do segundo arquivo e comparar com as do primeiro
    for elem in root2.iter():
        if elem.tag in tags_file1:
            for tag in tags_file1[elem.tag]:
                if ET.tostring(elem) == ET.tostring(tag):
                    # Remover a tag do dicionário se já existir em ambos os arquivos
                    tags_file1[elem.tag].remove(tag)
                    break

    # Adicionar as tags restantes do primeiro arquivo ao segundo arquivo
    for tag_list in tags_file1.values():
        for tag in tag_list:
            root2.append(tag)

    # Escrever o resultado no arquivo de saída
    tree2.write('arquivo02_atualizado.xml', encoding='utf-8', xml_declaration=True)

# Chamar a função com os nomes dos arquivos XML
#update_xml_tags('arquivo01.xml', 'arquivo02.xml')
