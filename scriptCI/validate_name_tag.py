import diff_tag_component

concat_string = ''
transformeted_string_to_list = []
resultado = {}
def convert_str_to_list(tag):    
    if (len(tag)) != 0:  # Diferente de zero para não imprimi o arquivo duplicado       
        string_separate = tag.replace(',',' ')
        global concat_string
        concat_string += f'{string_separate}' 
        global transformeted_string_to_list
        transformeted_string_to_list = concat_string.split(' ')
        for i in transformeted_string_to_list:
            if i == 'closed': # Se for igual à closed chama à lista
                list_tags()
     
def list_tags():
    transformeted_string_to_list.pop() # Remove o nome closed da lista
    value_unique_list = []

    for valor in transformeted_string_to_list:
        if valor not in value_unique_list:
            value_unique_list.append(valor)

    find_tags_in_source(value_unique_list)

def find_tags_in_source(list_tags): 
    file_xml()

    construct_dict_names_tags(list_tags)

    for i in list_tags:
        if i in file_xml():
            checks_tags(i,existed_tag=True)
        else:
            checks_tags(i,existed_tag=False)

def construct_dict_names_tags(list_tags):
    global resultado
    resultado = {}

    nome_atual = None
    valores_temporarios = []  # Inicializar variáveis temporárias

    for item in list_tags:
        if item.startswith('<name>'):
            nome_atual = item.lstrip('<name>').rstrip('</name>') # Pega o valor do name removendo às tags

            # Se encontrarmos uma tag <name>, atualizamos o nome atual
            if nome_atual is not None:
                # Adicionamos ao resultado o nome e os valores temporários, se houver
                resultado[nome_atual] = valores_temporarios[::1]
                valores_temporarios = []  # Limpar a lista de valores temporários
            
        else:
            # Adicionamos os valores à lista temporária
            valores_temporarios.append(item.lstrip('<members>').rstrip('</members>'))
    
    #print(resultado)

def checks_tags(tag,existed_tag):    
    # Condição para verificar se à tag name é nova no package.xml da pasta source
    if ('<name>' in tag) and (existed_tag == False):       
        value_tag_name = tag.lstrip('<name>').rstrip('</name>')   
        #create_new_tag(value_tag_name, resultado[value_tag_name]) # A chave será o valor da tag name. Ex.: CustomObject. E resultado[tag_name] será os valores do members

    # Condição para verificar se à tag name já existi no package.xml da pasta source
    elif ('<name>' in tag) and (existed_tag == True):   
        value_tag_name = tag.lstrip('<name>').rstrip('</name>') 
        for element in resultado[f'{value_tag_name}']:
            members = f'<members>{element}</members>'
            if members not in file_xml():        
                existing_tag(value_tag_name,members)

def file_xml():
    with open('package.xml', 'r') as file:
        conteudo = file.read()
    return conteudo

def create_new_tag(value_tag_name, value_members):
    members = ''
    espace_four = ' ' * 4
    espace_eight = ' ' * 8
    if type(value_members) is list:
        for item in value_members:
            members += f'{espace_eight}<members>{item}</members>\n'
    
    new_tag =  f'{espace_four}<types>\n{members}{espace_eight}<name>{value_tag_name}</name>\n{espace_four}</types>\n'
    #print(new_tag)
    diff_tag_component.add_new_tag_component('types', new_tag, 'package.xml')

def existing_tag(value_tag_name, value_member):
    espace_eight = ' ' * 8
    diff_tag_component.add_existing_tag_component(f'<name>{value_tag_name}', f'{espace_eight}{value_member}', 'package.xml')


