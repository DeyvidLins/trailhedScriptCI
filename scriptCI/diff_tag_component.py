def add_new_tag_component(tag,tag_completed_component,name_file_source):# Abrir o arquivo para leitura
    last_tags= f'</{tag}>'
    
    with open(name_file_source, 'r') as f:
        lines = f.readlines()

    # Procurar pela tags que foi passada no parametro e adicionar uma quebra de linha após a última ocorrência
    index_last = None
    for i, line in enumerate(lines):
        if f'{last_tags}' in line:
            index_last = i

    # Adicionar uma quebra de linha após a última ocorrência 
    if index_last is not None:
        lines.insert(index_last+ 1, f'{tag_completed_component}')

    # Escrever as alterações de volta para o arquivo
    with open(name_file_source, 'w') as f:
        f.writelines(lines)

def add_existing_tag_component(tag, tag_completed_component, name_file_source):
    # Abrir o arquivo para leitura
    find_tag_name = tag

    with open(name_file_source, 'r') as f:
        lines = f.readlines()

    # Encontrar a posição da última ocorrência da tag
    index_last = None
    for i, line in enumerate(lines):
        if f'{find_tag_name}' in line:
            index_last = i

    # Adicionar a tag completada na frente do <name>
    if index_last is not None:
        # Encontrar a posição do <name> após a última ocorrência da tag
        index_name = None
        for i in range(index_last, len(lines)):
            if '<name>' in lines[i]:
                index_name = i
                break

        # Adicionar a tag completada na frente do <name>
        if index_name is not None:
            lines.insert(index_name, f'{tag_completed_component}\n')

    # Escrever as alterações de volta para o arquivo
    with open(name_file_source, 'w') as f:
        f.writelines(lines)

# Teste do método
