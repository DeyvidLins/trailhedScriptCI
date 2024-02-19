import os
import shutil
import compare_file_duplicates

def source_for_destination(folder_src,name_folder):
    destination_directory = fr'{folder_src}/{name_folder}'
    find_components(destination_directory)    
    return destination_directory


def find_components(destination_directory_source):
    folder_manifest = '../manifestXML/'
    files_folder_retrieve = os.listdir(folder_manifest)  # Componentes que foram realizado o retrieve    
    files_folder_source = os.listdir(destination_directory_source)  # Diretório da pasta componentes de source onde contém metadados
    list_component_retrieve = []   
    list_files_source = []
    diretory_retrieve = ''
    diretory_source = ''
    name_component = ''

    for element in files_folder_retrieve: 
        if element != 'backup_package.xml':
            name_component =  element  
            diretory_retrieve = fr'{folder_manifest}/{element}'
            metadata_retrieve = os.listdir(diretory_retrieve)

            for m in metadata_retrieve:  
                list_component_retrieve.append(m)                
                
    for element in files_folder_source:
        diretory_source = fr'{destination_directory_source}/{element}'
        metadata_source = os.listdir(diretory_source) # todos metadatas da pasta source

        for m in metadata_source:   
            dir_source_metadatas = fr'{diretory_source}/{m}'
            list_files_source.append(dir_source_metadatas)

    move_new_files(name_component,list_component_retrieve,diretory_retrieve, diretory_source, list_files_source,destination_directory_source)

def move_new_files(name_component,list_component_retrieve,diretory_retrieve,diretory_source,list_files_source,destination_directory_source):    
    
    if list_component_retrieve == []:
        print("Não é possível move nenhum metadado, pois à pasta encontra-se vazia !!")
        exit()

    list_find_source = [path.split('/')[-1] for path in list_files_source]

    # Verificar se os itens da list_component_retrieve estão contidos em algum item da list_files_source 
    items_found_files_not_duplicados = [item for item in list_component_retrieve if item not in list_find_source]
    items_found_files_duplicados = [item for item in list_component_retrieve if item in list_find_source]

    
    # Move à pasta dos componentes novos
    if len(diretory_source) == 0:   
        print('------------ NOVO(S) COMPONENTE(S) --------------')   
        print(name_component)
        shutil.move(fr'{diretory_retrieve}', fr'{destination_directory_source}')
    
    
    if  (len(items_found_files_not_duplicados) == 0):
        # Se à lista items_found_files_not_duplicados NÃO estive vazia, os componentes duplicados e sobreescreve o arquivo em source    
        for files_duplicates in items_found_files_duplicados:
            compare_file_duplicates.check_type_files(diretory_retrieve,diretory_source,files_duplicates)

    # Se à lista items_found_files_not_duplicados NÃO estive vazia, move apenas os componentes que não existem em source 
    for files_duplicates in items_found_files_not_duplicados:        
        compare_file_duplicates.check_type_files(diretory_retrieve,diretory_source,files_duplicates)
    

    
    


#print(source_for_destination(fr'C:\Users\deyvi\OneDrive\Área de Trabalho\Todos os arquivos\pasta01\TodosMeusProjetos\Python\sfdxNewProject\Retrieeve xml','source'))
