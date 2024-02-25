import os
import shutil
import find_folder_git


# Verifica os componetes que foi realizado o retrieve
def check_componenentes_retrieeve():   
    dir = r"../metadataXML/unpackaged/unpackaged"

    rename_file(dir)
    find_folders = os.listdir(dir)   
    

    print("Metadados encontrados: ")
    for folder in find_folders:  
        print(f' ---> {folder}')     
        move_file(dir,folder)


# Renomea o arquivo package.xml
def rename_file(dir):
    arquivo_antigo = "package.xml"
    arquivo_novo = "backup_package.xml"
    
    try:
        os.rename(os.path.join(dir, arquivo_antigo), os.path.join(dir, arquivo_novo))
    except:
        print("Arquivo backup XML já existe")


# Move para o diretório raiz: metadataXML
def move_file(dir,folder):          
    shutil.move(fr'{dir}\{folder}', '../metadataXML') 
    find_folders = os.listdir(dir)

    if find_folders == []: # Vai entrar nesse if se não estiver mais nada no diretório que foi realizado o retrieve
        remove_dir()


# Remove às pasta vazias unpackaged
def remove_dir():      
    delete_folder_zip_empty = r"../metadataXML/unpackaged"
    shutil.rmtree(delete_folder_zip_empty)
    find_git()

def find_git():
    find_folder_git.folder_git()





