import retrieve
import os

def find_folder_git():
    dir_actual = os.getcwd()    
    for folder, subfolders, _ in os.walk(dir_actual):
        if '.git' in subfolders:           
            name_folder_directory_git = os.path.basename(folder)
            return name_folder_directory_git
            

def folder_actual():
    dir_actual = os.getcwd() 
    return os.listdir(dir_actual)


if find_folder_git() in folder_actual():
    print("VOCÊ NÃO ESTÁ NO DIRETORIO DO REPOSITÓRIO - ENTRE E TENTE NOVAMENTE")                    
else:
    retrieve.retrieveXML()