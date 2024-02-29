import xmltodict
import diff_tag_component

def print_content_tag(name_file_retrieve,name_file_source,tag_parent):  
    dic_tags = {}
    # Abrir o arquivo XML e carregá-lo como um dicionário
    with open(name_file_retrieve, 'r', encoding='utf-8') as arquivo:
        xml_dict = xmltodict.parse(arquivo.read())

    # Verificar se a tag pai existe no dicionário
    if tag_parent in xml_dict:
        # Imprimir o conteúdo completo da tag pai
        dic_tags = (xml_dict[tag_parent])
    else:
        print(f"A tag pai '{tag_parent}' não foi encontrada no XML.")
    
    for key in dic_tags.keys():
        if key != '@xmlns':
            build_file(key,dic_tags[f'{key}'],name_file_source) # Envia o conteúdo/valor da tag/dicionario
         
def build_file(name_tag_initial,body_tag,name_file_source): # TRATAR TRATAR TRATAR PORQUE DAR ERRO QUANDO TEM MUITA TAG NO COMPONENTE
    list_tags = []  # Lista para armazenar os dicionários incrementados
    if (type(body_tag)) is list:
        for n,body in enumerate(body_tag):
            incremet_dict = f'tag_dict_{n}'
            dict_tag = {f'{incremet_dict}': body}
            list_tags.append(dict_tag) 
    else:
        quantity_keys = len(body_tag.keys())  # Quantidade das chaves que vem do dicionario
        keys = list(body_tag.keys()) # Pega o nome de todas às chaves do dicionário e transforma em lista
        include_dict_tag(name_tag_initial,quantity_keys,keys,body_tag,name_file_source)

    if list_tags != []:
        for n, dic in enumerate(list_tags):
            incremet_dict = f'tag_dict_{n}'
            value_tag_child = dic[f'{incremet_dict}'] 
            keys = list(value_tag_child.keys()) # Pega o nome de todas às chaves do dicionário e transforma em lista
            quantity_keys = len(value_tag_child.keys()) 
            include_dict_tag(name_tag_initial,quantity_keys,keys,value_tag_child,name_file_source)

def include_dict_tag(name_tag_initial,quantity_keys,keys,body_tag,name_file_source):     
    four_space = " " * 4
    eight_space  = " " * 8
    tag_full_content_child = ''
    tag_completed_component  = ''
    for i in range(0,quantity_keys):
        name_key_tag_child = keys[i]
        value_tag_child = body_tag[f'{name_key_tag_child}']       
        if type(value_tag_child) is list:
            string = ', '.join(value_tag_child)
            string = string.replace("[", "").replace("]", "").replace(","," ")            
            tag_full_content_child += f'<{name_key_tag_child}>{string}</{name_key_tag_child}>\n'.replace(" ",f"</{name_key_tag_child}>\n").replace(f"\n</{name_key_tag_child}>\n",f"\n<{name_key_tag_child}>")
            tag_with_spaces_child  = "\n".join([eight_space + linha for linha in tag_full_content_child.split("\n")])
            remove_last_line_break = tag_with_spaces_child.rstrip()
            tag_completed_component = f"{four_space}<{name_tag_initial}>\n{remove_last_line_break}\n{four_space}</{name_tag_initial}>\n"

        else:
            tag_full_content_child += f'<{name_key_tag_child}>{value_tag_child}</{name_key_tag_child}>\n'
            tag_with_spaces_child  = "\n".join([eight_space + linha for linha in tag_full_content_child.split("\n")])
            remove_last_line_break = tag_with_spaces_child.rstrip()
            tag_completed_component = f"{four_space}<{name_tag_initial}>\n{remove_last_line_break}\n{four_space}</{name_tag_initial}>\n"

    #print(tag_completed_component)    
    
    find_tag = [tag_full_content_child.split("\n")][0][0]
    #print(find_tag)
   
    verificated_tags(tag_completed_component,name_file_source,find_tag)

def verificated_tags(tag_completed_component,name_file_source,find_tag):    
    with open(name_file_source, 'r') as file:
        conteudo = file.read()
    if (find_tag in conteudo):
        #print(find_tag)      
        diff_tag_component.overwrite(find_tag,tag_completed_component,name_file_source)
    else:
        tags = tag_completed_component.replace(' ','')
        tag_main = tags.split('\n')

        find_tag_main = tag_main[0].replace('<','').replace('>','')
        #print(find_tag_main)
        diff_tag_component.add_new_tag_component_and_package_xml(find_tag_main,tag_completed_component,name_file_source)

