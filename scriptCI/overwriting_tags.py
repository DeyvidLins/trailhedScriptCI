from bs4 import BeautifulSoup
import re


def overwrite(name_file_source,name_tag_initial,find_tag_duplicate,tag_completed_component):
    # Abrir o arquivo XML para leitura
    regex = r'<(.*?)>'
    result = re.search(regex, find_tag_duplicate)
    tag_child = result.group(1)

    value_tag_child = find_tag_duplicate.lstrip(f'<{tag_child}>').rstrip(f'</{tag_child}>') 

    with open(name_file_source, 'r') as arquivo:
        conteudo = arquivo.read()

    soup = BeautifulSoup(conteudo, 'xml')

    # Encontre todas as ocorrências de actionOverrides
    ocorrencias = soup.find_all('actionOverrides')

    # Itere sobre as ocorrências encontradas e verifique se contém actionName desejado
    for ocorrencia in ocorrencias:
        action_name = ocorrencia.find('actionName')
        if action_name and action_name.text == 'CallHighlightAction':
            print(ocorrencia)