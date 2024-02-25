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
         

def build_file(tag_parent,body_tag,name_file_source):
    content_space_parent = " " * 4
    content_space_child  = " " * 8
    tag_full_content_child  = ''
    quantity_keys = len(body_tag.keys())  # Quantidade das chaves que vem do dicionario
    keys = list(body_tag.keys()) # Pega o nome de todas às chaves do dicionário e transforma em lista


    for i in range(0,quantity_keys):
        name_tag_child = keys[i]
        value_tag_child = body_tag[f'{name_tag_child}']
        tag_full_content_child += f'<{name_tag_child}>{value_tag_child}</{name_tag_child}>\n'
    
    # Incluir espaço na string
    tag_with_spaces_child  = "\n".join([content_space_child + linha for linha in tag_full_content_child.split("\n")])
    remove_last_line_break = tag_with_spaces_child.rstrip()
   
    new_tag_component = f"{content_space_parent}<{tag_parent}>\n{remove_last_line_break}\n{content_space_parent}</{tag_parent}>\n"

    #print(new_tag_component)
    diff_tag_component.add_new_tag_component(tag_parent,new_tag_component,name_file_source)




'''nome_arquivo = "../manifestXML/objects/Account.object"
tag_pai = "CustomObject"
print_content_tag(nome_arquivo, tag_pai)'''