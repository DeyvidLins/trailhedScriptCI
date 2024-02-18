import os
import move_file_repository
import time


# Procura pelo nome da pasta que contém o .git que é de versionamento de código
def folder_git():
    dir_actual = os.getcwd()    
    for folder, subfolders, _ in os.walk(dir_actual):
        if '.git' in subfolders:
            return find_source(folder)

# Procura pela pasta onde fica os componentes do Salesforce
def find_source(folder_src):
    possible_component_folders = ['source','src']
    find_folders = os.listdir(folder_src)  
    for name_folder in possible_component_folders:
        if name_folder in find_folders:
            return files(folder_src,name_folder)

# Concatena o diretório com à pasta para depois mover
def files(folder_src,name_folder):
    time.sleep(10)
    return move_file_repository.source_for_destination(folder_src,name_folder)

