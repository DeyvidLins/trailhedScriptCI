import construction_tag_component
import os
import shutil
import xmltodict


# Verifica o tipo do arquivo
def check_type_files(diretory_retrieve,diretory_source,file):    
    not_overwrite = ['object','profile']
    find_type = file.split(".")
    type = find_type[-1]
 
    if (type not in not_overwrite):        
        shutil.move(fr'{diretory_retrieve}/{file}', fr'{diretory_source}/{file}') # Move os metadados novos que não são repetidos
    else:    

        compare_file_difference(diretory_retrieve,diretory_source,file) # Move às tags dos arquivos repetidos
    
    if file == '':
        print("Não existi mais nenhum metadado para ser movido")

def diretories():
    dir_actual = os.getcwd()     
    list_diretories = []
                
    for folder_source, subfolders, _ in os.walk(dir_actual):
        if '.git' in subfolders:
            list_diretories.append(folder_source)
    
    return list_diretories


def compare_file_difference(diretory_retrieve,directory_source,file):   
    dir_retrieve = fr'{diretory_retrieve}/{file}'
    dir_source = fr'{directory_source}/{file}'

    name_type_file(dir_retrieve)
    construction_tag_component.print_content_tag(dir_retrieve,dir_source,name_type_file(dir_retrieve))

# Recebe o diretório do retrieve com o nome do tipo do componente e captura o primeiro elemento
def name_type_file(diretory_retrieve):
    with open(diretory_retrieve, 'r', encoding='utf-8') as arquivo:
        xml_dict = xmltodict.parse(arquivo.read())    
    return list(xml_dict.keys())[0]
