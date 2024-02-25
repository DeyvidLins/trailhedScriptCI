import os
import xmltodict
import validate_name_tag

def update_tags_xml():
    dict_xml = {}
    dir_manisfet_file_xml = r'../manifest/package.xml'

    with open(dir_manisfet_file_xml, 'r', encoding='utf-8') as arquivo:
        xml_dict = xmltodict.parse(arquivo.read())
        
        dict_package_xml = xml_dict['Package']
        #print(dict_package_xml)

        for key in dict_package_xml.keys():
            if key == 'types':
                dict_xml = dict_package_xml[f'{key}']
                separate_tags_members_and_name(dict_xml)

# Separa às tags e captura os valores 
def separate_tags_members_and_name(body_tag):
    quantity_list = len(body_tag)  # Quantidade da lista
    for i in range(0,quantity_list):
        name_tag = body_tag[i]
        for key in name_tag.keys():
            if key == 'members':
                members = name_tag[f'{key}']
                tag_full(members,key)
            else:
                name = name_tag[f'{key}']
                tag_full(name,key)

    tag_full('closed','') # Serve para informar que não encontrou mais nenhum nome do componente no xml

# Cria à tag completa
def tag_full(value_tag,type):
    tag_members = ''
    tag_name = ''
    if isinstance(value_tag, list): # Se tive mais de um members, será uma lista e este if trata
        for item in value_tag:
            tag_members += f'<members>{item}</members>,'
            validate_name_tag.convert_str_to_list(tag_members)
    else:
        if type == 'name':
            tag_name += f'<name>{value_tag}</name>,'
            validate_name_tag.convert_str_to_list(tag_name)


        elif type == 'members':
            tag_members += f'<members>{value_tag}</members>,'
            validate_name_tag.convert_str_to_list(tag_members)
        
        else:
            validate_name_tag.convert_str_to_list(value_tag) # Vai enviar Closed, informando que encerrou 

  
    
    
#update_tags_xml()