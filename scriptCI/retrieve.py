import os
import re
import verifique_componentes


def retrieveXML():
    # Executa o comando e captura a saída
    output = os.popen('sfdx force:org:list').read()

    # Procura pela última linha que contém (U)
    match = re.findall(r'^\|.*\(U\).*$', output, re.MULTILINE)

    if match:
        # Se houver correspondência, imprime a última linha encontrada
        last_line = match[-1]

        items = last_line.split(' ')

        # Remove os espaços em branco de cada item e adiciona-os à lista final
        item_list = [item.strip() for item in items if item.strip()]
        item_list.remove('|')
        
        print('--------------')
        print(f"ORG PRINCIPAL CONECTADA: {'SIM' if item_list[0].upper() == '(U)' else 'NÃO'}")
        print(f"ALIAS ORG: {item_list[1]}")
        print(f"NOME DO USUÁRIO CONECTADO: {item_list[2]}")
        print(f"ID DA ORG CONECTADA: {item_list[3]}")
        print(f"STATUS: {item_list[4]}")
        print('--------------')
              
    else:
        print("Nenhuma correspondência encontrada.")


    os.system(f'sf project retrieve start --manifest ../manifest/package.xml --target-org {item_list[1]} --target-metadata-dir ../metadataXML --unzip')

    verifique_componentes.check_componenentes_retrieeve()