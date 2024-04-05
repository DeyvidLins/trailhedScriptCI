import os
import shutil
import find_folder_git
from distutils import dir_util


# Verifica os componetes que foi realizado o retrieve
def check_componenentes_retrieeve():   
    dir = r"../metadataXML/unpackaged/unpackaged"

    rename_file(dir)
    find_folders_zip = os.listdir(dir)   
    

    print("Metadados encontrados: ")
    for folder_zip in find_folders_zip:  
        print(f' ---> {folder_zip}')   
        try:  
            move_file(dir,folder_zip)
        except:
            print('entrou aqui')
            #remove_components_old(dir,folder_zip)

# Renomea o arquivo package.xml
def rename_file(dir):
    arquivo_antigo = "package.xml"
    arquivo_novo = "backup_package.xml"
    
    try:
        os.rename(os.path.join(dir, arquivo_antigo), os.path.join(dir, arquivo_novo))
    except:
        print("Arquivo backup XML já existe")

# Move para o diretório raiz: metadataXML
def move_file(dir,folder_zip):          
    shutil.move(fr'{dir}\{folder_zip}', '../metadataXML') 
    find_folders = os.listdir(dir)

    if find_folders == []: # Vai entrar nesse if se não estiver mais nada no diretório que foi realizado o retrieve
        remove_dir()

    find_git()

# Remove às pasta vazias unpackaged
def remove_dir():      
    delete_folder_zip_empty = r"../metadataXML/unpackaged"
    shutil.rmtree(delete_folder_zip_empty)

def find_git():
    find_folder_git.folder_git()

def remove_components_old(dir,folder_zip):
    dir_retrieve = '../metadataXML/'
    shutil.rmtree(dir_retrieve)

    #move_file(dir,folder_zip)




