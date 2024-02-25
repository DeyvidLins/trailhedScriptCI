def add_new_tag_component(tag,new_tag_component,name_file_source):# Abrir o arquivo para leitura

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
        lines.insert(index_last+ 1, f'{new_tag_component}')

    # Escrever as alterações de volta para o arquivo
    with open(name_file_source, 'w') as f:
        f.writelines(lines)





    


    
    